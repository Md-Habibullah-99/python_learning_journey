#merge the pdf with pypdf
from pypdf import PdfReader
from pypdf import PdfWriter

#reading
reader = PdfReader("b1.pdf")
number_of_page = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)
reader.close()

#merging
merge = PdfWriter()
for pdf in ["b1.pdf","b2.pdf"]:
  merge.append(pdf)
merge.write("b.pdf")
merge.close()

