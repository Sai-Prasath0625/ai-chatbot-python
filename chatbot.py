print("AI Chatbot (type 'bye' to exit)")
print("-----------------------------------")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I'm just code, but I'm doing great!")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intellingence.")

    elif user == "your name":
        print("Bot: I'm your simple AI chatbot.")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand. Try another question.")
