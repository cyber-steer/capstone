import telegram
chat_token = "5781093194:AAGj5G9KNiMR2qxoZHK7oY5N_RyMfH-TuKc"
chat = telegram.Bot(token=chat_token)
bot = telegram.Bot(chat_token)
text = '등록되지 않은 사람이 인식되었습니다.'
bot.sendMessage(chat_id = "5600518771", text=text)