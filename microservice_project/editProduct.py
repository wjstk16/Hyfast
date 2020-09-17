from flask import Flask, render_template, json, request , redirect , url_for , session
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from mydb import mysql
from db_manager import call_db_manager
import io , os , uuid


app = Flask(__name__)


@app.route('/showAddProduct/<id_num>')
def showAddProduct(id_num):
    return render_template('addProduct.html' , id_num = id_num)


@app.route('/addProduct/<id_num>',methods=['GET' , 'POST'])
def addProduct(id_num):
    if request.method == 'POST':

        _title = request.form['inputTitle']
        _description = request.form['inputDescription']
        _user_id = id_num
        _state = request.form['inputState']
        _price = request.form['inputPrice']
        if len(request.form.get('filePath'))==0:
            _filePath = 'http://microdcn.com:9002/static/Uploads/noimage.png'
        else:
            _filePath = request.form.get('filePath')
        if len(request.form.get('filePath2'))==0:
            _filePath2 = 'http://microdcn.com:9002/static/Uploads/noimage.png'
        else:
            _filePath2 = request.form.get('filePath2')
        if len(request.form.get('filePath3'))==0:
            _filePath3 = 'http://microdcn.com:9002/static/Uploads/noimage.png'
        else:
            _filePath3 = request.form.get('filePath3')

        data = (_title, _description, _user_id , _state , _price , _filePath , _filePath2 , _filePath3)

        print(data)



        if _title and _description and _user_id and _state and _price:
            booltype = call_db_manager('sp_addWish' , data)
            if booltype:

            # return json.dumps({'message': 'Add product successfully !'})
            # return render_template(''  , id_num = id_num)
            # return redirect('http://microdcn.com:3000/userHome/' + id_num)
                return render_template('s_add.html'  , id_num = id_num)


            else:
                return json.dumps({'error': _title})


        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})

    else:
        return render_template('s_add.html', id_num=id_num)



@app.route('/updateProduct/<id_num>' , methods=['POST'])
def updateProduct(id_num):


    _user = id_num
    _title = request.form['title']
    _description = request.form['description']
    _p_id = request.form['id']
    _filePath = request.form['filePath']

    booltype = call_db_manager('sp_updateProduct' , (_title, _description , _p_id , _user , _filePath))

    if booltype :
        # return render_template('s_update.html' , id_num=id_num)
        return json.dumps({'status': 'OK'})
    else:
        # return render_template('f_updata.html' , id_num = id_num)

        return json.dumps({'status': 'ERROR'})


@app.route('/deleteProduct/<id_num>', methods=['POST'])
def deleteProduct(id_num):


            _id = request.form['id']
            _user = id_num

            booltype = call_db_manager('sp_deleteProduct' , (_id, _user))

            if booltype:

                return json.dumps({'status': 'OK'})
            else:


                return json.dumps({'status': 'ERROR'})

@app.route('/like/<id_num>', methods=['POST'])
def like(id_num):

    _id  = request.form['id']
    _user = id_num
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#')
    print(_id)
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#')
    booltype = call_db_manager('sp_AddUpdateLikes', (_id, _user))
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#')

    if booltype:

        return json.dumps({'status': 'OK'})
    else:

        return json.dumps({'status': 'ERROR'})








if __name__ == "__main__":
    app.run(host = '0.0.0.0' ,port=5000)