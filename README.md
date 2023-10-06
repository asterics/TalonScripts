# TalonScripts
Some Talon scripts and actions for FlipMouse voice control, see: https://talonvoice.com/ and https://github.com/asterics/FLipMouse
Basic concepts how the FlipMouse can be controlled via speech commands are demonstrated. 
(AT commands are sent to the FlipMouse device via PySerial, this could be applied for FABI or FlipPad in similar ways)

## Installation
* download and install Talon as described here: https://talonvoice.com/docs/
* copy (clone) the files in this repository into the Talon user folder
* install pyserial in the python environment of your Talon installation 
  (eg. using `\work\talon-windows\venv_bin\pip.bat`)

## Usage
* on startup, all available COM ports are scanned for a connected FlipMouse - if a Flipmouse device is found, the COM port identified is stored (but the port close again in order to not block it)
* upon certain voice commands or context switches (change of window focus), AT commands for slot changes are sent of key mappings are changed (see the .talon files)
