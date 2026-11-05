# my_main.py
# Author: Rayan Benjelloun

from my_assistant import SoccerAssistant
from my_tool import TrainingSchedule
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are CoachBot, a support assistant for the Soccer Academy.
Answer in one short sentence.
The academy is located at 100 Soccer Lane.
Players should bring cleats, shin guards, and a water bottle.
Only state facts that appear in these instructions.
If you do not know, say you do not know and offer to pass the customer to a staff member."""

SESSIONS = {
    "u12": "Monday at 5 PM",
    "u15": "Tuesday at 6 PM",
    "u18": "Thursday at 7 PM",
}

training_tool = TrainingSchedule(SESSIONS)
model = OllamaModel(MODEL_NAME)

bot = SoccerAssistant("CoachBot", INSTRUCTIONS, training_tool, model)

print("Welcome to the Soccer Academy!")
print("Type a message, or type quit to stop.")

user_message = input("You: ")

while user_message != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
