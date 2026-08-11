# Sesión 0.1: Bifurcaciones Lógicas y Decisiones Condicionales (`if`, `elif`, `else`)

## Guía de la Sesión para el Estudiante

Bienvenido a la primera sesión del módulo de nivelación. En esta clase se estudiará cómo las computadoras toman decisiones binarias y compuestas evaluando proposiciones lógicas.

---

### 1. Objetivos de Aprendizaje

- **Comprender el control de flujo condicional:** Estructuras `if`, `elif`, y `else` en Python.
- **Dominar el Álgebra Booleana:** Operadores lógicos (`and`, `or`, `not`), evaluación de cortocircuito (*short-circuit evaluation*) y tablas de verdad.
- **Diferenciar Identidad vs. Igualdad:** Uso estricto de `is` (identidad en memoria) frente a `==` (equivalencia de valor).
- **Entender el concepto de *Truthiness*:** Evaluación de tipos nativos (números, cadenas, listas, diccionarios) en contextos booleanos.
- **Implementar Heurísticas de Clasificación:** Construir un firewall por software basado en reglas y un clasificador de spam manual.
- **Evaluar la Matriz de Confusión Heurística:** Cuantificar Verdaderos Positivos (VP), Verdaderos Negativos (VN), Falsos Positivos (FP) y Falsos Negativos (FN).

---

### 2. Estructura de Materiales

* **`01_Condicionales_Firewall_y_Luminancia.ipynb`**: Cuaderno guiado paso a paso con datasets reales de red y matrices de píxeles.
* **`01_Guia_de_Trabajo_Soluciones.md`**: Guía pedagógica con soluciones completas y consejos didácticos para el docente.
* **`01_Laboratorio_Evaluacion.ipynb`**: Reto autónomo con bloques `# TODO` para clasificar spam con reglas manuales y evaluar la matriz de confusión.
* **`01_Soluciones_Laboratorio.md`**: Respuestas y argumentación del impacto financiero y de seguridad del laboratorio.
* **`01_Presentacion_Clase.tex`**: Presentación académica en LaTeX Beamer (Tema *Madrid*, Color *whale*).
* **`generar_graficas.py`**: Script para generar los diagramas de flujo y matrices en formato PNG.

---

### 3. Instrucciones de Trabajo

1. Abre el cuaderno guiado `01_Condicionales_Firewall_y_Luminancia.ipynb` en Google Colab o JupyterLab y ejecuta secuencialmente cada celda.
2. Lee atentamente la **Analogía Infantil** antes de pasar a las definiciones formales de álgebra booleana.
3. Resuelve los ejercicios intercalados de filtrado de paquetes y umbralización de color.
4. Pasa al cuaderno `01_Laboratorio_Evaluacion.ipynb` y completa los bloques marcados con `### TU CÓDIGO AQUÍ`.
5. Redacta las conclusiones analíticas sobre el costo del error en los cuatro cuadrantes de la matriz de confusión.
