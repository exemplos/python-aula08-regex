import re

f = open("ips.txt", "r", encoding="utf-8")
lines = f.read().splitlines()
prog = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
ips = []
for line in lines:
    result = prog.findall(line)
    ips.append(result)

print(ips)

f.close()