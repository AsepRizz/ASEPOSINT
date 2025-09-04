import subprocess

def detect_tech(url):
    result = f"Web technology detection results for: {url}\n\n"
    
    try:
        # Using whatweb for technology detection
        output = subprocess.check_output([
            "whatweb", url
        ], text=True)
        result += output
    except subprocess.CalledProcessError as e:
        result += f"Error during technology detection: {e.output}\n"
    except FileNotFoundError:
        result += "whatweb not installed. Please run install.sh\n"
    
    return result
