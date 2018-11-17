import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
import requests
import datetime
import re

class VKBot:
    """
    VKBot object
    """
    vk = 0
    vk_session = 0
    session = 0
    upload = 0
    long_poll = 0
    event = 0

    def __init__(self, log=None, passwd=None, token=None):
        """
        Run authorization methods.
        To choose login type enter token or your login and password.
        How to get token: https://vk.com/dev/bots_docs
        :param log: your VK.com login
        :param passwd: your VK.com passsword
        :param token: your community token
        """
        if token:
            self.vk_session = vk_api.VkApi(token=token)
        else:
            self.vk_session = vk_api.VkApi(log, passwd)
            try:
                self.vk_session.auth()
            except vk_api.AuthError as error_msg:
                print(error_msg)
                return
        self.vk = self.vk_session.get_api()
        self.session = requests.session()
        self.upload = VkUpload(self.vk_session)
        self.long_poll = VkLongPoll(self.vk_session)

    def damerau_levenshtein_distance(self, s1, s2):
       d = {}
       lenstr1 = len(s1)
       lenstr2 = len(s2)
       for i in range(-1, lenstr1 + 1):
           d[(i, -1)] = i + 1
       for j in range(-1, lenstr2 + 1):
           d[(-1, j)] = j + 1
       for i in range(lenstr1):
           for j in range(lenstr2):
               if s1[i] == s2[j]:
                   cost = 0
               else:
                   cost = 1
               d[(i, j)] = min(
                   d[(i - 1, j)] + 1,  # deletion
                   d[(i, j - 1)] + 1,  # insertion
                   d[(i - 1, j - 1)] + cost,  # substitution
               )
               if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                   d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)  # transposition
       return d[lenstr1 - 1, lenstr2 - 1]

    def unknow_message(self, message, vk):
        vk.messages.send(user_id=message.user_id, message=u"""
                Кажется, сообщение с ошибками или не относится к расписанию (команда 'Инфо' выведет список моих возможностей).
                """)

    def get_data_from_message(self, messages_with_date):
        first_months = {'ФЕВРАЛЯ':'2', 'МАРТА':'3','АПРЕЛЯ':'4','МАЯ':'5'}
        second_months = {'СЕНТРЯБРЯ':'9', 'ОКТЯБРЯ':'10','НОЯБРЯ':'11','ДЕКАБРЯ':'12'}
        for message in messages_with_date:
            match = re.search(r'\d+', message)
            match2 = re.search(r'\d+.\d+', message)
            if match2!=None:
                try:
                    date = datetime.datetime.strptime(match2.group()+'.2018', '%d.%m.%Y').date()
                    if date.month > 8 and date.month <= 12: 
                        return date
                except:
                    print('ОШИБКА1')
            elif match!=None:
                break

        for message in messages_with_date:   
            if message.upper() in second_months:
                month = second_months[message.upper()]
                try:
                    date = datetime.datetime.strptime(match.group()+'.'+month+'.'+'2018', '%d.%m.%Y').date()
                    return date
                except:
                    print('ОШИБКА2')
                break
        return False

    def __command_handler__(self, commands, handler):
        """
        Run user function if message contain a commands
        :param commands: list of command. For example ["command1", "command2", ...]
        :param handler: function, that should run if message contain a command
        """
        message_set = self.event.text.split(u' ')
        for command in commands:           
            for message in message_set:
                if handler.__name__=='on_date' and self.get_data_from_message(message_set)!=False:
                    handler(self.event, self.vk, self.get_data_from_message(message_set))
                    return 1 
                if handler.__name__=='start' and bool(re.search(r'[А-Яа-я]{4}-\d{2}-\d{2}', message)):
                    handler(self.event, self.vk)
                    return 1 
                distance = len(message)
                d = self.damerau_levenshtein_distance(message.lower(), command)
                if d < distance:
                    distance = d
                    key = command
                    if distance == 0:
                        handler(self.event, self.vk)
                        return 1
            if distance < len(message)*0.4 and message.lower() not in ["неделя", "нед", "недели"]:
                handler(self.event, self.vk)
                return 1

    def __query_manager__(self, queryset):
        """
        Sets a query of commands and handlers
        :param queryset: list of commands and hanlers. For example [["command", handler], ...]
        """
        for item in queryset:
            if (self.__command_handler__(item[0], item[1])) == 1:
                return 1


    def run(self, query):
        """
        Main bot`s cycle.
        :param query: list of commands and hanlers. For example [["command", handler], ...]
        """
        for event in self.long_poll.listen():
            if datetime.datetime.now().strftime('%H:%M:%S')=='03:45:00' and datetime.datetime.now().weekday()!=6:
                break
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                self.event = event
                if (self.__query_manager__(query))==1:
                    break
                else:
                    self.unknow_message(self.event, self.vk)

                

