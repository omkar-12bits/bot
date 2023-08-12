import os 
import telebot
from Helper import Helper


os.environ['BOT_TOKEN'] = ""
BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)
assist = Helper()

@bot.message_handler(commands=['start','hello'])
def send_welcome(message):
    markup = assist.generate_buttons(['help/помощь','monster/монстр'])
    result = bot.reply_to(message,"Howdy, how are you doing?",reply_markup=markup)

    if result.text in "help/помощь":
        bot.register_next_step_handler(result,sign_handler)
    if result.text in "monster/монстр":
        bot.register_next_step_handler(result,sign_handler)

        
@bot.message_handler(commands=["help"])
def help_handler(message):
    text = "to see monster formation please use /monster command /n then choose monster code and type it to see formation" 
    bot.send_message(message.chat.id,text)
    
            
@bot.message_handler(commands=['monster'])
def sign_handler(message):
    text = "choose from monster code from listed monster names : "
    with open('monsters/monsters.jpg','rb') as mp:
        bot.send_photo(message.chat.id,mp)
    sent_msg = bot.send_message(message.chat.id,text,parse_mode="Markdown")
   

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "help/помощь":
        help_handler(message)
    elif message.text == "monster/монстр":
        sign_handler(message)
    elif message.text == "start":
        send_welcome(message)
    else:
        monster = message.text.lower() 
        bot.send_message(message.chat.id,monster)
        assist.show_monsters(message,bot,monster)



bot.infinity_polling()

# vSpJ52Yu_bMAgxvXCemNa1K98SLYR5yfgu28iV6Cq
# vSpJ52Yu



179351
179730
111414
161785
195832
178882
166181
198052
202051
