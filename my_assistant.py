# my_assistant.py
# Author: Rayan Benjelloun

HANDOFF_WORDS = ["register", "payment", "cancel"]


class SoccerAssistant:
    """A mock assistant for a soccer training academy."""

    def __init__(self, name, training_tool):
        """Store the assistant's name, tool, and conversation history."""
        self.name = name
        self.training_tool = training_tool
        self.history = []

    def respond(self, user_message):
        """Record the user message and the assistant's reply."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a reply based on keywords."""
        text = user_message.lower()

        if self.needs_human(text):
            return "Please contact our staff for registration or payment help."

        if "training" in text or "schedule" in text:
            return self.training_reply(user_message)

        if "hello" in text:
            return f"Hello! I'm {self.name}. I can help with soccer training schedules."

        return "I'm not sure how to help with that. I can check training schedules."

    def needs_human(self, text):
        """Check whether a staff member is needed."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def training_reply(self, user_message):
        """Use the training tool to find a schedule."""
        group = self.training_tool.find_group(user_message)

        if group is None:
            return "Which age group? I can check U12, U15, or U18."

        session = self.training_tool.get_session(group)
        return f"Training for {group} is {session}."
