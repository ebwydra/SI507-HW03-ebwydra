def ask_question():
    question = ""
    while question != "quit":
        question = input("What is your question? ")
        if question == "quit":
            print("Goodbye.")
        elif question[-1] != "?":
            print("I'm sorry, I can only answer questions.")
    return question
