# Task Manager



## Project Overview



- **Project Title**: Task Manager

- **Project Video**: [Task Manager Demo Video](https://youtu.be/HQucyD31re4?feature=shared)



## Table of Contents



- [Description](#description)

- [Files and Components](#files-and-components)

- [Features](#features)

- [Installation](#installation)

- [Usage](#usage)

- [Design Choices](#design-choices)



## Description



The Task Manager is a simple yet effective command-line Python application designed to assist users in managing their tasks efficiently. Life is busy, and staying organized can be a challenge. This tool aims to simplify task management by providing a straightforward interface to add, list, complete, and remove tasks, ultimately helping users stay on top of their to-do lists and boost productivity.



## Files and Components



### `project.py`



- **Description**: This is the main script of the Task Manager application. It contains the core functionality and user interface for managing tasks.



- **Contents**:

  - `main()`: This is the main function of the script that serves as the entry point for the application. It displays a menu with options for adding tasks, listing tasks, completing tasks, and quitting the application. It also handles user input and calls the corresponding functions based on the user's choice.



  - `add_task(task_list, task_description)`: This function adds a new task to the task list. It takes a task description as input and appends a dictionary representing the task (including its description and completion status) to the `task_list`.



  - `list_tasks(task_list)`: This function lists all the tasks in the `task_list`. It displays the task descriptions and their completion statuses.



  - `complete_task(task_list, task_index)`: This function marks a task as completed based on its index in the `task_list`. It updates the completion status of the selected task.



### `test_project.py`



- **Description**: This file contains unit tests for the Task Manager's functions. It ensures that each function behaves as expected and maintains code quality by catching bugs or regressions.



- **Contents**:

  - `test_add_task()`: This function tests the `add_task` function. It creates an empty task list, adds a task to it, and then checks whether the task list contains the added task with the correct description and completion status.



  - `test_list_tasks(capsys)`: This function tests the `list_tasks` function. It creates a task list with a sample task, captures the standard output using `capsys`, and checks if the output matches the expected task listing.



  - `test_complete_task()`: This function tests the `complete_task` function. It creates a task list with an incomplete task, marks the task as completed, and then checks whether the task's completion status is updated correctly.



These files and functions work together to provide the core functionality of the Task Manager application. The `project.py` script handles user interaction and task management, while the `test_project.py` script ensures the reliability and correctness of the functions through unit tests.



## Features



### 1. Add Task



- Users can add new tasks by providing a task description.



### 2. List Tasks



- Users can view a list of all their tasks, including their descriptions and completion status.



### 3. Complete Task



- Tasks can be marked as completed, helping users track their progress.



### 4. Quit



- Exit the application when your are done.



## Installation



1. Clone the repository:



   ```bash

   git clone https://github.com/me50/ManikantaReddy-13.git

   cd project

   

2. pip install -r requirements.txt



##Usage



1. To run the Task Manager, execute the following command:

   

   python project.py

   

2. Follow the on-screen menu to perform various operations on your tasks.



##Design Choices



 In developing the Task Manager, several design choices were made to ensure simplicity and ease of use:



1. Command-Line Interface (CLI): We chose a command-line interface for its simplicity and platform independence. Users can interact with the Task Manager through a text-based interface, making it accessible to a wide range of users.



2. Minimalistic Features: The Task Manager focuses on essential task management features, keeping the interface uncluttered and user-friendly. We believe that a minimalist approach enhances usability.



3. Test-Driven Development (TDD): The project was developed following test-driven development principles. This ensures that each component is thoroughly tested, resulting in a reliable and robust application.



The Task Manager is designed to simplify your task management, making it easy to stay organized and on top of your to-do list. We hope you find it useful in your daily tasks and projects!



For a detailed demonstration of the Task Manager, watch the Demo Video.
