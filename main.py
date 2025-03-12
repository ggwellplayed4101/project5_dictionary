from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def defintion(word):
     
    df = pd.read_csv("dictionary.csv")
    definition = df.loc[df['word'] == word.strip()]['definition'].squeeze()
    print(definition)

    reuslt_dictionary = {"word": word,
                         "defintion": (definition)}
                          
    return (reuslt_dictionary)

app.route
if __name__ == "__main__":
    app.run(debug=True)