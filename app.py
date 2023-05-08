# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Anish Anil" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father_webpage():
    name = "Father"
    return render_template("father.html",index_variable=name)
app.run(debug=True)
# define the route to mother webpage
@app.route("/mother")
def mother_webpage():
    name = "Mother"
    return render_template("mother.html",index_variable=name)
app.run(debug=True)
# define the route to friends webpage
@app.route("/friend")
def friends_webpage():
    name = "Friends"
    return render_template("friend.html", index_variable=name)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
