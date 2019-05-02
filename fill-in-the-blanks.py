# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

def find_blank(word, blanks):
    for pos in blanks:
        if pos in word:
            return pos
    return None

def play_game(in_string, blanks, answers):
    for blank in blanks:
        index = in_string.find(blank)
        
        if index != -1:
            try_left = 5
            user_answer_correct = False
            while(not user_answer_correct and try_left > 0):
                user_answer = ask_user("What should be substituted in for " + blank + "? ")
                if user_answer == answers.get(blank):
                    in_string = in_string.replace(blank, user_answer)
                    user_answer_correct = True
                else:
                    try_left -= 1
                    print("That isn't the correct answer!  Let's try again; you have " + str(try_left) + " trys left!")
            print(in_string)

        else:
            return

# Ask the user functionality
def ask_user(question):
	user_input = raw_input(question)
	type(user_input)
	return user_input

def get_user_option():
    option = -1
    while(option == -1):
        print("Please select a game difficulty by typing it in!")
        print("Possible choices include easy, medium, and hard.")
        user_input = ask_user("")

        if user_input == "easy":
            option = 1
        elif user_input == "medium":
            option = 2
        elif user_input == "hard":
            option = 3
        else:
            print("That's not an option!")

    return option

easy_blanks = ["___1___", "___2___", "___3___", "___4___"]
easy_answers = {
	"___1___" : "function",
	"___2___" : "arguments",
	"___3___" : "none",
	"___4___" : "list"
}

medium_blanks = ["___1___", "___2___", "___3___", "___4___"]
medium_answers = {
	"___1___" : "function",
	"___2___" : "arguments",
	"___3___" : "none",
	"___4___" : "list"
}

hard_blanks = ["___1___", "___2___", "___3___", "___4___"]
hard_answers = {
	"___1___" : "function",
	"___2___" : "arguments",
	"___3___" : "none",
	"___4___" : "list"
}

option = get_user_option()

blanks = None
answers = None
if option == 1:
    print("You've chosen easy!")
    blanks = easy_blanks
    answers = easy_answers
elif option == 2:
    print("You've chosen medium!")
    blanks = easy_blanks
    answers = easy_answers
elif option == 3:
    print("You've chosen hard!")
    blanks = easy_blanks
    answers = easy_answers

play_game(sample, blanks, answers)

