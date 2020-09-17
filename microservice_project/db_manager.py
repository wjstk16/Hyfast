from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from mydb import mysql
from flask import Flask


app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'hj'
app.config['MYSQL_DATABASE_HOST'] = '192.168.12.230'
mysql.init_app(app)



def call_db_manager(procedure , tuple):
    conn = mysql.connect()
    cursor = conn.cursor()
    if procedure == 'sp_validateLogin':
        cursor.callproc('sp_validateLogin', tuple)
        data = cursor.fetchall()
        return data

    elif procedure == 'sp_createUser':
        cursor.callproc('sp_createUser' , tuple)
        data = cursor.fetchall()
        if len(data) is 0:
            conn.commit()
            return True
        else:
            return False

    elif procedure == 'sp_addWish':
        cursor.callproc('sp_addWish' , tuple)
        data = cursor.fetchall()
        if len(data) is 0:
            conn.commit()
            return True
        else:
            return False
    elif procedure == 'sp_getUser':
        cursor.callproc('sp_getUser' , tuple)
        data = cursor.fetchall()
        return data

    elif procedure == 'sp_getList':
        cursor.callproc('sp_getList' , tuple)
        wishes = cursor.fetchall()
        wishes_dict = []
        for wish in wishes:
            wish_dict = {
                'product_id': wish[0],
                'product_title': wish[1],
                'product_description': wish[2],
                'product_user_id': wish[3],
                'product_date' : wish[4],
                'product_state': wish[5],
                'product_price': wish[6],
                'product_file_path' : wish[7]
            }

            wishes_dict.append(wish_dict)


        return wishes_dict
    elif procedure == 'sp_getTimeList':
        cursor.callproc('sp_getTimeList' , tuple)
        wishes = cursor.fetchall()
        cursor.close()
        cursor = conn.cursor()
        cursor.execute('SELECT @_sp_getTimeList_1')
        vivivi = cursor.fetchall()


        wishes_dict = []
        response = []
        for wish in wishes:
            wish_dict = {
                'product_id': wish[0],
                'product_title': wish[1],
                'product_description': wish[2],
                'product_user_id': wish[3],
                'product_date': wish[4],
                'product_state': wish[5],
                'product_price': wish[6],
                'product_file_path': wish[7],
                'product_sum_like' : wish[8],
                'product_user_like' : wish[9]
            }

            wishes_dict.append(wish_dict)
        response.append(wishes_dict)
        response.append({'total' : vivivi[0][0]})
        print( "##############################################################################################################################################################################################")
        print(wishes_dict)

        return response

    elif procedure == 'sp_GetProductById':

        cursor.callproc('sp_GetProductById', tuple)
        data = cursor.fetchall()
        return data

    elif procedure == 'sp_updateProduct':
        cursor.callproc('sp_updateProduct' , tuple)
        print('hear@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print(tuple)
        data =  cursor.fetchall()

        if len(data) is 0:
            conn.commit()
            return True
        else:
            return False

    elif procedure == 'sp_deleteProduct':
        cursor.callproc('sp_deleteProduct' , tuple)
        data = cursor.fetchall()

        if len(data) is 0:
            conn.commit()
            return True
        else:
            return False
    elif procedure == 'sp_noneFilter':
        cursor.callproc('sp_noneFilter', tuple)
        wishes = cursor.fetchall()
        wishes_dict = []
        for wish in wishes:
            wish_dict = {
                'product_id': wish[0],
                'product_title': wish[1],
                'product_description': wish[2],
                'product_user_id': wish[3],
                'product_date': wish[4],
                'product_state': wish[5],
                'product_price': wish[6],
                'product_file_path': wish[7]
            }

            wishes_dict.append(wish_dict)

        return wishes_dict
    elif procedure == 'sp_filter':
        cursor.callproc('sp_filter', tuple)
        wishes = cursor.fetchall()
        wishes_dict = []
        for wish in wishes:
            wish_dict = {
                'product_id': wish[0],
                'product_title': wish[1],
                'product_description': wish[2],
                'product_user_id': wish[3],
                'product_date': wish[4],
                'product_state': wish[5],
                'product_price': wish[6],
                'product_file_path': wish[7]
            }

            wishes_dict.append(wish_dict)

        return wishes_dict
    elif procedure == 'sp_filterOrderPop':
        cursor.callproc('sp_filterOrderPop', tuple)
        wishes = cursor.fetchall()
        wishes_dict = []
        for wish in wishes:
            wish_dict = {
                'product_id': wish[0],
                'product_title': wish[1],
                'product_description': wish[2],
                'product_user_id': wish[3],
                'product_date': wish[4],
                'product_state': wish[5],
                'product_price': wish[6],
                'product_file_path': wish[7]
            }

            wishes_dict.append(wish_dict)

        return wishes_dict
    elif procedure == 'sp_filterOrderPrice':
        cursor.callproc('sp_filterOrderPrice', tuple)
        wishes = cursor.fetchall()
        wishes_dict = []
        for wish in wishes:
            wish_dict = {
                'product_id': wish[0],
                'product_title': wish[1],
                'product_description': wish[2],
                'product_user_id': wish[3],
                'product_date': wish[4],
                'product_state': wish[5],
                'product_price': wish[6],
                'product_file_path': wish[7]
            }

            wishes_dict.append(wish_dict)

        return wishes_dict
    elif procedure == 'sp_filterOrderDate':
        cursor.callproc('sp_filterOrderDate', tuple)
        wishes = cursor.fetchall()
        wishes_dict = []
        for wish in wishes:
            wish_dict = {
                'product_id': wish[0],
                'product_title': wish[1],
                'product_description': wish[2],
                'product_user_id': wish[3],
                'product_date': wish[4],
                'product_state': wish[5],
                'product_price': wish[6],
                'product_file_path': wish[7]
            }

            wishes_dict.append(wish_dict)

        return wishes_dict




    elif procedure == 'sp_GetWishByUser':
        cursor.callproc('sp_GetWishByUser' , tuple)
        wishes = cursor.fetchall()
        cursor.close()
        cursor = conn.cursor()
        cursor.execute('SELECT @_sp_GetWishByUser_3');
        vivivi = cursor.fetchall()

        print(wishes)
        wishes_dict = []
        for wish in wishes:
            wish_dict = {
                'product_id': wish[0],
                'product_title': wish[1],
                'product_description': wish[2],
                'product_user_id': wish[3],
                'product_date': wish[4],
                'product_state': wish[5],
                'product_price': wish[6],
                'product_file_path': wish[7]
            }
            print(wishes_dict)
            wishes_dict.append(wish_dict)
            wishes_dict.append({'total' : vivivi[0][0]})

        return wishes_dict
    elif procedure == 'sp_AddUpdateLikes':
        cursor.callproc('sp_AddUpdateLikes' , tuple)
        data = cursor.fetchall()

        if len(data) is 0:
            conn.commit()
            return True
        else:
            return False





















