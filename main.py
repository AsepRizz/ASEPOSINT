#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
from datetime import datetime
from modules import username_checker, ip_lookup, whois_lookup, metadata_extractor
from modules import port_scanner, subdomain_scanner, directory_bruteforce, web_tech_detector, reverse_ip_lookup

# Color codes for terminal
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    banner = f"""
    {Colors.RED}╔══════════════════════════════════════════════════════════╗
    {Colors.RED}║{Colors.CYAN}     ___   _____  ______  _____  ____  _   _ _______  {Colors.RED}║
    {Colors.RED}║{Colors.CYAN}    / _ \\ |  __ \\|  ____|/ ____|/ __ \\| \\ | |__   __| {Colors.RED}║
    {Colors.RED}║{Colors.CYAN}   / /_\\ \\| |  \\/| |__  | (___ | |  | |  \\| |  | |    {Colors.RED}║
    {Colors.RED}║{Colors.CYAN}  |  _  || | __ |  __|  \\___ \\| |  | | . ` |  | |    {Colors.RED}║
    {Colors.RED}║{Colors.CYAN}  | | | || |_\\ \\| |____ ____) | |__| | |\\  |  | |    {Colors.RED}║
    {Colors.RED}║{Colors.CYAN}  \\_| |_/ \\____/|______|_____/ \\____/\\_| \\_/  |_|    {Colors.RED}║
    {Colors.RED}║{Colors.YELLOW}               OSINT + Reconnaissance Tool            {Colors.RED}║
    {Colors.RED}╚══════════════════════════════════════════════════════════╝{Colors.RESET}
    """
    print(banner)

def print_menu():
    menu = f"""
    {Colors.GREEN}[1]{Colors.RESET} Username Checker
    {Colors.GREEN}[2]{Colors.RESET} IP Lookup
    {Colors.GREEN}[3]{Colors.RESET} WHOIS Lookup
    {Colors.GREEN}[4]{Colors.RESET} Metadata Extractor
    {Colors.GREEN}[5]{Colors.RESET} Port Scanner
    {Colors.GREEN}[6]{Colors.RESET} Subdomain Scanner
    {Colors.GREEN}[7]{Colors.RESET} Directory Brute Force
    {Colors.GREEN}[8]{Colors.RESET} Web Technology Detector
    {Colors.GREEN}[9]{Colors.RESET} Reverse IP Lookup
    {Colors.GREEN}[10]{Colors.RESET} Email & Phone Regex Checker
    {Colors.RED}[0]{Colors.RESET} Exit
    """
    print(menu)

def loading_animation(message):
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", 
                 "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", 
                 "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    
    for i in range(len(animation)):
        time.sleep(0.1)
        sys.stdout.write(f"\r{Colors.CYAN}{message} {animation[i % len(animation)]}{Colors.RESET}")
        sys.stdout.flush()
    
    sys.stdout.write("\r" + " " * (len(message) + 15) + "\r")
    sys.stdout.flush()

def save_results(data, tool_name, format="txt"):
    # Create results directory if it doesn't exist
    if not os.path.exists("results"):
        os.makedirs("results")
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"results/{tool_name}_{timestamp}.{format}"
    
    # Save data to file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(data)
    
    return filename

def main():
    clear_screen()
    print_banner()
    
    while True:
        print_menu()
        choice = input(f"\n{Colors.YELLOW}[?] Select an option: {Colors.RESET}").strip()
        
        if choice == "0":
            print(f"\n{Colors.RED}[!] Exiting... Goodbye!{Colors.RESET}")
            break
        
        elif choice == "1":
            username = input(f"{Colors.YELLOW}[?] Enter username to search: {Colors.RESET}").strip()
            if username:
                loading_animation("Checking username across platforms")
                result = username_checker.check_username(username)
                filename = save_results(result, "username_check")
                print(f"{Colors.GREEN}[+] Results saved to: {filename}{Colors.RESET}")
            else:
                print(f"{Colors.RED}[!] Please enter a valid username{Colors.RESET}")
        
        elif choice == "2":
            ip = input(f"{Colors.YELLOW}[?] Enter IP address: {Colors.RESET}").strip()
            if ip:
                loading_animation("Looking up IP information")
                result = ip_lookup.lookup_ip(ip)
                filename = save_results(result, "ip_lookup")
                print(f"{Colors.GREEN}[+] Results saved to: {filename}{Colors.RESET}")
            else:
                print(f"{Colors.RED}[!] Please enter a valid IP address{Colors.RESET}")
        
        elif choice == "3":
            domain = input(f"{Colors.YELLOW}[?] Enter domain: {Colors.RESET}").strip()
            if domain:
                loading_animation("Performing WHOIS lookup")
                result = whois_lookup.lookup_whois(domain)
                filename = save_results(result, "whois_lookup")
                print(f"{Colors.GREEN}[+] Results saved to: {filename}{Colors.RESET}")
            else:
                print(f"{Colors.RED}[!] Please enter a valid domain{Colors.RESET}")
        
        elif choice == "4":
            file_path = input(f"{Colors.YELLOW}[?] Enter file path: {Colors.RESET}").strip()
            if file_path and os.path.exists(file_path):
                loading_animation("Extracting metadata")
                result = metadata_extractor.extract_metadata(file_path)
                filename = save_results(result, "metadata_extract")
                print(f"{Colors.GREEN}[+] Results saved to: {filename}{Colors.RESET}")
            else:
                print(f"{Colors.RED}[!] Please enter a valid file path{Colors.RESET}")
        
        elif choice == "5":
            target = input(f"{Colors.YELLOW}[?] Enter target IP or domain: {Colors.RESET}").strip()
            if target:
                loading_animation("Scanning ports")
                result = port_scanner.scan_ports(target)
                filename = save_results(result, "port_scan")
                print(f"{Colors.GREEN}[+] Results saved to: {filename}{Colors.RESET}")
            else:
                print(f"{Colors.RED}[!] Please enter a valid target{Colors.RESET}")
        
        elif choice == "6":
            domain = input(f"{Colors.YELLOW}[?] Enter domain: {Colors.RESET}").strip()
            if domain:
                loading_animation("Scanning for subdomains")
                result = subdomain_scanner.scan_subdomains(domain)
                filename = save_results(result, "subdomain_scan")
                print(f"{Colors.GREEN}[+] Results saved to: {filename}{Colors.RESET}")
            else:
                print(f"{Colors.RED}[!] Please enter a valid domain{Colors.RESET}")
        
        elif choice == "7":
            url = input(f"{Colors.YELLOW}[?] Enter URL: {Colors.RESET}").strip()
            if url:
                loading_animation("Brute forcing directories")
                result = directory_bruteforce.brute_directories(url)
                filename = save_results(result, "directory_bruteforce")
                print(f"{Colors.GREEN}[+] Results saved to: {filename}{Colors.RESET}")
            else:
                print(f"{Colors.RED}[!] Please enter a valid URL{Colors.RESET}")
        
        elif choice == "8":
            url = input(f"{Colors.YELLOW}[?] Enter URL: {Colors.RESET}").strip()
            if url:
                loading_animation("Detecting web technologies")
                result = web_tech_detector.detect_tech(url)
                filename = save_results(result, "web_tech_detect")
                print(f"{Colors.GREEN}[+] Results saved to: {filename}{Colors.RESET}")
            else:
                print(f"{Colors.RED}[!] Please enter a valid URL{Colors.RESET}")
        
        elif choice == "9":
            ip = input(f"{Colors.YELLOW}[?] Enter IP address: {Colors.RESET}").strip()
            if ip:
                loading_animation("Performing reverse IP lookup")
                result = reverse_ip_lookup.reverse_lookup(ip)
                filename = save_results(result, "reverse_ip_lookup")
                print(f"{Colors.GREEN}[+] Results saved to: {filename}{Colors.RESET}")
            else:
                print(f"{Colors.RED}[!] Please enter a valid IP address{Colors.RESET}")
        
        elif choice == "10":
            text = input(f"{Colors.YELLOW}[?] Enter text to scan for emails/phones: {Colors.RESET}").strip()
            if text:
                loading_animation("Scanning for emails and phone numbers")
                # Simple regex patterns for demonstration
                import re
                email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                phone_pattern = r'\b(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})\b'
                
                emails = re.findall(email_pattern, text)
                phones = re.findall(phone_pattern, text)
                
                result = "=== EMAILS FOUND ===\n"
                result += "\n".join(emails) if emails else "No emails found"
                
                result += "\n\n=== PHONE NUMBERS FOUND ===\n"
                result += "\n".join(["".join(phone) for phone in phones]) if phones else "No phone numbers found"
                
                filename = save_results(result, "regex_check")
                print(f"{Colors.GREEN}[+] Results saved to: {filename}{Colors.RESET}")
            else:
                print(f"{Colors.RED}[!] Please enter some text to scan{Colors.RESET}")
        
        else:
            print(f"{Colors.RED}[!] Invalid option. Please try again.{Colors.RESET}")
        
        input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")
        clear_screen()
        print_banner()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Interrupted by user. Exiting...{Colors.RESET}")
        sys.exit(0)
