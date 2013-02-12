import datetime

class Task:

    priority = ""
    contexts = []
    projects = []
    original = ""
    text = ""
    date = None
    done = False
    date_done = None

    def __init__(self, task_string):
        """
        """
        pass
    
class TaskList:

    tasks = []

    def __init__(self, task_file):
        """
        """
        pass
    
    def by_priority(self, priority):
        """
        Return a TaskList of the tasks filtered by the priorities
        """
        return TaskList([])

    def by_context(self, context):
        """
        Return a TaskList of the tasks filtered by the context
        """
        return TaskList([])

    def by_project(self, project):
        """
        Return a TaskList of the tasks filtered by the project
        """
        return TaskList([])
    
    def __iter__(self):
        return self.tasks.__iter__()
