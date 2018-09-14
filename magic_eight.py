import random

def ask_question():
    question = input("What is your question? ")
    answers = ["It is certain.","It is decidedly so.","Without a doubt.","Yes-definitely.","You may rely on it.","As I see it, yes.", "Most likely.","Outlook good.","Yes.","Ask again later.","Reply hazy, try again","Concentrate and ask again","Don't count on it.","Very doubtful","My sources say no"]
    return random.choice(answers)
