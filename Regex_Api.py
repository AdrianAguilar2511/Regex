import os
import json
import re
import pandas as pd
import requests

os.system('cls')


url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()


# Mostrar JSON bonito
print(json.dumps(data, indent=4))

#pause = input("Press Enter")

# Regex para teléfonos
#pattern = r'\(\d{3}\)\d{3}-\d{4}\s*x\d+'

pattern = r'[\(]?\d{1,3}[\)]?[-.\s]?\d{3}[-.\s]?\d{4}(?:\s*x\d+)?'

# Lista resultados
results = []

# Recorrer JSON
for entry in data:

    phone = entry.get("phone", "")

    matches = re.findall(pattern, phone)

    for match in matches:

        results.append({
            "name": entry.get("name"),
            "phone_found": match
        })

# Crear DataFrame
df = pd.DataFrame(results)

print("\nRESULTS:")
print(df)

df.to_csv("phones.csv", index=False)


'''
Lo dividimos por partes
1. [\(]?
[\(]?

Significa:

“un paréntesis ( opcional”

Explicación
Parte	Significado
[ ]	conjunto de caracteres
\(	el caracter (
?	opcional (0 o 1 vez)
Coincide con:

✅

(

o también:
✅ nada

2. \d{1,3}
\d{1,3}

Significa:

“de 1 a 3 números”

Explicación
Parte	Significado
\d	cualquier número
{1,3}	entre 1 y 3 veces
Coincide con:

✅

1
12
123
3. [\)]?
[\)]?

Significa:

“un ) opcional”

Coincide con:

✅

)

o nada.

Hasta aquí
[\(]?\d{1,3}[\)]?

acepta:

✅

(254)
254
1
010
4. [-.\s]?
[-.\s]?

Significa:

“un separador opcional”

Explicación
Parte	Significado
-	guion
.	punto
\s	espacio
?	opcional
Coincide con:

✅

-
.
(space)
5. \d{3}
\d{3}

Significa:

exactamente 3 números

Coincide con:

✅

770
254
976
6. Otro [-.\s]?

Otro separador opcional.

7. \d{4}
\d{4}

Significa:

exactamente 4 números

Hasta aquí el patrón ya acepta:

✅

770-736-8031
210.067.6132
(254)954-1289
024-648-3804
8. (?:\s*x\d+)?

Esta es la parte MÁS avanzada.

(?: )
(?: )

Significa:

“grupo NO capturable”

Solo agrupa regex.
No guarda resultados separados.

\s*
\s*

Significa:

cero o más espacios

x

literal:

x
\d+
\d+

Significa:

uno o más números

Todo junto
(?:\s*x\d+)?

Significa:

“una extensión opcional”

Coincide con:

✅

 x56442
 x140
 x156

o nada.

Resultado final

TODO el patrón:

[\(]?\d{1,3}[\)]?[-.\s]?\d{3}[-.\s]?\d{4}(?:\s*x\d+)?

acepta MUCHOS formatos:

✅

1-770-736-8031 x56442
010-692-6593 x09125
1-463-123-4447
493-170-9623 x156
(254)954-1289
210.067.6132
586.493.6943 x140
024-648-3804
(775)976-6794 x41206
Esto es EXACTAMENTE lo que pasa en enterprise

Los datos reales:

vienen inconsistentes
múltiples vendors
múltiples formatos
errores humanos

Y regex sirve para:

limpiar
validar
extraer
normalizar datos

Muy alineado con:

DataOps
ETL
operational pipelines
data quality engineering.

'''