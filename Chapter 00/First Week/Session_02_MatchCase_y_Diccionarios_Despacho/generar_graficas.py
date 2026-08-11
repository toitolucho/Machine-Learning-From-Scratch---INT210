"""
Script de Generación Gráfica: Sesión 0.2
Genera y exporta en formato PNG la comparación de complejidad computacional O(N) vs O(1).
"""

import matplotlib.pyplot as plt
import numpy as np

# Configuración de estilo académico
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11

def graficar_complejidad():
    """Genera la curva comparativa de complejidad temporal."""
    N = np.linspace(1, 1000, 100)
    
    # Tiempo lineal O(N) vs Tiempo constante O(1)
    tiempo_lineal = 0.05 * N
    tiempo_constante = np.full_like(N, 2.5)
    
    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
    
    ax.plot(N, tiempo_lineal, label=r'Cadena Lineal $if-elif$ ($\mathcal{O}(N)$)', color='#d9534f', linewidth=2.5)
    ax.plot(N, tiempo_constante, label=r'Diccionario de Despacho Hash ($\mathcal{O}(1)$)', color='#0275d8', linewidth=2.5, linestyle='--')
    
    ax.set_xlabel('Número de Rutas / Opciones de Despacho ($N$)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Tiempo de Búsqueda Relativo ($\mu s$)', fontsize=11, fontweight='bold')
    ax.set_title(r'Complejidad Computacional: $\mathcal{O}(N)$ vs $\mathcal{O}(1)$', fontsize=13, fontweight='bold', pad=15)
    
    ax.annotate('Degradación de Latencia en SOC', xy=(800, 40), xytext=(400, 45),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6),
                fontweight='bold', color='#d9534f')
    
    ax.legend(frameon=True, loc='upper left', fontsize=10)
    plt.tight_layout()
    plt.savefig('complejidad_despacho_02.png', dpi=300)
    plt.close()
    print("Gráfica exportada: complejidad_despacho_02.png")

if __name__ == '__main__':
    graficar_complejidad()
