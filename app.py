from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/services')
def service():
    return render_template('services.html')

@app.route('/contacts')
def contact():
    return render_template('contacts.html')
    
if __name__ == '__main__':
    app.run(debug=True)