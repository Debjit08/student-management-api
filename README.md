
# Student Management System API

## Setup Instructions

1. Create a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up MySQL database and run the SQL script:
   ```bash
   mysql -u root -p < schema.sql
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Access Swagger UI at:
   ```
   http://localhost:5000/
   ```
