from TaskManager import TaskManager

manager = TaskManager()
manager.newTask('сделать уборку', 4)
manager.newTask('помыть посуду', 4)
manager.newTask('отдохнуть', 1)
manager.newTask('поплавать в бассейне', 3)
print(manager)
manager.newTask('поесть', 2)
manager.newTask('учиться', 2)
print(manager)

