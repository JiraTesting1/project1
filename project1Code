from flask import Flask,render_template, make_response
from datetime import *
# import serial
import json
import random
from time import *
import pickle
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'system.maintenance.info@gmail.com'
app.config['MAIL_PASSWORD'] = 'DPR_1234'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/vibration_data')
def vibration_data():
    # arduino_port = "COM3" 
    # baud = 115200  

    # ser = serial.Serial(arduino_port, baud)

    # #display the data to the terminal
    # removerChar="b\'\\rn"

    # # def vibration_data():
    # getData=str(ser.readline())
    # for i in removerChar:
    #     getData = getData.replace(i,"")

    # vibration = int(getData)

    vibration = random.randint(100,300)
    time_var = time()*1000
    vibration_data = [time_var, vibration]
    return vibration_data

@app.route('/')
def main():
    vibration = vibration_data()
    vibration = vibration[1]
    # x = "real: "
    print("vibration: ",vibration)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    pre = model.predict([[vibration]])
    print("pre 0: ",pre[0])
    # print("pre 1: ",pre[1])

    days = int(pre[0])
    hrs = int((pre[0] - int(pre[0])) * 24)
    rul = f'{days} days and {hrs} hrs.'
    percentage = int((days/365)*100)

    if percentage>=30:
        risk = "Safe"
        color = "green"
        return render_template('index.html', vibration=vibration, risk=risk, color=color, current_time=current_time, rul=rul, percentage=percentage)

    elif percentage>0 and percentage<30:
        recipients = []#'170390116049@saffrony.ac.in','170390116004@saffrony.ac.in','170390116033@saffrony.ac.in'] #yhaa pe apne 3 ke mail daal do saffrony vaale
        msg = Message('System Alert ', sender = 'system.maintenance.info@gmail.com', recipients = recipients)
        now = datetime.now()
        cur_time = now.strftime("%H:%M:%S") 
        msg.body = f"Alert at {cur_time} \nRUL : {days} day(s) and {hrs} hour(s) ({percentage}%) remains life of the fan!!!"
        mail.send(msg)
        risk = "Alert"
        color = "Orange"
        return render_template('index.html', vibration=vibration, risk=risk, color=color, current_time=current_time, rul=rul, percentage=percentage)

    else:
        risk = "Fail"
        color = "red"
        return render_template('index.html', vibration=vibration, risk=risk, color=color, current_time=current_time, rul=rul, percentage=percentage)

@app.route('/data')
def data():
    data = vibration_data()
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response    

if __name__ == "__main__":
    app.run(debug=True)
