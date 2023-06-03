import random
def capitalsQuiz(totalcorrect, totalincorrect, states):
    print("Welcome to the Capitals Quiz!")

    if(states == []):
        states=[
            {
                "name": "Alabama",
                "capital": "Montgomery"
            },
            {
                "name": "Alaska",
                "capital": "Juneau"
            },
            {
                "name": "Arizona",
                "capital": "Phoenix"
            }
        ]

    random.shuffle(states)

    for state in states:
        print(f'What is the capital of this state: {state["name"]}')
        if(("correct" in state) == False):
            state["correct"] = 0
        if(("incorrect" in state) == False):
            state["incorrect"] = 0



        userInput = input()
        userInput = userInput.capitalize()
        if(userInput == state["capital"]):
            totalcorrect += 1
            state["correct"] += 1
            print("Correct!")
            print(f'You have gotten this state right {state["correct"]} times and wrong {state["incorrect"]} times!')
            print(f'Total Correct Answers: {totalcorrect} Total Incorrect Answers: {totalincorrect}')

        else:
            totalincorrect += 1
            state["incorrect"] += 1
            print("Incorrect :(")
            print(f'You have gotten this state right {state["correct"]} times and wrong {state["incorrect"]} times!')
            print(f'Total Correct Answers: {totalcorrect} Total Incorrect Answers: {totalincorrect}')

    print("Would you like to play again?")
    userInput = input()
    if(userInput == "yes"):
        capitalsQuiz(totalcorrect, totalincorrect, states)
    else:
        print(f'Thanks for playing! Total Scores: --Correct: {totalcorrect}-- --Incorrect: {totalincorrect}--')



capitalsQuiz(0,0,[])