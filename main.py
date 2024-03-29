import os
from pypdf import PdfWriter

def arquivos(caminho:str)->list:
    itens = os.listdir(caminho)
    for f in itens:
        if os.path.isfile(f):
            itens.append(f)
    return itens

def juntaPDF(arquivos:list)->bool:
    merger = PdfWriter()
    for pdf in arquivos:
        merger.append(pdf)
    merger.write("ArquivosUnidos.pdf")
    merger.close()




print(arquivos("./arquivos"))