import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def configurar_branding():
    color_fondo = '#F7FAFC'
    color_primario = '#1A365D'
    color_secundario = '#4A5568'
    color_acento = '#319795'
    
    plt.rcParams.update({
        'figure.facecolor': color_fondo,
        'axes.facecolor': color_fondo,
        'axes.edgecolor': color_secundario,
        'axes.labelcolor': color_secundario,
        'text.color': color_secundario,
        'xtick.color': color_secundario,
        'ytick.color': color_secundario,
        'font.family': 'sans-serif',
        'axes.titlesize': 14,
        'axes.titleweight': 'bold',
        'axes.titlecolor': color_primario,
        'lines.color': color_acento,
        'patch.edgecolor': color_fondo
    })
    sns.set_palette(sns.color_palette([color_acento, color_primario, color_secundario]))

def draw_outlier_concept():
    configurar_branding()
    fig, ax = plt.subplots(figsize=(8, 4))
    
    # Simular estaturas (niños normales vs jugador NBA)
    np.random.seed(42)
    normales = np.random.normal(130, 5, 20)
    outlier = np.array([220])
    data = np.concatenate([normales, outlier])
    
    sns.boxplot(x=data, ax=ax, color='#319795', flierprops={'marker': 'o', 'markerfacecolor': '#1A365D', 'markersize': 10})
    
    ax.annotate('Outlier Masivo\n(Gigante)', xy=(220, 0), xytext=(200, 0.2),
                arrowprops=dict(facecolor='#1A365D', shrink=0.05),
                ha='center', color='#1A365D', fontweight='bold')
                
    ax.annotate('IQR (Límites de Seguridad)', xy=(130, 0), xytext=(130, 0.3),
                arrowprops=dict(facecolor='#4A5568', shrink=0.05),
                ha='center', color='#4A5568', fontweight='bold')
    
    plt.title('Detección de Outliers (El Enano y El Gigante)', pad=15)
    plt.xlabel('Estatura Estimada (cm)')
    plt.tight_layout()
    plt.savefig('d:/Documents/USFX/INT210/Machine-Learning-From-Scratch---INT210/Semana_02/outlier_concept.png', dpi=300)
    plt.close()

if __name__ == "__main__":
    draw_outlier_concept()
    print("outlier_concept.png generated successfully.")
