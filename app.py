from flask import Flask, render_template
app = Flask(__name__) # initialize

@app.route('/')
def home():
    return render_template('home.html') 

@app.route("/tab_test")
def tab_test():
    return render_template("tab_test.html")

app.run()