proibidas = ["bolota","rolha","tapado","uiuiui","tu","cheiro","seboso"]

def proibido(texto):
    for proibida in proibidas:
        if proibida.lower() in texto.lower():
            texto = texto.lower().replace(proibida.lower(), '*' * len(proibida))
    print(texto)
    return texto
            
texto = input("Digite o texto: ")
proibido(texto)