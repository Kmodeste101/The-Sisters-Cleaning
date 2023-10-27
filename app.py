from flask import Flask

app = Flask(__name__)

@app.route("/") #creates the  / for when you move between pages on the websites url
def hello_world():
  return"Modeste, Bonjour!"
print(__name__)

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)