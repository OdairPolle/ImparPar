# Bibliotecas
from time import sleep as zz
from random import randint

# Printa o logo do jogo colorido
print()
print()
print(f'*' * 37)
print('*->->->' + ' Bem Vindo ao ImparPar ' + '<-<-<-*')
print('*' * 37)
print()
zz(1)

# explicaçao da logica do jogo
print('Tente ganhar no par ou impar da')
print('INTELIGENCIA ARTIFICIAL o maximo de')
print('vezes seguidas para entrar no RANK')
print('do jogo !!!')
zz(1)
print()

# contagem do jogo
vitoria = 0
perda = 0
nome = ''

# Laço para repetir o jogo enquando jogador estiver ganhando
while perda == 0:
    if vitoria == 0:
        nome = str(input('Qual e´ o seu nome?\n ')).title().strip()
        print()
        zz(1)

    # Laço que garante que a entrada seja par ou impar
    while True:
        try:
            escolha = str(input(f'{nome} Par ou Impar?\n ')).title().strip()
            if escolha == 'Impar' or escolha == 'Par':
                break
        except:
            pass
        else:
            pass
    print()
    zz(1)

    # Laço que garante que a entrada seja de 0 a 10''
    while True:
        try:
            numero_jogador = int(input(f'{nome} escolha um numero de 0 a 10!\n '))
            if numero_jogador >= 0 and numero_jogador <= 10:
                break
        except:
            pass
        else:
            pass
    print()
    zz(1)

    # Variavel recebe
    numero_IA = randint(0, 10)
    print('A Inteligencia Artificial escolheu: ')
    zz(1)
    print(f' {numero_IA}')
    zz(1)
    print()

    # Calculo do resultado
    soma = numero_jogador + numero_IA
    if escolha == 'Par' and soma % 2 == 0:
        vitoria += 1
        if vitoria == 1:
            print(f' A soma é {soma}')
            zz(1)
            print(f' {nome} voce  GANHOU {vitoria} vez da I.A.')
        elif vitoria > 1:
            print(f' A soma é {soma}')
            zz(1)
            print(f' {nome} voce  GANHOU {vitoria} vezes da IA!')
    elif escolha == 'Par' and soma % 2 != 0:
        print(f' A soma é {soma}')
        zz(1)
        print(f' {nome} voce PERDEU CORNO!')
        perda += 1
    elif escolha == 'Impar' and soma % 2 == 0:
        print(f' A soma é {soma}')
        zz(1)
        print(f' {nome} voce PERDEU CORNO!')
        perda += 1
    elif escolha == 'Impar' and soma % 2 != 0:
        vitoria += 1
        if vitoria == 1:
            print(f' A soma é {soma}')
            zz(1)
            print(f' {nome} voce  GANHOU {vitoria} vez da IA!')
        elif vitoria > 1:
            print(f' A soma é {soma}')
            zz(1)
            print(f' {nome} voce  GANHOU {vitoria} vezes da IA!')
    print()
    print()
    zz(1)

# ADD RANK
with open('rank.txt', 'a') as rank:
    rank.write(f'{str(vitoria)} {nome},\n')
# logo Rank
print(f'*' * 37,)
print('*->->->->'
      + ' RANK D VENCEDORES '
      + '<-<-<-<-*')
print('*' * 37)
print()
zz(1)

# abrir rank
with open('rank.txt') as rank:
    lista = rank.readlines()

# organizar lista
ordem = sorted(lista, reverse=True)

lugar = 1

for linha in range(0, len(ordem)):
    dados = ordem[linha]
    print(f'{lugar}° - {dados[2:-2]} ganhou {dados[:2]} vezes seguidas')
    lugar += 1
    print()
    zz(1)
    if lugar == 7:
        break
