
#2. re.findall() → extraer todos
#Extrae TODAS las coincidencias.

import re
import os

os.system('cls')


text = "TEMP=35 HUMIDITY=80 SPEED=120"

result = re.findall(r"\d", text)

print(result)

result = re.findall(r"\d+", text)

print(result)



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


Ejemplo del uso de +

sin el + pone son 1 digito de cada coincidencia

['3', '5', '8', '0', '1', '2', '0']

con el + es mas por lo que devuelve todo los encontrado

['35', '80', '120']
'''
