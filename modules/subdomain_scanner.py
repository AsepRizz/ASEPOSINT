import subprocess

def scan_subdomains(domain):
    result = f"Subdomain scan results for: {domain}\n\n"
    
    try:
        # Using subfinder for subdomain enumeration
        output = subprocess.check_output([
            "subfinder", "-d", domain, "-silent"
        ], text=True)
        result += "Found subdomains:\n"
        result += output
        
        # Also try amass if available
        try:
            output = subprocess.check_output([
                "amass", "enum", "-d", domain, "-silent"
            ], text=True)
            result += "\nAdditional subdomains from amass:\n"
            result += output
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
            
    except subprocess.CalledProcessError as e:
        result += f"Error during subdomain scan: {e.output}\n"
    except FileNotFoundError:
        result += "subfinder not installed. Please run install.sh\n"
    
    return result
