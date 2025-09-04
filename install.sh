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
pkg install -y python git curl nmap whois python-pip perl make golang openssl-tool

# Install Python packages
echo -e "\033[93m[+] Installing Python packages...\033[0m"
pip install --upgrade pip
pip install requests beautifulsoup4 python-whois dnspython rich

# Install ExifTool (paket Termux)
echo -e "\033[93m[+] Installing ExifTool...\033[0m"
pkg install -y perl-image-exiftool

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

# Install Subfinder menggunakan Go
echo -e "\033[93m[+] Installing SubFinder...\033[0m"
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
mv -f $HOME/go/bin/subfinder $PREFIX/bin/

# Install Dirsearch untuk directory brute forcing
echo -e "\033[93m[+] Installing DirSearch...\033[0m"
git clone https://github.com/maurosoria/dirsearch.git

# Install WhatWeb untuk web technology detection
echo -e "\033[93m[+] Installing WhatWeb...\033[0m"
git clone https://github.com/urbanadventurer/WhatWeb.git
cd WhatWeb
chmod +x whatweb
cp -f whatweb $PREFIX/bin/
cd ..

# Create results directory
mkdir -p results

echo -e "\033[92m[+] Installation completed!\033[0m"
echo -e "\033[92m[+] Run: python main.py\033[0m"
