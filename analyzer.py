#count = 0
#with open("auth.log", "r") as f:
#    for line in f:
#        if "FAILED" in line:
#            count =count + 1
#            parts=line.split()
#            ip = parts[-1].replace("ip="," ")
#            print("failed ip address:", ip)
#print("failed logins:", count)

count ={}
with open ("auth.log", "r") as f:
    for line in f:
        if "FAILED" in line:
            parts = line.split()
            ip= parts[-1].replace("ip=", "")
            if ip in count:
                count[ip]= count[ip] + 1
            else:
                count[ip]= 1
with open("alerts.txt", "w") as out:
    for ip,total in count.items():
        print(f"{ip} had {total} failed logins")
        if total >= 3:
            out.write(f"Alert:ip {ip} had {total} failed logins. \n")
