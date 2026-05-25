
#2. re.findall() → extraer todos
#Extrae TODAS las coincidencias.

import re
import os

os.system('cls')


import re


# compilar patrón
pattern = re.compile(r"LOT\d+")

text1 = "LOT100 moved to operation 3000"

text2 = "ERROR ON LOT200"

text3 = "LOT300 COMPLETED"

print(" buscar reutilizando patrón")

print(pattern.search(text1).group())

print(pattern.search(text2).group())

print(pattern.search(text3).group())

print("En este caso el patron el LOT y mas +")


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
