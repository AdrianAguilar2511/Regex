
#2. re.findall() → extraer todos
#Extrae TODAS las coincidencias.

import re
import os

os.system('cls')



import re

text = "123ABC"


print("Partial Match: " + str(re.match(r"\d+", text)))

print("Full Match: " + str(re.fullmatch(r"\d+", text)))





'''
Símbolos importantes Regex
Regex	Significado
\d	número
\w	letra/número
.	cualquier caracter
*	cero o más
+	uno o más
^	inicio
$	final



'''
