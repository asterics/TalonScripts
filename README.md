# TalonScripts for FlipMouse 
Some Talon scripts which provide voice control for the FlipMouse, see: https://talonvoice.com/ and https://github.com/asterics/FLipMouse.
Basic concepts how the FlipMouse can be controlled via speech commands are demonstrated. 

## Installation
* Download and install Talon as described here: https://talonvoice.com/docs/
* Copy (clone) this repository into the Talon user folder
* Install pySerial in the python environment of your Talon installation 
  (`pipTalon.bat install pyserial` can be used under Windows after updating the path to your Talon installation folder in the batch script.)

## Operation 
* The .talon files define voice commands and key mappings for different contexts (eg. browsing, editing, gaming) - depending on the focused application window
* FMActions.py establishes communication to the FlipMouse
  * On startup, all available serial ports are scanned for a connected FlipMouse - if a Flipmouse device is found, the COM port identified is stored
  * The port is closed immediately after startup, so that it can be used by other applications as well - it will be opened on demand for sending subsequent commands)
  * AT commands for loading the next configuration slot (or a particular slot) are sent to the FlipMouse device upon voice command or context switch  
* New voice commands / behaviours can be added as described here: https://talon.wiki/unofficial_talon_docs/


## Combination of Talon with Eyetracking / Gaze-OCR
* How to get Tobii trackers working with Talon: https://talon.wiki/tobii_5/
  * Demo video  Talon + Tobii Gaze Tracker + OptiKey: https://www.youtube.com/watch?v=PQkJE-rtn-g
* James Stout Blog about Gaze OCR and Talon: https://handsfreecoding.org/
  * Demo video Gaze OCR: https://www.youtube.com/watch?v=qkFy66WF3bU
* Video by Wolfram Wingerath showing hands-free coding and gaming techniques: https://www.youtube.com/watch?v=HtoJ7PyjsSY

