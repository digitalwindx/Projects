from getpass import getpass
import subprocess

username = input("Please input your username:")
dst_ip = input("What is the IP address:")
dst_directory = input("What is the destined directory:")
local_directory = input("What is the local directory:")

if username and dst_ip and dst_directory and local_directory:
	scp_cmd = (f"scp {username}@{dst_ip}:{dst_directory} {local_directory}")
	subprocess.run(scp_cmd, shell=True)
else:
	print("Please input into all fields")