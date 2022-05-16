import pyautogui as pag

pag.FAILSAFE = False


def obtemPosicao():
    pag.displayMousePosition()
    print('Digite a posição para mover o mouse (left, top):')
    resposta = input()
    if resposta == 'sair' or resposta == 'exit':
        return False
    posicao = resposta.split(',')
    if len(posicao) != 2:
        print('Posição inválida! Para sair digite "sair" ou "exit".')
        return obtemPosicao()
    try:
        pag.moveTo(int(posicao[0]), int(posicao[1]), duration=0.5)
        print('Mouse na posição: {}'.format(pag.position()))
    except ValueError:
        print('Posição inválida!'+ValueError)
    return obtemPosicao()


obtemPosicao()
