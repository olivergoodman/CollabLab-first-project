#first flask server
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    author = "Olly Goodman"
    name = "you"
    var = "blah"
    return render_template('index.html', author=author, name=name, var=var)

app.run(debug=True)

if __name__ == "__main__":
    app.run()





