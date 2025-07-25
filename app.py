import os
from datetime import datetime
from random import sample

name = ""

def obter_resposta(texto: str) -> str:
    global name
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
        ('olá', 'boa tarde', 'bom dia'): f'Olá tudo bem, {name}!',
        ('como estás', 'como vais'): f'Estou bem, obrigado! E tu, {name}?',
        ('bem', 'andando'): 'Que bom! ^_^',
        'mal': 'Oh... Lamento Ó_Ò',
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',
        ('sabes fazer', 'consegues fazer'): 'Posso dizer-te a data de hoje, as horas, e mais umas quantas coisinhas ^_^',
        ('tempo', 'meteorologia'): 'Está um lindo dia de sol!',
        'horas': f'São, neste momento: {datetime.now():%H:%M}',
        ('data', 'hoje'): f'A data de hoje é: {datetime.now():%d-%m-%Y}',
        ('nome', 'chama'): 'O meu nome é Bot ^_^',
        'adivinha': 'adivinhas()'
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
            if chave == 'adivinha':
                texto2 += eval(resposta)
            else:
                texto2 += resposta + " "
    if texto2 == "":
        return f'Desculpa, não entendi a questão! "{texto}"'
    else:
        texto2 = texto2.strip()
        return texto2

def adivinhas():
    adivinha = {'quanto mais se tira, maior fica?': 'Um buraco!',
                'tem pernas mas não anda?': 'Uma mesa!',
                'cai em pé e corre deitada?': 'A chuva!',
                'tem boca mas não fala e tem leito mas não dorme?': 'Um rio!',
                'se cai ao chão fica amarela?': 'Um ovo!'}
    pergunta = sample(list(adivinha.keys()), 1)[0]
    print('Bot: Qual é a coisa, qual é ela, que', pergunta)
    resp_correta = adivinha[pergunta].split(' ')[1][:-1]
    resposta = str(input("Tu: ").strip())
    if resp_correta in resposta:
        return 'Muito bem!'
    else:
        return f'A resposta correta é: {adivinha[pergunta]}'
    

def chat() -> None:
    global name
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name = str(input('Bot: Como te chamas?\n> ')).strip()
    print(f'Bot: Olá, {name}!\nComo te posso ajudar?')

    while True:
        user_input: str = input('Tu: ').strip()
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