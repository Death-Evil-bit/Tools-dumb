#!/data/data/com.termux/files/usr/bin/bash
echo "[+] Installing School Dump Tool..."

pkg update -y && pkg upgrade -y
pkg install python python-pip -y
pip install requests bs4

curl -o school_dump.py https://raw.githubusercontent.com/Deat-Evil-bit/school-dump/main/school_dump.py
chmod +x school_dump.py

echo "[+] Installation complete!"
echo "[+] Run: python school_dump.py"
