# tests/test_my_assistant.py

from mock_model import MockModel
from my_assistant import SoccerAssistant
from my_tool import TrainingSchedule


def make_assistant():
    """Create a fresh soccer assistant for each test."""
    sessions = {
        "u12": "Monday at 5 PM",
        "u15": "Tuesday at 6 PM",
        "u18": "Thursday at 7 PM",
    }
    tool = TrainingSchedule(sessions)
    return SoccerAssistant("CoachBot", "Be friendly.", tool, MockModel())


def test_training_schedule():
    bot = make_assistant()
    reply = bot.respond("What is the U15 training schedule?")
    assert reply == "Training for u15 is Tuesday at 6 PM."


def test_unknown_age_group():
    bot = make_assistant()
    reply = bot.respond("What is the U19 training schedule?")
    assert "Which age group?" in reply


def test_registration_goes_to_human():
    bot = make_assistant()
    reply = bot.respond("I want to register")
    assert "staff" in reply


def test_unknown_question():
    bot = make_assistant()
    reply = bot.respond("What is your favorite color?")
    assert "not sure" in reply


def test_conversation_history():
    bot = make_assistant()
    bot.respond("hello")
    bot.respond("What is the U12 training schedule?")
    assert len(bot.history) == 4


class SilentModel:
    """Stand in for a model that cannot answer."""

    def reply(self, instructions, history):
        # Return None so we can test the assistant's safe reply.
        return None


def test_other_messages_go_to_model():
    bot = make_assistant()
    assert bot.respond("hello") == "Hello! How can I help you today?"


def test_safe_reply_when_model_has_no_answer():
    tool = TrainingSchedule({"u15": "Tuesday at 6 PM"})
    bot = SoccerAssistant("CoachBot", "Be friendly.", tool, SilentModel())
    assert bot.respond("hello") == (
        "Sorry, I can't answer that right now. Please contact our staff."
    )
