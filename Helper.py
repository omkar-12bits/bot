from telebot import types
import telebot

class Helper:

    def __init__(self):
        self.bot = "Chikxxan"

    #This will generate buttons for us in more elegant way
    def generate_buttons(self ,bts_names):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=len(bts_names))
        for button in bts_names:
            markup.add(types.KeyboardButton(button))
        return markup
    
    def show_heros(self,name:str):
        return "Dark Follower"

    def show_gears(self,name:str):
        pass

    def show_monsters(self,message,bot:telebot,monster:str):
        match monster:
            case "marc":
                with open('monsters/mns3.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mbla":
                with open('monsters/mns9.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mbon":
                with open('monsters/mns9.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mcot":
                with open('monsters/mns5.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mfro":
                with open('monsters/mns6.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mgar":
                with open('monsters/mns3.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mgaw":
                with open('monsters/mns2.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mgri":
                with open('monsters/mns6.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mgry":
                with open('monsters/mns5.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mhar":
                with open('monsters/mns12.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mhel":
                with open('monsters/mns11.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mhoo":
                with open('monsters/mns4.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mjad":
                with open('monsters/mns1.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mmec":
                with open('monsters/mns2.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mmeg":
                with open('monsters/mns7.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mnec":
                with open('monsters/mns1.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mnoc":
                with open('monsters/mns12.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mque":
                with open('monsters/mns8.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "msab":
                with open('monsters/mns11.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mser":
                with open('monsters/mns10.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "msno":
                with open('monsters/mns8.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mter":
                with open('monsters/mns4.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mtid":
                with open('monsters/mns10.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case "mvoo":
                with open('monsters/mns7.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)
            case 'help':
                with open('monsters/monsters.jpg','rb') as photo:
                    bot.send_photo(message.chat.id, photo)

    def show_stages(self,name:str):
        pass

    def show_colosseum(self):
        pass




monsters = ['Рино', 'древний голем', 'Саблезуб', 'адский драйдер', 'Вьюжник', 'Королева пчёл', 'Магот',
      'Шаман вуду', 'Ледокрыл', 'Мрачный жнец', 'Грифон', 'бешеный теремок', 'Наг гладиатор', 'Титан', 
      'Тощая Вивиан', 'чернокрыл', 'Жуткая лапа', 'шип ужаса', 'Освальд', 'гаргантюа', 'Большой УК', 
      'троянский конь', 'Нефритовый змей', 'некрозис', '']