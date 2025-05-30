from math import *
from random import *
from json import *
from geopy.distance import geodesic
from tabulate import *
from datetime import *

def gerar_nome_empresa():

    prefixos = ["Tech", "Info", "Data", "Net", "Cloud", "Global"]
    sufixos = ["Solutions", "Corp", "Group", "Systems", "Enterprises", "Labs"]

    prefixo = choice(prefixos)
    sufixo = choice(sufixos)

    return f"{prefixo} {sufixo}"

def gerar_chamado():
  chamado = sample(range(1,100), k=randint(10,15))

  cord_lat = sample(range(233600000,240000000),1)
  cord_long = sample(range(463600000,468400000),1)
  
  chamado_x = (cord_lat[0] / 10000000) * -1
  chamado_y = (cord_long[0] / 10000000) * -1
  
  cord_chamado = [chamado_x, chamado_y]
  areas = []
  areas_arquivo = []

  nome_fake = gerar_nome_empresa()

  with open("BackEnd/arquivos/areas_tecnicas_conserto.txt", "r", encoding="utf-8") as file:
    for area in file:
      areas_arquivo.append(area)

  for id in chamado:
    areas.append(areas_arquivo[id - 1])
  
  return [chamado, nome_fake, cord_chamado, areas]

def similaridade(list1, list2):
  set1 = set(list1)
  set2 = set(list2)
  inter = set1.intersection(set2)
  uni = set1.union(set2)
  jaccard = float(len(inter))/float(len(uni))
  return jaccard

def amostragem(lista, ordenacao, empresa, distancias, max_distance, chamado, areas_escritas):
    with open("BackEnd/arquivos/tecnicos.txt", "r", encoding="utf-8") as arq_tecs:
        content = arq_tecs.readlines()

    tabela = []
    posicao = 0

    for o, t in enumerate(lista):
        for l in content:
            if content.index(l) == ordenacao[o] - 1:
                partes = l.strip().split(", ")
                amostra_distancia = distancias[ordenacao[o]]
                if amostra_distancia <= max_distance and (t * 100) != 0:
                  posicao += 1
                  tabela.append([posicao, partes[0], partes[1], f"{t * 100:.2f}%", f"{amostra_distancia} km"])
    
    salvar_resultado(tabela)

    print(f"A empresa {empresa}, esta solicitando os seguintes serviços: ")
    for id in chamado:
      print(areas_escritas[id - 1])
    print("\n")
    print(f"O Rank dos Técnicos mais apropriados considerando um raio de {max_distance}kms são: ")
    print(tabulate(tabela, headers=["#", "Nome", "CPF", "Proximidade", "Distância"], tablefmt="grid"))

def log(onde : str, erro : str):
    with open("BackEnd/arquivos/log.txt", "a+") as arq:
        arq.write( "ocorreu um erro em - " + onde + " - erro: " + str(erro) + ". As " + str(datetime.now()) + "\n")

def peso_distancia(x, limite):
    return max(1, min(3, 3 - max(0, x - 0.2 * limite) / (0.8 * limite)))

def filtragem(cord_chamado, areas_chamado, max_distance):

  distancias = []
  tecs_pesados = []

  while True:
    with open("BackEnd/arquivos/tecnicos.txt", "r", encoding="utf-8") as arq_tecs:
      for l in arq_tecs:
        parts = l.strip().split(", ")
        if len(parts) >= 4:
          cord_x = float(parts[2])
          cord_y = float(parts[3])
          cordenadas_tec = ((cord_x, cord_y))
          dis = geodesic(cord_chamado, cordenadas_tec).km
          distancias.append(round(dis, 1))
      break

  while True:
    with open("BackEnd/arquivos/especialidades.txt", "r", encoding="utf-8") as arq_especialidade:
      especialidades = arq_especialidade.readlines()
      for i, linha in enumerate(especialidades):
        tecnico = []
        tecnico+= loads(linha)
        simi = similaridade(areas_chamado, tecnico)
        simi_pesado = simi * (peso_distancia(distancias[i],max_distance)) 
        tecs_pesados.append(round(simi_pesado, 5))
      break


  indices = list(range(100))
  indices_ordenados_pesados = sorted(range(len(tecs_pesados)), key=lambda i: tecs_pesados[i], reverse=True)
  tecs_pesados_ordenados = [tecs_pesados[i] for i in indices_ordenados_pesados]
  ordem_pesada = [indices[i] for i in indices_ordenados_pesados]

  return tecs_pesados_ordenados, ordem_pesada, distancias

def salvar_chamado(chamado):
    with open("BackEnd/arquivos/chamados.txt", "w", encoding="utf-8") as arq_chamados:
        arq_chamados.write(f"{chamado}")

def carregar_chamados():
   chamado = []
   try:
       with open("BackEnd/arquivos/chamados.txt", "r", encoding="utf-8") as arq_chamados:
           for linha in arq_chamados:
               chamado.append(linha.strip())
   except FileNotFoundError:
       print("Arquivo de chamados não encontrado.")

def salvar_resultado(tabela):
    with open("BackEnd/arquivos/resultados.txt", "w", encoding="utf-8") as arq_resultados:
        arq_resultados.write(f"{tabela}")