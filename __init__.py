from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

my_absolute_path = r'C:\Users\hello\project3\flask_app\__init__.py'

with open(my_absolute_path, 'rb') as pickle_file:
    model = pickle.load(pickle_file)

@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    temp = [[data1, data2, data3, data4, data5]]
    test_df = pd.DataFrame(data=temp, columns=['발생시','발생지시도','가해자법규위반','가해자_당사자종별','피해자_당사자종별'])
    result = model.predict(test_df)
    pred = int(result)
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)
