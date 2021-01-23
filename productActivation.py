import subprocess, re, pyperclip

command_line = subprocess.run(["wmic", "path", "softwarelicensingservice", "get", "OA3xOriginalProductKey"], capture_output = True).stdout.decode()
print(command_line)

pyperclip.copy(command_line)




