import re
import os

os.system('cls')


text = "Connection failed from IP 192.168.1.10"

pattern = r"\d+\.\d+\.\d+\.\d+"

match = re.findall(pattern, text)

print(match)

    
'''
pattern = r"\d+\.\d+\.\d+\.\d+"


'''
