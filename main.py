from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def defintion(word):
     reuslt_dictionary = {"defintion": (word.upper()), 
                          "word": word}
                          
     return (reuslt_dictionary)

app.route
if __name__ == "__main__":
    app.run(debug=True)