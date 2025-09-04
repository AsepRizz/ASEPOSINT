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
pkg install -y python git curl nmap python-pip perl make golang

# Install Python packages
echo -e "\033[93m[+] Installing Python packages...\033[0m"
pip install requests beautifulsoup4 python-whois

# Install ExifTool from source
echo -e "\033[93m[+] Installing ExifTool...\033[0m"
wget https://exiftool.org/Image-ExifTool-12.85.tar.gz
tar xzf Image-ExifTool-12.85.tar.gz
cd Image-ExifTool-12.85
perl Makefile.PL
make
make install
cd ..
rm -rf Image-ExifTool-12.85 Image-ExifTool-12.85.tar.gz

# Install external tools
echo -e "\033[93m[+] Installing external tools...\033[0m"

# Install Sherlock for username checking
if [ ! -d "sherlock" ]; then
    git clone https://github.com/sherlock-project/sherlock.git
    cd sherlock
    pip install -r requirements.txt
    cd ..
fi

# Install subfinder for subdomain enumeration
if [ ! -f "/data/data/com.termux/files/usr/bin/subfinder" ]; then
    git clone https://github.com/projectdiscovery/subfinder.git
    cd subfinder/v2/cmd/subfinder
    go build .
    mv subfinder /data/data/com.termux/files/usr/bin/
    cd ../../..
fi

# Install dirsearch for directory brute forcing
if [ ! -d "dirsearch" ]; then
    git clone https://github.com/maurosoria/dirsearch.git
fi

# Install whatweb for web technology detection
if [ ! -f "/data/data/com.termux/files/usr/bin/whatweb" ]; then
    git clone https://github.com/urbanadventurer/WhatWeb.git
    cd WhatWeb
    chmod +x whatweb
    cp whatweb /data/data/com.termux/files/usr/bin/
    cd ..
fi

# Create results directory
mkdir -p results

echo -e "\033[92m[+] Installation completed!\033[0m"
echo -e "\033[92m[+] Run: python main.py\033[0m"
