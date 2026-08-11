"""
Script de Generación Gráfica: Sesión 0.8
Genera y exporta en formato PNG la comparación de consumo de memoria base: Nativo vs Pandas.
"""

import matplotlib.pyplot as plt

# Configuración de estilo académico
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11

def graficar_ingesta():
    """Genera la comparativa de memoria base y tiempo de arranque."""
    tecnologias = ['Python Nativo\n(csv + namedtuple)', 'Pandas\nDataFrame']
    memoria_mb = [12.5, 68.0]
    cold_start_ms = [10.0, 1850.0]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), dpi=300)
    
    # Gráfica 1: Memoria Base
    barras1 = ax1.bar(tecnologias, memoria_mb, color=['#5cb85c', '#d9534f'], width=0.5, edgecolor='black')
    ax1.set_ylabel('Memoria Base en RAM (MB)', fontsize=10, fontweight='bold')
    ax1.set_title('Huella de Memoria Base', fontsize=11, fontweight='bold')
    for b in barras1:
        ax1.text(b.get_x() + b.get_width()/2, b.get_height() + 2, f"{b.get_height():.1f} MB",
                 ha='center', fontweight='bold', fontsize=10)
    ax1.set_ylim(0, 90)
    
    # Gráfica 2: Tiempo de Arranque (Cold Start)
    barras2 = ax2.bar(tecnologias, cold_start_ms, color=['#5cb85c', '#d9534f'], width=0.5, edgecolor='black')
    ax2.set_ylabel('Latencia Cold Start (ms - Escala Log)', fontsize=10, fontweight='bold')
    ax2.set_yscale('log')
    ax2.set_title('Tiempo de Arranque Inicial', fontsize=11, fontweight='bold')
    for b in barras2:
        ax2.text(b.get_x() + b.get_width()/2, b.get_height() * 1.3, f"{int(b.get_height())} ms",
                 ha='center', fontweight='bold', fontsize=10)
    ax2.set_ylim(1, 5000)
    
    plt.suptitle('Evaluación de Ingesta: Python Nativo vs Librerías Pesadas', fontsize=12, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('comparativa_ingesta_08.png', dpi=300)
    plt.close()
    print("Gráfica exportada: comparativa_ingesta_08.png")

if __name__ == '__main__':
    graficar_ingesta()
