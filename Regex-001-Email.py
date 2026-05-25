
import re
import os



os.system('cls')

email = "adrian@gmail.com"

pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"


if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid")




    
'''
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

^                inicio
[\w\.-]+         usuario
@                arroba
[\w\.-]+         dominio
\.               punto
\w+              extensión
$                final
'''