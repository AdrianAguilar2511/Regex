
#2. re.findall() → extraer todos
#Extrae TODAS las coincidencias.

import re
import os

os.system('cls')



import re

text = "POAS,IRAZU,RINCON"

result = re.split(r",", text)

print("Texto: " + text)


print("Split: in list format " + str(result))

print(type(result))


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
