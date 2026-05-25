
#2. re.findall() → extraer todos
#Extrae TODAS las coincidencias.

import re
import os

os.system('cls')



import re

text = "123ABC"

print("Texto: " + text)


result = re.sub(r"\d+", "XXXzzz", text)


print("Replace numbers: " + str(result))



import re

text = "123ABC"

result = re.sub(r"[A-Z]+", "ZZZ", text)



print("Replace letters: " + str(result))



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
