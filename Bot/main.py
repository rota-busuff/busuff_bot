from dotenv import dotenv_values
from telegram.ext import ApplicationBuilder, CommandHandler
from controller import Controle
from view import Mensagem

config = dotenv_values(".env") 

if __name__ == "__main__":
    app = ApplicationBuilder().token(config.get("TELEGRAM_TOKEN_BOT_2")).build()
    app.add_handlers(handlers=[
        CommandHandler(["iniciar"], Mensagem.inicia),
        CommandHandler(["atualizar"], Mensagem.atualiza),
        CommandHandler(["finalizar"], Mensagem.encerra),
    ])
    
    print("Bot está rodando...")
    app.run_polling()