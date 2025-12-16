from datetime import datetime

class Record:
    def __init__(self, record_id, name, age, course):
        self.record_id = record_id
        self.name = name
        self.age = age
        self.course = course
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_list(self):
        """Convert record to list for saving in CSV"""
        return [self.record_id, self.name, self.age, self.course, self.created_at]
