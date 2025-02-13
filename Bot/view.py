from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from datetime import datetime
from controller import Controle

class Mensagem:
    id_canal = "-1002278468597"

    @staticmethod
    async def inicia(update: Update, context: CallbackContext):
        semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
        dia = datetime.now().weekday()

        mensagem = f"🌞💪 Bom dia! Mais uma {semana[dia]} vigiando o Busuff para você não perder o horário do ônibus."
        
        await context.bot.send_message(chat_id=Mensagem.id_canal, text=mensagem)

    @staticmethod
    async def atualiza(update: Update, context: CallbackContext):
        informacoes = Controle.consultar()
        mensagem = ""

        if (informacoes != None):
            for info in informacoes:
                if (info['online'] == 1):
                    mensagem = mensagem + f"\n\n🚌 *{info['rota']}*\n📍 {info['posicao']}\n⏰ {info['mensagem']}"
                
                else:
                    mensagem = mensagem + f"\n\n🚌 *{info['rota']}*\n🚫 Motorista offline\."

        else:
            mensagem = "⚠️🔌 Serviço indisponível no momento\!"

        mensagem = mensagem + f"\n\n Atualizado por último às *{datetime.now().strftime('%H:%M:%S')}*"

        await context.bot.send_message(chat_id=Mensagem.id_canal, text=mensagem, parse_mode="MarkdownV2")

    @staticmethod
    async def encerra(update: Update, context: CallbackContext):

        diaSemana = datetime.now().weekday()

        if (diaSemana < 4):
            mensagem = "🏠💤 O expediente acabou, agora é hora de descansar. Até amanhã!"

        else:
            mensagem = "🌇🍻  O expediente acabou, agora é hora de relaxar. Nos vemos na segunda!"

        await context.bot.send_message(chat_id=Mensagem.id_canal, text=mensagem)