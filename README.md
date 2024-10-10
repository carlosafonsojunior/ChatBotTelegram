# ChatBotTelegram

Instale a biblioteca python-telegram-bot: Execute o comando abaixo para instalar a biblioteca necessária: pip install python-telegram-bot==13.7

Crie um bot no Telegram:

Abra o Telegram e pesquise por "BotFather".
Use o comando /newbot e siga as instruções para criar seu bot.
Ao final, você receberá um Token de acesso.

Menu Inicial:

O comando /start exibe um menu com três opções principais: "Suporte Técnico", "Informações de Produto" e "Fale com um atendente".

Lógica de Conversação:

Dependendo da escolha do usuário, o bot responde com mais perguntas ou respostas relacionadas à opção escolhida.
A função handle_message contém as lógicas de resposta com base no texto da mensagem enviada pelo usuário.
Botões de Resposta Rápida:

São criados botões no teclado do usuário para facilitar a navegação e escolha de opções, usando ReplyKeyboardMarkup.

Respostas Padrão:

Caso o bot não entenda o que foi enviado, ele responde com uma mensagem padrão e exibe o menu novamente.

Como executar:

Execute o arquivo no terminal com:python bot.py
