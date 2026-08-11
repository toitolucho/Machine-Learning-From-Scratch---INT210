"""
Script de Generación Gráfica: Sesión 0.6
Genera y exporta en formato PNG el histograma de frecuencias de palabras clave de Phishing.
"""

import matplotlib.pyplot as plt

# Configuración de estilo académico
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11

def graficar_frecuencias():
    """Genera el gráfico de barras horizontales para términos más comunes."""
    terminos = ['urgent', 'verify', 'account', 'reward', 'claim', 'login', 'bank']
    frecuencias = [18, 15, 14, 12, 11, 9, 8]
    
    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
    
    barras = ax.barh(terminos[::-1], frecuencias[::-1], color='#d9534f', edgecolor='black', height=0.6)
    
    for barra in barras:
        ancho = barra.get_width()
        ax.text(ancho + 0.3, barra.get_y() + barra.get_height()/2, f'{int(ancho)}',
                ha='left', va='center', fontweight='bold', color='#333333')
        
    ax.set_xlabel('Frecuencia Absoluta de Aparición en Corpus Malicioso', fontsize=11, fontweight='bold')
    ax.set_title('Top Términos de Phishing Detectados con Counter', fontsize=13, fontweight='bold', pad=15)
    ax.set_xlim(0, 22)
    
    plt.tight_layout()
    plt.savefig('frecuencia_phishing_06.png', dpi=300)
    plt.close()
    print("Gráfica exportada: frecuencia_phishing_06.png")

if __name__ == '__main__':
    graficar_frecuencias()
