import json

with open("info.json", "r") as f:
    data = json.loads(f.read())
ip_addr = []
for host in range(len(data["hosts"])):
    if data["hosts"][host]["ip_address"] is None:
        continue
    if data["hosts"][host]["ip_address"] in ip_addr:
        continue
    else:
        ip_addr.append(data["hosts"][host]["ip_address"])
with open("ips.txt", "w") as f:
    for ip in ip_addr:
        f.write(str(ip) + "\n")
