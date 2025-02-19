from dotenv import dotenv_values
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
from telegram import Update 
import datetime, time
from controller import Controle
from view import Mensagem

config = dotenv_values(".env") 

async def main(update: Update, context: CallbackContext):
    hora_atual = datetime.datetime.now()
    # DEFINIR INTERVALO DE TRABALHO DO BOT
    hora_inicio = hora_atual.replace(hour=19, minute=30, second=0, microsecond=0)
    hora_fim = hora_atual.replace(hour=19, minute=42, second=0, microsecond=0)

    while True:
        if hora_atual >= hora_inicio:
            await Mensagem.inicia(update, context)

            while hora_atual < hora_fim:
                await Mensagem.atualiza(update, context)
                time.sleep(10) # DEFINIR TEMPO ENTRE AS REQUISIÇÕES
                hora_atual = datetime.datetime.now()

            break

    await Mensagem.encerra(update, context)

if __name__ == "__main__":
    app = ApplicationBuilder().token(config.get("TELEGRAM_TOKEN_BOT")).build()

    # COLOCAR UM HANDLER QUE SIRVA DE TOKEN PRA INICIAR O BOT
    app.add_handlers(handlers=[CommandHandler("iniciar_turno_bot", main)])

    print("Bot rodando")

    app.run_polling()