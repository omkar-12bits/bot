import os 
import telebot
from Helper import Helper
from Guild import Guild
from Admin import Admin,SubAdmin

os.environ['BOT_TOKEN'] = " "
BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)
assist = Helper()
guild_regulator = Guild()
admin = Admin()


@bot.message_handler(commands=['start','hello'])
def send_welcome(message):
    markup = assist.generate_buttons(['/guild','/🤨❓','/monster','/contact developer'])
    bot.reply_to(message,"Lets get started !!!",reply_markup=markup)

        
@bot.message_handler(commands=["help",'🤨❓'])
def help_handler(message):
    print(f"user : {message.from_user.username} commanded : {message.text}")
    text = "to see monster formation please use /monster command \nthen type the monster code see formation" 
    bot.send_message(message.chat.id,text)
    
            
@bot.message_handler(commands=['monster'])
def monster_handler(message):
    print(f"user : {message.from_user.username} commanded : {message.text}")
    text = "choose from monster code from listed monster names : "
    with open('monsters/monsters.jpg','rb') as mp:
        bot.send_photo(message.chat.id,mp)
    sent_msg = bot.send_message(message.chat.id,text,parse_mode="Markdown")
   
# Guild Specific Commands

@bot.message_handler(commands=['guild'])
def guild(message):
    print(f"user : {message.from_user.username} commanded : {message.text}")
    text = """Here's your guilds log:
    \n/rules to know your guilds rules
    \n/event to know your guilds main event and their minimum score
    \n/announcement if your guild or leader have any """
    bot.send_message(message.chat.id,text=text.lstrip())

@bot.message_handler(commands=['event','rules','announcement'])
def guild_handler(message):
    if "announcement" in message.text:
        guild_regulator.announcements(message,bot)
    elif "rules" in message.text:
        guild_regulator.rules(message,bot)
    elif "event" in message.text:
        guild_regulator.event(message,bot)


# Admin Specific Commands

@bot.message_handler(commands=['admin'])
def admin_handler(message):
    admin.set_admin(message=message)
    markup = assist.generate_buttons(['/change_admin','/add_subAdmin','/remove_subAdmin','/check_subAdmins'])
    bot.reply_to(message,"Admin Privilege Mode ",reply_markup=markup)

@bot.message_handler(commands=['change_admin','add_subAdmin','remove_subAdmin','check_subAdmins'])
def admin_commands(message):
    command = message.text

    if 'change_admin' in command:
        admin.change_admin(message=message)
    elif 'add_subadmin' in command:
        admin.add_subAdmin(message=message)
    elif 'remove_subAdmin' in command:
        admin.remove_subAdmin(message=message)
    elif 'check_subAdmins' in command:
        admin.check_subAdmins(message=message)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    monster = message.text.lower() 
    print(f"user : {message.from_user.username} commanded : {message.text}")
    assist.show_monsters(message,bot,monster)


bot.infinity_polling()

