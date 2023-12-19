#!/usr/bin/python3
"""Trivia Question"""

import pprint
from random import randint
import requests

base_url = "https://opentdb.com/api.php?"

def main():

    print("Welcome! I'm going to give you some trivia questions. Are you ready?")
    print("How many questions do you want?")
    amount = input(">>> ")

    print("How difficult do you want to questions? (easy, medium, or hard)")
    difficulty = input(">>> ")

    trivia = requests.get(base_url + f"amount={amount}&difficulty={difficulty}").json()

    question = trivia.get('results')[randint(0, int(amount) - 1)]["question"]

    #print(trivia, amount, difficulty)
    #pprint.pprint(trivia.get("results"))

    #print(question)
    for result in trivia["results"]:
        print(result.get("question"))
        print(result.get("correct_answer"))


if __name__ == "__main__":
    main()


