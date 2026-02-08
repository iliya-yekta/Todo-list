import os

# Sample text file: t.txt
def choice_ToDo_list(t):
    file_path = str(input("Enter name (press e to exit): "))
    
    if file_path != 'e':
        try:        
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    # Readlines method to read all lines of the file(returns a list of strings)
                    for i in f.readlines():
                        if i == "" or i == "\n": continue
                        r = i.split(" ")
                        # Append existed tasks to temporary database
                        t.append((int(r[0]), r[3], False) if r[6] == 'not' else (int(r[0]), r[3], True))
                    print("Completed")
                return file_path
            else:
                print("File doesn't exist. Try again")
                choice_ToDo_list(t)
                return None
        except FileNotFoundError:
            print("File not found")
        # When cannot read the file for any reason
        except PermissionError:
            print("Permission denied")
        except Exception:
            print("Something went wrong. Try again...")
    else:
        return None

def show_ToDo_list():
    try:
        with open(file_path, 'r') as f:
            for i in f:
                print(i.strip())
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Something went wrong. Try again")


def add_task():
        task_name = input("Enter the task name: ").strip()
        tasks_stat.append((count, task_name, False))
        edit()
        print(f"Task '{task_name}' has added")

# Rewrite the file
def edit():
    j = 0
    with open(file_path, "w+") as f:
        while j<len(tasks_stat):
            f.write(f"{tasks_stat[j][0]} | task: {tasks_stat[j][1]} | condition: {"completed" if tasks_stat[j][2] == True else "not completed"}\n")
            j += 1

def complete_task():
    task_name = input("Enter the task name to mark as completed: ").strip()
    for i in range(len(tasks_stat)):
        if tasks_stat[i][1] == task_name:
            tasks_stat[i] = (tasks_stat[i][0], tasks_stat[i][1], True)
            print(f"Task '{task_name}' marked as completed")



    again = str(input("Do you want any change? "))
    complete_task() if again.lower() == "yes" or again.lower() == "y" else edit()

def show_completed_tasks():
    return list(filter(lambda x: x[2] == True, tasks_stat))

def remove_task():
    task_name = input("Enter the task name to remove: ").strip()
    for i in range(len(tasks_stat)):
        if task_name == tasks_stat[i][1]:
            index = i
            tasks_stat.pop(i)
            for i in range(index, len(tasks_stat)):
                tasks_stat[i] = (tasks_stat[i][0]-1, tasks_stat[i][1], tasks_stat[i][2])
            print(f"Task '{task_name}' has removed")
            edit()
            break
        



def main():
    # Temporary databases
    global tasks_stat, file_path, count
    file_path = None
    tasks_stat = []
    # Task number
    count = 0
    while 1:
        print("""
              1 -> choice ToDo list file            5 -> complete task
              2 -> show the ToDo list               6 -> show completed tasks
              3 -> add task                         7 -> exist
              4 -> remove task
            """)
        try:
            choice = int(input("■ Enter command: "))
            # Match case instead of multiple if-elif statements
            match(choice): 
                case 1:
                        # Refresh temporary database
                        tasks_stat = []
                        # The file path
                        file_path = choice_ToDo_list(tasks_stat) 
                        count = int(tasks_stat[-1][0]) if len(tasks_stat) > 0 else 0

                case 2: show_ToDo_list() if file_path != None else print("Enter the file path first")
                case 3: 
                    if file_path != None:
                        # Refresh the count
                        count = len(tasks_stat)
                        count+=1
                        add_task()
                    else:
                        print("Enter the file path first")
                case 4: remove_task() if file_path != None else print("Enter the file path first")
                case 5: complete_task() if file_path != None else print("Enter the file path first")
                case 6: print(show_completed_tasks() if file_path != None else "Enter the file path first")
                case 7: break
                case _:
                    print("Invalid choice. Enter the number from 1 to 6")
        except ValueError:
            print("The command should be a number")
        except Exception:
            print("Something went wrong. Try again...")

main()