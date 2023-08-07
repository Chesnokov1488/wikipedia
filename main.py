import telebot , wikipedia, re

bot = telebot.TeleBot('6209808823:AAF_VEfKXg1VCu_FqLONBHb9HlilRpvTxCk')

wikipedia.set_lang('ru')

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)

        return wikitext2

    except Exception as e:
        return 'В энциклопедии нет информации об этом'

@bot.message_handler(commands=['start','help'])
def start(message, res=False):
    bot.send_message(message.chat.id,'Привет, я бот Википедия, я могу дать определение любому слову и любому предмету и событию, просто напиши мне что ты хочешь узнать🧠')
    bot.send_message(message.chat.id,'Тебе нужен крутой функциональный бот🤖?Подписывайся на телеграмм канал, и напиши разработчику🦾'
                     'https://t.me/creatoroftelegrambots')

@bot.message_handler(content_types=["text"])
def go(message):
    bot.send_message(message.chat.id,getwiki(message.text))

bot.polling(none_stop=True)

