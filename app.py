from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
  url = 'https://raw.githubusercontent.com/crencricca/datasets/master/EU-GDP.csv'
  df = pd.read_csv(url)
  if request.method == 'POST':
      if request.form.get('Submit') == 'Submit':
        print("Getting year " + request.form['Year'])
      else:
        print("Oops :(")
  return render_template('index.html', form="form")

if __name__ == "__main__":
  app.run(debug=True)
  