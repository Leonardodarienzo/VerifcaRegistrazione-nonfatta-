from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
  return render_template("index.html")  

@app.route('/register', methods=['POST'])
def register():
  nome = request.form['name']
  username = request.form['username']
  cognome = request.form['cognome']
  password = request.form["password"]
  passwordC = request.form["passwordC"]
  email = request.form["email"]
  permission = request.form["consenso"]
  data = request.form["data"]

  if password == passwordC and str.find(email, "@"):
    return render_template("register.html", nm=nome, cm=cognome, ps=password, email=email, permission=permission, username=username, data=data)
  elif password != passwordC:
    return render_template("errore.html", input="password")
  elif not str.find(email, "@"):
    return render_template("errore.html", input="email")

@app.route('/errore', methods=['POST', 'GET'])
def errore():
  return render_template("errore.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)