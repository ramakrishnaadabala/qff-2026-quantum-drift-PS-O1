import matplotlib.pyplot as plt
import pandas as pd

def plot_processor_comparison(csv_path, output_path):
    df = pd.read_csv(csv_path)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.bar(df['Processor'], df['Depth'], color=['#3498db', '#e74c3c'])
    ax1.set_title('Transpiled Circuit Depth')
    ax1.set_ylabel('Depth')
    ax2.bar(df['Processor'], df['2Q_Gates'], color=['#3498db', '#e74c3c'])
    ax2.set_title('Two-Qubit Gate Count (Overhead)')
    ax2.set_ylabel('CX Count')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
