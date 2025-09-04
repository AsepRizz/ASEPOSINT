import requests

def lookup_ip(ip):
    result = f"IP lookup results for: {ip}\n\n"
    
    try:
        # Using ip-api.com for IP lookup
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        
        if data["status"] == "success":
            result += f"IP: {data['query']}\n"
            result += f"Country: {data['country']}\n"
            result += f"Region: {data['regionName']}\n"
            result += f"City: {data['city']}\n"
            result += f"ISP: {data['isp']}\n"
            result += f"Organization: {data['org']}\n"
            result += f"AS: {data['as']}\n"
            result += f"Latitude: {data['lat']}\n"
            result += f"Longitude: {data['lon']}\n"
            result += f"Timezone: {data['timezone']}\n"
            result += f"Zip: {data['zip']}\n"
        else:
            result += "IP lookup failed\n"
    except Exception as e:
        result += f"Error during IP lookup: {str(e)}\n"
    
    return result
