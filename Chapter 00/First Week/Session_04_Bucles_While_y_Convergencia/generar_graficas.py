"""
Script de Generación Gráfica: Sesión 0.4
Genera y exporta en formato PNG la curva de convergencia exponencial del error residual epsilon.
"""

import matplotlib.pyplot as plt
import numpy as np

# Configuración de estilo académico
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11

def graficar_convergencia():
    """Genera la curva de decaimiento del error residual y criterio de parada epsilon."""
    iteraciones = np.arange(1, 25)
    tasa_aprendizaje = 0.7
    error_residual = 100.0 * (tasa_aprendizaje ** iteraciones)
    epsilon = 0.05
    
    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
    
    ax.plot(iteraciones, error_residual, marker='o', color='#0275d8', linewidth=2.2, label=r'Error Residual $|x_{k+1} - x_k|$')
    ax.axhline(epsilon, color='#d9534f', linestyle='--', linewidth=2, label=r'Umbral de Tolerancia $\epsilon = 0.05$')
    
    # Punto de corte
    idx_corte = np.where(error_residual < epsilon)[0][0]
    ax.scatter(iteraciones[idx_corte], error_residual[idx_corte], color='#5cb85c', s=120, zorder=5, label='Convergencia Alcanzada')
    
    ax.set_yscale('log')
    ax.set_xlabel('Iteración / Rebote ($k$)', fontsize=11, fontweight='bold')
    ax.set_ylabel(r'Error Residual $\Delta_k$ (Escala Log)', fontsize=11, fontweight='bold')
    ax.set_title(r'Convergencia Numérica en Procesos Iterativos', fontsize=13, fontweight='bold', pad=15)
    
    ax.legend(frameon=True, loc='upper right')
    plt.tight_layout()
    plt.savefig('curva_convergencia_04.png', dpi=300)
    plt.close()
    print("Gráfica exportada: curva_convergencia_04.png")

if __name__ == '__main__':
    graficar_convergencia()
