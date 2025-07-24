from bson import ObjectId
from datetime import datetime

class TaskModel:
    def __init__(self, mongo):
        self.tasks = mongo.db.tasks

    def add_task(self, username, task_text, start_date=None, end_date=None):
        # If start_date or end_date are provided, make sure they are in proper datetime format
        if start_date:
            start_date = self.format_date(start_date)
        if end_date:
            end_date = self.format_date(end_date)
        
        task = {
            "username": username,
            "task": task_text,
            "completed": False,
            "start_date": start_date,
            "end_date": end_date
        }
        self.tasks.insert_one(task)

    def get_tasks(self, username):
        return list(self.tasks.find({"username": username}))

    def complete_task(self, task_id):
        self.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": {"completed": True}})

    def delete_task(self, task_id):
        self.tasks.delete_one({"_id": ObjectId(task_id)})

    def get_completion_percentage(self, tasks):
        if not tasks:
            return 0
        completed = sum(1 for task in tasks if task["completed"])
        return round((completed / len(tasks)) * 100)

    def format_date(self, date_string):
        """
        Takes a string date in 'YYYY-MM-DD' or 'YYYY-MM-DDTHH:MM' format
        and returns a datetime object.
        """
        try:
            # Check for date with time (ISO 8601 format: 'YYYY-MM-DDTHH:MM')
            if "T" in date_string:
                return datetime.strptime(date_string, "%Y-%m-%dT%H:%M")
            # Otherwise, just a date
            return datetime.strptime(date_string, "%Y-%m-%d")
        except ValueError:
            # If the date is not in the expected format, return None or handle it as needed
            return None
