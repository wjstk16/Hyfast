from flask import Flask, render_template, json, request

from werkzeug.security import generate_password_hash
from db_manager import call_db_manager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/<id_num>')
def dash(id_num):
    return render_template('dashboard.html' , id_num=id_num)




@app.route('/getList/<id_num>')
def getList(id_num):

    data = call_db_manager('sp_getList' , (id_num,))
    return json.dumps(data)


@app.route('/getTimeList/<id_num>'  , methods=['POST'])
def getTimeList(id_num):

    _total_records = 0
    _offset = request.form['offset']

    data = call_db_manager('sp_getTimeList' , (_offset,  _total_records))

    return json.dumps(data)


@app.route('/getListByUser/<id_num>'  , methods=['POST'])
def getUserList(id_num):

    _total_records = 0
    _offset = request.form['offset']

    data = call_db_manager('sp_GetListByUser' , (id_num ,_offset,  _total_records))

    return json.dumps(data)



@app.route('/showMyList/<id_num>')
def showMyList(id_num):
    return render_template('myList.html' , id_num = id_num)

@app.route('/showDashboard/<id_num>')
def showDashboard(id_num):
    return render_template('dashboard.html' , id_num = id_num)


@app.route('/getProductById/<id_num>' ,methods=['POST'])
def getWishById(id_num):

            _id = request.form['id']
            _user = id_num
            data = call_db_manager('sp_GetProductById' , (_id, _user))
            product_data = []
            product_data.append({'product_id':data[0][0],'product_title':data[0][1],'product_description':data[0][2] , 'product_file_path' : data[0][7] })

            return json.dumps(product_data)

@app.route('/getDashboard/<id_num>'  )
def getDash(id_num):


    data = call_db_manager('sp_getProductByLike' , (id_num,))
    return json.dumps(data)

@app.route('/<id_num>/<p_num>')
def showSearch(id_num , p_num):

    data = call_db_manager('sp_GetProductById' , (p_num , id_num))
    print(data[0][0])



    return render_template('detail.html' , id_num = id_num , product_id=data[0][0] ,product_title=data[0][1],product_description=data[0][2],product_user_id=data[0][3],product_date=data[0][4],product_state=data[0][5],product_price=data[0][6],product_file_path=data[0][7] ,product_file_path2=data[0][8] , product_file_path3=data[0][9])

if __name__ == "__main__":
    app.run(host = '0.0.0.0' ,port=5000)



