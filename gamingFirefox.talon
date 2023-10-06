# activated if the current app is "Firefox"
app.name: Firefox
-
settings():
    user.contextID = 'gaming'
	
# speech commands for key presses
hold air: key("a:down") 
release air: key("a:up") 

# map WASD to cursor keys
key(w:up): key("up:up")
key(w:down): key("up:down")
key(a:up): key("left:up")
key(a:down): key("left:down")
key(s:up): key("down:up")
key(s:down): key("down:down")
key(d:up): key("right:up")
key(d:down): key("right:down")
