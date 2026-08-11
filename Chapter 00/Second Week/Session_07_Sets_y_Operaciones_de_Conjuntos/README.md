# Sesión 0.7: Sets y Operaciones de Conjuntos en Alta Velocidad

## Guía de la Sesión para el Estudiante

En esta sesión se estudiará la estructura de datos `set` (Conjunto) en Python, sus fundamentos en la Teoría de Conjuntos y su desempeño para comprobación de pertenencia en tiempo constante $\mathcal{O}(1)$.

---

### 1. Objetivos de Aprendizaje

- **Dominar la Estructura `set`:** Colecciones no ordenadas de elementos únicos e inmutables (objetos *hashables*).
- **Comprender el Álgebra de Conjuntos:** Unión ($A \cup B$, `|`), Intersección ($A \cap B$, `&`), Diferencia ($A \setminus B$, `-`) y Diferencia Simétrica ($A \Delta B$, `^`).
- **Analizar la Complejidad de Membresía:** Demostrar analítica y experimentalmente por qué `x in conjunto` es $\mathcal{O}(1)$ mientras que `x in lista` es $\mathcal{O}(N)$.
- **Filtrar Amenazas de Ciberseguridad:** Intersección masiva de listas negras (*Blacklists*) para aislar IPs de una Botnet.
- **Extraer Paletas de Color en Arte Digital:** Reducción de millones de píxeles redundantes a conjuntos únicos de color.

---

### 2. Estructura de Materiales

* **`07_Sets_Blacklists_y_Paletas_Color.ipynb`**: Cuaderno guiado con **código completo primero y desglose línea por línea después**.
* **`07_Guia_de_Trabajo_Soluciones.md`**: Guía pedagógica con notas sobre elementos no hashables (mutables) y `frozenset`.
* **`07_Laboratorio_Evaluacion.ipynb`**: Reto autónomo con bloques `# TODO` para auditoría perimetral de IPs y extracción de paletas sin duplicados.
* **`07_Soluciones_Laboratorio.md`**: Código de solución y cálculo de matriz de confusión de bloqueo perimetral.
* **`07_Presentacion_Clase.tex`**: Presentación académica en LaTeX Beamer (Tema *Madrid*, Color *whale*).
* **`generar_graficas.py`**: Script de benchmarking temporal de búsqueda en Sets vs Listas.
