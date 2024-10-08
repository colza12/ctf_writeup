import hashlib

with open("flag-options.csv", 'r') as f:
    flag_list = [line.strip() for line in f.readlines()]

for flag in flag_list:
    candidate = hashlib.sha256(flag.encode()).hexdigest()
    if candidate == "3390a5081ea4d44e3173eaf3e9695d9216d60cfcb617027355c95b3b7275e8e3":
        print(flag)
