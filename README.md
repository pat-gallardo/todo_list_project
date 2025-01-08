# To-Do List API Program Documentation

This documentation outlines the structure and usage of the To-Do List API developed using Django and Django Rest Framework (DRF).

## Installation

1. Clone the Repository:
```
git clone <repository_url>
cd todo_project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Apply Migrations
```bash
python manage.py migrate
```

4. Run the server:
```bash
python manage.py runserver
```

5. Access the API: Open your browser or Postman and navigate to 
```bash
http://127.0.0.1:8000/api/tasks/
```

## API Endpoints

- GET /api/tasks - Retrieve a list of all tasks categorized into Incoming, Today, and Overdue.

- POST /api/tasks - Create a new task.
```bash
{
  "title": "Buy groceries",
  "description": "Buy milk, eggs, and bread.",
  "due_date": "2025-01-10"
}
```
- GET /api/tasks/<id> - Retrieve details of a specific task.

- PUT /api/tasks/<id>/update - Update an existing task.
```bash
{
  "title": "Wash car",
  "description": "Wash car using power washer.",
  "due_date": "2025-01-11"
}
```

- DELETE /api/tasks/<id>/delete - Delete a existing task.

## Notes
- Ensure your due_date field is properly formatted (YYYY-MM-DD) when creating or updating tasks