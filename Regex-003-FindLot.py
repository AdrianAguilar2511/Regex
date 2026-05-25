
import re
import os

os.system('cls')

text = "LOT_ID=ABC12345"

match = re.findall(r"ABC\d+", text)

print(match)
    
'''
4. El patrón completo
ABC\d+

Se divide así:

Parte	Significado
ABC	texto literal “ABC”
\d	cualquier número
+	uno o más

Entonces…
ABC\d+

significa:

“Busca texto que empiece con ABC y tenga números después.”

'''
