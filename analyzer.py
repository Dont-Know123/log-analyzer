count ={}
try:
    with open ("auth.log", "r") as f:
        for line in f:
            if "FAILED" in line:
                parts = line.split()
                ip= parts[-1].replace("ip=", "")
                if ip in count:
                    count[ip]= count[ip] + 1
                else:
                    count[ip]= 1
except FileNotFoundError:
    print("Log File Not Found. Check The File Name And Folder")
else:
    with open("alerts.txt", "w") as out:
        for ip,total in count.items():
            print(f"{ip} had {total} failed logins")
            if total >= 3:
                out.write(f"Alert:ip {ip} had {total} failed logins. \n")
