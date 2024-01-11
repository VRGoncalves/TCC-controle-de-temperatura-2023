#Importando bibliotecas
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#Criando as listas de dados
Lista_Temp = []
Lista_Seg = []
Lista_SetPoint = []
Lista_Pwm = []
Lista_Limite_Sup = []
Lista_Limite_Inf = []
residuals = []
SetPoint = 27.0
Limite_Sup = SetPoint + 0.5
Limite_Inf = SetPoint - 0.5

# Abrindo e lendo os arquivos de texto
with open("D:\Victor\Desktop\Testes TCC Fotovotaico\Monitor Script - 2 placas 27 graus - kp32 ki10 kd1.txt", "r") as arquivo:
    texto = arquivo.readlines()

#Extraindo os dados do arquivo de texto para as listas
for linha in texto:
    Temperatura = float(linha[6:11])
    Tempo = float(linha[-5:-2])
    Pwm = float (linha [18:24])
    Lista_Temp.append(Temperatura)
    Lista_Seg.append(Tempo)
    Lista_Pwm.append(Pwm)
    Lista_SetPoint.append(SetPoint)
    Lista_Limite_Sup.append(Limite_Sup)
    Lista_Limite_Inf.append(Limite_Inf)
    
#definindo o modelo da função da curva de ajuste dos dados experimentais
def model(z, h, a, b, c, d, e, f, g):
    return h*(z**7) + a*(z**6) + b*(z**5) + c*(z**4) + d*(z**3) + e*(z**2) + f*z + g

#Criando a funçao de regressao com base nos dados
popt, pcov = curve_fit(model, Lista_Seg, Lista_Temp)
xx = np.linspace(Lista_Seg[0], Lista_Seg[-1] ,int(Lista_Seg[-1]/4)+1)
yy = model(xx, *popt)

#Cálculo do R² da função de regressão
residuals = Lista_Temp - yy
ss_res = np.sum(residuals**2)
ss_tot = np.sum((Lista_Temp - np.mean(Lista_Temp))**2)
r_squared = round(1 - (ss_res / ss_tot),4)

#Criando e plotando os gráficos
fig1, ax = plt.subplots()
fig2, bx = plt.subplots()

#Grafico Temperatura x tempo
ax.plot(xx, yy, color='black', linestyle='--', label=f'R² = {r_squared}')
ax.plot(Lista_Seg, Lista_Limite_Inf,  linestyle='--', color='g', label=f'Tolerância Min = {Limite_Inf}° C')
ax.plot(Lista_Seg, Lista_Limite_Sup,  linestyle='--', color='g', label=f'Tolerância Max = {Limite_Sup}° C')
ax.plot(Lista_Seg, Lista_SetPoint,  linestyle='--', color='r', label=f'SetPoint = {SetPoint}°C')
ax.scatter(Lista_Seg, Lista_Temp,  marker='o', color='b', label='Dados Experimentais')

ax.set_ylabel('Temperatura da Célula FV (°C)')
ax.set_yticks(np.arange(SetPoint - 1,35,1))
ax.set_xticks(np.arange(0,315,25))
ax.set_xlabel('Tempo (s)')
ax.set_title('Variação da Temperatura da Célula FV - Setpoint 27° C')
ax.legend()
ax.grid(True)
fig1.savefig('Variação da Temperatura da Célula FV - Setpoint 27° C')

#Grafico pwm x tempo
bx.plot(Lista_Seg, Lista_Pwm, color='g', linestyle='--', marker='o', label='PWM - Dados Experimentais')
bx.set_ylabel('Intensidade do Sinal PWM')
bx.set_xticks(np.arange(0,315,25))
bx.set_xlabel('Tempo (s)')
bx.set_title('Variação do Sinal de Saída - Setpoint 27° C')
bx.legend()
bx.grid(True)
fig2.savefig('Variação do Sinal de Saída - Setpoint 27° C')