class todo:
    def main(self):
     tasks = []

     while True:
         print("\n===== To-Do List =====")
         print("1. Add Task")
         print("2. Show Tasks")
         print("3. Mark Task as Done")
         print("4. Exit")

         choice = input("Enter your choice: ")

         if choice == '1':
             print()
             try:
                n_tasks = int(input("How many tasks do you want to add: "))
                for i in range(n_tasks):
                    task = input("Enter the task: ").strip()
                    if task:
                        tasks.append({"task": task, "done": False})
                        print("Task added!")
                    else:
                        print("Task cannot be empty.")
                
             except ValueError:
                print("Invalid input. Please enter a number.")

         elif choice == '2':
            print("\nTasks:")
            if not tasks:
                print("No tasks found.")
            else:
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - {status}")

         elif choice == '3':
            try:
                task_index = int(input("Enter the task number to mark as done: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]["done"] = True
                    print("Task marked as done!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

         elif choice == '4':
            print("Exiting the To-Do List.")
            break

         else:
            print("Invalid choice. Please try again.")

cls=todo()
cls.main()