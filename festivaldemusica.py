from collections import deque

# Programação das bandas
programacao = {
    "Som do Sol": ["14:00", "Rock"],
    "Batida do Norte": ["15:30", "Forró"],
    "Noite Jazz": ["17:00", "Jazz"]
}

programacao["Luz Urbana"] = ["18:30", "Pop"]

print("\nBandas e estilos:")
for banda, info in programacao.items():
    print(f"{banda}: {info[1]}")

print("\nHorários das apresentações:")
for info in programacao.values():
    print(info[0])

# Fila de pessoas que vão assistir o show
fila_publico = deque()

fila_publico.appendleft("Ana (VIP)")
fila_publico.appendleft("Carlos (VIP)")

fila_publico.append("João")
fila_publico.append("Fernanda")

print("\nFila atual do público:")
print(list(fila_publico))

print("\nEntrada de 2 pessoas:")
print(f"{fila_publico.popleft()} entrou.")
print(f"{fila_publico.popleft()} entrou.")

fila_publico.append("Marcos")
print("\nFila atualizada após entrada e novo público:")
print(list(fila_publico))

#Menu de funcionamento do programa
def exibir_menu():
    print("\n--- MENU DO FESTIVAL ---")
    print("1. Cadastrar nova banda")
    print("2. Mostrar programação")
    print("3. Adicionar pessoa à fila")
    print("4. Remover pessoa da fila")
    print("5. Mostrar fila atual")
    print("0. Sair")

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome da banda: ")
        horario = input("Horário da apresentação (HH:MM): ")
        estilo = input("Estilo musical: ")
        programacao[nome] = [horario, estilo]
        print(f"Banda '{nome}' adicionada com sucesso.")
    
    elif opcao == "2":
        print("\nProgramação do Festival:")
        for banda, info in programacao.items():
            print(f"{banda} - {info[0]} - {info[1]}")
    
    elif opcao == "3":
        nome = input("Nome da pessoa: ")
        prioridade = input("É VIP? (s/n): ")
        if prioridade.lower() == "s":
            fila_publico.appendleft(nome + " (VIP)")
        else:
            fila_publico.append(nome)
        print(f"{nome} adicionado(a) à fila.")
    
    elif opcao == "4":
        if fila_publico:
            pessoa = fila_publico.popleft()
            print(f"{pessoa} entrou no festival.")
        else:
            print("Fila está vazia.")
    
    elif opcao == "5":
        print("\nFila atual do público:")
        print(list(fila_publico))
    
    elif opcao == "0":
        print("Encerrando o sistema.")
        break

    else:
        print("Opção inválida. Tente novamente.")
