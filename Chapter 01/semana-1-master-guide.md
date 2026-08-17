# Guía Docente Maestra - Semana 1: Fundamentos de IA, Machine Learning y la Jerarquía de Datos

Este documento sirve como la **Semilla Curricular y Guía de Estándares** para la asignatura "Machine Learning aplicado a la Ciberseguridad y el Diseño/Animación Digital". Está diseñado para que cualquier agente instruccional avanzado pueda replicar este formato exacto, nivel de rigor, analogías y estructura en las siguientes 17 semanas del curso.

---

## Estructura Operativa de la Semana (3 Clases por Semana)
*   **Clase 1: Sesión Teórica Magistral (1.5 horas)** - Explicación conceptual profunda, analogías lúdicas y formalización matemática.
*   **Clase 2: Práctica Guiada (1.5 horas)** - Programación interactiva paso a paso en Google Colab con apoyo del docente, exploración de datos reales con Pandas y visualización elemental.
*   **Clase 3: Laboratorio Evaluado (1.5 horas)** - Resolución autónoma de un desafío práctico por parte del estudiante, evaluación multimodelo y defensa analítica (Matriz de Confusión / Toma de decisiones).
*   **Trabajo Autónomo (Fuera de Aula)** - Tarea de investigación/programación y preparación del Quiz de Moodle.

---

# CLASE 1: SESIÓN TEÓRICA
## Tema: Introducción a la Inteligencia Artificial, Machine Learning y la Jerarquía de Necesidades de Datos

### 1. Desglose Teórico y Diferenciación de Dominios
Para comprender la disciplina, es indispensable trazar fronteras claras entre la Inteligencia Artificial (IA), el Machine Learning (ML), el Deep Learning (DL) y la Estadística tradicional [572]:

1.  **Inteligencia Artificial (IA):** El superconjunto teórico y práctico que abarca cualquier técnica que permita a las computadoras simular el comportamiento o razonamiento humano [571, 572]. Incluye sistemas basados en reglas fijas, lógica difusa y heurísticas duras [572, 576, 621].
2.  **Machine Learning (ML):** Un subcampo de la IA enfocado en el desarrollo de algoritmos que aprenden patrones directamente a partir de los datos, sin ser programados explícitamente [572, 575]. El rendimiento del sistema mejora de manera matemática conforme se incrementa el volumen de datos de entrenamiento [575, 629].
3.  **Deep Learning (DL):** Una especialización del ML que utiliza Redes Neuronales Artificiales Multicapa (profundas) para extraer automáticamente jerarquías de características de datos complejos y no estructurados (imágenes, video, audio) [572, 578, 615, 616].
4.  **Estadística vs. Machine Learning:** Mientras la estadística se centra en la inferencia, la significancia matemática de los parámetros y la comprobación de hipótesis bajo estrictos supuestos de distribución previa, el Machine Learning prioriza el poder predictivo, la generalización ante datos no observados y el análisis de patrones a gran escala [200, 423].

---

### 2. La Analogía Infantil (Enfoque "Para Niños de 10 Años")

> **¿Cómo diferenciar IA, ML y DL en el parque de diversiones?**
> 
> *   **La Inteligencia Artificial (IA) es un Robot de Juguete con un manual:** Imagina que tienes un robot programado con un manual muy estricto. El manual dice: *"Si ves una piedra roja, salta; si ves una azul, agáchate"*. El robot parece inteligente, pero si encuentra una piedra amarilla, se confunde por completo porque no está en su manual de reglas fijas.
> *   **El Machine Learning (ML) es un Cachorro Entrenable:** En lugar de darle un manual de reglas, le enseñas con ejemplos. Le muestras 100 fotos de gatos y 100 de perros. Al principio se equivoca, pero cada vez que acierta le das una galleta virtual (un premio matemático). Con el tiempo, el cachorro aprende por sí mismo a reconocer los rasgos de un gato (orejas puntiagudas, bigotes) sin que nadie le haya escrito una regla para ello.
> *   **El Deep Learning (DL) es un Detective con Supergafas:** Este detective no solo reconoce al gato, sino que tiene gafas especiales que desarman la imagen en millones de hilos invisibles. Primero mira las líneas de los bordes, luego junta esas líneas para formar la silueta de los ojos, luego junta los ojos con la nariz y finalmente entiende la cara completa del gato en la oscuridad profunda, procesando datos superdifíciles como si tuviera un cerebro gigante de capas infinitas.

---

### 3. Rigor Académico y Formalización Matemática

#### A. Representación Vectorial de una Muestra (Feature Vector)
En Machine Learning, cada instancia o muestra individual del mundo real se transforma en un vector matemático de características en un espacio multidimensional [345, 346, 367]:

$$\mathbf{x}_i = [x_{i,1}, x_{i,2}, \dots, x_{i,d}]^T \in \mathbb{R}^d$$

Donde:
*   $\mathbf{x}_i$ representa la $i$-ésima muestra (ej., una dirección IP sospechosa o un píxel digital) [345, 346].
*   $d$ representa la dimensionalidad del espacio de características (features) [345, 346].
*   $x_{i,j}$ es el valor numérico de la característica $j$ para la muestra $i$ [345].

#### B. La Función de Mapeo Predictivo (Target Function)
El objetivo de un algoritmo de aprendizaje supervisado es aproximar una función predictiva $f$ que mapee las características de entrada al espacio de etiquetas de salida, minimizando el error empírico [327, 339, 362]:

$$f: \mathcal{X} \to \mathcal{Y}$$

Para clasificación binaria (ej. Tránsito de Red Seguro vs. DDoS):

$$\mathcal{Y} = \{0, 1\} \quad \text{o} \quad \mathcal{Y} = \{-1, +1\} [370, 381]$$

Para regresión (ej. tiempo de renderizado de un fotograma en segundos):

$$\mathcal{Y} = \mathbb{R} [370, 378]$$

#### C. Tipos de Aprendizaje Matemático
1.  **Supervisado:** Contamos con un dataset etiquetado $\mathcal{D} = \{(\mathbf{x}_i, y_i)\}_{i=1}^n$ donde el modelo aprende minimizando una función de pérdida $\mathcal{L}(y_i, f(\mathbf{x}_i))$ [339, 340, 367].
2.  **No Supervisado:** El dataset carece de etiquetas $\mathcal{D} = \{\mathbf{x}_i\}_{i=1}^n$. El modelo debe encontrar la estructura subyacente o agrupaciones (Clustering) minimizando distancias internas o maximizando la densidad de probabilidad [343, 344, 401, 407].
3.  **Semi-supervisado:** Se dispone de una pequeña cantidad de datos etiquetados y una gran cantidad de datos no etiquetados para mejorar la precisión del clasificador a bajo costo [225].
4.  **Por Refuerzo:** Un agente interactúa con un entorno dinámico y aprende a tomar decisiones secuenciales mediante un sistema de recompensas y penalizaciones en tiempo real [225, 637].

#### D. La Jerarquía de Necesidades de Datos (Monica Rogati)
No podemos modelar sin una base robusta. Joe Reis y Matt Housley, basándose en la pirámide de Monica Rogati, advierten que el 70%-80% del tiempo de un científico de datos se consume en las capas inferiores [296, 298]:

```
      /\
     /  \      Inteligencia Artificial / Machine Learning (Modelado)
    /____\     ---------------------------------------------------
   /      \    A/B Testing / Experimentación / Heurísticas de Reglas
  /________\   ---------------------------------------------------
 /          \  Limpieza de Datos / Anomaly Detection / Preparación
/____________\ ---------------------------------------------------
|            | Ingesta / Movimiento / Pipelines ETL robustos
|____________| ---------------------------------------------------
|   COLLECT  | Sensores / Logs de Red / Captura de Eventos / APIs
|____________|
```

Intentar entrenar un algoritmo avanzado de clasificación de malware o generación de arte digital sin pipelines de datos estables, almacenamiento consistente y procesos de limpieza previos es un antipatrón costoso e inviable [296, 297].

---

# CLASE 2: PRÁCTICA GUIADA (GOOGLE COLAB)
## Tema: Exploración de Datos con Pandas e Introducción Práctica al Workspace

### 1. Importación y Carga de Datos
En este laboratorio guiado, cargaremos el dataset **Iris Species** directamente desde el repositorio público de scikit-learn utilizando Pandas para analizar sus atributos físicos antes de entrenar un clasificador [327, 360, 364].

#### Comando en Python:
```python
import pandas as pd
from sklearn.datasets import load_iris

# Carga del dataset Iris
iris_raw = load_iris()
df = pd.DataFrame(data=iris_raw.data, columns=iris_raw.feature_names)
df['species'] = iris_raw.target

# Mapeo de códigos numéricos a nombres reales de las especies
species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
df['species_name'] = df['species'].map(species_map)

# Mostrar las primeras 5 filas
df.head()
```

#### Explicación del Código:
1. `import pandas as pd`: Importa la librería estándar para la manipulación y análisis de estructuras de datos bidimensionales (DataFrames) [358].
2. `load_iris()`: Descarga de manera determinista el dataset clásico que contiene 150 muestras de flores Iris con 4 atributos numéricos de longitud y ancho de sépalos y pétalos [327, 360].
3. `pd.DataFrame(data=..., columns=...)`: Instancia la estructura tabular de Pandas asignando los nombres correspondientes a cada columna de características [358, 362].
4. `df['species'] = iris_raw.target`: Agrega la columna de etiquetas numéricas que representan la clase real de cada flor (0, 1 o 2) [360, 367].
5. `df['species_name'] = df['species'].map(...)`: Realiza un mapeo semántico para facilitar la comprensión humana del dataset al transformar números en categorías reales [415].

---

### 2. Consultas y Filtros Avanzados (Pandas Queries)
Para desarrollar el pensamiento analítico, obligaremos a los estudiantes a explorar el comportamiento de los datos mediante consultas personalizadas.

#### Consulta A: Filtrado de Flores con Características de Píxel/Dimensión Extrema
*Objetivo:* Buscar aquellas flores de la especie *setosa* que poseen pétalos extremadamente delgados (ancho menor a 0.2 cm), simulando un filtro de seguridad de umbral bajo.

```python
# Consulta usando query() de Pandas
filtro_setosa = df.query("species_name == 'setosa' and `petal width (cm)` <= 0.2")
print(f"Total de muestras encontradas: {len(filtro_setosa)}")
filtro_setosa.head()
```

#### Explicación del Código:
1. `df.query(...)`: Evalúa una expresión lógica en formato de cadena directamente sobre las columnas del DataFrame. Al contener espacios el nombre de la columna `petal width (cm)`, se encierra entre comillas invertidas (backticks) para proteger la sintaxis.
2. `and`: Operador lógico booleano de intersección que exige el cumplimiento simultáneo de ambas condiciones lógicas.

#### Consulta B: Análisis de Correlación Lineal
*Objetivo:* Calcular la correlación de Pearson entre la longitud del pétalo y el ancho del pétalo para entender si el crecimiento de una característica es proporcional a la otra [213, 232].

```python
# Cálculo de la matriz de correlación
correlacion_features = df[['petal length (cm)', 'petal width (cm)']].corr(method='pearson')
print(correlacion_features)
```

#### Explicación del Código:
1. `df[['col1', 'col2']]`: Filtra el DataFrame original seleccionando únicamente las columnas numéricas de interés.
2. `.corr(method='pearson')`: Calcula el coeficiente de correlación lineal de Pearson, produciendo un valor entre -1 y +1, donde +1 denota una relación lineal positiva perfecta.

---

# CLASE 3: LABORATORIO EVALUADO (SOPORTE AUTÓNOMO)
## Entregable: Clasificador Heurístico Manual vs. Baseline Predictivo

### Instrucciones del Desafío para el Estudiante:
1.  **Cargar el Dataset Real:** Ingesta el dataset de Iris usando la estructura guiada en la Clase 2 [360].
2.  **Construir un "Modelo Heurístico" (Hecho a mano):** Programa una función puramente algorítmica utilizando bloques `if-elif-else` que prediga si una flor es *setosa* o *no-setosa* basándote únicamente en el umbral del pétalo observado en tus análisis visuales de la Clase 2 [364, 365].
3.  **Comparar con un "Modelo Algorítmico":** Aplica de forma conceptual el clasificador básico de Vecinos Más Cercanos ($k$-NN) de scikit-learn con $k=3$ [327, 365, 413].
4.  **Generar la Matriz de Confusión y Defender de Negocio:** Calcula manualmente la matriz de confusión de tu modelo heurístico contra el objetivo real. Describe detalladamente las implicaciones del negocio utilizando los cuatro extremos de la matriz en un entorno simulado de ciberseguridad corporativa.

---

### Código Base del Laboratorio (Para Google Colab):

```python
import numpy as np
from sklearn.metrics import confusion_matrix

# 1. Definición del Clasificador Heurístico Manual
def clasificador_manual(row):
    # Regla basada en el análisis visual: las setosas tienen pétalos muy cortos
    if row['petal length (cm)'] < 2.0:
        return 0  # Setosa
    else:
        return 1  # No-Setosa (Versicolor o Virginica)

# Aplicar la función fila por fila sobre el DataFrame
df['prediccion_heuristica'] = df.apply(clasificador_manual, axis=1)

# Clasificación Real Binaria: 0 (Setosa), 1 (Otras)
df['label_binario'] = df['species'].apply(lambda x: 0 if x == 0 else 1)

# 2. Calcular la Matriz de Confusión Manualmente
y_real = df['label_binario']
y_pred = df['prediccion_heuristica']

conf_matrix = confusion_matrix(y_real, y_pred)
print("Matriz de Confusión Obtenida:")
print(conf_matrix)
```

---

### Defensa Analítica Requerida (Rubrica de Evaluación Docente):

El estudiante debe responder por escrito en una celda de texto de Google Colab la siguiente interpretación de negocio, simulando que la especie **"Setosa" es una Alerta de Intrusión Crítica (Malware)** y **"No-Setosa" es Tráfico de Red Legítimo**:

*   **Verdadero Positivo (VP):** El modelo manual clasifica una muestra como *Setosa* (Malware) y realmente es una *Setosa* (Malware) [620]. *Implicación:* Éxito rotundo. El firewall por software intercepta la amenaza en tiempo real y protege los activos digitales de la empresa de diseño.
*   **Verdadero Negativo (VN):** El modelo clasifica el paquete como *No-Setosa* (Tráfico Legítimo) y en verdad es *No-Setosa* (Tráfico Legítimo). *Implicación:* Eficiencia operativa óptima. El tráfico fluye sin fricciones y los diseñadores renderizan sus animaciones 3D sin bloqueos innecesarios.
*   **Falso Positivo (FP) - Error Tipo I:** El modelo predice que un paquete de red es *Setosa* (Malware) pero en realidad es *No-Setosa* (Tráfico Legítimo de renderizado 3D) [620]. *Costo de Negocio:* Alta fricción. Se interrumpe la conexión del equipo de animación digital en pleno envío de renders críticos hacia la granja de servidores, generando retrasos operativos y falsas alarmas que saturan al equipo de operaciones de seguridad (SOC).
*   **Falsos Negativos (FN) - Error Tipo II (El Extremo Más Peligroso):** El modelo predice que un paquete es *No-Setosa* (Tráfico Legítimo) pero en realidad es *Setosa* (Malware infiltrado) [620]. *Costo de Negocio:* Catástrofe de Ciberseguridad. Se permite el ingreso silencioso de un Ransomware a la red corporativa, comprometiendo la propiedad intelectual del estudio (modelos 3D y secuencias de animación protegidas por contratos de confidencialidad) y cifrando los servidores locales de almacenamiento de datos [584, 585].

---

# TAREAS AUTÓNOMAS Y COMPLEMENTOS

### 1. Tarea para la Casa (Homework):
*   **Instrucciones:** Modifica los umbrales de tu `clasificador_manual` utilizando ahora la columna `petal width (cm)` en lugar de la longitud [364]. Encuentra de forma iterativa el umbral exacto que minimice a **cero** los Falsos Negativos, sin importar que se incrementen levemente los Falsos Positivos [372, 393]. Argumenta matemáticamente por qué esta parametrización es preferible en un entorno de ciberseguridad reactiva [312, 314].

---

### 2. Quiz de Moodle (Formato Aiken para Importación Directa)

```text
¿Qué subcampo de la IA se enfoca específicamente en entrenar algoritmos para aprender patrones directamente de los datos sin ser programados explícitamente?
A. Inteligencia Artificial General
B. Machine Learning
C. Sistemas Expertos basados en Reglas
D. Procesamiento de Lenguaje Natural duro
ANSWER: B

¿En la Matriz de Confusión, qué representa un Falso Negativo (Error Tipo II) en el contexto de detección de intrusiones de red?
A. Clasificar un tráfico de red legítimo como una intrusión maliciosa.
B. Clasificar un tráfico malicioso como si fuera un acceso seguro y legítimo.
C. Bloquear preventivamente el acceso a un servidor de almacenamiento local.
D. Identificar correctamente un ataque DDoS en tiempo real.
ANSWER: B

De acuerdo con la Jerarquía de Necesidades de Datos de Monica Rogati, ¿qué fase se encuentra en la base fundamental antes de intentar construir modelos de Machine Learning?
A. Redes Neuronales Profundas (Deep Learning)
B. Pruebas A/B y Experimentación avanzada
C. Recolección de Datos (Collect / Ingesta / Logs de Red)
D. Optimización fina de hiperparámetros
ANSWER: C

¿Qué representa matemáticamente la variable "d" en un vector de características representado como x = [x1, x2, ..., xd]?
A. El número total de muestras o instancias en el dataset de entrenamiento.
B. La etiqueta o variable objetivo que deseamos predecir.
C. La dimensionalidad o cantidad de atributos característicos de la muestra.
D. El coeficiente de correlación lineal de Pearson obtenido.
ANSWER: C

¿Cuál es la principal diferencia metodológica entre la Estadística tradicional y el Machine Learning moderno?
A. El Machine Learning busca comprobar supuestos de distribución paramétrica rigurosa por encima de todo.
B. La Estadística tradicional prioriza el rendimiento predictivo ante datos nuevos no observados.
C. El Machine Learning prioriza el poder de predicción y la capacidad de generalización del modelo.
D. El Machine Learning solo trabaja con variables cualitativas y nominales.
ANSWER: C
```

---

## Referencias Bibliográficas (Norma APA)

*   Grus, J. (2019). *Data Science from Scratch: First Principles with Python* (2nd ed.). O'Reilly Media. [199, 203]
*   Müller, A. C., & Guido, S. (2017). *Introduction to Machine Learning with Python: A Guide for Data Scientists*. O'Reilly Media. [324]
*   Reis, J., & Housley, M. (2022). *Fundamentals of Data Engineering: Plan and Build Robust Data Systems*. O'Reilly Media. [296]
*   Jamison, P. (2023). *The (Absolute) Beginner’s Guide to AI: Discover the Exciting History of Artificial Intelligence, Today's Developments, and Tomorrow's Solutions*. Paul Jamison Publishing. [567]
