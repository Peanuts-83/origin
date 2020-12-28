from employee import Employee
from datetime import datetime

class Manager(Employee):
    """
    Doc
    """
    def __init__(self, name, email_address, title, phone_number=''):
        super().__init__(name, email_address, title, phone_number)
        self.meetings = []

    def schedule_meeting(self, invitees, meeting_time):
        self.meetings.append({'invitees': invitees, 'time': meeting_time})
        self.meetings.sort(key = lambda x: x['time'])

    def run_next_meeting(self):
        return self.meetings.pop(0)



