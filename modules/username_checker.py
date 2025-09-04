import os
import subprocess

def check_username(username):
    result = f"Username check results for: {username}\n\n"
    
    # Using Sherlock for username checking
    if os.path.exists("sherlock/sherlock.py"):
        try:
            output = subprocess.check_output([
                "python", "sherlock/sherlock.py", 
                "--no-color", username
            ], stderr=subprocess.STDOUT, text=True)
            result += output
        except subprocess.CalledProcessError as e:
            result += f"Error running Sherlock: {e.output}\n"
    else:
        result += "Sherlock not installed. Please run install.sh\n"
    
    return result
