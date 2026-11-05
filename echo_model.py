# echo_model.py
# Author: Rayan Benjelloun


class EchoModel:
    """A model that returns the last message. It does not use any AI."""

    def reply(self, instructions, history):
        """Return the last message in the history."""
        last_message = history[-1]["content"]
        return f"You said: {last_message}"
