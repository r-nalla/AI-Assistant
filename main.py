def ai_reply(message):
    print("AI Assistant: ", message)
print("====================================")
print(" Welcome to AI Assistant ")
print(" Type 'exit' to stop ")
print("====================================")

while True:
    user_message = input("You: ")
    message = user_message.lower()

    if message == "exit":
        ai_reply("Bye dude, good work today!")
        break

    elif message == "hi":
        ai_reply("Hello! 👋")

    elif message == "how are you":
        ai_reply("I'm doing great! 😄")

    elif message == "bye":
        ai_reply("See you later! 👋")

    else:
        ai_reply("Sorry, I don't understand.")
        