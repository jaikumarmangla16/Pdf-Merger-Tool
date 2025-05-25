from PyPDF2 import PdfMerger

merger = PdfMerger()

pdfs=[]
n=int(input("Enter the number of PDFs to merge: "))
for i in range(0,n):
    name= input(f"Enter the name of PDF {i+1}: ")
    pdfs.append(name)

for pdf in pdfs:
    print(pdf)
    print(f"Merging {pdf}...")
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
