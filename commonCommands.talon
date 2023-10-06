# common speech commands for key presses
press tab: key(tab)
hold control: key("ctrl:down") 
release control: key("ctrl:up") 

# FlipMouse slot change commands
next slot:
	user.nextSlot()
slot mouse:
	user.loadSlot("mouse")
slot gamekey:
	user.loadSlot("gamekey")
slot mouse bt:
	user.loadSlot("mouse-bt")

# sleep and wake up speech recognition
^talon sleep [<phrase>]$: speech.disable()

key(f8):
	speech.enable()
	app.notify("f8: speech recognition enabled")
