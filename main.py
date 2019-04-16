from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True




@app.route("/validation", methods=['POST'])
def validation():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    

    email_error = request.args.get("email_error")
    username_error = request.args.get("username_error")
    password_error = request.args.get("password_error")
    v_password_error = request.args.get("v_password_error")

    email_error = ""
    username_error = ""
    password_error = ""
    v_password_error = ""



    if " " in username:
        username_error = "This is not a valid username"
        
    
    if len(username) <3 or len(username) >20:     
        username_error = "This is not a valid username"
        
    if username == "":    
        username_error = "This is not a valid username"
          
    
    if " " in password:
        
        password_error = "This is not a valid password"
        
    
    if len(password) <3 or len(password) >20:
        
        password_error = "This is not a valid password"
        
    
    if password == "":
        
        password_error = "This is not a valid password"
        
    
    if password != verify_password:
        
        v_password_error = "Passwords do not match"
        
    
    if verify_password == "":
        
        v_password_error = "Passwords do not match"
        
    if email == "":
        email = email
    else: 
        if len(email) < 3 or len(email) >20:
            email_error = "The email has to be between 3 and 20 characters."
        elif "@" not in email or "." not in email:
            email_error = "This is not a valid email"
        elif " " in email:
            email_error = "This is not a valid email"
        
    
    if not email_error and not username_error and not password_error and not v_password_error:
        return render_template("welcome.html", username=username)
    else:
        return render_template('index.html', username_error = username_error, password_error = password_error, v_password_error = v_password_error, email_error=email_error, username=username, email=email)


@app.route("/")
def index():
    
    return render_template('index.html')

app.run()
