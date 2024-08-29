import json
from datetime import datetime

from backend.ToDoBackEnd.loggers import get_my_logger


def info_logger(function):
    def wrapper(self, *args, **kwargs):
        all_to_dos = function(self, *args, **kwargs)
        my_logger = get_my_logger()
        my_logger.info("Database Available")
        return all_to_dos

    return wrapper


class UserToDo:
    def __init__(self, task_id=0, description="No Task Found for ID: "):
        datetime_now = datetime.now()
        datetime_now_str = datetime_now.strftime("%d/%m/%Y %H:%M:%S")
        self.task_id: int = task_id
        self.description: str = description
        self.status: str = "todo"
        self.created_at: str = datetime_now_str
        self.updated_at: str = datetime_now_str


class ToDoBackEnd:
    @info_logger
    def load_database(self):
        try:
            with open("database.json", 'r') as toDo:
                toDos = json.load(toDo)
            return toDos
        except FileNotFoundError:
            get_my_logger().info("Creating Database File")
            with open("database.json", 'w') as toDo:
                user_to_do = UserToDo()
                default_data = {
                    0: {
                        "task_id": user_to_do.task_id,
                        "description": user_to_do.description,
                        "status": user_to_do.status,
                        "created_at": user_to_do.created_at,
                        "updated_at": user_to_do.updated_at
                    }
                }
                json.dump(default_data, toDo)
            return json.dumps(default_data)

    @staticmethod
    def save_task(**kwargs):
        with open("database.json", 'r') as toDo:
            toDos = json.load(toDo)
        next_task_id = max([int(some_id) for some_id in toDos.keys()]) + 1
        new_todo = UserToDo(task_id=next_task_id, description=kwargs['description'])
        data = {
            "task_id": new_todo.task_id,
            "description": new_todo.description,
            "status": new_todo.status,
            "created_at": new_todo.created_at,
            "updated_at": new_todo.updated_at
        }
        with open("database.json", 'w') as toDo:
            toDos[next_task_id] = data
            new_todo_data = toDos
            json.dump(new_todo_data, toDo)
        return data

    @staticmethod
    def update_task(*args):
        with open("database.json", 'r') as toDo:
            toDos = json.load(toDo)
        task_id = args[0]
        key = args[1]
        value = args[2]
        todo = toDos.get(str(task_id), toDos.get("0"))
        if int(todo["task_id"]):
            with open("database.json", 'w') as toDo:
                todo[f"{key}"] = value
                todo["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                toDos[str(todo['task_id'])] = todo

                new_todo_data = toDos
                json.dump(new_todo_data, toDo)
                return todo
        else:
            return todo["description"] + str(task_id)

    @staticmethod
    def delete_task(task_id):
        with open("database.json", 'r') as toDo:
            toDos = json.load(toDo)
        try:
            toBeDeleted = toDos[str(task_id)]
        except KeyError:
            return {"detail": f"No Task Found For ID: {str(task_id)}"}

        if toBeDeleted:
            with open("database.json", 'w') as toDo:
                toDos.pop(str(task_id))
                json.dump(toDos, toDo)
                return "Task deleted with id " + str(task_id)

        return "No task with id " + str(task_id)

    @staticmethod
    def filter(term):
        if term in {'done', 'todo', 'in-progress', 'default'}:
            with open("database.json", 'r') as toDo:
                toDos = json.load(toDo)
                if term == 'default':
                    return None
            results = {k: v for k, v in toDos.items() if v['status'] == term and v['task_id'] != 0}
            return results
        return {"detail": f"Unknown Term"}


if __name__ != "__main__":
    my_backend = ToDoBackEnd
