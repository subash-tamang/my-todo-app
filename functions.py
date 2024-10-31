FILEPATH = "todos.txt"


def get_todos(file_path=FILEPATH):
    """
    Read a text file and return the list of
    to-do items.
    """
    with open(file_path, "r") as file:
        todos_local = file.readlines()
    return todos_local


# print(help(get_todos))


def write_todos(todos_arg, file_path=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(file_path, "w") as file_local:
        file_local.writelines(todos_arg)


# print(__name__)
if __name__ == "__main__":
    print("hello")
