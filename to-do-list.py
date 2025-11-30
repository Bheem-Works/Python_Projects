def main():
    tasks = []

    while True:
        print("\n=== to - do - list ==")
        print("1. add task")
        print("2. show tasks")
        print("3. mark task as done")
        print("4. exit")

        choice = inpu("Enter the choice : ")

        if choice == '1':
            print()
            n_tasks = int(input("how many tasks you want to add : "))

            for i in range(n_tasks):
                task = input("Enter the tasks: ")
                tasks.append({"task": task, "done",False})
                print("Task added")

            elif choice == '2':
                print("\n_tasks : ") 
                for index,task in enumerate(tasks):
                    status = "Done " if task['done'] else "Not Done"
                    print(f"{index + 1},{task['task']} - {status}")

            elif choice == '3':
                task_index = int(input("Enter the tasks number to mark as done : "))
                if 0 <= task_index < len(tasks):
                    tasks[task_index]["done"] = True
                    print("Taks marked as done")
                else:
                    print("invalid tasks number ")
            
            elif choice == '4':
                print("exiting the to-d0-list.")
                break
            else:
                print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()
