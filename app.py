from flask import render_template, Flask, request
from Moudles import get_data

app = Flask(__name__)
value = 'a'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/loginpage', endpoint='loginpage')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'], endpoint='login')
def check():
    global value

    User = request.form['username']
    Pass = request.form['password']

    if User == '' or Pass == '':
        return render_template('login(Failed).html')

    response = get_data(User)

    if response[len(response)-1] == Pass:
        job = get_data(User)
        return render_template('student.html')
    else :
        return 'اشتباه'

if __name__ == "__main__":
    app.run()