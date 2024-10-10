from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Substitua 'TELEGRAM_BOT_TOKEN' pelo token gerado pelo BotFather
TOKEN = 'TELEGRAM_BOT_TOKEN'

# Função para iniciar a conversa e mostrar o menu inicial
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        ['📞 Suporte Técnico', '📦 Informações de Produto'],
        ['❓ Fale com um atendente']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    
    update.message.reply_text(
        'Bem-vindo ao Suporte! Como podemos ajudar?',
        reply_markup=reply_markup
    )

# Função que trata as mensagens enviadas pelo usuário
def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text.lower()  # Converte o texto para minúsculo
    chat_id = update.message.chat_id

    if 'suporte técnico' in text:
        update.message.reply_text(
            'Você escolheu Suporte Técnico. Em que podemos ajudar?\n'
            '1. Problemas de conexão\n'
            '2. Erro no sistema\n'
            '3. Configuração'
        )
    elif 'informações de produto' in text:
        update.message.reply_text(
            'Sobre qual produto você gostaria de saber mais?\n'
            '1. Produto A\n'
            '2. Produto B\n'
            '3. Produto C'
        )
    elif 'fale com um atendente' in text:
        update.message.reply_text(
            'Um de nossos atendentes entrará em contato em breve. Por favor, aguarde.'
        )
    elif 'problemas de conexão' in text:
        update.message.reply_text(
            'Para problemas de conexão, verifique se o seu roteador está funcionando corretamente e se a internet está ativa.'
        )
    elif 'erro no sistema' in text:
        update.message.reply_text(
            'Erro no sistema? Tente reiniciar o software. Se o problema persistir, entre em contato com o suporte técnico.'
        )
    elif 'configuração' in text:
        update.message.reply_text(
            'Precisa de ajuda com a configuração? Acesse nosso guia online ou siga as instruções enviadas para o seu e-mail.'
        )
    elif 'produto a' in text:
        update.message.reply_text(
            'Produto A é nosso software mais avançado, com recursos de AI e automação. Para saber mais, visite nosso site.'
        )
    elif 'produto b' in text:
        update.message.reply_text(
            'Produto B é ideal para pequenas empresas, oferecendo gerenciamento de tarefas e relatórios. Mais informações no nosso site.'
        )
    elif 'produto c' in text:
        update.message.reply_text(
            'Produto C é uma solução econômica, focada em startups. Oferece tudo o que você precisa para começar.'
        )
    else:
        # Resposta padrão caso a mensagem não corresponda a nenhuma opção
        keyboard = [
            ['📞 Suporte Técnico', '📦 Informações de Produto'],
            ['❓ Fale com um atendente']
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text(
            'Desculpe, não entendi sua mensagem. Escolha uma das opções abaixo:',
            reply_markup=reply_markup
        )

# Função principal para rodar o bot
def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    # Comando /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Handler para mensagens de texto
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Inicia o bot
    updater.start_polling()

    # Mantém o bot rodando até que seja interrompido manualmente
    updater.idle()

if __name__ == '__main__':
    main()
