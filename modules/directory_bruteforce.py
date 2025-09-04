import subprocess

def brute_directories(url):
    result = f"Directory brute force results for: {url}\n\n"
    
    try:
        # Using dirsearch for directory brute forcing
        output = subprocess.check_output([
            "python", "dirsearch/dirsearch.py", 
            "-u", url, "--simple-report=/dev/stdout"
        ], text=True)
        result += output
    except subprocess.CalledProcessError as e:
        result += f"Error during directory brute force: {e.output}\n"
    except FileNotFoundError:
        result += "dirsearch not installed. Please run install.sh\n"
    
    return result
