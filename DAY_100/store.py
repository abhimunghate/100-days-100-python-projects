from dataclasses import asdict, dataclass

@dataclass
class Task:
    id: int
    title: str
    completed: bool = False
    
    def to_dict(self):
        return asdict(self)
    
class TaskStore:
    def __init__(self):
        self.tasks = {
            1: Task(1, "Plan the Day 100 release"),
            2: Task(2, "Record the final course demo", True)
        }
        
    def list(self):
        return [task.to_dict() for task in self.tasks.values()]
    
    def create(self, title):
        if not title.strip():
            raise ValueError("Task title is required")
        
        task = Task(max(self.tasks, default=0) + 1, title.strip())
        self.tasks[task.id] = task
        return task.to_dict()
    
    def toggle(self, task_id):
        task = self.tasks.get(task_id)
        if not task:
            raise LookupError("Task not found")
        
        task.completed = not task.completed
        return task.to_dict()
    
# Done