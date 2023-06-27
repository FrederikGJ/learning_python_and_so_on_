from flask import Flask, render_template
from main import Main
import pandas as pd 
import plotly
import plotly.express as px
import json


app = Flask(__name__)

@app.route('/')
def home(): 
    main = Main()
    
    total_negative = main.total_negative
    total_positive = main.total_positive

    total_word = [["Negative ord", total_negative],["Postitive ord", total_positive]]

    data_frame = pd.DataFrame(total_word, columns=['Type', 'Count'])

    figure = px.bar(data_frame, x='Type', y='Count', barmode='group')
    
    graphJSON = json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', total_negative=total_negative, total_positive=total_positive, graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True)
