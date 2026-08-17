import matplotlib.pyplot as plt
import numpy as np

def draw_pyramid():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Coordinates for the pyramid layers
    # Base to Top
    layers = [
        ("AI / Deep Learning", "#e63946"),
        ("A/B Testing & ML", "#f4a261"),
        ("Analytics & Metrics", "#e9c46a"),
        ("Cleaning & Anomaly Detection", "#2a9d8f"),
        ("Reliable Data Flow & Storage", "#264653"),
        ("Collect: Instrumentation, Logging, Sensors", "#1d3557")
    ]
    
    # Reverse layers so bottom is at the bottom
    layers = list(reversed(layers))
    
    num_layers = len(layers)
    height = 10
    width = 12
    
    y_coords = np.linspace(0, height, num_layers + 1)
    
    for i in range(num_layers):
        y_bottom = y_coords[i]
        y_top = y_coords[i+1]
        
        # Calculate width at bottom and top based on a triangle
        w_bottom = width * (1 - y_bottom/height)
        w_top = width * (1 - y_top/height)
        
        x_bottom_left = -w_bottom / 2
        x_bottom_right = w_bottom / 2
        x_top_left = -w_top / 2
        x_top_right = w_top / 2
        
        poly = plt.Polygon(
            [[x_bottom_left, y_bottom], [x_bottom_right, y_bottom], 
             [x_top_right, y_top], [x_top_left, y_top]], 
            color=layers[i][1], ec='white', lw=2
        )
        ax.add_patch(poly)
        
        # Add text
        y_center = (y_bottom + y_top) / 2
        ax.text(0, y_center, layers[i][0], ha='center', va='center', 
                color='white', fontweight='bold', fontsize=11)

    ax.set_xlim(-width/2 - 1, width/2 + 1)
    ax.set_ylim(-1, height + 1)
    ax.axis('off')
    
    plt.title("Jerarquía de Necesidades de Datos (Monica Rogati)", fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('d:/Documents/USFX/INT210/Machine-Learning-From-Scratch---INT210/Semana_01/jerarquia_datos.png', dpi=300, transparent=True)
    plt.close()

if __name__ == "__main__":
    draw_pyramid()
    print("jerarquia_datos.png generated successfully.")
