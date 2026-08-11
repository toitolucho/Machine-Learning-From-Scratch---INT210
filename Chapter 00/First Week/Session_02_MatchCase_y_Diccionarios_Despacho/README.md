# Sesión 0.2: Estructuras Multicamino y Diccionarios de Despacho

## Guía de la Sesión para el Estudiante

En esta sesión se estudiará el manejo eficiente de bifurcaciones múltiples mediante el moderno `match-case` (*Structural Pattern Matching* introducido en Python 3.10) y el patrón clásico de ingeniería de software: **Diccionarios de Despacho** (*Dispatch Dictionaries*).

---

### 1. Objetivos de Aprendizaje

- **Dominar el emparejamiento de patrones:** Sintaxis `match-case`, captura de variables y patrones comodín (`_`).
- **Implementar Diccionarios de Despacho:** Encapsulamiento de funciones de primera clase como valores de diccionarios hash.
- **Analizar la Complejidad Computacional:** Demostrar por qué una cadena de $N$ condicionales tiene costo temporal $\mathcal{O}(N)$ en el peor caso, mientras que un diccionario hash opera en tiempo constante promedio $\mathcal{O}(1)$.
- **Aplicar enrutamiento de ciberseguridad:** Triaje automatizado de incidentes SOC (Malware, Phishing, DoS, Exfiltración).
- **Controlar renderizado multiformato:** Despacho de procesadores gráficos según el contenedor de imagen (PNG, JPEG, SVG, WebP).

---

### 2. Estructura de Materiales

* **`02_Despacho_Alertas_y_Formatos_Render.ipynb`**: Cuaderno guiado con benchmarking de rendimiento $\mathcal{O}(N)$ vs $\mathcal{O}(1)$ y despacho funcional.
* **`02_Guia_de_Trabajo_Soluciones.md`**: Solucionario docente con análisis de la tabla hash de CPython y tips pedagógicos.
* **`02_Laboratorio_Evaluacion.ipynb`**: Reto autónomo con bloques `# TODO` para crear un enrutador de mitigación de amenazas y evaluar la matriz de tiempo de respuesta.
* **`02_Soluciones_Laboratorio.md`**: Código de referencia y argumentación de impacto en SLAs corporativos.
* **`02_Presentacion_Clase.tex`**: Presentación académica en LaTeX Beamer (Tema *Madrid*, Color *whale*).
* **`generar_graficas.py`**: Script para generar la gráfica comparativa de complejidad temporal $\mathcal{O}(N)$ vs $\mathcal{O}(1)$.
