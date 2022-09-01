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
    html.Button('Button 1 To Send 0x1111', id='btn-nclicks-1', n_clicks=0),
    html.Button('Button 2', id='btn-nclicks-2', n_clicks=0),
    html.Button('Button 3', id='btn-nclicks-3', n_clicks=0),
    html.Div(id='container-button-timestamp')
])

@app.callback(
    Output('container-button-timestamp', 'children'),
    Input('btn-nclicks-1', 'n_clicks'),
    Input('btn-nclicks-2', 'n_clicks'),
    Input('btn-nclicks-3', 'n_clicks')
)
def displayClick(btn1, btn2, btn3):
    msg = "None of the buttons have been clicked yet"

    if "btn-nclicks-1" == ctx.triggered_id:
        msg = "Button 1 was most recently clicked"
        msg2send = "0xFFA25D" #POWER	
        bits = len(msg2send)*4
        msg1 = head + "\"" + str(bits) + head2 + msg2send + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg1)
        print(msg1)
        time.sleep(1.0)

        msg2send1 = "0xFF30CF" #nb 1
        bits1 = len(msg2send1)*4
        msg11 = head + "\"" + str(bits1) + head2 + msg2send1 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg11)
        print(msg11)
        time.sleep(1.0)

        msg2send2 = "0xFF02FD" #SET	
        bits2 = len(msg2send2)*4
        msg12 = head + "\"" + str(bits2) + head2 + msg2send2 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg12)
        print(msg12)
        time.sleep(1.0)


        msg2send3 = "0xFF9867" #first nb 0
        bits3 = len(msg2send3)*4
        msg13 = head + "\"" + str(bits3) + head2 + msg2send3 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg13)
        print(msg13)
        time.sleep(1.0)

        msg2send4 = "0xFF7A85" #second nb 3
        bits4 = len(msg2send4)*4
        msg14 = head + "\"" + str(bits4) + head2 + msg2send4 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg14)
        print(msg14)
        time.sleep(1.0)

        msg2send5 = "0xFFA857" #OK
        bits5 = len(msg2send5)*4
        msg15 = head + "\"" + str(bits5) + head2 + msg2send5 + "\"}"
        client1 = paho.Client("control1")                           #create client object
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker,port)                                 #establish connection
        ret = client1.publish(topic,msg15)
        print(msg15)
        time.sleep(1.0)

    elif "btn-nclicks-2" == ctx.triggered_id:
        msg = "Button 2 was most recently clicked"
    elif "btn-nclicks-3" == ctx.triggered_id:
        msg = "Button 3 was most recently clicked"
    return html.Div(msg)

if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',port='11212')

