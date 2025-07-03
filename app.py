import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    # if comando in ('olá', 'boa tarde', 'bom dia'):
    #     return 'Olá tudo bem!'
    # if comando == 'como estás':
    #     return 'Estou bem, obrigado!'
    # if comando == 'como te chamas?':
    #     return 'O meu nome é: Bot :)'
    # if comando == 'tempo':
    #     return 'Está um dia de sol!'
    # if comando in ('bye', 'adeus', 'tchau'):
    #     return 'Gostei de falar contigo! Até breve...'
    # if 'horas' in comando:
    #     return f'São: {datetime.now():%H:%M} horas'
    # if 'data' in comando:
    #     return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    # return f'Desculpa, não entendi a questão! {texto}'

    respostas = {
        ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        'como estás': 'Estou bem, obrigado!',
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',
        ('sabes fazer', 'consegues fazer'): 'Posso dizer-te a data de hoje, as horas, e mais umas quantas coisinhas :)',
        ('tempo', 'meteorologia'): 'Está um lindo dia de sol!',
        'horas': f'São, neste momento: {datetime.now():%H:%M}',
        ('data', 'hoje'): f'A data de hoje é: {datetime.now():%d-%m-%Y}',
        ('nome', 'chama'): 'O meu nome é Bot (^_^)'
    }
    texto2 = ""
    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                texto2 += resposta + " "
            else:
                for i in chave:
                    if comando.__contains__(i):
                        texto2 += resposta + " "
        elif chave in comando:
            texto2 += resposta + " "
    if texto2 == "":
        return f'Desculpa, não entendi a questão! "{texto}"'
    else:
        texto2 = texto2.strip()
        return texto2

def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas?\n> ')
    print(f'Bot: Olá, {name}!\nComo te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta = obter_resposta(user_input)
        print("Bot:", resposta)
        
        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()