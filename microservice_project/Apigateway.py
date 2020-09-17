from flask import Flask, render_template , redirect , request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def Base():
    # id_num = request.args.get('id_num' ,  '')
    return render_template('index.html')
#메인화면용 index와 상속용 index 따로만들것.


@app.route('/showLogin')
def Login():
    return render_template('index_login.html')

@app.route('/showSignUp')
def Signin():
    # requests.get('http://192.168.12.252:5002/')
    return render_template('index_signup.html')

@app.route('/userHome')
def UserHome():
    return render_template('userHome.html')

@app.route('/userHome/<id_num>')
def UserHome_id(id_num ):
    return render_template('userHome.html' , id_num = id_num)
#메인화면용 userHome과 상속용 따로만들것.

@app.route('/showAddProduct/<id_num>')
def AddProduct(id_num):
    return render_template('index_addProduct.html' , id_num = id_num)

@app.route('/logout')
def logout():
    return redirect('http://microdcn.com/login/logout')

@app.route('/myList/<id_num>')
def myList(id_num):
    return render_template('index_myList.html', id_num = id_num)

@app.route('/dashboard/<id_num>')
def dashboard(id_num):
    return render_template('index_dashboard.html', id_num = id_num)

@app.route('/update/<id_num>' , methods=['POST'])
def update(id_num):

    return redirect('http://microdcn.com/editProduct/updateProduct/' + id_num)

@app.route('/delete/<id_num>' , methods=['POST'])
def delete(id_num):

    return redirect('http://microdcn.com/editProduct/deleteProduct/' + id_num)


@app.route('/showSearch/<id_num>')
def search(id_num):
    return render_template('index_search.html' , id_num=id_num)


@app.route('/detail/<id_num>/<p_id>/')
def detail(id_num , p_id ):
    # return render_template('detail.html' ,   id_num=id_num , p_id=p_id)
    return redirect('http://microdcn.com/getList/' + id_num +'/'+ p_id)

@app.route('/test/<id_num>')
def search22(id_num):
    return render_template('test.html' , id_num=id_num)

@app.route('/tests/<id_num>')
def search223(id_num):
    return render_template('s_add.html' , id_num=id_num)








if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

