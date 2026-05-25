# 2. re.sub() → reemplazar

import re
import os

os.system('cls')

text = "ERROR CODE 500"

# patrón regex busca numeros y mas
pattern = r"\d+"

# reemplazar números por 999
result = re.sub(
    pattern,
    "999",
    text
)

 

print("Find and replace")

print("Original Text: " + text)

print("Results: " + result)




'''
Símbolos importantes Regex

Regex   Significado

\d      número
\w      letra/número
.       cualquier caracter
*       cero o más
+       uno o más
^       inicio
$       final
'''
