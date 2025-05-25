# PDF Merger

A simple Python script to merge multiple PDF files into a single PDF using [PyPDF2](https://pypdf2.readthedocs.io/).

## Features

- Merge any number of PDF files interactively.
- Outputs a single merged PDF named `merged-pdf.pdf`.

## Requirements

- Python 3.x
- [PyPDF2](https://pypdf2.readthedocs.io/)

## Installation

Install PyPDF2 using pip:

```sh
pip install PyPDF2
```

## Usage

1. Place the PDF files you want to merge in the same directory as `main.py`.
2. Run the script:

```sh
python main.py
```

3. Enter the number of PDFs to merge when prompted.
4. Enter the filenames (including `.pdf` extension) as prompted.

The merged PDF will be saved as `merged-pdf.pdf` in the same directory.

## Example

```
Enter the number of PDFs to merge: 2
Enter the name of PDF 1: jai[1].pdf
Enter the name of PDF 2: mpdf(1).pdf
Merging jai[1].pdf...
Merging mpdf(1).pdf...
```

## License

This project is licensed under the MIT License.
