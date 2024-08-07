# Django To-Do List Application

This is a Django-based web application for managing to-do lists. Users can add tasks, categorize them by day of the week, and clear all tasks to start a new week.

## Features

- Add tasks with titles, descriptions, and assigned days.
- View tasks grouped by day.
- Mark tasks as completed.
- Clear all tasks to start a new week.

## Requirements
- Python 3.12.4
- Django 5.0.7

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Dillon-mac/todolist.git

2. Navigate to the project directory:
   ```bash
   cd todolist

3. Install the required packages:
   ```bash
   pip install -r requirements.txt

4. Apply migrations:
   ```bash
   python manage.py migrate

5. Start the development server:
   ```bash
   python manage.py runserver

6. Open your web browser and go to http://127.0.0.1:8000 to see the application in action, and prepare to be mildly impressed!

## Usage

1. **Add a Task:**

   - Enter the task title and description.
   - Select the day of the week for the task.
   - Click the "Add Task" button.

2. **View Tasks:**

   - Tasks are displayed grouped by the selected day of the week.

3. **Mark Tasks as Completed:**

   - Click the checkbox next to a task to mark it as completed.

4. **Clear All Tasks:**

   - Click the "New Week" button to clear all tasks and start a new week.
  
## Screenshot

![Screenshot 2024-08-07 172603](https://github.com/user-attachments/assets/e46f7c88-4704-4825-8400-7cc319d56d58)
