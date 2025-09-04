import subprocess

def scan_ports(target):
    result = f"Port scan results for: {target}\n\n"
    
    try:
        # Using nmap for port scanning
        output = subprocess.check_output([
            "nmap", "-sV", "-sC", "-O", target
        ], text=True)
        result += output
    except subprocess.CalledProcessError as e:
        result += f"Error during port scan: {e.output}\n"
    except FileNotFoundError:
        result += "nmap not installed. Please run install.sh\n"
    
    return result
