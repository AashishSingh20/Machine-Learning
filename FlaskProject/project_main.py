from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

# Setting a secret key for encrypting session data
app.secret_key = 'aashish1234'

# Dictionary to store user and password
users = {
    'Aashish' : '1234',
    'Lokesh' : '4321'
}

# To render the login form
@app.route('/')
def view_form():
    return render_template('login.html')

@app.route('/handle_get', methods = ['GET'])  # This method is a GET method
def handle_get():
    if request.method == 'GET':     # In this method I can see username and password in url tab
        username = request.args['username'] 
        password = request.args['password']
        print(username,password)

        if username in users and users[username] == password:
            return render_template('welcome.html', username = username)
        else:
            return '<h1> Invalid Credentials!</h1>'
    else:
        return render_template('login.html')  # If the method is not get then return login.html page 
    

@app.route('/handle_post', methods = ['POST'])  # This method is a POST method
def handle_post():
    if request.method == 'POST':       # In this method I can't see username and password in url tab
        username = request.form['username']
        password = request.form['password']
        print(username,password)

        if username in users and users[username] == password:
            return render_template('welcome.html', username = username)
        else:
            return '<h1> Invalid Credentials!</h1>'
    else:
        return render_template('login.html')  # If the method is not get then return login.html page 

if __name__ == "__main__":
    app.run(debug=True)