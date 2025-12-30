import subprocess
from getpass import getpass

username = ""
password = ""
target_ip = ""

username = input(f"Enter Username:{username}")
password = getpass("Enter Password:")
target_ip = input(f"Enter Target IP:{target_ip}")

if username and password and target_ip:
    cmd = (f'sudo xfreerdp /u:{username} /p:"{password}" /v:{target_ip} /cert-ignore /bpp:8 /network:modem /compression -themes -wallpaper /clipboard /audio-mode:1 /auto-reconnect -glyph-cache /dynamic-resolution /relax-order-checks')
    subprocess.run(cmd, shell=True)
else:
    print("username, password and target ip are required.")