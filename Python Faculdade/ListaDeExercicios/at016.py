import datetime

def data_por_extenso(data_str):
    meses = {
        1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril", 5: "maio", 6: "junho",
        7: "julho", 8: "agosto", 9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
    }
    
    try:
        data = datetime.datetime.strptime(data_str, "%d/%m/%Y")
        
        dia = data.day
        mes = meses[data.month]
        ano = data.year
        
        return f"{dia} de {mes} de {ano}"
    
    except ValueError:
        return None

data = input("Digite uma data no formato DD/MM/AAAA: ")
resultado = data_por_extenso(data)

if resultado:
    print("Data formatada:", resultado)
else:
    print("Data inválida.")