<div align="center">
  <h1>Task Manager</h1>
    A Python-Django Task Manager Project with REST API
  <h3>Project Demo</h3>


https://github.com/jayeeed/task_manager/assets/137998593/27c39555-7b63-4bf6-8ee6-c4d69f86d72f


</div>

## Technology Used

- **Frontend:** HTML5, CSS3, Bootstrap5, JavaScript
- **Backend:** Python=3.11.6, Django=5.0.1
- **Database:** Serverless PostgreSQL hosted on Neon.tech
- **API:** Django-REST-Framework
- **Version Control:** Git, GitHub
- **Editor:** VS Code
- **Operating System:** Windows/Linux

## Getting Started

Follow below instructions for running project locally:

- Clone the repository

```bash
git clone https://github.com/jayeeed/task_manager.git
```

- Go to the project directory

```bash
cd task_manager
```

- Create a virtual environment

```bash
python -m venv .venv
```

- Activate the virtual environment

```bash
.venv\Scripts\activate
```

- Install the dependencies

```bash
pip install -r requirements.txt
```

- Run the server

```bash
python manage.py runserver
```

- Open the browser and go to http://127.0.0.1:8000/

### Admin Panel

- Run the server

```bash
python manage.py runserver
```

- Open the browser and go to http://127.0.0.1:8000/

- To access the admin panel, go to http://127.0.0.1:8000/admin/

- Login with the following credentials:

  - Username: `jayed`
  - Password: `1234`

- If these credentials don't work, you can create a superuser by running the following command:

```bash
python manage.py createsuperuser
```

- Enter the username, email, and password

- Now you can access the admin panel with the credentials you have just created

## API Details

- **Endpoint:** http://127.0.0.1:8000/tasks/api/tasks/
- **Method:** GET
- **Description:**
  - Returns all the tasks
- **Endpoint:** http://127.0.0.1:8000/tasks/api/tasks/1/
- **Method:** GET, PUT, PATCH, DELETE
- **Description:**
  - Returns a single task
  - Updates a single task
  - Partially updates a single task
  - Deletes a single task
