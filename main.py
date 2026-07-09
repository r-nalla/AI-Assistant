print("====================================")
print(" Welcome to AI Assistant ")
print(" Type 'exit' to stop ")
print("====================================")

while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        print("AI Assistant: Bye dude, good work today!")
        break

    print(f"AI Assistant: You said '{user_message}'")