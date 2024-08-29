class UserInput:
    __choices = ['add', 'update', 'delete', 'mark-in-progress', 'mark-done', 'list']
    __list_options = {'done', 'todo', 'in-progress', 'default'}
    __ACTION = None
    __TITLE = None
    __NEW_TITLE = None
    __TASK_ID = None

    def __init__(self):
        arguments = self.__user_input()
        self.__OPERATION = arguments.operation
        self.__action_id = arguments.action
        self.__new_title = arguments.new_title
        self.__set_all_values()

    @property
    def OPERATION(self):
        return self.__OPERATION

    @property
    def ACTION(self):
        if self.OPERATION == 'add':
            return self.__TITLE
        return self.__TITLE if self.__TITLE is not None else self.__TASK_ID

    @property
    def NEW_TITLE(self):
        if self.OPERATION == 'update':
            return self.__NEW_TITLE

    @staticmethod
    def __user_input():
        import argparse
        my_parser = argparse.ArgumentParser(description="To-Do List CLI")
        my_parser.add_argument("operation", choices=UserInput.__choices, help="Choose an operation")
        my_parser.add_argument("action", nargs="?", default="default")
        my_parser.add_argument("new_title", nargs="?", default=" ")
        return my_parser.parse_args()

    def __set_all_values(self):

        if self.OPERATION[0] == "l":
            self.__set_list_values()

        if self.OPERATION[0] == "a":
            self.__set_add_values()

        if self.OPERATION[0:2] in {'up', 'de', 'ma'}:
            self.__set_other_values()

    def __set_list_values(self):
        list_option = self.__action_id
        if list_option not in UserInput.__list_options and list_option is not None:
            print("Valid Queries for listing Tasks are {}".format(", ".join(UserInput.__list_options)))
            return
        UserInput.__TITLE = list_option
        return

    def __set_add_values(self):
        title = self.__action_id
        if len(title) > 4:
            UserInput.__TITLE = title
            return
        print("Please Give the Task Title of more than 4 characters")

    def __set_other_values(self):
        try:
            task_id = int(self.__action_id)
            if self.OPERATION == 'update':
                if self.__new_title and self.__new_title != '':
                    UserInput.__TASK_ID = task_id
                    UserInput.__NEW_TITLE = self.__new_title
                    return

                print("Please Give the New Task Title")

            UserInput.__TASK_ID = task_id
            return
        except ValueError:
            print("Invalid Task ID")


if __name__ != "__main__":
    user_input = UserInput()
