# my_main.py
# Author: Rayan Benjelloun

from my_assistant import SoccerAssistant
from my_tool import TrainingSchedule

SESSIONS = {
    "u12": "Monday at 5 PM",
    "u15": "Tuesday at 6 PM",
    "u18": "Thursday at 7 PM",
}

training_tool = TrainingSchedule(SESSIONS)

bot = SoccerAssistant("CoachBot", training_tool)

print("Welcome to the Soccer Academy!")
print("Type a message, or type quit to stop.")

user_message = input("You: ")

while user_message != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
