from telebot import TeleBot, Telebot
from Guild import Guild

class Admin:

    def __init__(self,bot=TeleBot):
        self.admin = None
        self.developer = "cursor0P"
        self.bot = bot
        self.subAdmins = []

    def set_admin(self,message):
        warn_msg = "You are not allowed to use admin commands!"

        if self.admin is None:
            self.admin = message.from_user.username
            self.bot.send_message(message.chat.id,f"{self.admin} is assigned as an admin")

        
    def change_admin(self, message):
        warn_msg = "You are not allowed to use admin commands"
        text = "To change Admin please pass new admin username after /admin command."

        if self.admin == message.from_user.username and len(message.text.split(" "))>1:
            new_admin = message.text.split(" ")[1]
            self.admin = new_admin
        elif message.from_user.username != self.admin:
            self.bot.send_message(message,warn_msg)
        else:
            self.bot.send_message(message.chat.id,text,text=text)

    def add_subAdmin(self,message):
        if message.from_user.username == self.admin:
            if len(message.text.split(" ")) >1:
                subAdmin = message.split(" ")[1]
                self.subAdmins.append(subAdmin)
                self.bot.send_message(message.chat.id,f"new sub-admin added {subAdmin}")
        else:
            self.bot.send_message(message.chat.id,"Only admin can add sub admins!")

    def remove_subAdmin(self,message):
        if message.from_user.username == self.admin and len(message.text.split(" ")) >1:
            subAdmin = message.text.split(' ')[1]
            if subAdmin in self.subAdmins:
                self.subAdmins.remove(subAdmin)
            else:
                self.bot.send_message(message.chat.id,f"{subAdmin} is not a subAdmin")

    def check_subAdmins(self,message):
        self.bot.send_message(message.chat.id,f"current subAdmins are: {self.subAdmins}")




class SubAdmin(Guild,Admin):

    def __init__(self):
        super().__init__()
        self.authorized_members = self.subAdmins.append(self.admin)
    
    def set_guild_name(self, message):
        if message.from_user.username in self.authorized_members and message.text.split(" ")>1:
            guild_name = message.text.split(' ')[1]
            self.guild_name = guild_name
        elif message.from_user.username in self.authorized_members and message.text == "/set_guild_name":
            self.bot.send_message(message.chat.id,"To change guild name please enter a guild name after the command /set_guild_name")
        else:
            self.bot.send_message(message.chat.id,"You are not allowed to change guild name!")
    
    def change_event_info(self,message):

        if message.from_user.username in self.authorized_members and message.text == "/change_event_info":
            self.bot.send_message(message.chat.id,"To change event info type info after /change_event_info command")

        elif message.from_user.username in self.authorized_members and message.text.split(" ")>1:
            self.event_info = message.text.split(" ")[1:]
        else:
            self.bot.send_message(message.chat.id,"You are not authorized to do this!")
    

    def change_rules(self,message):
        if message.from_user.username in self.authorized_members and message.text == "/change_rules":
            self.bot.send_message(message.chat.id,"To change event info type info after /change_rules command")

        elif message.from_user.username in self.authorized_members and message.text.split(" ")>1:
            self.rules_info = message.text.split(" ")[1:]
        else:
            self.bot.send_message(message.chat.id,"You are not authorized to do this!")


    def change_announcements(self, message):
        if message.from_user.username in self.authorized_members and message.text == "/change_announcements":
            self.bot.send_message(message.chat.id,"To change event info type info after /change_announcements command")

        elif message.from_user.username in self.authorized_members and message.text.split(" ")>1:
            self.event_info = message.text.split(" ")[1:]
        else:
            self.bot.send_message(message.chat.id,"You are not authorized to do this!")


    def check_subAdmins(self, message):
        return super().check_subAdmins(message)