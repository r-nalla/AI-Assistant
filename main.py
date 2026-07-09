print("====================================")
print(" Welcome to AI Assistant ")
print(" Type 'exit' to stop ")
print("====================================")

while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        print("AI Assistant: Bye dude, good work today!")
        break

    elif user_message.lower() == "hi":
        print("AI Assistant: Hello! 👋")

    elif user_message.lower() == "how are you":
        print("AI Assistant: I'm doing great! 😄")

    elif user_message.lower() == "bye":
        print("AI Assistant: See you later! 👋")

    else:
        print("AI Assistant: Sorry, I don't understand.")
        