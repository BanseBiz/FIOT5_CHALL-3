from dash import Dash, dcc, html, Input, Output, State
import paho.mqtt.client as paho
import sys
import time

broker="192.168.0.152"
port=1883
#1881

topic="cmnd/tasmota_23DFCF/IRsend"
head="{\"Protocol\":\"NEC\",\"Bits\":"
head2="\",\"Data\":"
data2send ="0x1111";
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

nums = {0: "0xFF9867",
            1: "0xFF30CF",
            2: "0xFF18E7",
            3: "0xFF7A85",
            4: "0xFF10EF",
            5: "0xFF38C7",
            6: "0xFF5AA5",
            7: "0xFF42BD",
            8: "0xFF4AB5",
            9: "0xFF52AD"}


app = Dash(__name__)

app.layout = html.Div([html.Div('',className='container'),
html.h1('Speaker Countdown timer', id='headline'),
html.h1(' ', id='headline'), 
html.Div('', id='countdown'),
html.ul([html.li([html.span(id='minutes')],'Minutes'), html.span(id='seconds')],'Seconds')])],
html.Button('Button 1', id='btn-nclicks-1', n_clicks=0),
html.Button('Button 2', id='btn-nclicks-2', n_clicks=0),
html.Button('Button 3', id='btn-nclicks-3', n_clicks=0),
html.Div(id='container-button-timestamp')
])


html.Div([
    html.Div('Example Div', style={'color': 'blue', 'fontSize': 14}),
    html.P('Example P', className='my-class', id='my-p-element')
], style={'marginBottom': 50, 'marginTop': 25})


<div style="margin-bottom: 50px; margin-top: 25px;">
    <div style="color: blue; font-size: 14px">
        Example Div
    </div>
    <p class="my-class", id="my-p-element">
        Example P
    </p>
</div>

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
    elif "btn-nclicks-2" == ctx.triggered_id:
        msg = "Button 2 was most recently clicked"
    elif "btn-nclicks-3" == ctx.triggered_id:
        msg = "Button 3 was most recently clicked"
    return html.Div(msg)

'''
app.layout = html.Div([
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit')
])


@app.callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)

def update_output(n_clicks, value):
#	for value in sys.argv[1:] :
#	bits = len(value)*4
#	msg = head + "\"" + str(bits) + head2 + value + "\"}"
#	client1 = paho.Client("control1")                           #create client object
#	client1.on_publish = on_publish                          #assign function to callback
#	client1.connect(broker,port)                                 #establish connection
#	ret = client1.publish(topic,data2send)
#	print(data2send)
#	time.sleep(1.0)
            try:
                data = int(value)
                print("You entered: ", data)
                first_param = nums[int(value[0])]
                second_param = nums[int(value[1])]
                print(first_param)
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


                msg2send3 = first_param #first nb 0
                bits3 = len(msg2send3)*4
                msg13 = head + "\"" + str(bits3) + head2 + msg2send3 + "\"}"
                client1 = paho.Client("control1")                           #create client object
                client1.on_publish = on_publish                          #assign function to callback
                client1.connect(broker,port)                                 #establish connection
                ret = client1.publish(topic,msg13)
                print(msg13)
                time.sleep(1.0)


                msg2send4 = second_param #second nb 3
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
                return 'The input value was "{}" and the button has been clicked {} times'.format(
                   value,
                   n_clicks
                  )
                break;
            except ValueError:
                return 'INVALID INPUT'
'''
if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',port='65432')

