from flask import Flask, render_template

#referencing this file
app = Flask(__name__)

#create an index route so that when we browse to the url we don't immediately get 404
@app.route('/')
def index():
    #return "Hello World!"
    return render_template('index.html') #don't need to specify the template folder

if __name__ == "__main__":
    app.run(debug = True) #debug=True pops up error on the page itself
