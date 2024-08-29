# TASK CLI APP

#### How To Use 
implementing https://roadmap.sh/projects/task-tracker
install from the requirement file 
then interact with the system
through commands like
#### Adding a new task
```shell
py task-cli.py add "Buy groceries"
```
 Output: Task added successfully (ID: 1)

#### Updating and deleting tasks
```shell
py task-cli.py update 1 "Buy groceries and cook dinner"
py task-cli.py delete 1
```

#### Marking a task as in progress or done
```shell
py task-cli.py mark-in-progress 1
py task-cli.py mark-done 1
```

#### Listing all tasks
```shell
py task-cli.py list
```
#### Listing tasks by status
```shell
py task-cli.py list done
py task-cli.py list todo
py task-cli.py list in-progress
```
