
#2. re.findall() → extraer todos
#Extrae TODAS las coincidencias.

import re
import os

os.system('cls')


import re

text = "TEMP=35 HUMIDITY=80 SPEED=120"

for m in re.finditer(r"\d+", text):

    print("MATCH:", m.group())

    print("START:", m.start())

    print("END:", m.end())

    print("SPAN:", m.span())

    print("-----")




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
