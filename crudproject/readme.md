Django REST Framework CRUD – Employee API

📅 Date: 12 Feb 2026

📌 Project Description

This project is a simple CRUD (Create, Read, Update, Delete) REST API built using Django and Django REST Framework.
It manages Employee details such as name, email, and salary.

🛠 Technologies Used

Python

Django

Django REST Framework

SQLite (default database)

📂 Project Structure
crudproject/
│
├── crudproject/
│   ├── urls.py
│   └── settings.py
│
├── employee/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py
│
├── manage.py
└── README.md

🚀 Setup Instructions
1️⃣ Install Dependencies
pip install django djangorestframework

2️⃣ Create Database Tables
python manage.py makemigrations
python manage.py migrate

3️⃣ Create Superuser (Optional – for Admin Panel)
python manage.py createsuperuser

4️⃣ Run Server
python manage.py runserver

🔗 API Endpoints
Action	Method	URL
Create Employee	POST	/employees/
Get All Employees	GET	/employees/
Get Employee by ID	GET	/employees/<id>/
Update Employee	PUT / PATCH	/employees/<id>/
Delete Employee	DELETE	/employees/<id>/
📥 Sample Request Body (POST / PATCH)
{
  "name": "Lakshmi",
  "email": "lakshmi@gmail.com",
  "salary": 25000
}

🧪 Testing

You can test APIs using:

Postman

Thunder Client

Browser (GET requests)

🧠 Key Concepts Learned

Django project & app structure

Models and migrations

Serializers

@api_view decorator

Request & Response

CRUD operations

Django Admin Panel

🎯 Conclusion

This project demonstrates a basic REST API using Django REST Framework, suitable for beginners and interview preparation.