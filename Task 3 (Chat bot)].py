import random
import time

now = time.ctime()
qna = {
    "hi": "hey",
    "how are you": "I am fine",
    "what is your name": "my name is Dell Laptop",
    "what is your age": "My age is not limited because of AI",
    "what is the time now": now,
    "good" : "Thanks for appreciation",
    "nice" : "Thanks for appreciation",
    "quit" : "Goodbye!",
    "by" : "Goodbye!",
    "ok" : "Goodbye!"
}

print("Welcome to ChatBot AI:")
while True:
    qs = input("You: ")
    if qs in  qna:
        response = qna[qs]
        print("Bot:", response)
        if qs in  ["quit","ok","by"]:
            break
    else:
        print("Bot: Sorry, I didn't understand that.")