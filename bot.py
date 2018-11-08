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

    def __command_handler__(self, commands, handler):
        """
        Run user function if message contain a commands
        :param commands: list of command. For example ["command1", "command2", ...]
        :param handler: function, that should run if message contain a command
        """
        message_set = self.event.text.split(u' ')
        for command in commands:
            # print(re.search(r'(\d+/\d+/\d+)', command))
            if command in message_set:
                handler(self.event, self.vk)
                break

    def __query_manager__(self, queryset):
        """
        Sets a query of commands and handlers
        :param queryset: list of commands and hanlers. For example [["command", handler], ...]
        """
        for item in queryset:
            self.__command_handler__(item[0], item[1])

    def run(self, query):
        """
        Main bot`s cycle.
        :param query: list of commands and hanlers. For example [["command", handler], ...]
        """
        for event in self.long_poll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                self.event = event
                self.__query_manager__(query)
                break

    def get_user_id(self):
        for event in self.long_poll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                return event.user_id

