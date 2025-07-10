# Django for APIs Practice Projects 

This repository contains all the hands-on projects and exercises completed while following the **"Django for APIs"** book by *William S. Vincent*.

It demonstrates how to build robust and RESTful APIs using Django and Django REST Framework, with real-world examples such as blog posts, user authentication, schema generation, and interactive API documentation.

---

## 📚 Contents

- ✅ Basic API using Django REST Framework
- ✅ Class-Based Views & Permissions
- ✅ Serializers & Relationships
- ✅ Authentication & Authorization (Session, Token, JWT)
- ✅ ViewSets & Routers
- ✅ `dj-rest-auth` & `django-allauth` for user registration/login
- ✅ Schema generation with `drf-spectacular`
- ✅ API Documentation using Redoc

---

## 🛠️ Tech Stack

- **Python 3.12**
- **Django**
- **Django REST Framework (DRF)**
- **dj-rest-auth**
- **django-allauth**
- **drf-spectacular**
- **SQLite** (default DB for testing)
- **Redoc** for API documentation

---

## 🚀 Getting Started

## 1. Clone the repository

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
## 2. Create and activate virtual environment
```
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```
3. Install dependencies
```
pip install -r requirements.txt
```
## 4. Apply migrations
```
python manage.py migrate
```
## 5. Create superuser (optional for admin access)
```
python manage.py createsuperuser
```
## 6. Run the development server
```
python manage.py runserver
```
Visit your app at http://127.0.0.1:8000/.
🧪 API Endpoints
Endpoint	Description
/api/v1/	Posts API
/api/v1/dj-rest-auth/	Login/Logout/Password management
/api/v1/dj-rest-auth/registration/	User registration
/api-auth/	Browsable API login/logout
/api/schema/	OpenAPI schema (machine-readable)
/api/schema/redoc/	Redoc API documentation (human-readable)
🧾 License

This project is for educational purposes. Feel free to use and adapt it.Acknowledgments
Thanks to William S. Vincent for writing the book Django for APIs and making learning Django fun and practical.
