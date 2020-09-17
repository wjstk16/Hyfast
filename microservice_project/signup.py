from flask import Flask, render_template, json, request

from werkzeug.security import generate_password_hash
from db_manager import call_db_manager


app = Flask(__name__)

@app.route('/')
def main():
    id_num=1
    return render_template('signup.html' , id_num = id_num)

@app.route('/signUp',methods=['POST'])
def signUp():



    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    _phonenumber = request.form['inputPhonenumber']

    _hashed_password = generate_password_hash(_password)

    if _name and _email and _password and _phonenumber:
        booltype = call_db_manager('sp_createUser' , (_name, _email, _hashed_password , _phonenumber))
        if booltype:
            return json.dumps({'message': 'User created successfully !'})
        else:
            return json.dumps({'error': _name})

    else:
         return json.dumps({'html': '<span>Enter the required fields</span>'})





if __name__ == "__main__":
    app.run(host = '0.0.0.0' ,port=5000)