@echo off
set python=D:\work\talon-windows\python.exe
"%python%" "-c" "import sys; sys.path.remove(''); import runpy; runpy._run_module_as_main('pip')" %*
