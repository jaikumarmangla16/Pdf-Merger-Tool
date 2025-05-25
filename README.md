
# 🧩 PDF Merger Tool

A simple command-line utility written in Python that merges multiple PDF files into a single PDF document using `PyPDF2`.

## 📦 Features

- Merge any number of PDF files
- Input filenames dynamically via terminal
- Saves the merged file as `merged-pdf.pdf`

## 🛠️ Requirements

- Python 3.7+
- PyPDF2 library

Install the required library using pip:

```bash
pip install PyPDF2
```

## 🚀 How to Use

1. Place your PDF files in the same directory as the script.
2. Run the script:

```bash
python your_script_name.py
```

3. Enter the number of PDF files you want to merge.
4. Enter the names of the PDF files (including the `.pdf` extension) one by one.

Example:

```bash
Enter the number of PDFs to merge: 3
Enter the name of PDF 1: file1.pdf
Enter the name of PDF 2: file2.pdf
Enter the name of PDF 3: file3.pdf
```

The script will merge all the provided PDF files and create a new file named `merged-pdf.pdf`.

## 📂 Output

The merged PDF will be saved in the same directory as:

```
merged-pdf.pdf
```

## 🧑‍💻 Author

Developed by **Jai Kumar Mangla**  
Python enthusiast & automation lover.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
