from talon import app, settings
from talon import Context, Module
import sys
import glob
import user.serialcomm as ser

ctx = Context()    
mod = Module()

currentContext = mod.setting(
    "contextID",
    type=str,
    default="none",
    desc="string identifier for context switches",
)

def settings_change_handler(*args):
    contextID=str(args[0])
    print ("contextID changed to:"+ contextID)
    if contextID == 'browse':
        ser.sendAT(fmPort,'LO mouse')
    if contextID == 'gaming':
        ser.sendAT(fmPort,'LO gamekey')
    

settings.register("user.contextID", settings_change_handler)

 
@mod.action_class
class Actions:
    def nextSlot():
        "activates the next slot"
        ser.sendAT(fmPort,'NE',False);

    def loadSlot(s: str):
        "Mangles the input string in the appropriate manner."
        ser.sendAT(fmPort,'LO '+s,False);        
         
fmPort=ser.openFMPort()
if fmPort != None:
    app.notify(title="FlipMouse voice control enabled.",
               body="currentContext="+str(currentContext.get()))
    ser.sendAT(fmPort,'NE',False);
else: 
    app.notify(title="no FlipMouse found!")


'''
app.register("ready", onReady)
app.notify(title="FlipMouse voice control enabled.",
           body="say your commands now!",
           sound=False)
'''

