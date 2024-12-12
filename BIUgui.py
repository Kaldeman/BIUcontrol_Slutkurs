#!/usr/bin/env python3

from guizero import App, TextBox, Text, PushButton, CheckBox
from subprocess import call, Popen, run
#Download Mock.GPIO if working on non-RPi system! This will test wether or not to use the real or simulated Pi
try:
    import RPi.GPIO as GPIO
except:
    import Mock.GPIO as GPIO
import BIUpinlist as pin

def startprocess():
    print("starting process")
    spraytime        = str(float(stime.value)/1000)
    retractiondelay  = str(float(rdelay.value)/1000)
    plungedelay      = str(float(pdelay.value)/1000)
    arguments = ["python3","BIUapplyandplunge.py","--stime",spraytime,"--rdelay",retractiondelay,"--pdelay",plungedelay]
    if donotplunge.value==1:
        arguments.append("--donotplunge")
    call(arguments)
    #button_start.disable()
    
def powerup():
    print("Power up")
    arguments = ["python3","BIUpowerupdown.py","--updown","up"]
    call(arguments)
    #button_start.enable()
    
def powerdown():
    print("Power down")
    arguments = ["python3","BIUpowerupdown.py","--updown","down"]
    call(arguments)
    #button_start.disable()
    
def cleanprocess(): # DEACTIVATED: This process is currently not being used for the plunger, it is meant to clean the spray nozzle. 
    print("starting clean process")
    spraytime  = str(float(cleantime.value)/1000)
    cycles = cleancycles.value
    arguments = ["python3","BIUclean.py","--stime",spraytime,"--cycles",cycles]
    #print(arguments)
    #call(arguments)
    Popen(arguments)
    #call(["python3","cleancontrol.py","--stime",stime,"--cycles",cycles])

"""def pedal(): # Currently not being used!
    GPIO.setup(pin.pedalsensor,GPIO.IN, pull_up_down = GPIO.PUD_UP)
    if button_start.enabled and GPIO.input(pin.pedalsensor)==0:
        print("Pedal triggered")
        startprocess()
"""        
def powerupee():
    print("Power up")
    arguments = ["python3","BIUpowerupdown.py","--updown","up"]
    call(arguments)
    #button_start.enable()
    
def powerdownee():
    print("Power down")
    arguments = ["python3","BIUpowerupdown.py","--updown","down"]
    call(arguments)
    #button_start.disable()

def blotplunge():
    print("Starting blot and plunge")
    plungedelay      = str(float(pdelay.value)/1000)
    retractiondelay  = str(float(rdelay.value)/1000)
    arguments = ["python3","BIUapplyandplunge.py","--stime","0","--rdelay",retractiondelay,"--pdelay",plungedelay, "--startblot"]
    if donotplunge.value==1: #TEST
        arguments.append("--donotplunge")
    call(arguments)

def greenlight():
    print('Changing color to green')
    run(['python','lamp_green.py'])   

    print('Done')

def bluelight():
    print('Changing color to blue')
    run(['python','lamp_blue.py']) 
    print('Done')
    
def redlight():
    print('Changing color to red')
    run(['python','lamp_red.py']) 
    print('Done')

def lamp_one():
    print('Turning on lamp')
    run(['python','lamp_on.py']) 
    print('Done')
    lamp_onoff._command = lamp_off
    lamp_onoff.text = 'Lamp ON'
    lamp_onoff.bg = 'yellow'

def lamp_off():
    print('Turning off lamp')
    run(['python','lamp_off.py']) 
    print('Done')
    lamp_onoff._command = lamp_one
    lamp_onoff.text = 'Lamp OFF'
    lamp_onoff.bg = None

    
app = App(title="Back-it-up", layout="grid")
rdelaylabel = Text(app, text="Retraction delay (msec)", grid=[0,1])
rdelay      = TextBox(app, grid=[1,1], text="50")
pdelaylabel = Text(app, text="Plunge delay (msec)", grid=[0,2])
pdelay      = TextBox(app, grid=[1,2], text="50")
#stimelabel  = Text(app, text="Spray time (msec)", grid=[0,3]) #DEACTIVATED: No spray nozzle currently installed
#stime       = TextBox(app, grid=[1,3], text="30")



donotplunge = CheckBox(app, text="Do not plunge", grid=[0,4])
button_up   = PushButton(app, command=powerup,text="Ready", grid=[0,5])
button_down = PushButton(app, command=powerdown, text="Abort", grid=[1,5])
button_blot_plunge= PushButton(app, command=blotplunge, text="Blot & Plunge", grid=[0,6])
#button_start= PushButton(app, command=startprocess, text="Spray & Plunge", grid=[1,6])
button_up.bg="orange"
#button_start.bg = "red"
#button_start.disable()

cleancycleslabel = Text(app, text="Cleaning cycles", grid=[3,1]) # DEACTIVATED
cleancycles      = TextBox(app, text="5",grid=[4,1])   
cleantimelabel   = Text(app, text="Cleaning pulse (msec)", grid=[3,2])
cleantime        = TextBox(app, text="200",grid=[4,2]) 
clean            = PushButton(app, command=cleanprocess, text="Clean", grid=[3,5])

lamp_onoff = PushButton(app, command=lamp_one, text = 'Lamp OFF', grid = [0,8])
lamp_green = PushButton(app, command=greenlight, text = 'Lamp Green', grid = [0,9])
lamp_blue = PushButton(app, command=bluelight, text = 'Lamp Blue', grid = [1,9])
lamp_red = PushButton(app, command=redlight, text = 'Lamp Red', grid = [3,9])

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#app.repeat(100,pedal)
app.display()


