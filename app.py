from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

SERVICES = [
  {
  'id': 1,
  'title': 'Window Cleaning',
  'description': 'Cleaning windows in the house',
  'cost': '$50.00'
  
},
  {'id':2,
  'title':'Post-construction cleaning',
  'description':'Cleaning windows in the house',
  'cost':'$100.00'
             
  }
]

@app.route("/")
def home():
  return render_template('home.html',
                         services = SERVICES)
  
@app.route("/booking")
def booking():
  return render_template('booking.html')


@app.route('/contact')
def contact():
  return render_template('contact.html')
  
if__name__="__main__"
app.run(host='0.0.0.0',debug=True)
