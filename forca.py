import random
'''
Regras do jogo:
1- Você perde quando sua vida chega a zero (vidas representam as partes do corpo do boneco) 
2- Você pode arriscar a palavra secreta a qualquer momento mas se errar perde o jogo
3- Mais de um caracter é considerado tentativa de chute 
4- Se você errar uma letra perde uma vida 

Comentários:
Esse código teve o objetivo de ser o mais simples possível, só para mostrar que com pouca bagagem é possível fazer
muitas coisas em python, existem muitas outras formas de fazer o jogo da forca, umas mais otimizadas e outras com a 
parte visual mais desenvolvida.
Tente fazer com menos linhas de código!
'''

palavras = ['cachorro', 'maleta', 'planta', 'elefante', 'biscoito', 'chocolate', 'sorvete', 'granola', 'computador']
resposta = palavras[random.randint(0, len(palavras)-1)].upper()
usadas = []
vidas = 6
complete = list(len(resposta) * '_')
print('------ Bem vindo à |FORCA|, cuidado para não ser enforcado!! ------\n')
print('Sua palavra tem {} letras >>>> {}'.format(len(resposta), ''.join(complete)))
while True:
    print(f'\nVocê tem {vidas} vidas...'  
          '\n______________________________________________________________________')
    letra = input('\nDigite uma letra, ou tente acertar a palavra: ').upper().strip()
    if letra == resposta:
        print(f'\nParabéns você acertou!!! A resposta era {resposta} !')
        break
    elif letra != resposta and len(letra) != 1:
        print(f'\nQue pena, você errou o chute... A resposta era {resposta} !')
        break
    else:
        if letra not in usadas and letra in resposta:
            n = 0
            while resposta.find(letra, n) != -1:
                complete[resposta.find(letra, n)] = letra
                n = resposta.find(letra, n) + 1
            usadas.append(letra)
            print(''.join(complete))
            print('Letras usadas >>> {}'.format(','.join(usadas)))
            if ''.join(complete) == resposta:
                print(f'\nParabéns você acertou!!!')
                break
        elif letra not in usadas and letra not in resposta:
            print('\nEssa letra não está na palavra secreta, tente novamente...')
            usadas.append(letra)
            print('Letras usadas >>> {}'.format(','.join(usadas)))
            print(''.join(complete))
            vidas -= 1
            if vidas == 0:
                print(f'\nVocê foi enforcado... A resposta era {resposta}')
                break
        else:
            print('\nVocê já usou essa letra, tente outra...')
            print('\nLetras usadas >>> {}'.format(','.join(usadas)))
            print(''.join(complete))
