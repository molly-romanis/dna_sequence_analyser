# DNA Sequence Analyser

A beginner-friendly interactive DNA sequence analysis tool written in Python. This CLI-based project supports analysis of DNA sequences from various file types, including:

- '.fasta' / '.fa'
- '.txt'
- '.csv'

The tool provides:
- Nucleotide counts (A, T, G, C)
- GC content
- Transcription (DNA -> RNA)
- Translation (RNA -> Protein)
- Optional: nucleotide distribution plots

---

## Preview

+-------------------------------------------+
|           DNA Sequence Analyser           |
+-------------------------------------------+

Choose an option:

1. Analyse sequence(s)
2. Show nucleotide plot(s)
3. Exit

---

## Features

- Analyse multiple files in one run
- Accepts FASTA, TXT, and CSV files
- Clean, colorful terminal output using Rich
- Interactive plot output using matplotlib
- Built-in menu-based interface
- Platform-independent

---

## Sample Input Formats

### FASTA ('.fasta')
```bash
>identifier1 description1
ATGCTAGCTAGCATCGATCG
GACTGACTGACAGTCTGATG
>identifier2 description2
CGTAGCTAGCGTACGTAGC
ATGCTAGCTAGCATCGATCG
```

### TXT ('.txt')
```bash
>identifier1 description1
ATGCTAGCTAGCATCGATCGGACTGACTGACAGTCTGATG
>identifier2 description2
CGTAGCTAGCGTACGTAGCATGCTAGCTAGCATCGATCG
```

### CSV ('.csv')
```bash
Identifier,Description,Sequence
identifier1,description1,ATGCTAGCTAGCATCGATCGGACTGACTGACAGTCTGATG
identifier2,description2,CGTAGCTAGCGTACGTAGCATGCTAGCTAGCATCGATCG
```

---

## Setup

```bash
git clone https://github.com/molly-romanis/dna_sequence_analyser.git
cd dna_sequence_analyser
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
---

## 💻 Usage

From the menu, you can:

- Choose [1] to analyse DNA files
- Choose [2] to generate nucleotide bar plots
- Choose [3] to exit the program

For each option, you will be prompted to enter one or more file paths, comma-separated.

Example:
sample_data/seq1.fasta, sample_data/seq2.csv

---

## Tech Stack

- Python
- Biopython
- matplotlib
- Rich

---

## Project Structure

dna-sequence-analyser/
├── src/
│   └── analyser.py           # Main application script
├── sample_data/              # Test input files
│   ├── seq1.fasta
│   ├── seq2.txt
│   └── seq3.csv
├── requirements.txt
└── README.txt

---
