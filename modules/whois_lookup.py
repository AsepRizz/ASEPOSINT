import whois

def lookup_whois(domain):
    result = f"WHOIS lookup results for: {domain}\n\n"
    
    try:
        details = whois.get_whois(domain)
        
        for key, value in details.items():
            result += f"{key}: {value}\n"
    except Exception as e:
        result += f"Error during WHOIS lookup: {str(e)}\n"
    
    return result

