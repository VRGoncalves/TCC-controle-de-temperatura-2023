#Importando bibliotecas
import matplotlib.pyplot as plt
import numpy as np

# Abrindo e lendo os arquivos de texto
with open("D:\Victor\Desktop\Testes TCC Fotovotaico\Monitor Script - 2 placas 22 graus - kp60 ki0 kd0.txt", "r") as arquivo2260:
    texto2260 = arquivo2260.readlines()

with open("D:\Victor\Desktop\Testes TCC Fotovotaico\Monitor Script - 2 placas 20 graus - kp60 ki0 kd0.txt", "r") as arquivo2060:
    texto2060 = arquivo2060.readlines()

with open("D:\Victor\Desktop\Testes TCC Fotovotaico\Monitor Script - 2 placas 22 graus - kp65 ki0 kd0.txt", "r") as arquivo2265:
    texto2265 = arquivo2265.readlines()

with open("D:\Victor\Desktop\Testes TCC Fotovotaico\Monitor Script - 2 placas 20 graus - kp65 ki0 kd0.txt", "r") as arquivo2065:
    texto2065 = arquivo2065.readlines()

with open("D:\Victor\Desktop\Testes TCC Fotovotaico\Monitor Script - 2 placas 22 graus - kp70 ki0 kd0.txt", "r") as arquivo2270:
    texto2270 = arquivo2270.readlines()

with open("D:\Victor\Desktop\Testes TCC Fotovotaico\Monitor Script - 2 placas 20 graus - kp70 ki0 kd0.txt", "r") as arquivo2070:
    texto2070 = arquivo2070.readlines()

with open("D:\Victor\Desktop\Testes TCC Fotovotaico\Monitor Script - 2 placas 22 graus - kp75 ki0 kd0.txt", "r") as arquivo2275:
    texto2275 = arquivo2275.readlines()

with open("D:\Victor\Desktop\Testes TCC Fotovotaico\Monitor Script - 2 placas 20 graus - kp75 ki0 kd0.txt", "r") as arquivo2075:
    texto2075 = arquivo2075.readlines()


#Criando as listas de dados
Lista_Temp2260 = []
Lista_Seg2260 = []

Lista_Temp2060 = []
Lista_Seg2060 = []

Lista_Temp2265 = []
Lista_Seg2265 = []

Lista_Temp2065 = []
Lista_Seg2065 = []

Lista_Temp2270 = []
Lista_Seg2270 = []

Lista_Temp2070 = []
Lista_Seg2070 = []

Lista_Temp2275 = []
Lista_Seg2275 = []

Lista_Temp2075 = []
Lista_Seg2075 = []

#Extraindo os dados do arquivo de texto para as listas
for linha in texto2260:
    Temperatura = float(linha[6:11])
    Tempo = float(linha[-5:-2])
    Lista_Temp2260.append(Temperatura)
    Lista_Seg2260.append(Tempo)

for linha in texto2060:
    Temperatura = float(linha[6:11])
    Tempo = float(linha[-5:-2])
    Lista_Temp2060.append(Temperatura)
    Lista_Seg2060.append(Tempo)

for linha in texto2265:
    Temperatura = float(linha[6:11])
    Tempo = float(linha[-5:-2])
    Lista_Temp2265.append(Temperatura)
    Lista_Seg2265.append(Tempo)

for linha in texto2065:
    Temperatura = float(linha[6:11])
    Tempo = float(linha[-5:-2])
    Lista_Temp2065.append(Temperatura)
    Lista_Seg2065.append(Tempo)

for linha in texto2270:
    Temperatura = float(linha[6:11])
    Tempo = float(linha[-5:-2])
    Lista_Temp2270.append(Temperatura)
    Lista_Seg2270.append(Tempo)

for linha in texto2070:
    Temperatura = float(linha[6:11])
    Tempo = float(linha[-5:-2])
    Lista_Temp2070.append(Temperatura)
    Lista_Seg2070.append(Tempo)

for linha in texto2275:
    Temperatura = float(linha[6:11])
    Tempo = float(linha[-5:-2])
    Lista_Temp2275.append(Temperatura)
    Lista_Seg2275.append(Tempo)

for linha in texto2075:
    Temperatura = float(linha[6:11])
    Tempo = float(linha[-5:-2])
    Lista_Temp2075.append(Temperatura)
    Lista_Seg2075.append(Tempo)

#Criando e plotando os gráficos
fig1, ax = plt.subplots()
fig2, bx = plt.subplots()
fig3, cx = plt.subplots()
fig4, dx = plt.subplots()

#Figura Ax - Variação da Temperatura da Célula FV - Kp = 60
ax.scatter(Lista_Seg2260, Lista_Temp2260,  marker='o', color='b', edgecolor = 'black', label='Setpoint = 22° C')
ax.plot(Lista_Seg2260, Lista_Temp2260, color='b', linestyle='-', marker='o')
ax.scatter(Lista_Seg2060, Lista_Temp2060,  marker='o', color='r', edgecolor = 'black', label='Setpoint = 20° C')
ax.plot(Lista_Seg2060, Lista_Temp2060, color='r', linestyle='-', marker='o')

ax.set_ylabel('Temperatura da Célula FV (°C)')
ax.set_xlabel('Tempo (s)')
ax.set_title('Variação da Temperatura da Célula FV - Kp = 60')
ax.legend()
ax.set_yticks(np.arange(20,32,1))
ax.set_xticks(np.arange(0,275,25))
ax.grid(True)
fig1.savefig('Variação da Temperatura da Célula FV - Kp = 60.png')

#Figura Bx - Variação da Temperatura da Célula FV - Kp = 65
bx.scatter(Lista_Seg2265, Lista_Temp2265,  marker='o', color='b', edgecolor = 'black', label='Setpoint = 22° C')
bx.plot(Lista_Seg2265, Lista_Temp2265, color='b', linestyle='-', marker='o')
bx.scatter(Lista_Seg2065, Lista_Temp2065,  marker='o', color='r', edgecolor = 'black', label='Setpoint = 20° C')
bx.plot(Lista_Seg2065, Lista_Temp2065, color='r', linestyle='-', marker='o')

bx.set_ylabel('Temperatura da Célula FV (°C)')
bx.set_xlabel('Tempo (s)')
bx.set_title('Variação da Temperatura da Célula FV - Kp = 65')
bx.legend()
bx.set_yticks(np.arange(20,31,1))
bx.set_xticks(np.arange(0,275,25))
bx.grid(True)
fig2.savefig('Variação da Temperatura da Célula FV - Kp = 65.png')

#Figura Cx - Variação da Temperatura da Célula FV - Kp = 70
cx.scatter(Lista_Seg2270, Lista_Temp2270,  marker='o', color='b', edgecolor = 'black', label='Setpoint = 22° C')
cx.plot(Lista_Seg2270, Lista_Temp2270, color='b', linestyle='-', marker='o')
cx.scatter(Lista_Seg2070, Lista_Temp2070,  marker='o', color='r', edgecolor = 'black', label='Setpoint = 20° C')
cx.plot(Lista_Seg2070, Lista_Temp2070, color='r', linestyle='-', marker='o')

cx.set_ylabel('Temperatura da Célula FV (°C)')
cx.set_xlabel('Tempo (s)')
cx.set_title('Variação da Temperatura da Célula FV - Kp = 70')
cx.legend()
cx.set_yticks(np.arange(20,30,1))
cx.set_xticks(np.arange(0,250,25))
cx.grid(True)
fig3.savefig('Variação da Temperatura da Célula FV - Kp = 70.png')

#Figura Dx - Variação da Temperatura da Célula FV - Kp = 75
dx.scatter(Lista_Seg2275, Lista_Temp2275,  marker='o', color='b', edgecolor = 'black', label='Setpoint = 22° C')
dx.plot(Lista_Seg2275, Lista_Temp2275, color='b', linestyle='-', marker='o')
dx.scatter(Lista_Seg2075, Lista_Temp2075,  marker='o', color='r', edgecolor = 'black', label='Setpoint = 20° C')
dx.plot(Lista_Seg2075, Lista_Temp2075, color='r', linestyle='-', marker='o')

dx.set_ylabel('Temperatura da Célula FV (°C)')
dx.set_xlabel('Tempo (s)')
dx.set_title('Variação da Temperatura da Célula FV - Kp = 75')
dx.legend()
dx.set_yticks(np.arange(20,33,1))
dx.set_xticks(np.arange(0,250,25))
dx.grid(True)
fig4.savefig('Variação da Temperatura da Célula FV - Kp = 75.png')





