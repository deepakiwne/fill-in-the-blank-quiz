from __future__ import print_function

def play_game(in_string, blanks, answers, limit):

    """
    Game loop
    Asks user about each blank and handles user response
    """

    for blank in blanks:
        index = in_string.find(blank)
        
        try_left = limit
        user_answer_correct = False

        while(not user_answer_correct and try_left > 0):
            user_answer = ask_user("\n\nWhat should be substituted in for " + blank + "? ")
            
            if user_answer == answers.get(blank):
                in_string = handle_correct_response(in_string, user_answer, blank)
                user_answer_correct = True
            else:
                try_left -= 1

                if try_left == 0:
                    return False
                
                handle_wrong_response(in_string, try_left)

            print(in_string)

    return True

def handle_correct_response(in_string, user_answer, blank):

    """
    Handles correct response from user
    """
    
    print("\nCorrect!" + "\n\n\nThe current paragraph reads as such:\n")
    return in_string.replace(blank, user_answer)

def handle_wrong_response(in_string, try_left):

    """
    Handles incorrect response from user
    """
    
    print("That isn't the correct answer!", end='')

    if try_left == 1:
        print(" You only have 1 try left!  Make it count! \n")
    else:
        print(" Let's try again; you have " + str(try_left) + " trys left! \n")

    print("The current paragraph reads as such: \n")
    print(in_string)

def ask_user(question):

    """
    Print question on console and return user response
    """

    user_input = raw_input(question)
    type(user_input)
    return user_input.lower()

def get_user_option():
    
    """
    Allows users to select a game difficulty mode

    """

    option = -1
    while(option == -1):
        print("Please select a game difficulty by typing it in!")
        print("Possible choices include easy, medium, and hard.")
        user_input = ask_user("")

        if (user_input == "easy" or user_input == "e" or user_input == "1"):
            option = 1
        elif (user_input == "medium" or user_input == "m" or user_input == "2"):
            option = 2
        elif (user_input == "hard" or user_input == "h" or user_input == "3"):
            option = 3
        else:
            print("That's not an option!")

    return option

def get_user_try_limit():

    """
    Allows users to input the limit for wrong guesses

    """

    limit = -1
    while not (limit >= 1 and limit <=10):
        print("Please enter limit for wrong guesses!")
        print("Possible range is 1 to 10")
        user_input = ask_user("")

        try:
            limit = int(user_input)
        except ValueError:
            print("This is not an integer!")
            continue

        if (limit < 1 or limit > 10):
            print("The limit is out of range!")

    return limit

easy_question = '''A common first thing to do in a language is display
'Hello __1__!'  In __2__ this is particularly easy; all you have to do
is type in:
__3__ "Hello __1__!"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the __3__ command, and
produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an __4__ file in a browser, but it's
a step in learning __2__ syntax, and that's really its purpose.'''

easy_blanks = ["__1__", "__2__", "__3__", "__4__"]

easy_answers = {
    "__1__" : "world",
    "__2__" : "python",
    "__3__" : "print",
    "__4__" : "html"
}

medium_question = '''A __1__ is created with the def keyword.  You specify the inputs a
__1__ takes by adding __2__ separated by commas between the parentheses.
__1__s by default returns __3__ if you don't specify the value to retrun.
__2__ can be standard data types such as string, integer, dictionary, tuple,
and __4__ or can be more complicated such as objects and lambda functions.'''

medium_blanks = ["__1__", "__2__", "__3__", "__4__"]

medium_answers = {
    "__1__" : "function",
    "__2__" : "arguments",
    "__3__" : "none",
    "__4__" : "list"
}

hard_question = '''When you create a __1__, certain __2__s are automatically
generated for you if you don't make them manually. These contain multiple
underscores before and after the word defining them.  When you write
a __1__, you almost always include at least the __3__ __2__, defining
variables for when __4__s of the __1__ get made.  Additionally, you generally
want to create a __5__ __2__, which will allow a string representation
of the method to be viewed by other developers.

You can also create binary operators, like __6__ and __7__, which
allow + and - to be used by __4__s of the __1__.  Similarly, __8__,
__9__, and __10__ allow __4__s of the __1__ to be compared
(with <, >, and ==).'''

hard_blanks = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__", "__7__", "__8__", "__9__", "__10__"]

hard_answers = {
	"__1__" : "class",
	"__2__" : "method",
	"__3__" : "__init__",
	"__4__" : "instance",
    "__5__" : "__repr__",
    "__6__" : "__add__",
    "__7__" : "__sub__",
    "__8__" : "__lt__",
    "__9__" : "__gt__",
    "__10__" : "__eq__",
}

option = get_user_option()

question = None
blanks = None
answers = None

if option == 1:
    print("You've chosen easy! \n")
    question = easy_question
    blanks = easy_blanks
    answers = easy_answers
elif option == 2:
    print("You've chosen medium! \n")
    question = medium_question
    blanks = medium_blanks
    answers = medium_answers
elif option == 3:
    print("You've chosen hard! \n")
    question = hard_question
    blanks = hard_blanks
    answers = hard_answers

try_limit = get_user_try_limit()

print("You will get " + str(try_limit) + " guesses per problem \n")
print("The current paragraph reads as such: \n")

print(question)

game_success = play_game(question, blanks, answers, try_limit)

if game_success:
    print("You won!")
else:
    print("You've failed too many straight guesses!  Game over!")