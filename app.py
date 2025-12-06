from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "demo_secret_key"

# Title
@app.route('/')
def index():
    return render_template('index.html')

# greet router
@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return render_template('greet.html', name=name)

# About page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
