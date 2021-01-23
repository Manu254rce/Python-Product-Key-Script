#Python Product Activation Key for Windows
#Written by Manu254rce, all rights reserved

import subprocess, pyperclip

command_line = subprocess.run(["wmic", "path", "softwarelicensingservice", "get", "OA3xOriginalProductKey"], capture_output = True).stdout.decode()#run the code to open up cmd interface
#and key in the strings
print(command_line)
#the program will open up the command line, print the output in the python shell, then pyperclip will copy the code onto the clipboard

pyperclip.copy(command_line)




