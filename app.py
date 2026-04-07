print("="*40)
print("   PESQUISA DE SATISFAÇÃO - TUDO WEB   ")
print("="*40)

#Regra dos contadores
qtde_excelente = 0
qtde_ruim = 0

#Estrutura da repetição (50 entrevistas)
for i in range(1, 51):
    print(f"\nEntrevistado Nº: {i}")
    nome = input("Digite o seu nome: ")
    while True:
        try: 
            idade = int(input("Digite a sua idade: "))
            break
        except ValueError:
            print("❌ ERRO!! Digite somente números")

#Loop com while até a resposta válida
    while True: 
        print(f" - Prezado(a) {nome}, como foi a sua experiência na TudoWeb?")
        pesquisa = input(" - Considere 1(Excelente) ou 2(Bom) ou 3(Ruim): ")
    
        if pesquisa in ["1" , "2" , "3"]:
            print("Obrigado pela participação!!")
 
#Contagem das pontuações 
            if pesquisa == "1":
                qtde_excelente += 1
            elif pesquisa == "3":
                qtde_ruim += 1
            break
# Encerra o while e saegue para o proximo entrevistado
        else:
            print(" ⚠️ Nota inválida! Por favor, digite 1, 2 ou 3 ")

#Relatório da pesquisa
print("\n" + "="*40)
print("   RESULTADO DA PESQUISA   ")
print(f" - Quantidade de respostas 'EXCELENTE': {qtde_excelente}")
print(f" - Quantidade de respostas 'RUIM': {qtde_ruim}")
print("="*40 + "\n")
