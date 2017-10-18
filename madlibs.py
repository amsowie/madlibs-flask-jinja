"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/game')
def show_madlib_form():
    """Direct user from yes/no to game page or goodbye"""
    game_choice = request.args.get("gamebutton")

    if game_choice == 'no':
        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():
    """Show madlib with user input in it"""
    person = request.args.get("person")
    color = request.args.get("color")
    noun1 = request.args.get("noun1")
    noun2 = request.args.get("noun2")
    noun3 = request.args.get("noun3")
    verb = request.args.get("verb")
    animal = request.args.get("animal")
    adjective_list = request.args.getlist("adjectives")

    # import pdb; pdb.set_trace()

    default_adjectives = ["funny", "cute", "nice", "smelly", "short"]

    while len(adjective_list) < 3:
        adjective_list.append(choice(default_adjectives))

    adjective_list = sample(adjective_list, 3)
    # count = 0
    # adjectives_dict = {}
    # for adjective in range(len(adjective_list)):
    #     key = "adjective" + str(count)
    #     adjectives_dict[key] = adjective
    #     count += 1
    options = ["madlib.html", "madlib1.html"]
    return render_template(choice(options),
                           person=person,
                           color=color,
                           noun1=noun1,
                           noun2=noun2,
                           noun3=noun3,
                           verb=verb,
                           animal=animal,
                           adjectives=adjective_list,)


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
