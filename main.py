import matplotlib.pyplot as plt


#le o arquivo e preenche o vetor
dia = []
peso = []
file = open("dados.txt", "r")
for line in file:
    if(" - " in line):
        dado = line.split(" - ")
        dia.append(dado[0])
        if(len(dado)>1):
            peso.append(float(dado[1]))


# gera o primeiro grafico
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(dia, peso, color='tab:blue')

ax.set_title('Grafico diario')

plt.show()


#calcula as medias semanais
pesoM = []
semana = []
for i in range(0, len(dia), ++7):
    execept = False
    for j in range(i, i+7):
        if(len(dia)>j):
            if (len(pesoM) <= i//7):
                pesoM.append(0)
                semana.append(0)
            pesoM[i//7] += peso[j]
        else:
            execept = True
            break
    if(execept):
        j-=1
    print(j, i)
    print(j-i+1)
    pesoM[i//7] = pesoM[i//7]/(j-i+1)
    semana[i//7] = dia[i] + "-" + dia[j]


#gera o segundo grafico
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(semana, pesoM, color='tab:blue')

ax.set_title('Grafico semanal')

plt.show()