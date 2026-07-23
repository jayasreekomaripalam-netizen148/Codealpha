def chatbot():
    print("🤖 ChatBot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! How can I help you?")
        elif user == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user == "what is your name":
            print("Bot: I'm a simple Python ChatBot.")
        elif user == "help":
            print("Bot: You can say hello, how are you, or bye.")
        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()