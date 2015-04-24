from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi!</title>
        </head>
        <body>
            <p>Hi! This is the home page.</p>
            <a href="/hello">This links to hello</a>
        </body>
    </html>

    """
# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/greet">
                <label style="color: red">What's your name? <input type="text" name="person"></label>
    
                <br>
                <br>
                <label>Compliment <select name="compliment">
                    <option value="Nice">Nice</option>
                    <option value="Awesome">Awesome</option>
                    <option value="Great">Great</option>
                    <option value="Smart">Smart</option>
                    </select>
                </label>
                
                <br>
                <br>
                <label>Favorite City: </label>  
                    <label><input type="radio" name="city" value="San Francisco">San Francisco</label>
                    <label><input type="radio" name="city" value="New York">New York</label>
                    <label><input type="radio" name="city" value="Miami">Miami</label>
                
                <br>
                <br>
                <input type="submit">

            </form>
        </body>
    </html>

    """

@app.route('/greet')
def greet_person():
    player = request.args.get("person","Shabnam")
    compliment = request.args.get("compliment","nice")
    city = request.args.get("city","DC")

    # AWESOMENESS = [
    #     'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    #     'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    # compliment = choice(AWESOMENESS)

    return """

    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi %s I think you're %s! You live in %s!
        </body>
    </html>""" % (player, compliment, city)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
