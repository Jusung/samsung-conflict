todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"'{task}' added to the list!")
    
# 실행 예제
add_task("Learn Python")
add_task("Do Git practice")
show_tasks()
remove_task(0)
show_tasks()