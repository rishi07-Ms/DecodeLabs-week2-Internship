import random
import datetime
import os
import time

# =========================
# Typing Effect Function
# =========================
def typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

# =========================
# Save Chat History
# =========================
def save_chat(user, bot):
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write(f"You: {user}\n")
        file.write(f"Bot: {bot}\n\n")
# =========================
# Greeting Responses
# =========================
greetings = [
    "Hello there 😊",
    "Hi! Nice to meet you 🚀",
    "Hey! How can I help you today?",
    "Greetings human 🤖"
]

# =========================
# Motivation Responses
# =========================
motivations = [
    "Success starts with consistency 💡",
    "You are stronger than you think 💪",
    "Every expert was once a beginner 🌟",
    "Small progress every day matters 🚀"
]

# =========================
# Joke Responses
# =========================
jokes = [
    "Why do programmers hate nature? Too many bugs 😆",
    "Why did Python go to school? To improve its class 😂",
    "Why do Java developers wear glasses? Because they can't C 😎"
]

# =========================
# Mood Responses
# =========================
sad_responses = [
    "Tough times don't last 💙",
    "Everything will be okay 🌈",
    "Believe in yourself ✨"
]

happy_responses = [
    "That's amazing 😄",
    "I love your positivity 🌟",
    "Keep smiling 😊"
]

# =========================
# Welcome Screen
# =========================
print("=" * 60)
print("🤖          INTELLIBOT PRO - AI ASSISTANT")
print("=" * 60)

name = input("\nEnter your name: ")

typing_effect(f"\nHello {name}! I am IntelliBot Pro 🤖")
typing_effect("Your smart AI assistant is now online.")
typing_effect("Type 'help' to see available commands.\n")

# =========================
# Main Chat Loop
# =========================
while True:

    user_input = input(f"{name}: ").lower().strip()

    # Exit
    if user_input in ["exit", "bye", "quit"]:
        bot_reply = "Goodbye! Have a wonderful day 🌟"
        typing_effect(f"Bot: {bot_reply}")
        save_chat(user_input, bot_reply)
        break

    # Greetings
    elif user_input in ["hello", "hi", "hey"]:
        bot_reply = random.choice(greetings)
        typing_effect(f"Bot: {bot_reply}")

    # How are you
    elif "how are you" in user_input:
        bot_reply = "I am functioning perfectly 🚀"
        typing_effect(f"Bot: {bot_reply}")

    # Name
    elif "your name" in user_input:
        bot_reply = "I am IntelliBot Pro, your AI assistant 🤖"
        typing_effect(f"Bot: {bot_reply}")

    # Motivation
    elif "motivation" in user_input:
        bot_reply = random.choice(motivations)
        typing_effect(f"Bot: {bot_reply}")

    # Sad Mood
    elif "sad" in user_input:
        bot_reply = random.choice(sad_responses)
        typing_effect(f"Bot: {bot_reply}")

    # Happy Mood
    elif "happy" in user_input:
        bot_reply = random.choice(happy_responses)
        typing_effect(f"Bot: {bot_reply}")

    # Joke
    elif "joke" in user_input:
        bot_reply = random.choice(jokes)
        typing_effect(f"Bot: {bot_reply}")

    # Current Time
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        bot_reply = f"Current time is {current_time}"
        typing_effect(f"Bot: {bot_reply}")

    # Current Date
    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        bot_reply = f"Today's date is {current_date}"
        typing_effect(f"Bot: {bot_reply}")

    # Calculator Feature
    elif "calculate" in user_input:
        try:
            expression = user_input.replace("calculate", "")
            result = eval(expression)
            bot_reply = f"Result = {result}"
            typing_effect(f"Bot: {bot_reply}")
        except:
            bot_reply = "Invalid calculation ❌"
            typing_effect(f"Bot: {bot_reply}")

    # Help Menu
    elif user_input == "help":
        bot_reply = """
📌 AVAILABLE COMMANDS

• hello / hi / hey
• how are you
• your name
• motivation
• sad
• happy
• joke
• time
• date
• calculate 5 + 10
• exit

"""
        typing_effect(bot_reply)

    # Unknown Input
    else:
        unknown_replies = [
            "Sorry, I don't understand that yet 🤔",
            "Can you say that differently?",
            "Interesting... tell me more 👀",
            "I'm still learning new things 🚀"
        ]

        bot_reply = random.choice(unknown_replies)
        typing_effect(f"Bot: {bot_reply}")

    # Save Chat
    save_chat(user_input, bot_reply)

# =========================
# End Message
# =========================
print("\nChat history saved successfully 📁")
print("Thank you for using IntelliBot Pro 🤖")