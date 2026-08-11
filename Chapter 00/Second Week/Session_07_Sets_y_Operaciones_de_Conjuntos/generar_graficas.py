"""
Script de Generación Gráfica: Sesión 0.7
Genera y exporta en formato PNG la comparación de tiempo de búsqueda: List vs Set.
"""

import matplotlib.pyplot as plt
import numpy as np

# Configuración de estilo académico
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11

def graficar_benchmark():
    """Genera la comparativa de latencia de búsqueda de pertenencia."""
    tamanios = ['1 Mil', '10 Mil', '100 Mil', '1 Millón']
    
    # Tiempos representativos en microsegundos (us)
    tiempo_lista_us = [25.0, 240.0, 2500.0, 26000.0]
    tiempo_set_us = [0.08, 0.08, 0.09, 0.09]  # Tiempo constante O(1)
    
    x = np.arange(len(tamanios))
    ancho = 0.35
    
    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
    
    ax.bar(x - ancho/2, tiempo_lista_us, ancho, label=r'Búsqueda Secuencial en Lista ($\mathcal{O}(N)$)', color='#d9534f')
    ax.bar(x + ancho/2, tiempo_set_us, ancho, label=r'Búsqueda Hash en Set ($\mathcal{O}(1)$)', color='#5cb85c')
    
    ax.set_ylabel('Tiempo de Búsqueda ($\mu s$ - Escala Log)', fontsize=11, fontweight='bold')
    ax.set_yscale('log')
    ax.set_xlabel('Tamaño de la Colección de IPs', fontsize=11, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(tamanios, fontweight='bold')
    ax.set_title(r'Eficiencia de Membresía: $x \in Set$ vs $x \in List$', fontsize=13, fontweight='bold', pad=15)
    
    ax.legend(frameon=True, loc='upper left')
    plt.tight_layout()
    plt.savefig('benchmark_sets_07.png', dpi=300)
    plt.close()
    print("Gráfica exportada: benchmark_sets_07.png")

if __name__ == '__main__':
    graficar_benchmark()
