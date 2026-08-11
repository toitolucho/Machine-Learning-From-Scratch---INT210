"""
Script de Generación Gráfica: Sesión 0.3
Genera y exporta en formato PNG la comparación de consumo de memoria RAM: Range vs List.
"""

import matplotlib.pyplot as plt
import numpy as np

# Configuración de estilo académico
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11

def graficar_memoria():
    """Genera la comparativa de asignación en memoria RAM."""
    elementos = ['1 Mil', '100 Mil', '1 Millón', '10 Millones']
    
    # Memoria en Megabytes (Aproximada en CPython 64-bit)
    memoria_lista_mb = [0.08, 0.8, 8.0, 80.0]
    memoria_range_mb = [0.000048, 0.000048, 0.000048, 0.000048]  # 48 bytes constantes
    
    x = np.arange(len(elementos))
    ancho = 0.35
    
    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
    
    ax.bar(x - ancho/2, memoria_lista_mb, ancho, label=r'Lista Materializada en RAM ($\mathcal{O}(N)$)', color='#d9534f')
    ax.bar(x + ancho/2, memoria_range_mb, ancho, label=r'Secuencia Virtual $range()$ ($\mathcal{O}(1)$)', color='#5cb85c')
    
    ax.set_ylabel('Consumo de Memoria RAM (MB - Escala Log)', fontsize=11, fontweight='bold')
    ax.set_yscale('log')
    ax.set_xlabel('Tamaño de la Secuencia (Elementos)', fontsize=11, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(elementos, fontweight='bold')
    ax.set_title('Impacto Espacial: Evaluación Perezosa vs Memoria RAM', fontsize=13, fontweight='bold', pad=15)
    
    ax.legend(frameon=True, loc='upper left')
    plt.tight_layout()
    plt.savefig('consumo_memoria_iteradores_03.png', dpi=300)
    plt.close()
    print("Gráfica exportada: consumo_memoria_iteradores_03.png")

if __name__ == '__main__':
    graficar_memoria()
