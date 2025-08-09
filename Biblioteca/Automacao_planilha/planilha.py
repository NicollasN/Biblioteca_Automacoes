import openpyxl

def atualizar_planilha():
    workbook = openpyxl.load_workbook("dados.xlsx")
    aba = workbook.active
    aba.append(["Nicollas", 19, "Automação TI"])
    workbook.save("dados.xlsx")
    print('Planilha atualizada')