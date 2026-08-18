import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def configurar_branding():
    """Configura plt.rcParams para igualar la identidad visual del curso."""
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
        'font.family': 'sans-serif', # Asumiendo fuentes genéricas limpias si no están instaladas
        'axes.titlesize': 14,
        'axes.titleweight': 'bold',
        'axes.titlecolor': color_primario,
        'lines.color': color_acento,
        'patch.edgecolor': color_fondo
    })
    
    # Paleta de Seaborn predeterminada a tonos Verde Azulado
    sns.set_palette(sns.color_palette([color_acento, color_primario, color_secundario]))

def draw_pyramid():
    configurar_branding()
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Coordinates for the pyramid layers
    layers = [
        ("AI / Deep Learning", "#319795"),
        ("A/B Testing & ML", "#1A365D"),
        ("Analytics & Metrics", "#4A5568"),
        ("Cleaning & Anomaly Detection", "#319795"),
        ("Reliable Data Flow & Storage", "#1A365D"),
        ("Collect: Instrumentation, Logging, Sensors", "#4A5568")
    ]
    layers = list(reversed(layers))
    
    num_layers = len(layers)
    height = 10
    width = 12
    y_coords = np.linspace(0, height, num_layers + 1)
    
    for i in range(num_layers):
        y_bottom = y_coords[i]
        y_top = y_coords[i+1]
        
        w_bottom = width * (1 - y_bottom/height)
        w_top = width * (1 - y_top/height)
        
        x_bottom_left = -w_bottom / 2
        x_bottom_right = w_bottom / 2
        x_top_left = -w_top / 2
        x_top_right = w_top / 2
        
        poly = plt.Polygon(
            [[x_bottom_left, y_bottom], [x_bottom_right, y_bottom], 
             [x_top_right, y_top], [x_top_left, y_top]], 
            color=layers[i][1], ec='#F7FAFC', lw=2
        )
        ax.add_patch(poly)
        
        y_center = (y_bottom + y_top) / 2
        ax.text(0, y_center, layers[i][0], ha='center', va='center', 
                color='#F7FAFC', fontweight='bold', fontsize=11)

    ax.set_xlim(-width/2 - 1, width/2 + 1)
    ax.set_ylim(-1, height + 1)
    ax.axis('off')
    
    plt.title("Jerarquía de Necesidades de Datos (Monica Rogati)", pad=20)
    plt.tight_layout()
    plt.savefig('d:/Documents/USFX/INT210/Machine-Learning-From-Scratch---INT210/Semana_01/jerarquia_datos.png', dpi=300)
    plt.close()

if __name__ == "__main__":
    draw_pyramid()
    print("jerarquia_datos.png generated successfully with new branding.")
