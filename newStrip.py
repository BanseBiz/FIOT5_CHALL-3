from dash import Dash, html, Input, Output, ctx
import paho.mqtt.client as paho
import sys
import time

broker="192.168.0.152"
port=1883

topic="cmnd/tasmota_23DFCF/IRsend"
head="{\"Protocol\":\"NEC\",\"Bits\":"
head2="\",\"Data\":"


def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

app = Dash(__name__)

app.layout = html.Div([
    html.Button('Power', id='btn-nclicks-power', n_clicks=0),
    html.Button('From Purple', id='btn-nclicks-p', n_clicks=0),
    html.Button('From Cyan', id='btn-nclicks-c', n_clicks=0),
    html.Button('From Red', id='btn-nclicks-r', n_clicks=0),
    html.Button('From Green', id='btn-nclicks-g', n_clicks=0),
    html.Button('From Blue', id='btn-nclicks-b', n_clicks=0),
    html.Div(id='container-button-timestamp')
])

@app.callback(
    Output('container-button-timestamp', 'children'),
    Input('btn-nclicks-power', 'n_clicks'),
    Input('btn-nclicks-p', 'n_clicks'),
    Input('btn-nclicks-c', 'n_clicks'),
    Input('btn-nclicks-r', 'n_clicks'),
    Input('btn-nclicks-g', 'n_clicks'),
    Input('btn-nclicks-b', 'n_clicks')
)

def displayClick(btn1, btn2, btn3, btn4, btn5, btn6):
    msg = "None of the buttons have been clicked yet"

    if "btn-nclicks-power" == ctx.triggered_id:

        msg = "Button POWER was most recently clicked"

        msg2send = "0xF7C03F" #POWER
        bits = len(msg2send)*4
        msg1 = head + "\"" + str(bits) + head2 + msg2send + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg1)
        print(msg1)
        time.sleep(1.0)

    elif "btn-nclicks-p" == ctx.triggered_id:
        msg = "Purple --> Yellow"

        msg2send1 = "0xF710EF" # 1
        bits1 = len(msg2send1)*4
        msg11 = head + "\"" + str(bits1) + head2 + msg2send1 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg11)
        print(msg11)
        time.sleep(1.0)

        msg2send2 = "0xF710EF" #2
        bits2 = len(msg2send2)*4
        msg12 = head + "\"" + str(bits2) + head2 + msg2send2 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg12)
        print(msg12)

        msg2send3 = "0xF710EF" #3
        bits3 = len(msg2send3)*4
        msg13 = head + "\"" + str(bits3) + head2 + msg2send3 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg13)
        print(msg13)
        time.sleep(1.0)
        
        msg2send31 = "0xF710EF" #4
        bits31 = len(msg2send31)*4
        msg131 = head + "\"" + str(bits31) + head2 + msg2send31 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg131)
        print(msg131)
        time.sleep(1.0)

        msg2send32 = "0xF710EF" #5
        bits32 = len(msg2send32)*4
        msg132 = head + "\"" + str(bits32) + head2 + msg2send32 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg132)
        print(msg132)
        time.sleep(1.0)
    elif "btn-nclicks-c" == ctx.triggered_id:
        msg = "Cyan --> Yellow"

        msg2send1 = "0xF710EF" # 1
        bits1 = len(msg2send1)*4
        msg11 = head + "\"" + str(bits1) + head2 + msg2send1 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg11)
        print(msg11)
        time.sleep(1.0)

        msg2send2 = "0xF710EF" #2
        bits2 = len(msg2send2)*4
        msg12 = head + "\"" + str(bits2) + head2 + msg2send2 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg12)
        print(msg12)

        msg2send3 = "0xF710EF" #3
        bits3 = len(msg2send3)*4
        msg13 = head + "\"" + str(bits3) + head2 + msg2send3 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg13)
        print(msg13)
        time.sleep(1.0)
        
        msg2send31 = "0xF710EF" #4
        bits31 = len(msg2send31)*4
        msg131 = head + "\"" + str(bits31) + head2 + msg2send31 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg131)
        print(msg131)
        time.sleep(1.0)

    elif "btn-nclicks-r" == ctx.triggered_id:
        msg = "Red --> Yellow"

        msg2send1 = "0xF710EF" # 1
        bits1 = len(msg2send1)*4
        msg11 = head + "\"" + str(bits1) + head2 + msg2send1 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg11)
        print(msg11)
        time.sleep(1.0)

        msg2send2 = "0xF710EF" #2
        bits2 = len(msg2send2)*4
        msg12 = head + "\"" + str(bits2) + head2 + msg2send2 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg12)
        print(msg12)

        msg2send3 = "0xF710EF" #3
        bits3 = len(msg2send3)*4
        msg13 = head + "\"" + str(bits3) + head2 + msg2send3 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg13)
        print(msg13)
        time.sleep(1.0)
        
    elif "btn-nclicks-g" == ctx.triggered_id:
        msg = "Green --> Yellow"

        msg2send1 = "0xF710EF" # 1
        bits1 = len(msg2send1)*4
        msg11 = head + "\"" + str(bits1) + head2 + msg2send1 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg11)
        print(msg11)
        time.sleep(1.0)

        msg2send2 = "0xF710EF" #2
        bits2 = len(msg2send2)*4
        msg12 = head + "\"" + str(bits2) + head2 + msg2send2 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg12)
        print(msg12)

    elif "btn-nclicks-b" == ctx.triggered_id:
        msg = "Blue --> Yellow"

        msg2send1 = "0xF710EF" # 1
        bits1 = len(msg2send1)*4
        msg11 = head + "\"" + str(bits1) + head2 + msg2send1 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg11)
        print(msg11)
        time.sleep(1.0)

        msg2send2 = "0xF710EF" #2
        bits2 = len(msg2send2)*4
        msg12 = head + "\"" + str(bits2) + head2 + msg2send2 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg12)
        print(msg12)
  
    return html.Div(msg)

if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',port='15168')

