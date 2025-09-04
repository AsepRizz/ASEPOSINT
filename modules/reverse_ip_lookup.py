import requests
from bs4 import BeautifulSoup

def reverse_lookup(ip):
    result = f"Reverse IP lookup results for: {ip}\n\n"
    
    try:
        # Using hackertarget.com for reverse IP lookup
        response = requests.post(
            "https://api.hackertarget.com/reverseiplookup/",
            data={"q": ip}
        )
        
        if response.status_code == 200:
            result += "Domains hosted on the same IP:\n"
            result += response.text
        else:
            result += "Reverse IP lookup failed\n"
    except Exception as e:
        result += f"Error during reverse IP lookup: {str(e)}\n"
    
    return result
