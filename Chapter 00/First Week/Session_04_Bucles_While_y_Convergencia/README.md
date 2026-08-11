# Sesión 0.4: Bucles Indeterminados (`while`), Centinelas y Convergencia Numérica

## Guía de la Sesión para el Estudiante

En esta sesión se estudiarán las iteraciones no deterministas (donde el número total de pasos no se conoce de antemano), el uso de centinelas de control (`break`, `continue`), la evasión rigurosa de bucles infinitos y los fundamentos de **convergencia numérica** aplicados a la computación visual y la ciberseguridad.

---

### 1. Objetivos de Aprendizaje

- **Dominar la estructura `while`:** Iteraciones guiadas por condiciones de guarda dinámicas.
- **Implementar Patrones de Señal Centinela:** Mecanismos de parada con `break` y filtrado con `continue`.
- **Prevenir el Problema del Bucle Infinito:** Condiciones de corte por límite de épocas/iteraciones máximas (*Guard Timeout*).
- **Comprender la Convergencia y el Teorema del Punto Fijo:** Iterar hasta que el error residual descienda por debajo de un umbral $\epsilon$ ($|x_{k+1} - x_k| < \epsilon$).
- **Simular un *Network Listener* en Ciberseguridad:** Escucha de paquetes en tiempo real hasta recibir paquetes de terminación (`FIN` / `RST`).
- **Implementar Renderizado Adaptativo en Arte Digital:** Refinamiento iterativo de iluminación y corrección de sombras.

---

### 2. Estructura de Materiales

* **`04_Network_Listener_y_Render_Adaptativo.ipynb`**: Cuaderno guiado con simulación de listener de paquetes y algoritmo iterativo de iluminación.
* **`04_Guia_de_Trabajo_Soluciones.md`**: Solucionario docente con notas teóricas sobre el Problema de la Parada de Turing (*Halting Problem*).
* **`04_Laboratorio_Evaluacion.ipynb`**: Reto autónomo con bloques `# TODO` para construir un analizador de anomalías por ventana deslizante iterativa y matriz de confusión.
* **`04_Soluciones_Laboratorio.md`**: Código de solución y análisis del impacto financiero de convergencia y estabilidad en producción.
* **`04_Presentacion_Clase.tex`**: Presentación académica en LaTeX Beamer (Tema *Madrid*, Color *whale*).
* **`generar_graficas.py`**: Script para generar la curva de convergencia exponencial del error residual $\epsilon$.
