def add_task(tasks, task_name):
    tasks.append(task_name)
    return tasks

# Example usage:
tasks = ["Task 1", "Task 2", "Task 3"]
new_task_name = "Task 4"
tasks = add_task(tasks, new_task_name)
print("Tasks after adding:", tasks)
