from flask import Flask, render_template, json, request , redirect , url_for , session
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from mydb import mysql
from db_manager import call_db_manager


app = Flask(__name__)


@app.route('/<id_num>')
def showSearch(id_num):
    return render_template('search.html' , id_num = id_num)


@app.route('/search/<id_num>',methods=['POST'])
def search(id_num):
    _title = request.form['inputtitle']
    strdata = request.form['inputsearch']
    fildata = request.form['inputfilter']

    if _title:
        datas = json.dumps(call_db_manager('sp_noneFilter' ,(_title ,)))
        print(datas)
        return render_template('searchRes.html' , datas=datas)
    elif strdata and fildata==0 :
        datas = json.dumps(call_db_manager('sp_filter', (_title,)))
        return render_template('searchRes.html', datas=datas)
    elif strdata and fildata==1 :
        datas = json.dumps(call_db_manager('sp_filterOrderPop', (_title,)))
        return render_template('searchRes.html', datas=datas)
    elif strdata and fildata==2 :
        datas = json.dumps(call_db_manager('sp_filterOrderPrice', (_title,)))
        return render_template('searchRes.html', datas=datas)
    elif strdata and fildata==3 :
        datas = json.dumps(call_db_manager('sp_filterOrderDate', (_title,)))
        return render_template('searchRes.html', datas=datas)





if __name__ == "__main__":
    app.run(host = '0.0.0.0' ,port=5000)