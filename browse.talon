# activated if the current app name is "Google Chrome"
app.name: Google Chrome
-
settings():
    user.contextID = 'browse'
	
go to google:
    # note: use key(cmd-t) on Mac
    key(ctrl-t)
    insert("google.com")
    key(enter)

next tab: key(ctrl-tab)

scroll up: key(pageup)
scroll down: key(pagedown)
