from telebot import Telebot


class Guild:

    def __init__(self,guild_name) :
        self.guild_name = "not set yet"
        self.event_info = """ event information"""
        self.rules_info = """ rules information"""
        self.announcement_info = """ announcement information"""

    def event(self,message,bot:Telebot):
        bot.send_message(message.chat.id,self.event_info)

    def rules(self,message,bot:Telebot):
        bot.send_message(message.chat.id,self.rules_info)

    def announcements(self,message,bot:Telebot):
        bot.send_message(message.chat.id,self.announcement_info)