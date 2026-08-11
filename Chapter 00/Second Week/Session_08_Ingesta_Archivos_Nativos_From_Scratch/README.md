# Sesión 0.8: Carga e Ingesta de Archivos Delimitados con Python Nativo (Ingesta "From Scratch")

## Guía de la Sesión para el Estudiante

En esta sesión se estudiará la ingesta y manipulación de archivos estructurados (CSV) utilizando exclusivamente las herramientas nativas de la librería estándar de Python (`with open()`, `csv.reader`, `csv.DictReader` y `collections.namedtuple`), sin recurrir a librerías de alto nivel como Pandas.

---

### 1. Objetivos de Aprendizaje

- **Dominar los Administradores de Contexto (*Context Managers*):** Apertura segura de archivos con `with open(...) as f:` que garantiza el cierre automático de descriptores de archivo (*File Descriptors*).
- **Controlar la Codificación de Caracteres:** Manejo riguroso de `encoding='utf-8'` y `newline=''`.
- **Parsear Archivos CSV Nativa y Eficientemente:** Uso de `csv.reader` para flujos de tuplas y `csv.DictReader` para mapeo automático de cabeceras (*Joel Grus, Cap. 9*).
- **Estructurar Datos en `NamedTuples`:** Creación de registros tipados e inmutables con bajo consumo de memoria.
- **Auditar Transacciones de Ciberseguridad:** Ingesta y filtrado heurístico de registros financieros sospechosos.

---

### 2. Estructura de Materiales

* **`transacciones_seguridad.csv`**: Archivo de datos delimitados real para las pruebas de ingesta.
* **`08_Ingesta_CSV_Nativo_From_Scratch.ipynb`**: Cuaderno guiado con **código completo primero y explicación línea por línea debajo**.
* **`08_Guia_de_Trabajo_Soluciones.md`**: Guía docente y solucionario con notas sobre streams I/O.
* **`08_Laboratorio_Evaluacion.ipynb`**: Reto autónomo con bloques `# TODO` para construir un parser CSV con casteo automático de tipos y matriz de confusión.
* **`08_Soluciones_Laboratorio.md`**: Código de solución y análisis de costo computacional.
* **`08_Presentacion_Clase.tex`**: Presentación académica en LaTeX Beamer (Tema *Madrid*, Color *whale*).
* **`generar_graficas.py`**: Script de visualización del pipeline de ingesta en PNG.
