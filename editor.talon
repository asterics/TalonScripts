# activate this .talon file if the current app name is "Notepad++"
# you can find app names by running ui.apps() in the REPL
app.name: Notepad++
-
# key_wait increases the delay when pressing keys (milliseconds)
# this is useful if an app seems to jumble or drop keys
settings():
    key_wait = 4.0

hello talon: "hello world"
insert code fragment:
    # A single command can perform a sequence of actions.
    insert("``````")
    key(left left left)
    # the number of times the key should be pressed can be specified after a colon
    key(shift-enter:2)
    key(up)

