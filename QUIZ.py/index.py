def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score(correct_guesses, guesses):
    print("------------------------------")
    print("RESULTS")
    print("------------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


def play_again():

    response = input("DO you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


questions = {
    "Who was the second Prime Minister of Israel?": "A",
    "Who was israel's sixth prime minister?": "B",
    "Who was the Chief of Staff of the Israel Defense Forces during the Yom Kippur War?": "C",
    "Who was the Chief of Staff of the Sixth Israel Defense Forces of the State of Israel?": "D",
    "Who was the chief of staff in the first Israel Defense Forces": "C"
}

options = [["A.Moshe Sharett", "B.David Ben-Gurion", "C.Theodor Herzl", "D.Chaim Weizmann"],
           ["A.Robin Williams", "B.Golda Meir", "C.Hayim Nahman Bialik", "D.Noshe Zuriel"],
           ["A.Shlomo Haim Artzi", "B.Chaim Weizmann", "C.David Elazar", "D.Shari Zuriel"],
           ["A.Mordechai Maklef", "B.Mordechai Gur", "C.Shlomo Haim Artzi", "D.Tzvi Tzur"],
           ["A.Shlomo Baraba", "B.Mordechai Maklef", "C.Yaakov Dori", "D.Shari Zuriel"]]


new_game()

while play_again():
    new_game()