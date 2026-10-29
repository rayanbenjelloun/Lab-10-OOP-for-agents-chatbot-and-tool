# my_tool.py
# Author: Rayan Benjelloun


class TrainingSchedule:
    """A tool that stores soccer training schedules."""

    def __init__(self, sessions):
        """Store the training sessions."""
        self.sessions = sessions

    def find_group(self, text):
        """Find an age group mentioned in a message."""
        message = text.lower()
        for group in self.sessions:
            if group.lower() in message:
                return group
        return None

    def get_session(self, group):
        """Return the schedule for an age group."""
        return self.sessions.get(group)
