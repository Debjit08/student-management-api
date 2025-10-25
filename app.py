
from flask import Flask, request
from flask_restx import Api, Resource, fields
import mysql.connector
import os

app = Flask(__name__)
api = Api(app, version='1.0', title='Student Management API', description='API for managing students')

# Database connection
DB_CONFIG = {
    'host': os.getenv("DB_HOST", "localhost"),
    'user': os.getenv("DB_USER", "root"),
    'password': os.getenv("DB_PASSWORD", ""),
    'database': os.getenv("DB_NAME", "student_db")
}

db = mysql.connector.connect(**DB_CONFIG)
cursor = db.cursor(dictionary=True)

# Swagger model
student_model = api.model('Student', {
    'roll': fields.String(required=True),
    'name': fields.String(required=True),
    'dob': fields.String(required=True, description='Date of Birth in YYYY-MM-DD'),
    'class_name': fields.String(required=True)
})

@api.route('/student')
class CreateStudent(Resource):
    @api.expect(student_model)
    def post(self):
        data = request.json
        query = "INSERT INTO students (roll, name, dob, class_name) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (data['roll'], data['name'], data['dob'], data['class_name']))
        db.commit()
        return {"message": "Student created successfully"}, 201

@api.route('/student/<int:id>')
class UpdateDeleteStudent(Resource):
    @api.expect(student_model)
    def put(self, id):
        data = request.json
        query = "UPDATE students SET roll=%s, name=%s, dob=%s, class_name=%s WHERE id=%s"
        cursor.execute(query, (data['roll'], data['name'], data['dob'], data['class_name'], id))
        db.commit()
        return {"message": "Student updated successfully"}

    def delete(self, id):
        cursor.execute("DELETE FROM students WHERE id=%s", (id,))
        db.commit()
        return {"message": "Student deleted successfully"}

@api.route('/students')
class GetAllStudents(Resource):
    def get(self):
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        return students

@api.route('/student/search')
class SearchStudent(Resource):
    def get(self):
        roll = request.args.get('roll')
        name = request.args.get('name')
        dob = request.args.get('dob')
        class_name = request.args.get('class')

        query = "SELECT * FROM students WHERE 1=1"
        params = []

        if roll:
            query += " AND roll=%s"
            params.append(roll)
        if name:
            query += " AND name=%s"
            params.append(name)
        if dob:
            query += " AND dob=%s"
            params.append(dob)
        if class_name:
            query += " AND class_name=%s"
            params.append(class_name)

        cursor.execute(query, tuple(params))
        result = cursor.fetchall()
        return result

if __name__ == '__main__':
    app.run(debug=True)
