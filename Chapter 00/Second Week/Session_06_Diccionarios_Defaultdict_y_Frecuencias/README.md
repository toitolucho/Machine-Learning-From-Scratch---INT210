# Sesión 0.6: Diccionarios, `defaultdict` y Contadores de Frecuencia

## Guía de la Sesión para el Estudiante

En esta sesión se estudiarán las colecciones asociativas clave-valor (**Diccionarios**) y las extensiones especializadas del módulo estándar `collections` (`defaultdict` y `Counter`). Se aplicarán en el conteo de frecuencias léxicas (NLP) para detección de *Phishing* y en el análisis forense de tráfico de red.

---

### 1. Objetivos de Aprendizaje

- **Dominar las Tablas Hash Nativas:** Mapeo de pares `clave: valor` con tiempo de acceso promedio $\mathcal{O}(1)$.
- **Mitigar la Excepción `KeyError`:** Uso de `dict.get()`, `dict.setdefault()` y `collections.defaultdict`.
- **Implementar Modelos de Bolsa de Palabras (*Bag-of-Words*):** Vectorizar textos mediante conteo de términos sospechosos (*Joel Grus, Cap. 2*).
- **Utilizar `collections.Counter`:** Extracción de los $k$ elementos más frecuentes con `.most_common()`.
- **Auditar Frecuencia de Ataques en Ciberseguridad:** Mapear direcciones IP a historiales de accesos no autorizados.

---

### 2. Estructura de Materiales

* **`06_Diccionarios_Defaultdict_NLP_Ciberseguridad.ipynb`**: Cuaderno guiado con **código completo primero y explicación línea por línea debajo**.
* **`06_Guia_de_Trabajo_Soluciones.md`**: Guía pedagógica con notas sobre la tabla hash compacta de Python 3.6+.
* **`06_Laboratorio_Evaluacion.ipynb`**: Reto autónomo con bloques `# TODO` para construir un analizador de frecuencia léxica de phishing y matriz de confusión.
* **`06_Soluciones_Laboratorio.md`**: Código de solución y análisis del impacto de la sobrecarga de diccionarios en memoria.
* **`06_Presentacion_Clase.tex`**: Presentación académica en LaTeX Beamer (Tema *Madrid*, Color *whale*).
* **`generar_graficas.py`**: Script de generación de histogramas de frecuencias de términos de ataque en PNG.
