def run_baseline_chatbot():
    print("Simple NLP Chatbot")
    print("Type 'exit' to quit")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break
        print("Bot: I am learning NLP concepts!")


if __name__ == "__main__":
    run_baseline_chatbot()
