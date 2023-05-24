def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("-------------------")
        print(key)
        for i in options[question_num - 1]:
            # 2 for  the increase of question number is for the outer  for loop
            print(i)
        guess = input("Enter A,B,C,D:")
        # equivalent to system out print and then assign it to String
        guess = guess.upper()
        guesses.append(guess)
        check_answer(questions.get(key), guess)
        # before going to the next question
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)


# --------------------


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
        # means you got the point
    else:
        print("Wrong!")
        return 0


# --------------------


def display_score(correct_guesses, guesses):
    print("--------------------")
    print("RESULTS:")
    print("--------------------")
    print("Answers:", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("Guesses:", end="")
    for i in guesses:
        print(i, end="")
    print()
    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is :" + str(score) + "%")


# --------------------


def play_again():
    response = input("Do you want to play again?(yes or no)")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False



# --------------------


# creating dictionary which has key value question
questions = {
    "Who created python?": "A",
    "What a year was python created?": "B",
    "Python was tribute to which comedy group?": "C",
    "Is the earth round?": "D"
}
# create 2 D list for the answers
options = [["A. Guido van Ross", "B. Elon Musk", "C. Bill Gates", "D. Mark ZuckerBurg"],
           ["A. 1998", "B. 1991", "C. 2000", "D. 2016"],
           ["A. lonely island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. Sometimes", "D. what is earth"]]
new_game()
while play_again():
    new_game()
print("Byeeeee!")
