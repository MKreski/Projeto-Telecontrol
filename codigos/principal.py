from funcoes import *

print("Bem vindo ao nosso protótipo")
while True:
    print("----------MENU----------")
    print("[0] - SAIR")
    print("[1] - Gerar Chamado")
    print("[2] - Filtrar Técnicos")
    opc = 99

    try:
        opc = int(input())
    except Exception as erro:
        opc == 99
        log("menu iniciar", erro)
    
    if opc == 0:
        print("Saindo...")
        break

    elif opc == 1:
        chamado = gerar_chamado()
        areas_chamado = chamado[0]
        empresa_chamado = chamado[1]
        cordenadas_chamado = chamado[2]
        areas_escritas = chamado[3]
        print(f"A empresa {empresa_chamado} localizada em {cordenadas_chamado} está solicitando: ")
        for id in areas_chamado:
            print(areas_escritas[id - 1])

    elif opc == 2:
        try:
            max_distancia = float(input("Insira o raio limite para filtragem em km: "))
            try:
                resultado = filtragem(cordenadas_chamado, areas_chamado, max_distancia)
                tecs = resultado[0]
                ordem = resultado[1]
                distancias = resultado[2]
                amostragem(tecs, ordem, empresa_chamado, distancias, max_distancia, areas_chamado, areas_escritas)
            except Exception as erro:
                print("Não existe chamado em aberto")
                log("filtragem",erro)
        except Exception as erro:
            print("Insira um valor valido")
            log("distancia maxima", erro)
    else:
        print("Opção Inválida")