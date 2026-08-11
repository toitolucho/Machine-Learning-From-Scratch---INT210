"""
Script de Generación Gráfica: Sesión 0.1
Genera y exporta en formato PNG las visualizaciones conceptuales para las diapositivas Beamer.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configuración de estilo académico
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11

def graficar_matriz_confusion():
    """Genera la visualización de la Matriz de Confusión Heurística."""
    matriz = np.array([[5, 0], [0, 5]])
    fig, ax = plt.subplots(figsize=(6, 5), dpi=300)
    
    sns.heatmap(matriz, annot=False, cmap='Blues', cbar=False,
                linewidths=2, linecolor='black', ax=ax)
    
    etiquetas = [
        ['Verdadero Positivo (VP)\n5\n(Ataque Bloqueado)', 'Falso Negativo (FN)\n0\n(Brecha de Seguridad)'],
        ['Falso Positivo (FP)\n0\n(Bloqueo Accidental)', 'Verdadero Negativo (VN)\n5\n(Tráfico Legítimo)']
    ]
    
    for i in range(2):
        for j in range(2):
            ax.text(j + 0.5, i + 0.5, etiquetas[i][j],
                    ha='center', va='center', color='darkblue' if matriz[i, j] > 0 else 'gray',
                    fontweight='bold', fontsize=10)
            
    ax.set_xticklabels(['Predicho Spam', 'Predicho Ham'], fontsize=11, fontweight='bold')
    ax.set_yticklabels(['Real Spam', 'Real Ham'], fontsize=11, fontweight='bold', va='center')
    ax.set_title('Matriz de Confusión: Clasificador Heurístico', fontsize=13, fontweight='bold', pad=15)
    
    plt.tight_layout()
    plt.savefig('matriz_confusion_01.png', dpi=300)
    plt.close()
    print("Gráfica exportada: matriz_confusion_01.png")

def graficar_escala_luminancia():
    """Genera el gradiente de segmentación tonal fotométrica."""
    fig, ax = plt.subplots(figsize=(8, 2.5), dpi=300)
    
    gradiente = np.linspace(0, 255, 256).reshape(1, -1)
    ax.imshow(gradiente, aspect='auto', cmap='gray', extent=[0, 255, 0, 1])
    
    ax.axvline(64, color='red', linestyle='--', linewidth=2, label='Umbral Low-Key (64)')
    ax.axvline(192, color='cyan', linestyle='--', linewidth=2, label='Umbral High-Key (192)')
    
    ax.text(32, 0.5, 'Low-Key\n(Sombras)', color='white', ha='center', va='center', fontweight='bold')
    ax.text(128, 0.5, 'Mid-Tone\n(Tonos Medios)', color='black', ha='center', va='center', fontweight='bold')
    ax.text(224, 0.5, 'High-Key\n(Altas Luces)', color='black', ha='center', va='center', fontweight='bold')
    
    ax.set_yticks([])
    ax.set_xlabel('Luminancia Fotométrica ($L \\in [0, 255]$)', fontsize=11, fontweight='bold')
    ax.set_title('Segmentación Tonal en Espacio RGB', fontsize=12, fontweight='bold')
    ax.legend(loc='upper left', frameon=True)
    
    plt.tight_layout()
    plt.savefig('escala_luminancia_01.png', dpi=300)
    plt.close()
    print("Gráfica exportada: escala_luminancia_01.png")

if __name__ == '__main__':
    graficar_matriz_confusion()
    graficar_escala_luminancia()
