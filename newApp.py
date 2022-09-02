from dash import Dash, dcc, html, Input, Output, State, ctx
import paho.mqtt.client as paho
import sys
import time
import dash_daq as daq

# brokerPi="192.168.0.152"
brokerPi="127.0.0.1"
#brokerPi="172.20.10.11"
port=1883
eps=1000
#1881

topic="cmnd/tasmota_23DFCF/IRsend"
topic_BLE="cmnd/ble"
topic_LS="cmnd/IRcommand"
##### CLOCK #####
head="{\"Protocol\":\"NEC\",\"Bits\":"
head2="\",\"Data\":"

count_sent=1

def on_publish(client,userdata,result):
    #create function for callback
    print("data published \n")
    pass


def publish_all(payload_LS, payload_DMX, payload_AM):
    clientPi.on_publish = on_publish  # assign function to callback
    ret = clientPi.publish(topic_LS, payload_LS)

    # print(payload_LS)
    clientPi.on_publish = on_publish  # assign function to callback
    ret = clientPi.publish(topic_LS, payload_DMX)
    # print(payload_DMX)
    clientPi.on_publish = on_publish  # assign function to callback
    ret = clientPi.publish(topic_BLE, payload_AM)
    # print(payload_AM)


# def publish_on(payload_LS, payload_AM):
#     clientPi.on_publish = on_publish  # assign function to callback
#     ret = clientPi.publish(topic_LS, payload_LS)
#
#     # print(payload_DMX)
#     clientPi.on_publish = on_publish  # assign function to callback
#     ret = clientPi.publish(topic_BLE, payload_AM)
#     # print(payload_AM)

def publish_off(payload_LS, payload_AM,payload_ALARM):
    clientPi.on_publish = on_publish  # assign function to callback
    ret = clientPi.publish(topic_LS, payload_LS)

    # print(payload_DMX)
    clientPi.on_publish = on_publish  # assign function to callback
    ret = clientPi.publish(topic_BLE, payload_AM)
    # print(payload_AM)
    clientPi.on_publish = on_publish  # assign function to callback
    ret = clientPi.publish(topic, payload_ALARM)
    payload_ALARM="OFF"
    clientPi.on_publish = on_publish  # assign function to callback
    time.sleep(5)
    ret = clientPi.publish(topic, payload_ALARM)



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

clientPi = paho.Client("control2")  # create client object
clientPi.connect(brokerPi, port)  # establish connection


app.layout = html.Div([html.Div('',className='container'),

html.H1('COLOR BUSTERS present'),
html.Br(),
html.Hr(),
html.Br(),
html.H1('Speaker Countdown Timer', id='headline'),
html.Br(),
#html.Div(id='countdown',children=[html.Ul(children=[html.Li([html.Span(id='minutes'),'Minutes']),html.Li([html.Span(id='seconds'),'Seconds'])])]),
daq.PowerButton(
        id='turn-off',
        on=False,
        size=100,
        color='#3CD014'
    ),
#    html.Button('Turn on/off', id='turn-off', n_clicks=0),
#html.Button('Turn On/Off', id='turn-off', n_clicks=0, style={"margin-left": "15px"}),


html.Br(),
html.Br(),

    dcc.Input(id='username', value='Time', type='text', style={"margin-left": "15px", 'width': "80", 'padding': "1em", "align-items": "center"}),
    ###DMX###

html.Button('Submit', id='submit-val', n_clicks=0, style={"margin-left": "15px"}),

    html.Div(id='container-button-basic',
             children='Enter a value and press submit'),
html.Br(),
#    html.Div(id='container-button-turn-off', children='(Turn off)', style={"margin-left": "50px"}),
])

@app.callback(
    Output('container-button-basic', 'children'),
    Input('turn-off', 'on'),
    Input('username', 'value'),
    Input('submit-val', 'n_clicks')
)

def update_output(on, value, n_clicks):

    print(ctx.triggered_id)
    #print("DMX-c" == ctx.triggered_id)
    ########TURN-OFF/ON#####
#print(value)
    #print(n_clicks)
    STATE_CLOCK = True

    if on == True and ctx.triggered_id==None:
        msgclock = "0xFFA25D"  # POWER ON
        bits = len(msgclock) * 4
        msg1 = head + "\"" + str(bits) + head2 + msgclock + "\"}"
        clientPi.on_publish = on_publish  # assign function to callback
        ret = clientPi.publish(topic, msg1)
        print(msg1)
        time.sleep(1.0)
        STATE_CLOCK = False

    if on == False and STATE_CLOCK == True and ctx.triggered_id==None:
        msgclock = "0xFFA25D"  # POWER ON
        bits = len(msgclock) * 4
        msg1 = head + "\"" + str(bits) + head2 + msgclock + "\"}"
        clientPi.on_publish = on_publish  # assign function to callback
        ret = clientPi.publish(topic, msg1)
        print(msg1)
        STATE_CLOCK = False 
        time.sleep(1.0)

    #######SET TIMER AND START ALL GADGETS#######

    #####ENTER VALUES AND SET#############
    if "submit-val"==ctx.triggered_id:
        print(value)
        print("You entered: ", value, type(value[0]), (value[1]))
        first_param = nums[int(value[0])]
        second_param = nums[int(value[1])]
        print(first_param)
        # msg2send = "0xFFA25D"  # POWER
        # bits = len(msg2send) * 4
        # msg1 = head + "\"" + str(bits) + head2 + msg2send + "\"}"
        # client1 = paho.Client("control1")  # create client object
        # client1.on_publish = on_publish  # assign function to callback
        # client1.connect(broker, port)  # establish connection
        # ret = client1.publish(topic, msg1)
        # print(msg1)
        time.sleep(1.0)

        msg2send1 = "0xFF30CF"  # nb 1
        bits1 = len(msg2send1) * 4
        msg11 = head + "\"" + str(bits1) + head2 + msg2send1 + "\"}"
        clientPi.on_publish = on_publish  # assign function to callback
        ret = clientPi.publish(topic, msg11)
        print(msg11)
        time.sleep(1.0)

        msg2send2 = "0xFF02FD"  # SET
        bits2 = len(msg2send2) * 4
        msg12 = head + "\"" + str(bits2) + head2 + msg2send2 + "\"}"
        clientPi.on_publish = on_publish  # assign function to callback
        ret = clientPi.publish(topic, msg12)
        print(msg12)
        time.sleep(1.0)

        msg2send3 = first_param  # first nb 0
        bits3 = len(msg2send3) * 4
        msg13 = head + "\"" + str(bits3) + head2 + msg2send3 + "\"}"
        clientPi.on_publish = on_publish  # assign function to callback
        ret = clientPi.publish(topic, msg13)
        print(msg13)
        time.sleep(1.0)

        msg2send4 = second_param  # second nb 3
        bits4 = len(msg2send4) * 4
        msg14 = head + "\"" + str(bits4) + head2 + msg2send4 + "\"}"
        clientPi.on_publish = on_publish  # assign function to callback
        ret = clientPi.publish(topic, msg14)
        print(msg14)
        time.sleep(1.0)

        msg2send5 = "0xFFA857"  # OK
        bits5 = len(msg2send5) * 4
        msg15 = head + "\"" + str(bits5) + head2 + msg2send5 + "\"}"
        clientPi.on_publish = on_publish  # assign function to callback
        ret = clientPi.publish(topic, msg15)
        print(msg15)
        time.sleep(1.0)

        ##### Light strip ###########
        ##send to MQTT IR

        #"COLOR_TOGGLE": "0xF710EF",
        #"COLOR_FLASH": "0xF7F00F"

        payload_LS = "ON"  # TURN ON LED STRIP
        clientPi.on_publish = on_publish  # assign function to callback
        ret = clientPi.publish(topic_LS, payload_LS)
        print(payload_LS)

        payload_LS = "COLOR_TOGGLE"  # TURN ON BOTH LED STRIPS
        clientPi.on_publish = on_publish  # assign function to callback
        ret = clientPi.publish(topic_LS, payload_LS)
        print(payload_LS)


        ##### Audiometer ###########
        ##send to RPi

        # "COLOR_BLU": "bc040600e502d3000055",
        # "COLOR_GRN": "bc040600480236000055",
        # "COLOR_YLW": "bc0406003c03eb000055",
        # "COLOR_ONG": "Bc0406000703a0000055",
        # "COLOR_RED": "bc0406000003eb000055",
        # "COLOR_WHT": "bc040600000000000055"


        payload_AM = "ON"  # TURN ON AUDIOMETER
        clientPi.on_publish = on_publish  # assign function to callback
        ret = clientPi.publish(topic_BLE, payload_AM)
        print(payload_AM)

        payload_AM = "COLOR_GRN"  # TURN ON AUDIOMETER GREEN
        clientPi.on_publish = on_publish  # assign function to callback
        ret = clientPi.publish(topic_BLE, payload_AM)
        print(payload_AM)

        ##### DMX ###########
        ##send to MQTT-IR

        # "COLOR_TOGGLE": "0x0",
        # "COLOR_FLASH": "0x0",
        # "COLOR_RED": "0x47DF38C7",
        # "COLOR_GRN": "0x47DF4AB5",
        # "COLOR_BLU": "0x47DFCA35",
        # "COLOR_YLW": "0x47DF30CF",
        # "COLOR_TRK": "0x47DF58A7",
        # "COLOR_ONG": "0x47DF807F",
        # "COLOR_VLT": "0x47DF00FF",
        # "COLOR_WHT": "0x47DF40BF"


        payload_DMX = "COLOR_GRN"  # TURN DMX GREEN
        clientPi.on_publish = on_publish  # assign function to callback
        ret = clientPi.publish(topic_LS, payload_DMX)
        print(payload_DMX)

        ## deal with time

        time_set = int(value)*60
        elapsed = 0
        time_start = time.time()

        ## COUNT DOWN #####
        no_sent1 = 1
        no_sent2 = 1
        no_sent3 = 1
        while (elapsed<time_set):
            print("Time passed: {}, Time set: {}".format(elapsed, time_set))
            if time_set / 4<=elapsed < 2*time_set / 4:
                if no_sent1<=count_sent:
                    payload_LS = "COLOR_TOGGLE"  # TOGGLE
                    payload_DMX="COLOR_YLW" #YELLOW
                    payload_AM = "COLOR_YLW"  # YELLOW
                    publish_all(payload_LS, payload_DMX, payload_AM)
                    no_sent1=no_sent1+1
            elif 2*time_set / 4<=elapsed < 3 * time_set / 4:
                if no_sent2<=count_sent:
                    payload_LS = "COLOR_TOGGLE"  # TOGGLE
                    payload_DMX = "COLOR_ONG"  # ORANGE
                    payload_AM = "COLOR_ONG"  # ORANGE
                    publish_all(payload_LS, payload_DMX, payload_AM)
                    no_sent2 = no_sent2 + 1
            elif 3*time_set / 4<=elapsed < time_set:
                if no_sent3<=count_sent:
                    payload_LS = "COLOR_TOGGLE"  # TOGGLE
                    payload_DMX = "COLOR_RED"  # RED
                    payload_AM = "COLOR_RED"  # RED
                    publish_all(payload_LS, payload_DMX, payload_AM)
                    no_sent3 = no_sent3 + 1
            # time.sleep(4)

            elapsed=time.time()-time_start
        # TURN OFF EVERYTHING
        payload_LS = "OFF" # TURN OFF BOTH DEVICES
        payload_AM = "OFF"
        payload_ALARM="SET"
        publish_off(payload_LS, payload_AM, payload_ALARM)
        time.sleep(5)
        return 'The input value was "{}" and the button has been clicked {} times'.format(
            value,
            n_clicks
        )

    else:
        return ' '


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')

