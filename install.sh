#!/data/data/com.termux/files/usr/bin/bash
# ASEPOSINT Installation Script for Termux

echo -e "\033[91m"
echo "╔══════════════════════════════════════════════════════════╗"
echo "║                 ASEPOSINT Installer                     ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo -e "\033[0m"

# Update packages
echo -e "\033[93m[+] Updating packages...\033[0m"
pkg update -y && pkg upgrade -y

# Install dependencies
echo -e "\033[93m[+] Installing dependencies...\033[0m"
pkg install -y python git curl nmap whois python-pip perl make golang

# Install Python packages
echo -e "\033[93m[+] Installing Python packages...\033[0m"
pip install requests beautifulsoup4

# Install ExifTool
echo -e "\033[93m[+] Installing ExifTool...\033[0m"
pkg install -y exiftool

# Bersihkan folder tools yang sudah ada
echo -e "\033[93m[+] Cleaning up existing tools...\033[0m"
rm -rf sherlock subfinder dirsearch WhatWeb

# Install external tools
echo -e "\033[93m[+] Installing external tools...\033[0m"

# Install Sherlock untuk username checking
echo -e "\033[93m[+] Installing Sherlock...\033[0m"
git clone https://github.com/sherlock-project/sherlock.git
cd sherlock
pip install -r requirements.txt
cd ..

# Install subfinder menggunakan Go
echo -e "\033[93m[+] Installing SubFinder...\033[0m"
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
mv $HOME/go/bin/subfinder /data/data/com.termux/files/usr/bin/

# Install dirsearch untuk directory brute forcing
echo -e "\033[93m[+] Installing DirSearch...\033[0m"
git clone https://github.com/maurosoria/dirsearch.git

# Install whatweb untuk web technology detection
echo -e "\033[93m[+] Installing WhatWeb...\033[0m"
git clone https://github.com/urbanadventurer/WhatWeb.git
cd WhatWeb
chmod +x whatweb
cp whatweb /data/data/com.termux/files/usr/bin/
cd ..

# Create results directory
mkdir -p results

echo -e "\033[92m[+] Installation completed!\033[0m"
echo -e "\033[92m[+] Run: python main.py\033[0m"
