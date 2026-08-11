# Módulo 0.2: Estructuras de Datos Nativas en Python para Machine Learning
## Semana 2: Fundamentos de Almacenamiento, Vectores y Procesamiento "From Scratch"

Bienvenido a la **Semana 2** del curso *INT210: Machine Learning From Scratch*. En esta semana se estudiarán las estructuras de datos nativas de Python (Listas, Tuplas, Diccionarios, Defaultdicts, Sets y Flujos I/O de Archivos) y su rol fundamental en la representación matemática de tensores, vectores y matrices antes de la introducción de librerías de alto nivel como NumPy o Pandas.

---

### Objetivos de Aprendizaje

1. **Dominar la Representación Vectorial:** Modelar vectores matemáticos ($Vector = \text{List}[float]$) y matrices de datos ($Matrix = \text{List}[Vector]$) utilizando estructuras nativas, implementando suma vectorial, producto punto y distancia euclidiana (*Joel Grus, Cap. 4*).
2. **Optimizar Consultas y Frecuencias en $\mathcal{O}(1)$:** Implementar diccionarios hash, `collections.defaultdict` y `collections.Counter` para el conteo de frecuencias de términos (NLP) y perfiles de ataque en ciberseguridad (*Joel Grus, Cap. 2*).
3. **Aplicar Álgebra de Conjuntos en Alta Velocidad:** Utilizar `set` para comprobaciones de membresía instantáneas ($\mathcal{O}(1)$) y operaciones relacionales (Unión, Intersección, Diferencia Simétrica) en filtrado de Blacklists y paletas cromáticas.
4. **Ingesta de Datos Nativa Sin Librerías Externas:** Leer, parsear y estructurar archivos CSV mediante `with open()` y el módulo estándar `csv.reader`, garantizando la gestión eficiente de memoria RAM y el casteo seguro de tipos (*Joel Grus, Cap. 9*).

---

### Estructura de la Semana 2

| Sesión | Tema Principal | Contexto Ciberseguridad | Contexto Videojuegos / Arte Digital |
| :--- | :--- | :--- | :--- |
| **Sesión 0.5** | Listas, Tuplas y Vectores Matemáticos | Vectores de características en detección de intrusos | Coordenadas de colisión 3D $[x,y,z]$ y canales RGBA |
| **Sesión 0.6** | Diccionarios, `defaultdict` y Frecuencias | Conteo de palabras clave sospechosas en Phishing | Mapeo de texturas y frecuencias de paletas de color |
| **Sesión 0.7** | Sets y Operaciones de Conjuntos $\mathcal{O}(1)$ | Filtrado masivo de IPs de una Botnet en Blacklists | Eliminación de duplicados cromáticos en renderizado |
| **Sesión 0.8** | Ingesta de Archivos Delimitados "From Scratch" | Auditoría y parseo puro de logs de transacciones CSV | Carga de coordenadas de trayectorias de animación |

---

### Mapa de Archivos por Sesión

Cada subcarpeta de sesión contiene los siete componentes estándar de la cátedra:
1. `README.md`: Guía de sesión y objetivos para el estudiante.
2. `0X_<Tema>.ipynb`: Cuaderno guiado con **código primero y explicación detallada paso a paso abajo**.
3. `0X_Guia_de_Trabajo_Soluciones.md`: Guía pedagógica y solucionario docente.
4. `0X_Laboratorio_Evaluacion.ipynb`: Cuaderno de reto autónomo con `# TODO`.
5. `0X_Soluciones_Laboratorio.md`: Código completo del laboratorio y análisis de impacto de negocio.
6. `0X_Presentacion_Clase.tex`: Diapositivas Beamer (Madrid/whale).
7. `generar_graficas.py`: Script Python para generar los diagramas y curvas de complejidad.
