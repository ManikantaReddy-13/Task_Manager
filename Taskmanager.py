# Initializing an empty task list

task_list = []



def main():

    print("Welcome to Task Manager!")



    while True:

        print("\nMenu:")

        print("1. Add Task")

        print("2. List Tasks")

        print("3. Complete Task")

        print("4. Quit")



        choice = input("Enter your choice: ")



        if choice == "1":

            task_description = input("Enter task description: ")

            add_task(task_list, task_description)

        elif choice == "2":

            list_tasks(task_list)

        elif choice == "3":

            list_tasks(task_list)

            task_index = int(input("Enter the index of the task to mark as completed: "))

            complete_task(task_list, task_index)

        elif choice == "4":

            print("Goodbye!")

            break

        else:

            print("Invalid choice. Please try again.")



def add_task(task_list, task_description):

    task_list.append({"description": task_description, "completed": False})

    print(f"Task '{task_description}' added successfully.")



def list_tasks(task_list):

    if not task_list:

        print("No tasks found.")

    else:

        print("Tasks:")

        for i, task in enumerate(task_list):

            status = "Completed" if task["completed"] else "Not Completed"

            print(f"{i+1}. {task['description']} - {status}")



def complete_task(task_list, task_index):

    if task_index >= 1 and task_index <= len(task_list):

        task_list[task_index - 1]["completed"] = True

        print("Task marked as completed.")

    else:

        print("Invalid task index.")



if __name__ == "__main__":

    main()

