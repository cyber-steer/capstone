import telegram

class Telegram:

    def __init__(self):
        # Telegram API
        self.chat_token = "5781093194:AAGj5G9KNiMR2qxoZHK7oY5N_RyMfH-TuKc"
        self.chat = telegram.Bot(token = self.chat_token)
        # updates = chat.getUpdates()
        # for u in updates:
        #     print(u.message['chat']['id'])

    def sendMessege(self):
        bot = telegram.Bot(self.chat_token)
        text = '등록되지 않은 사람이 인식되었습니다.'
        bot.sendMessage(chat_id = "5600518771", text=text)

    def sendImg(self, img):
        bot = telegram.Bot(self.chat_token)
        bot.send_photo(chat_id = '5600518771', photo=open(img, 'rb'))

    # 텔레그램 스레드
    def send(self, q, send, receive):
        while True:
            if receive.is_set():
                file = q.get()
                self.sendMessege()
                self.sendImg('Unknown.jpg')
                send.set()
                receive.clear()