from flask import Flask, render_template
from main import Main

app = Flask(__name__)

@app.route('/')
def home():
    main = Main()
    total_negative = main.total_negative
    total_positive = main.total_positive

    return render_template('index.html', total_negative=total_negative, total_positive=total_positive)

if __name__ == "__main__":
    app.run()

