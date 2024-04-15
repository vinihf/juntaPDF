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
        merger.append("./arquivos/"+pdf)
    merger.write("ArquivosUnidos.pdf")
    merger.close()
    return True


if __name__ == '__main__':
    lista_arquivos = arquivos("./arquivos")
    if len(lista_arquivos)>0:
        if juntaPDF(lista_arquivos):
            print("Arquivo gerado com sucesso.")
        else:
            print("Não foi possível gerar o arquivo.")
    else:
        print("Não há arquivos na pasta Arquivos.")
