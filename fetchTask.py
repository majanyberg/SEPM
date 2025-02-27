import random
from typing import Optional, List, Tuple

class Task:
    def __init__(self, task_id: int, exercise_id: int, level_id: int, content: str):
        self.task_id = task_id
        self.exercise_id = exercise_id
        self.level_id = level_id
        self.content = str(content)

class fetchTask:
    def __init__(self, backend):
        self.backend = backend

    def fetchTask(self, exercise_id: int, level_id: int, subset_size: int = 5) -> Tuple[Optional[List[Task]], Optional[str]]:
        # Check level access
        if not self.backend.is_level_unlocked(level_id):
            return None, "Complete previous tasks to unlock this."

        # Fetch and filter tasks
        all_tasks = self.backend.get_all_tasks()
        attempted_tasks = self.backend.user_progress["attempted_tasks"]
        
        eligible_tasks = [
            task for task in all_tasks
            if task.exercise_id == exercise_id
            and task.level_id == level_id
            and task.task_id not in attempted_tasks
        ]

        if not eligible_tasks:
            return None, "No exercises available. Please try later."

        # Shuffle and select subset
        random.shuffle(eligible_tasks)
        selected_tasks = eligible_tasks[:subset_size]

        # Persist attempted tasks
        self.backend.log_attempted_tasks([t.task_id for t in selected_tasks])

        return selected_tasks, None

