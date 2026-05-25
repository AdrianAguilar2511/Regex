
import re
import os

os.system('cls')

log = "2026-05-19 ERROR Database timeout"

pattern = r"ERROR"

if re.search(pattern, log):
    print("Error found")
else:
    print("No error")

    
'''
r"ERROR"

Busca la palabra ERROR 

'''
