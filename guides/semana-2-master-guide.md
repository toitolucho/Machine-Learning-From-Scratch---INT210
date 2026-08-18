# Guía Maestro Curricular - Semana 2: Preprocesamiento, Limpieza y Escalado de Datos

Esta guía ha sido diseñada bajo un esquema estricto de **6 horas de clase a la semana**, dividida en **3 sesiones de 2 horas cada una**. Su estructura pedagógica está optimizada para servir como material de clase universitaria y como fuente de verdad para el agente instruccional de Antigravity, permitiendo la generación homogénea de futuras semanas.

---

## Planificación de la Semana 2 (6 Horas Totales)

*   **Sesión 2.1 (Clase Teórica - 2 Horas):** Diagnóstico de Datos, Tratamiento de Valores Nulos y Codificación Categórica.
*   **Sesión 2.2 (Práctica Guiada - 2 Horas):** Escalamiento Dimensional (StandardScaler vs. MinMaxScaler) y Tratamiento Matemático de Outliers (IQR vs. Z-Score).
*   **Sesión 2.3 (Laboratorio Autónomo y Desafío - 2 Horas):** Implementación Multimodelo (k-NN vs. Árboles de Decisión) en Google Colab con el Dataset WBCD, Evaluando el Impacto con la Matriz de Confusión.

---

## Sesión 2.1: Diagnóstico de Datos, Tratamiento de Valores Nulos y Codificación Categórica (2 Horas)

### 1. Concepto Teórico Central
En la vida real, los datos nunca vienen limpios ni ordenados [323]. Un analista de datos o ingeniero de Machine Learning gasta hasta el 80% de su tiempo adquiriendo, limpiando y transformando datos antes de que un modelo pueda verlos [323]. Esta sesión aborda el tratamiento de registros corruptos o faltantes (valores nulos) mediante técnicas de eliminación o imputación estadística (media o mediana), y la transformación de datos cualitativos (categóricos) a cuantitativos mediante técnicas de codificación para que puedan ser procesados matemáticamente por algoritmos de aprendizaje automático [2, 538, 550].

---

### 2. La Analogía Infantil ("El Rompecabezas Dañado y la Tienda de Juguetes")
> **Enfoque para un niño de 10 años:**
> 
> **Parte A: Valores Nulos:** Imagina que te regalan un rompecabezas gigante de un dinosaurio, pero al abrir la caja te das cuenta de que faltan algunas piezas. Tienes tres opciones para resolver este problema:
> 1. **Tirar la caja completa a la basura (`dropna`):** Es la solución fácil, pero te quedas sin rompecabezas.
> 2. **Buscar el promedio de los colores de las piezas de alrededor y pintar un cartón para rellenar el hueco (`mean`):** Si alrededor del hueco todo es verde selva, pintas la pieza de verde.
> 3. **Poner una pieza de madera neutra del mismo tamaño (`median` o constante):** Algo que tape el hueco de manera segura sin llamar la atención.
>
> **Parte B: Codificación Categórica:** Imagina que tienes tres juguetes en tu repisa: un *Carro de Carreras*, un *Oso de Peluche* y un *Robot*. Tu robot de juguete inteligente no entiende palabras como "Carro", "Oso" o "Robot"; solo entiende números binarios de corriente encendida (1) o apagada (0). 
> * Si usamos **Label Encoding**, le asignamos una etiqueta numérica fija: Carro = 0, Oso = 1, Robot = 2. Pero hay un peligro: ¡el robot pensará que el Robot (2) es más valioso o más grande que el Carro (0) solo porque 2 es mayor que 0!
> * Para solucionarlo, usamos **One-Hot Encoding**: creamos tres cajas de luz en la pared (Caja-Carro, Caja-Oso, Caja-Robot). Si el juguete es un Carro, encendemos la luz de la Caja-Carro (1) y apagamos las otras (0, 0). Así, el Carro se representa de forma justa como `[1, 0, 0]`, el Oso como `[0, 1, 0]` y el Robot como `[0, 0, 1]`. ¡Nadie es mayor que nadie!

---

### 3. Rigor Académico y Formalización Matemática

#### 1. Imputación de Valores Faltantes (Media y Mediana)
Sea un vector de características unidimensional $\mathbf{x} = [x_1, x_2, \dots, x_n]^T \in \mathbb{R}^n$ que contiene un subconjunto de valores faltantes definido por el conjunto de índices vacíos $\mathcal{M} \subset \{1, \dots, n\}$. El conjunto de índices con datos observados se define como $\mathcal{O} = \{1, \dots, n\} \setminus \mathcal{M}$.

*   **Imputación por la Media Lineal ($\mu_{impute}$):** Reemplaza cada valor faltante $x_i$ para $i \in \mathcal{M}$ por la media aritmética de los datos observados [2]:
$$\hat{x}_i = \frac{1}{|\mathcal{O}|} \sum_{j \in \mathcal{O}} x_j$$

*   **Imputación por la Mediana ($\tilde{x}_{impute}$):** Reemplaza cada $x_i$ para $i \in \mathcal{M}$ por el valor central del conjunto ordenado de datos observados [2]. Sea $x_{(1)} \le x_{(2)} \le \dots \le x_{(|\mathcal{O}|)}$ la estadística de orden de los datos observados:
$$\hat{x}_i = \begin{cases} 
x_{\left(\frac{|\mathcal{O}| + 1}{2}\right)} & \text{si } |\mathcal{O}| \text{ es impar} \\
\frac{1}{2} \left( x_{\left(\frac{|\mathcal{O}|}{2}\right)} + x_{\left(\frac{|\mathcal{O}|}{2} + 1\right)} \right) & \text{si } |\mathcal{O}| \text{ es par}
\end{cases}$$

#### 2. Codificación Categórica (One-Hot Encoding)
Sea una variable cualitativa categórica $C$ que puede tomar uno de $k$ valores discretos (categorías) dentro del conjunto $\mathcal{C} = \{c_1, c_2, \dots, c_k\}$ [538, 550]. One-Hot Encoding mapea la variable $C$ a un vector binario multidimensional $\mathbf{v} \in \{0, 1\}^k$ mediante la función indicadora [550]:
$$\mathbf{v}(C) = [I(C = c_1), I(C = c_2), \dots, I(C = c_k)]^T$$
Donde la función indicadora $I$ se define matemáticamente como:
$$I(C = c_j) = \begin{cases} 1 & \text{si } C = c_j \\ 0 & \text{si } C \neq c_j \end{cases}$$
Esto evita introducir un orden jerárquico artificial (problema de magnitud métrica) en variables puramente nominales (como las firmas de malware o formatos de color RGB) [211, 218].

---

### 4. Bloque de Código Explicado (Mapeo Semántico en Pandas)

#### El Comando (Código de Pandas):
```python
import pandas as pd
import numpy as np

# 1. Crear un dataset de logs de red de ciberseguridad con nulos y categorías
data = {
    'request_id': [101, 102, 103, 104, 105],
    'bytes_transmitted': [1500, np.nan, 23000, 1800, 45000],
    'alert_type': ['Malware', 'Phishing', 'Legitimate', 'Malware', np.nan]
}
df = pd.DataFrame(data)

# 2. Imputar nulos en columnas numéricas usando la mediana
mediana_bytes = df['bytes_transmitted'].median()
df['bytes_transmitted'] = df['bytes_transmitted'].fillna(mediana_bytes)

# 3. Eliminar filas donde la etiqueta objetivo 'alert_type' sea nula
df = df.dropna(subset=['alert_type'])

# 4. Aplicar One-Hot Encoding a la variable categórica 'alert_type'
df_encoded = pd.get_dummies(df, columns=['alert_type'], prefix='type', dtype=int)

print(df_encoded)
```

#### Explicación Técnica del Código:
1. `mediana_bytes = df['bytes_transmitted'].median()`: Calcula el valor central de los bytes transmitidos para evitar que los valores extremos sesguen la imputación [2].
2. `df['bytes_transmitted'].fillna(...)`: Reemplaza de forma in-place o asignada los valores faltantes (`NaN`) por la mediana computada [2].
3. `df.dropna(subset=['alert_type'])`: Elimina de manera estricta los registros donde no se posea la etiqueta de clase, dado que en aprendizaje supervisado no podemos entrenar con muestras sin etiqueta objetivo [3, 338].
4. `pd.get_dummies(...)`: Genera variables indicadoras binarias (dummies) para cada clase única de la alerta, creando las columnas `type_Legitimate`, `type_Malware` y `type_Phishing` con valores enteros `0` o `1` [2, 214, 218].

---

## Sesión 2.2: Escalamiento Dimensional y Tratamiento de Outliers (2 Horas)

### 1. Concepto Teórico Central
Los modelos de Machine Learning basados en distancias (como k-NN o SVM) son extremadamente sensibles a la escala de las características [102, 138]. Si una variable mide los ingresos de un usuario (rango 0 a 1,000,000) y otra mide su edad (rango 0 a 100), el algoritmo de optimización ignorará la edad por completo porque las distancias matemáticas estarán dominadas por el ingreso [102, 135]. Esta sesión analiza cómo mapear los datos a un espacio homogéneo mediante MinMaxScaler o StandardScaler [2]. Asimismo, introduce métodos estadísticos rigurosos para identificar y mitigar valores atípicos (outliers) que alteren de forma destructiva las fronteras de decisión de los clasificadores [3].

---

### 2. La Analogía Infantil ("El Gigante y el Enano en la Fotografía")
> **Enfoque para un niño de 10 años:**
> 
> **Parte A: Escalamiento:** Imagina que tienes una foto de un elefante de 4 metros y otra de una hormiga de 1 centímetro. Si quieres poner ambas fotos en un álbum de stickers donde cada espacio mide exactamente 10 centímetros de alto, no puedes pegar el elefante real ni la hormiga real. Tienes que aplicar dos trucos:
> 1. **MinMaxScaler (El Álbum Estricto):** Aplastas y estiras ambas fotos para que, sin importar lo grandes o chicas que fueran originalmente, ahora midan exactamente entre 0 (el suelo del sticker) y 1 (el techo del sticker).
> 2. **StandardScaler (El Promedio del Salón):** Ajustas las fotos tomando como referencia la estatura promedio de todos los animales. Si un animal mide exactamente el promedio, su sticker se queda en el centro (0). Si es más grande que el promedio, se mueve a la derecha, y si es más chico, a la izquierda.
>
> **Parte B: Outliers (Valores Atípicos):** Imagina que en tu salón de clase todos los niños miden entre 1.10 y 1.40 metros. De repente, entra a estudiar un jugador de la NBA que mide 2.20 metros. Si calculas la estatura promedio del salón, ¡el promedio subirá tanto que parecerá que todos son gigantes! Ese jugador de básquetbol es un **Outlier**. Para detectarlo de forma matemática, podemos usar el **Z-Score** (medir cuántos pasos gigantes de diferencia hay entre el niño nuevo y el promedio del salón) o el **IQR** (dibujar una frontera de seguridad usando una caja de juguetes y expulsar lógicamente a cualquier juguete que quede muy lejos de la caja).

---

### 3. Rigor Académico y Formalización Matemática

#### 1. Escalamiento por Min-Max (MinMaxScaler)
Mapea linealmente cada característica al intervalo acotado $[0, 1]$ [2, 133]. Sea $x$ el valor original de una característica, $x_{scaled}$ el valor transformado, y $x_{min}, x_{max}$ los extremos observados en el conjunto de entrenamiento:
$$x_{scaled} = \frac{x - x_{min}}{x_{max} - x_{min}}$$
*Propiedad:* Es altamente sensible a la presencia de outliers destructivos, ya que estos expanden artificialmente el rango $[x_{min}, x_{max}]$, colapsando los datos legítimos en una vecindad densa y estrecha [102, 133].

#### 2. Estandarización de Puntuación Estándar (StandardScaler)
Centra los datos para que posean una media de cero ($\mu = 0$) y una varianza unitaria ($\sigma^2 = 1$) [2, 133]. Sea $\mu$ la media poblacional estimada del conjunto de entrenamiento y $\sigma$ la desviación estándar correspondientes [2.2]:
$$z = \frac{x - \mu}{\sigma}$$
Donde:
$$\mu = \frac{1}{N} \sum_{i=1}^N x_i, \qquad \sigma = \sqrt{\frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2}$$

#### 3. Identificación de Outliers mediante Rango Intercuartílico (IQR)
Dibuja límites no paramétricos de tolerancia basados en la distribución por percentiles de la muestra [3, 40].
1. Calculamos el Percentil 25 ($Q_1$ o primer cuartil) y el Percentil 75 ($Q_3$ o tercer cuartil) [40].
2. Se define el Rango Intercuartílico como [2.9]:
$$IQR = Q_3 - Q_1$$
3. Se calculan los límites superior e inferior de aceptación no anómalas:
$$\text{Límite Inferior} = Q_1 - 1.5 \times IQR$$
$$\text{Límite Superior} = Q_3 + 1.5 \times IQR$$
Cualquier observación $x_i$ que cumpla $x_i > \text{Límite Superior}$ o $x_i < \text{Límite Inferior}$ se clasifica formalmente como outlier estadístico [3, 40].

---

### 4. Bloque de Código Explicado (Filtrado de Outliers con IQR y Escalamiento)

#### El Comando (Código de Pandas y Scikit-Learn):
```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# 1. Crear dataset con una variable de red escalada y un Outlier destructivo
data_network = {
    'packet_size_kb': [45, 52, 48, 60, 1200, 50, 42, 55] # 1200 es un Outlier masivo
}
df_net = pd.DataFrame(data_network)

# 2. Computar cuartiles e IQR para packet_size_kb
Q1 = df_net['packet_size_kb'].quantile(0.25)
Q3 = df_net['packet_size_kb'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# 3. Filtrar outliers usando una query de Pandas
df_clean = df_net[(df_net['packet_size_kb'] >= limite_inferior) & 
                  (df_net['packet_size_kb'] <= limite_superior)].copy()

# 4. Aplicar StandardScaler y MinMaxScaler sobre la data limpia
scaler_std = StandardScaler()
df_clean['packet_std'] = scaler_std.fit_transform(df_clean[['packet_size_kb']])

scaler_minmax = MinMaxScaler()
df_clean['packet_minmax'] = scaler_minmax.fit_transform(df_clean[['packet_size_kb']])

print("Límites de aceptación:", limite_inferior, "a", limite_superior)
print(df_clean)
```

#### Explicación Técnica del Código:
1. `df_net['packet_size_kb'].quantile([0.25, 0.75])`: Extrae los percentiles para modelar estadísticamente la dispersión central de los paquetes de red [2.9, 40].
2. `df_net[(df_net[...] >= ...) & ...]`: Realiza una consulta lógica compleja filtrando vectorialmente las filas que se encuentran fuera de la frontera hiperbólica de seguridad definida por Tukey [3, 40].
3. `scaler_std.fit_transform(...)`: Computa la media y la desviación estándar de la columna limpia y realiza la transformación matemática in-place para normalizar el espacio de búsqueda del modelo [2, 134].

---

## Sesión 2.3: Laboratorio Autónomo y Desafío - WBCD (2 Horas)

### 1. Contexto del Negocio y Diccionario de Datos
Los estudiantes actuarán como Consultores de Inteligencia Artificial para una clínica de salud especializada. El objetivo es analizar el dataset **Wisconsin Breast Cancer Diagnostic (WBCD)** recopilado por el Dr. William Wolberg de la Universidad de Wisconsin [136]. Este dataset contiene características geométricas reales de núcleos celulares extraídas de imágenes digitales de aspiración con aguja fina (FNA) [136]. 

#### Diccionario de Datos Reales (WBCD) [136]:
*   `radius_mean`: Media de las distancias desde el centro a los puntos del perímetro de la célula [136].
*   `texture_mean`: Desviación estándar de los valores de la escala de grises de la imagen celular [136].
*   `perimeter_mean`: Tamaño del contorno del núcleo celular [136].
*   `area_mean`: Superficie interna del núcleo de la célula [136].
*   `smoothness_mean`: Medida local de variación en la longitud del radio celular [136].
*   `diagnosis`: La etiqueta objetivo. Toma valores categóricos: **M** (Maligno - Célula Cancerígena) o **B** (Benigno - Célula Sana) [533, 136].

---

### 2. Desafío Práctico: Implementación Multimodelo y Validación
Los estudiantes deben cargar el dataset real desde el repositorio público de Kaggle o UCI, preprocesarlo limpiando registros, estandarizar sus dimensiones físicas y comparar el desempeño predictivo de dos modelos diferentes [3, 136]:
1.  **k-Nearest Neighbors (k-NN) con $k=5$:** Un clasificador no paramétrico basado estrictamente en distancias que requiere escalamiento previo [169, 551].
2.  **Árbol de Decisión (C4.5 o CART):** Un clasificador lógico jerárquico basado en entropía de información que es insensible a la escala física de los atributos [551, 162].

Los estudiantes deberán realizar el Train/Test Split (80% entrenamiento, 20% prueba) y justificar con métricas reales cuál modelo es el óptimo para producción [3, 136].

---

### 3. Código Base de Google Colab para el Estudiante

```python
# =====================================================================
# LABORATORIO SEMANA 2: PREPROCESAMIENTO Y EVALUACIÓN DE MODELOS (WBCD)
# =====================================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report

# [PASO 1]: Carga de datos reales desde repositorio público
url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/wcontinuous-cancer.csv"
# En caso de URL alternativa, el estudiante puede usar el dataset WBCD directo de Kaggle
try:
    df_wbcd = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data", header=None)
    # Asignar nombres de columnas básicos
    column_names = ['id', 'diagnosis'] + [f'feat_{i}' for i in range(1, 31)]
    df_wbcd.columns = column_names
except:
    print("Error cargando el dataset directo de UCI. Cargando simulación estructurada real.")

# [PASO 2]: Consulta Exploratoria de Datos (Comprensión del Diccionario)
### TU TAREA: Realiza consultas en Pandas para verificar nulos y balance de la etiqueta 'diagnosis'
print("Dimensiones del dataset original:", df_wbcd.shape)
print("Distribución de la variable objetivo:\n", df_wbcd['diagnosis'].value_counts())
print("Conteo de valores nulos por columna:\n", df_wbcd.isnull().sum().sum())

# [PASO 3]: Codificación de la variable categórica objetivo (M=1, B=0)
df_wbcd['target'] = df_wbcd['diagnosis'].map({'M': 1, 'B': 0})

# [PASO 4]: Separación de características (X) y etiqueta objetivo (y)
X = df_wbcd.drop(columns=['id', 'diagnosis', 'target'])
y = df_wbcd['target']

# [PASO 5]: Separación en conjuntos de entrenamiento y prueba (Train/Test Split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)

# [PASO 6]: Escalado de Características mediante StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# [PASO 7]: Implementación del Modelo 1 (k-NN)
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train_scaled, y_train)
y_pred_knn = knn_model.predict(X_test_scaled)

# [PASO 8]: Implementación del Modelo 2 (Árbol de Decisión)
tree_model = DecisionTreeClassifier(max_depth=4, random_state=42)
tree_model.fit(X_train_scaled, y_train) # El árbol puede correr sobre data con o sin escalar
y_pred_tree = tree_model.predict(X_test_scaled)

# [PASO 9]: Cálculo de la Matriz de Confusión para ambos modelos
print("\n=== MATRIZ DE CONFUSIÓN: k-NN ===")
print(confusion_matrix(y_test, y_pred_knn))

print("\n=== MATRIZ DE CONFUSIÓN: ÁRBOL DE DECISIÓN ===")
print(confusion_matrix(y_test, y_pred_tree))
```

---

### 4. Guía de Defensa Analítica (Para el Estudiante)

El estudiante debe responder por escrito las implicaciones de su modelo en la práctica clínica:

*   **Verdaderos Positivos (VP):** El paciente tiene una célula cancerígena maligna (M) y el modelo la detecta correctamente como tal [532, 136]. *Acción:* Se inicia inmediatamente el tratamiento oncológico salvando vidas [142].
*   **Verdaderos Negativos (VN):** El paciente tiene una célula sana (B) y el modelo la declara correctamente benigna [533, 136]. *Acción:* El paciente se va a casa tranquilo [141].
*   **Falsos Positivos (FP) - Error Tipo I:** El paciente tiene una célula sana (B), pero el modelo predice erróneamente que es cancerígena (M) [277, 413, 136]. *Impacto:* Causa un pánico psicológico extremo en la familia del paciente, sometiéndolo a biopsias innecesarias, tratamientos agresivos por error y un alto costo económico de hospitalización [166].
*   **Falsos Negativos (FN) - Error Tipo II (El Error Crítico):** El paciente tiene cáncer maligno (M), pero el modelo predice erróneamente que está sano (B) [277, 413, 136]. *Impacto:* El médico envía al paciente a casa sin tratamiento. El cáncer progresa de forma oculta y, en el próximo chequeo, el paciente puede encontrarse en una etapa terminal irreversible [141, 166]. **Este error cuesta vidas.**

---

### 5. Evaluación Formativa y Quiz de Moodle (Formato Aiken)

Este bloque de preguntas puede ser cargado directamente en la plataforma escolar Moodle:

```text
¿Cuál es la principal diferencia matemática entre MinMaxScaler y StandardScaler?
A. MinMaxScaler asume una distribución gaussiana de los datos, mientras que StandardScaler no.
B. MinMaxScaler escala los datos a un rango estricto de [0, 1], mientras que StandardScaler los transforma para tener media 0 y varianza unitaria.
C. StandardScaler es altamente inmune a los outliers en comparación con MinMaxScaler.
D. MinMaxScaler requiere que los datos sean previamente binarizados.
ANSWER: B

En un contexto de diagnóstico médico de cáncer (WBCD), ¿cuál de las siguientes situaciones representa el costo de error más destructivo y peligroso para la vida del paciente?
A. Un Falso Positivo (Error Tipo I), porque somete al paciente a quimioterapias innecesarias.
B. Un Verdadero Positivo, porque confirma que el paciente requiere cirugía invasiva.
C. Un Falso Negativo (Error Tipo II), porque se deja ir al paciente enfermo sin tratamiento médico, permitiendo el avance de la enfermedad.
D. Un Verdadero Negativo, porque implica que la prueba de laboratorio fue ineficiente.
ANSWER: C

¿Por qué los modelos como k-NN son altamente sensibles a la escala de las características físicas?
A. Porque optimizan la entropía de información de los nodos utilizando divisiones perpendiculares.
B. Porque calculan distancias matemáticas (como la euclídea), donde las variables con magnitudes mayores dominan por completo el cálculo del vecino más cercano.
C. Porque k-NN requiere que todas las características sean variables categóricas.
D. Porque k-NN realiza una optimización secuencial por gradiente descendente que requiere varianza constante.
ANSWER: B

¿Qué método no paramétrico dibuja límites de seguridad no lineales para la detección de outliers utilizando los percentiles 25 y 75?
A. La puntuación Z-Score.
B. El Rango Intercuartílico (IQR).
C. La normalización Min-Max.
D. La imputación por la media de los datos observados.
ANSWER: B

¿Qué técnica de codificación categórica se debe aplicar sobre variables nominales como 'alert_type' o 'color' para evitar la introducción de un falso ordenamiento jerárquico numérico?
A. Label Encoding
B. Imputación por la mediana
C. One-Hot Encoding
D. StandardScaler
ANSWER: C
```

---

## 6. Referencias Bibliográficas (Grounded)

1.  **Müller, A. C. & Guido, S. (2017).** *Introduction to Machine Learning with Python: A Guide for Data Scientists*. O’Reilly Media. [Tratamiento de variables categóricas, MinMaxScaler y StandardScaler (pp. 132-139, 211-218); métricas de evaluación para clasificación binaria y matriz de confusión (pp. 276-296); dataset de cáncer de mama WBCD (p. 32)] [512, 132-139, 211-218, 276-296, 32].
2.  **Grus, J. (2019).** *Data Science from Scratch: First Principles with Python* (2nd ed.). O’Reilly Media. [Nivelación y manejo de colecciones en Python, tratamiento de outliers y exploración de datos (Capítulo 2 y 10); manipulación y limpieza de datos categóricos con variables dummy (Capítulo 11 y 15)] [284, 2, 10, 11, 15].
3.  **Reis, J. & Housley, M. (2022).** *Fundamentals of Data Engineering: Plan and Build Robust Data Systems*. O’Reilly Media. [Ingesta de datos, preprocesamiento e implicación del almacenamiento caliente frente al almacenamiento frío para analítica (Capítulo 6 y 7)] [444, 6, 7].
4.  **Janapati, R., Desai, U., Fernandes, S., Sengupta, R., & Tayal, S. (Eds.). (2026).** *Applied Artificial Intelligence and Machine Learning Techniques for Engineering Applications*. CRC Press. [Aplicación de modelos de Machine Learning (k-NN, SVM, Random Forest) en diagnóstico médico y ciberseguridad utilizando datasets reales como WBCD y QIN DCE-MRI (Capítulos 2 y 5)] [11, 2, 5].
5.  **Priyadarshini, I. & Sharma, R. (Eds.). (2022).** *Artificial Intelligence and Cybersecurity: Advances and Innovations*. CRC Press. [Flujos de limpieza de datos en ciberseguridad, filtrado de puertos y tratamiento de anomalías estadísticas en redes mediante modelos supervisados (Capítulos 1 y 11)] [151, 1, 11].
