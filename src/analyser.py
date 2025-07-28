from Bio.Seq import Seq
from collections import Counter
import matplotlib.pyplot as plt
from rich import print

def read_sequence(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()
    
def analyse_dna(seq):
    print(f"[bold]Original Sequecne:[/bold] {seq}")
    print(f"[bold]Length:[/bold] {len(seq)}")

    counts = Counter(seq.upper())
    print(f"[bold]Nucleotide Counts:[/bold] {counts}")

    gc_content = (counts['G'] + counts['C']) / len(seq) * 100
    print(f"[bold]GC Content: [/bold] {gc_content:.2f}%")

    rna = Seq(seq).transcribe()
    protein = rna.translate()
    print(f"[bold]RNA Sequence:[/bold] {rna}")
    print(f"[bold]Protein Translation:[/bold] {protein}")

    return counts

def plot_nucleotide_distribution(counts):
    labels = list(counts.keys())
    values = list(counts.values())
    plt.bar(labels, values, color=['green', 'blue', 'red', 'orange'])
    plt.title("Nucleotide Distribution")
    plt.xlabel("Nucleotides")
    plt.ylabel("Count")
    plt.show()

if __name__ == "__main__":
    dna = read_sequence("sample_data/example_data.txt")
    counts = analyse_dna(dna)
    plot_nucleotide_distribution(counts)