from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")


@app.route('/result', methods=["GET","POST"])
def user_result():
    name = request.form['name']
    location = request.form['location']
    favlang = request.form['favlang']
    comment = request.form['comment']
    print (request.form)
    if request.method == "POST":
      return render_template("result.html", name=request.form['name'], location=request.form['location'], language = request.form['favlang'], comment = request.form['comment'])
    else:
      return redirect("index.html")
    
    

if __name__=='__main__':
    app.run(debug=True)
