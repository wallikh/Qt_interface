#! /usr/bin/env python2.7
# * Running on http://127.0.0.1:5000/


from flask import Flask, jsonify, render_template, request, redirect, session, current_app
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import copy
import rospy
from std_msgs.msg import String
# from std_msgs.msg import Float64MultiArray
# from std_msgs.msg import Float64
# from std_msgs.msg import Int32
from woz_interface.msg import NameInfo
# sys.path.append(r'/home/walid/catkin_ws/src/platforms/qt_robot/woz_interface/script/Version4.0')  

from threading import Thread



# Thread(target=lambda:rospy.init_node("flask_interface",anonymous=True ,disable_signals=True)).start()
rospy.init_node("qt_flask_interface", anonymous=True, disable_signals=True)
app = Flask(__name__)
app.secret_key = "woz" 



@app.route('/')
def index(name=None):
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login(name=None):
    if request.method=='POST':
        #state.publish("true")
        print(request.form)
        session['user_name'] = request.form.get('fname')
        session['user_surname'] = request.form.get('lname')
        session['teacher_name'] = request.form.get('fname2')
        return render_template('scenarios.html', name=name)
    return render_template('login.html', name=name)

	
@app.route('/reactions')
def reactions(name=None):
    if not session.get('user_name') or not len(session.get('user_name')) or not len( session.get('user_surname') ) :
        return redirect('/')

    return render_template('reactions.html', name=name)

@app.route('/scenarios')
def scenarios(name=None):
    if not session.get('user_name') or not len(session.get('user_name')) or not len( session.get('user_surname') ) :
        return redirect('/')
    return render_template('scenarios.html', name=name)

@app.route('/theatre')
def theatre(name=None):
    if not session.get('user_name') or not len(session.get('user_name')) or not len( session.get('user_surname') ) :
        return redirect('/')
    return render_template('theatre.html', name=name)

	
# woz_command can send ros messages and call ros services
@app.route("/woz",methods=['POST'])
def ros_ini():

    button = rospy.Publisher('/woz/button',String,queue_size=10)
    prenom = str(session.get('user_name'))
    nom = str(session.get('user_surname'))
    prenom2 = str(session.get('teacher_name'))
    woz_command(button,prenom,nom,prenom2)
   
    return("")



def woz_command(button,prenom,nom,prenom2):
    payload = request.get_json() 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~",payload)
    my_button = None  # Initialisation de la valeur de my_button
    if 'command' in payload and payload['command'] != "":
        my_button = payload['command']
    if 'direction' in payload and payload['direction'] != "":
        my_button = payload['direction']
    if my_button is not None:
        button.publish(my_button)
    name_info = rospy.Publisher('/woz/nameinfo',NameInfo,queue_size=1)
    name_info.publish(str(session.get('user_name')),str(session.get('user_surname')),str(session.get('teacher_name')))

    return ("")



	
if __name__ == "__main__":
    app.run(host= '0.0.0.0',debug=True)

