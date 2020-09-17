from flask import Flask, render_template, json, request , redirect , url_for , session
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from mydb import mysql
from db_manager import call_db_manager


app = Flask(__name__)


@app.route('/')
def showLogin():
    return render_template('login.html')


@app.route('/validateLogin', methods=['POST'])
def validateLogin():
    try:
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']

        data = call_db_manager('sp_validateLogin' ,(_username ,))
        print(data)
        if len(data) > 0:
            if check_password_hash(str(data[0][3]), _password):

                return redirect('http://microdcn.com/userHome/' + str(data[0][1]))

            else:
                return render_template('error.html', error='Wrong Email address or Password.')
        else:
            return render_template('error.html', error='Wrong Email address or Password.')


    except Exception as e:
        return render_template('error.html', error=str(e))


@app.route('/logout')
def logout():
    return redirect('/')

if __name__ == "__main__":
    app.run(host = '0.0.0.0' ,port=5000)
