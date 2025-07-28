# 🧑‍💼 Employee Management System (Django)

A simple Employee Management System built with **Django** that allows user authentication, employee CRUD operations, and image upload functionality.

## 🚀 Features

- User Signup & Login with session management
- Add Employee with image upload
- View all employees
- Edit & update employee information with image preview
- Delete employee
- Django Admin panel support
- CSS styled frontend

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS
- **Database**: SQLite (default)
- **Other**: Django Forms, Static & Media file handling

## 📸 Screenshots

<img width="1920" height="1020" alt="Screenshot 2025-07-18 205358" src="https://github.com/user-attachments/assets/a4ca8464-c4c5-43db-8c11-003baf5d89da" />
Signup

<img width="1920" height="1020" alt="Screenshot 2025-07-18 205412" src="https://github.com/user-attachments/assets/b8f0dd10-2279-48f1-ba36-00d8f00e1ae7" />
Login

<img width="1920" height="1020" alt="Screenshot 2025-07-18 210039" src="https://github.com/user-attachments/assets/54e5561d-e699-4cd0-b753-b4550fc6c668" />
Home

<img width="1920" height="1020" alt="Screenshot 2025-07-18 210055" src="https://github.com/user-attachments/assets/889db0b9-dfd0-483b-a37d-cbba859bbdf1" />
Add Employee

<img width="1920" height="1020" alt="Screenshot 2025-07-18 210649" src="https://github.com/user-attachments/assets/b4246568-c276-4ecf-ba33-d44d74a7b55f" />
View Employees

<img width="1920" height="1020" alt="Screenshot 2025-07-18 210744" src="https://github.com/user-attachments/assets/82346c0e-6e2f-449a-a0a8-820dd231214b" />
Edit Employee

---

<img width="318" height="552" alt="Screenshot 2025-07-18 231231" src="https://github.com/user-attachments/assets/c25c6d27-f000-4d4b-bfa0-1eafa9c51ec0" />

.

---

## ⚙️ Setup Instructions

### 1. Create a Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

pip install django


python manage.py makemigrations
python manage.py migrate

python manage.py runserver
