from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('home.html')
  
@app.route("/booking")
def booking():
    return render_template('booking.html')
  
if__name__="__main__"
app.run(host='0.0.0.0',debug=True)
