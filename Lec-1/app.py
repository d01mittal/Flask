from flask import Flask

app=Flask(__name__)

@app.route("/")   #Creating an endpoint
@app.route("/home")
def home():
    return "<h1>Welcome to the Home Page!</h1>"


@app.route("/welcome/<name>")  #Creating a path parameter "name"
def welcome(name):
    return f"<h1>Hi {name.title()}, you're welcome to this Page!</h1>"


@app.route("/addition/<int:num>")  #Creating a path parameter "num" (int type)
def addition(num):
    return f"<h1>Input is {num}, Output is {num+10}</h1>"


@app.route("/addition_two/<int:num1>/<int:num2>")  #Creating two path parameters
def addition_two(num1, num2):
    return f"<h1>{num1} + {num2} is {num1+num2}</h1>"


@app.route("/about")
def about():
    return "<h1>Welcome to the About Page!</h1>"


if __name__=="__main__":
    app.run(debug=True)
