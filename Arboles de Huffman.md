## INFORME SOBRE LOS ÁRBOLES DE HUFFMAN

INTRODUCCIÓN
El Árbol de Huffman es una estructura de datos diseñada para la compresión de información sin pérdida. Fue creado por David Huffman en el año 1952 como una alternativa eficiente para reducir el tamaño de los archivos digitales sin eliminar contenido original. Este método es fundamental en la informática moderna.

CONCEPTOS CLAVE
La idea principal es la codificación de longitud variable. En lugar de usar la misma cantidad de espacio para cada letra o símbolo, este sistema asigna códigos muy cortos a los elementos que más se repiten y códigos más largos a los que aparecen poco. Para evitar confusiones al leer los datos, se asegura de que ningún código sea el inicio de otro.

EL ALGORITMO
El proceso para construir el árbol sigue estos pasos generales:
Primero se cuenta cuántas veces aparece cada símbolo en el texto.
Se crean pequeños nodos para cada símbolo con su respectiva frecuencia.
Se toman los dos nodos con los valores más bajos y se unen para formar un nuevo grupo.
Este proceso de unión se repite hasta que todos los elementos forman parte de un solo árbol principal.
Finalmente, se asignan ceros y unos a las ramas para generar el código binario de cada símbolo.

EFICIENCIA
Este método es considerado óptimo porque logra la representación más compacta posible basada en las probabilidades de aparición de los caracteres. Es la base para entender cómo se ahorra espacio en la transmisión de datos a gran escala.

APLICACIONES PRÁCTICAS
Hoy en día, este algoritmo se encuentra en muchas tecnologías comunes:
En archivos comprimidos como los formatos ZIP y GZIP.
En la codificación de imágenes JPEG para reducir su peso.
En formatos de música como el MP3.
En protocolos de internet que ayudan a que las páginas web carguen más rápido.

REFERENCIAS ACADÉMICAS
Huffman, D. (1952). Un método para la construcción de códigos de redundancia mínima.
Knuth, D. (1985). Codificación dinámica de Huffman.
Sedgewick, R. (2011). Algoritmos y estructuras de datos.

## links

https://www.researchgate.net/publication/225338470_A_method_for_the_construction_of_minimum-redundancy_codes
https://en.wikipedia.org/wiki/Introduction_to_Algorithms
