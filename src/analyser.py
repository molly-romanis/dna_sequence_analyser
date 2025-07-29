import os
from Bio import SeqIO
from Bio.Seq import Seq
from collections import Counter
import matplotlib.pyplot as plt
from rich import print
from rich.panel import Panel


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def home_menu():
    clear()
    print(Panel.fit("[bold cyan]DNA Sequence Analyser[/bold cyan]", subtitle="by Molly Romanis"))
    print("Choose an option:\n")
    print("1. Analyse sequence(s)")
    print("2. Show nucleotide plot(s)")
    print("3. Exit")

    choice = input("\nEnter your choice (1/2/3): ").strip()
    return choice


def select_file_paths():
    print("\nEnter paths to input files (comma separated):")
    files = input(" > ").strip().split(",")
    return [f.strip() for f in files if f.strip()]


def read_sequence_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    sequences = []

    try:
        if ext in [".fasta", ".fa"]:
            for record in SeqIO.parse(file_path, "fasta"):
                sequences.append((record.id, str(record.seq)))
        elif ext == ".csv":
            with open(file_path, 'r') as f:
                for i, line in enumerate(f):
                    seq = line.strip().split(',')[0]
                    sequences.append((f"{os.path.basename(file_path)}_seq_{i+1}", seq))
        elif ext == ".txt":
            with open(file_path, 'r') as f:
                seq = f.read().strip()
                sequences.append((os.path.basename(file_path), seq))
        else:
            print(f"[red]Unsupported file type:[/red] {ext}")
    except Exception as e:
        print(f"[red]Error reading {file_path}[/red]: {e}")

    return sequences


def analyse_sequence(name, seq):
    seq = seq.upper()
    counts = Counter(seq)
    gc = (counts.get("G", 0) + counts.get("C", 0)) / len(seq) * 100
    rna = Seq(seq).transcribe()
    protein = rna.translate()

    return {
        "name": name,
        "length": len(seq),
        "counts": counts,
        "gc_content": gc,
        "rna": str(rna),
        "protein": str(protein)
    }


def output_terminal(result):
    print(f"\n[bold yellow]Analysis for:[/bold yellow] {result['name']}")
    print(f"Length: {result['length']}")
    print(f"Nucleotide Counts: {dict(result['counts'])}")
    print(f"GC Content: {result['gc_content']:.2f}%")
    print(f"RNA: {result['rna']}")
    print(f"Protein: {result['protein']}")


def output_plot(result):
    counts = result["counts"]
    plt.bar(counts.keys(), counts.values(), color="mediumseagreen")
    plt.title(f"Nucleotide Distribution: {result['name']}")
    plt.xlabel("Nucleotides")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()


def main():
    while True:
        choice = home_menu()

        if choice == "1":
            file_paths = select_file_paths()
            for file_path in file_paths:
                sequences = read_sequence_file(file_path)
                for name, seq in sequences:
                    result = analyse_sequence(name, seq)
                    output_terminal(result)
            input("\nPress Enter to return to menu...")

        elif choice == "2":
            file_paths = select_file_paths()
            for file_path in file_paths:
                sequences = read_sequence_file(file_path)
                for name, seq in sequences:
                    result = analyse_sequence(name, seq)
                    output_plot(result)

        elif choice == "3":
            print("\n[bold green]Goodbye![/bold green]")
            break

        else:
            print("[red]Invalid choice. Try again.[/red]")
            input("Press Enter...")


if __name__ == "__main__":
    main()
