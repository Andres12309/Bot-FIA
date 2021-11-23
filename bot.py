from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from colorama import init, Fore, Back, Style

# Creamos una instancia de Criptus
bot = ChatBot(
    'Criptus',
    storage_adapter=
    'chatterbot.storage.SQLStorageAdapter',  # Importamos el adaptador de almacenamiento
    logic_adapters=[
        {
            'import_path':
            'chatterbot.logic.BestMatch'  # importamos el adaptador para las respuestas
        },
        {
            'import_path':
            'chatterbot.logic.SpecificResponseAdapter',  # Adaptador para respuestas especificas
            'input_text':
            'Hola',  # Entrada del usuario
            'output_text':
            Fore.RED +
            'Mi nombre es Criptus, puedo informarte sobre criptomonedas' +
            Fore.WHITE  # Respuesta de bot
        },
        {
            'import_path':
            'chatterbot.logic.SpecificResponseAdapter',  # Adaptador para respuestas especificas
            'input_text':
            'Sabes que es Bitcoin',  # Entrada del usuario
            'output_text':
            Fore.RED +
            'Es una criptomoneda y un sistema de pago​​ sin banco central o administrador único.​​ En principio, los usuarios de bitcoin pueden transferir dinero entre sí a través de una red entre iguales usando software libre y de código abierto'
            + Fore.WHITE  # Respuesta de bot
        },
        {
            'import_path':
            'chatterbot.logic.SpecificResponseAdapter',  # Adaptador para respuestas especificas
            'input_text':
            'Sabes que es ETH',  # Entrada del usuario
            'output_text':
            Fore.RED +
            'Ethereum es una plataforma open source, que sirve para programar contratos inteligentes. La plataforma es descentralizada a diferencia de otras cadenas de bloques.'
            + Fore.WHITE  # Respuesta de bot
        },
        {
            'import_path':
            'chatterbot.logic.SpecificResponseAdapter',  # Adaptador para respuestas especificas
            'input_text':
            'Binance',  # Entrada del usuario
            'output_text':
            Fore.RED +
            'Es una plataforma de intercambio de criptomonedas que proporciona una plataforma para comerciar más de 100 activos digitales.'
            + Fore.WHITE  # Respuesta de bot
        },
        {
            'import_path':
            'chatterbot.logic.SpecificResponseAdapter',  # Adaptador para respuestas especificas
            'input_text':
            'Huobi',  # Entrada del usuario
            'output_text':
            Fore.RED +
            'Huobi es un intercambio de criptomonedas con sede en Seychelles.'
            + Fore.WHITE  # Respuesta de bot
        },
        {
            'import_path':
            'chatterbot.logic.SpecificResponseAdapter',  # Adaptador para respuestas especificas
            'input_text':
            'LTC',  # Entrada del usuario
            'output_text':
            Fore.RED +
            'Litecoin es una criptomoneda y proyecto de software de código abierto publicado bajo la licencia MIT​ inspirado y prácticamente idéntico en su aspecto técnico​ a Bitcoin.'
            + Fore.WHITE  # Respuesta de bot
        },
        {
            'import_path':
            'chatterbot.logic.SpecificResponseAdapter',  # Adaptador para respuestas especificas
            'input_text':
            'BNB',  # Entrada del usuario
            'output_text':
            Fore.RED +
            'Binance Coin es la criptomoneda oficial del criptoexchange o casa de cambio Binance, cuyo nombre es un acrónimo compuesto de las palabras “binary” y “finance”.'
            + Fore.WHITE  # Respuesta de bot
        }
    ],
    #trainer='chatterbot.trainers.ListTrainer' # Entrenamos al bot
)

trainer = ListTrainer(bot)

print('Bienvenido escribe alguna cosa...')
while True:
    try:
        user_input = input()
        bot_response = bot.get_response(user_input)
        print(bot_response)
    except (Exception, EOFError, SystemExit):
        break
