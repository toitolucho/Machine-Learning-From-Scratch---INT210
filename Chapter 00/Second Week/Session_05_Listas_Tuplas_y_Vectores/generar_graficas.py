"""
Script de Generación Gráfica: Sesión 0.5
Genera y exporta en formato PNG el diagrama de vectores 3D y distancia euclidiana.
"""

import matplotlib.pyplot as plt
import numpy as np

# Configuración de estilo académico
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11

def graficar_vectores_3d():
    """Genera la proyección 3D de dos vectores y su distancia relativa."""
    fig = plt.figure(figsize=(7, 5), dpi=300)
    ax = fig.add_subplot(111, projection='3d')
    
    # Origen y vectores
    origen = [0, 0, 0]
    v_a = [30, 20, 15]
    v_b = [15, 40, 25]
    
    # Dibujar vectores desde el origen
    ax.quiver(0, 0, 0, v_a[0], v_a[1], v_a[2], color='#0275d8', arrow_length_ratio=0.08, linewidth=2.5, label=r'Vector Nave $\vec{u}$')
    ax.quiver(0, 0, 0, v_b[0], v_b[1], v_b[2], color='#d9534f', arrow_length_ratio=0.08, linewidth=2.5, label=r'Vector Amenaza $\vec{v}$')
    
    # Línea de distancia euclidiana entre las puntas
    ax.plot([v_a[0], v_b[0]], [v_a[1], v_b[1]], [v_a[2], v_b[2]], color='#5cb85c', linestyle='--', linewidth=2, label=r'Distancia $d(\vec{u}, \vec{v})$')
    
    ax.set_xlabel('Eje X', fontweight='bold')
    ax.set_ylabel('Eje Y', fontweight='bold')
    ax.set_zlabel('Eje Z', fontweight='bold')
    ax.set_title('Representación Vectorial en Espacio Tridimensional $\mathbb{R}^3$', fontsize=12, fontweight='bold', pad=10)
    
    ax.legend(loc='upper left', frameon=True)
    plt.tight_layout()
    plt.savefig('vectores_3d_05.png', dpi=300)
    plt.close()
    print("Gráfica exportada: vectores_3d_05.png")

if __name__ == '__main__':
    graficar_vectores_3d()
