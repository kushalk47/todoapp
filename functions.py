def read_todos(file_name="todo.txt"):
    """Reads the tasks from the file and returns them as a list."""
    try:
        with open(file_name, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def write_todos(todos, file_name="todo.txt"):
    """Writes the list of tasks to the file."""
    with open(file_name, "w") as file:
        file.writelines(todos)