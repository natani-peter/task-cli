# task-cli

# How To Use 
install from the requirement file 
then interact with the system
through commands like
# Adding a new task
py task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
py task-cli update 1 "Buy groceries and cook dinner"
py task-cli delete 1

# Marking a task as in progress or done
py task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
py task-cli list

# Listing tasks by status
py task-cli list done
py task-cli list todo
py task-cli list in-progress