# Sesión 0.3: Bucles Iterativos Deterministas (`for`), `enumerate` y Comprensiones

## Guía de la Sesión para el Estudiante

En esta sesión se abordará la iteración sobre secuencias de longitud finita o conocida. Se estudiarán los protocolos iteradores nativos de Python, las funciones generadoras de secuencias (`range()`, `enumerate()`, `zip()`) y la técnica de **List/Dict Comprehensions** para procesamiento de alto rendimiento.

---

### 1. Objetivos de Aprendizaje

- **Dominar el bucle `for`:** Recorrido ordenado sobre estructuras iterables.
- **Comprender el Protocolo Iterador:** Métodos mágicos `__iter__()` y `__next__()` y la excepción `StopIteration`.
- **Diferenciar Evaluación Perezosa (*Lazy Evaluation*) vs. Memoria RAM:** `range()` como generador virtual frente a listas materializadas en memoria.
- **Aplicar `enumerate()` y `zip()`:** Indexación simultánea y combinación de flujos de datos sin variables contadoras manuales.
- **Escribir Comprensiones Pythonicas:** Construcción concisa de listas y diccionarios con filtros condicionales integrados.
- **Procesar matrices de color RGB en Arte Digital:** Conversión a escala de grises e inversión cromática.
- **Auditar puertos de red en Ciberseguridad:** Escaneo e identificación de vectores de ataque por puertos expuestos.

---

### 2. Estructura de Materiales

* **`03_Iteracion_Matrices_RGB_y_Logs_Puertos.ipynb`**: Cuaderno guiado con manipulación matricial de píxeles y escaneo de puertos de red.
* **`03_Guia_de_Trabajo_Soluciones.md`**: Solucionario docente y consejos sobre gestión de memoria RAM vs generadores.
* **`03_Laboratorio_Evaluacion.ipynb`**: Reto autónomo con bloques `# TODO` para auditoría masiva de logs de puertos y normalización de paletas artísticas.
* **`03_Soluciones_Laboratorio.md`**: Código completo y evaluación de la matriz de confusión sobre detección de puertos anómalos.
* **`03_Presentacion_Clase.tex`**: Presentación académica en LaTeX Beamer (Tema *Madrid*, Color *whale*).
* **`generar_graficas.py`**: Script para generar diagramas de memoria RAM vs Lazy Evaluation.
