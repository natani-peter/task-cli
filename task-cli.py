from backend.ToDoBackEnd.userinput import user_input
from backend.ToDoBackEnd.UserTransaction import my_backend


class Main:
    OPERATION = user_input.OPERATION
    ACTION = user_input.ACTION
    NEW_TITLE = user_input.NEW_TITLE

    def __init__(self):
        self.initialise_database()
        self.__feed_back = self.do_operation()

    @classmethod
    def initialise_database(cls):
        cls.DATABASE_TASKS = my_backend().load_database()

    @property
    def feed_back(self):
        return self.__feed_back

    def do_operation(self):
        operation = self.OPERATION
        task_id = self.ACTION
        title = self.ACTION
        status = self.ACTION if self.ACTION or self.ACTION is None else "UnKnown"
        new_title = self.NEW_TITLE

        if self.OPERATION == "add":
            new_todo = my_backend().save_task(description=title)
            return {"message": "Task added Successfully", "new_todo": new_todo}

        if self.OPERATION == "list":
            if status:
                results = my_backend().filter(status)
                if results is not None:
                    return results

                return {"data": {k: v for k, v in self.DATABASE_TASKS.items() if int(k) > 0}}

        if self.OPERATION == "update":
            updated_todo = my_backend().update_task(task_id, "description", new_title)
            return {"data": updated_todo}

        if self.OPERATION[0:2] in {"ma", "de"}:
            if self.OPERATION[0:2] == "ma":
                status_choice = "done" if operation == "mark-done" else "in-progress"

                updated_todo = my_backend().update_task(task_id, "status", status_choice)

                return {"data": updated_todo}

            return my_backend().delete_task(task_id)


if __name__ == "__main__":
    values = Main()
    print(" ")
    print(values.feed_back)
    print(" ")
