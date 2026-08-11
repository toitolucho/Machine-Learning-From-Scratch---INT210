# Módulo 0: Fundamentos Algorítmicos y Estructuras de Control en Python
## Semana 1: Nivelación Algorítmica y Control de Flujo Computacional

Bienvenido a la **Semana 1** del Diplomado en Ciencia de Datos e Inteligencia Artificial (*INT210: Machine Learning From Scratch*). Este módulo de nivelación ha sido rigurosamente diseñado para dotar a los estudiantes de perfiles en **Ciberseguridad** y **Arte/Animación Digital** de las bases fundamentales de control de flujo algorítmico, lógica proposicional y estructuras de datos nativas de Python.

---

### Objetivos de Aprendizaje

1. **Dominar el Control de Flujo:** Comprender la bifurcación lógica condicional (`if-elif-else`), estructuras multicamino (`match-case` y diccionarios de despacho), e iteraciones deterministas e indeterminadas (`for`, `while`).
2. **Construir Modelos Heurísticos basados en Reglas:** Implementar clasificadores manuales de detección de anomalías y filtrado sin librerías de caja negra.
3. **Evaluar el Desempeño con Rigor:** Calcular y argumentar matrices de confusión manuales, comprendiendo el costo operativo de los Falsos Positivos y Falsos Negativos en seguridad y entornos multimedia.
4. **Optimizar Complejidad y Memoria:** Distinguir entre complejidades temporales $\mathcal{O}(1)$ y $\mathcal{O}(N)$, así como el impacto de la evaluación perezosa (*lazy evaluation*) frente a colecciones en memoria RAM.

---

### Estructura de la Semana 1

| Sesión | Tema Principal | Contexto Ciberseguridad | Contexto Arte Digital |
| :--- | :--- | :--- | :--- |
| **Sesión 0.1** | Bifurcaciones Condicionales y Álgebra Booleana | Firewall por reglas y filtrado de paquetes IP | Umbrales de luminancia y segmentación de píxeles |
| **Sesión 0.2** | `match-case` y Diccionarios de Despacho | Triaje de alertas SOC (Malware, Phishing, DoS) | Decodificador y renderizado multiformato (PNG, SVG, RAW) |
| **Sesión 0.3** | Bucles `for`, `enumerate` y Comprensiones | Auditoría de escaneo de puertos de red | Filtros matriciales sobre canales RGB y escala de grises |
| **Sesión 0.4** | Bucles `while`, Centinelas y Convergencia | Listener continuo de tráfico de red | Algoritmos adaptativos de iluminación y sombreado |

---

### Mapa de Archivos por Sesión

Cada subcarpeta de sesión contiene siete componentes estándar:
1. `README.md`: Hoja de ruta y objetivos específicos para el estudiante.
2. `0X_<Tema>.ipynb`: Cuaderno guiado paso a paso con datasets reales.
3. `0X_Guia_de_Trabajo_Soluciones.md`: Solucionario y notas metodológicas para el docente.
4. `0X_Laboratorio_Evaluacion.ipynb`: Cuaderno de reto autónomo para el estudiante (`# TODO`).
5. `0X_Soluciones_Laboratorio.md`: Respuestas y análisis de impacto de negocio del reto.
6. `0X_Presentacion_Clase.tex`: Diapositivas Beamer (LaTeX) con los fundamentos teóricos.
7. `generar_graficas.py`: Script Python para generar los diagramas y figuras visuales.

---

### Requisitos Previos y Entorno

- **Python 3.10+** (Requerido para la sintaxis de *Structural Pattern Matching* `match-case`).
- Librerías principales: `pandas`, `numpy`, `matplotlib`, `seaborn`.
- Compatibilidad directa con Google Colab y JupyterLab.
