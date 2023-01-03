import wmi
import time
import win32com.client

def check_if_running():
    c = wmi.WMI()
    processes = c.Win32_Process()
    for process in processes:
        if process.Name == "python.exe" and "run.py" in process.CommandLine:
            return True
    return False

while True:
    if not check_if_running():
        # If the script is not running, start it
        # Create a new command prompt window
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.Run("cmd")
        time.sleep(1)

        # Send the first line of code to the command prompt window
        shell.SendKeys("cd..{ENTER}")

        # Send the second line of code to the command prompt window
        shell.SendKeys("cd..{ENTER}")

        # Send the third line of code to the command prompt window
        shell.SendKeys("cd bot{ENTER}")

        # Send the fourth line of code to the command prompt window
        shell.SendKeys(".venv\\Scripts\\activate.bat{ENTER}")

        # Send the fifth line of code to the command prompt window
        shell.SendKeys("py run.py --config accounts/my.insta.acc/config.yml{ENTER}")

    # Wait for 5 minutes before checking if the script is running again
    time.sleep(5 * 60)
