# from bot import VKBot
# from random import randint
# from importlib import reload
# import pymysql
# import datetime

# conn = pymysql.connect(host='127.0.0.1', port=3307, user='root', passwd='denis', db='timetable')

# cur = conn.cursor()

# lecture_phisic = [1, 5, 9, 13]
# laba_phisic = [2, 6, 10, 14]

# def get_week(data):
# 	time = data.isocalendar()[1]
# 	time1 = datetime.datetime(2018, 9, 1).isocalendar()[1]
# 	week = time - time1
# 	return week


# def create_message(request):
# 	mes = ''
# 	for row in cur:
# 		mes = mes + str(row[0])+' пара ('+ str(row[1]) + ', с ' + str(row[2]) + ' до ' + str(row[3]) + '): \n' + str(row[4]) + ', ' + str(row[5])+'\n\n'
	
# 	if mes=='':
# 		mes = 'Занятий нет.'

# 	return mes

# def monday(message, vk, data):
# 	if get_week(data)%2!=0:
# 		req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM bbbo02 WHERE Day_of_week='ПОНЕДЕЛЬНИК' AND Subject IS NOT NULL AND WEEK = 'I'")
# 		vk.messages.send(user_id=message.user_id, message='Пары на понедельник:\n\n' + create_message(req))
# 	else:
# 		req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM bbbo02 WHERE Day_of_week='ПОНЕДЕЛЬНИК' AND Subject IS NOT NULL AND WEEK = 'II'")
# 		vk.messages.send(user_id=message.user_id, message='Пары на понедельник:\n\n' + create_message(req))

# def tuesday(message, vk, data):
# 	if get_week(data)%2!=0:
# 		req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM bbbo02 WHERE Day_of_week='ВТОРНИК' AND Subject IS NOT NULL AND WEEK = 'I'")
# 		vk.messages.send(user_id=message.user_id, message='Пары на вторник:\n\n' + create_message(req))
# 	else:
# 		req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM bbbo02 WHERE Day_of_week='ВТОРНИК' AND Subject IS NOT NULL AND WEEK = 'II'")
# 		vk.messages.send(user_id=message.user_id, message='Пары на вторник:\n\n' + create_message(req))

# def wednesday(message, vk, data):
# 	if get_week(data)%2!=0:
# 		req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM bbbo02 WHERE Day_of_week='СРЕДА' AND Subject IS NOT NULL AND WEEK = 'I'")
# 		vk.messages.send(user_id=message.user_id, message='Пары на среду:\n\n' + create_message(req))
# 	else:
# 		req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM bbbo02 WHERE Day_of_week='СРЕДА' AND Subject IS NOT NULL AND WEEK = 'II'")
# 		vk.messages.send(user_id=message.user_id, message='Пары на среду:\n\n' + create_message(req))

# def thursday(message, vk, data):
# 	if get_week(data)%2!=0:
# 		req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM bbbo02 WHERE Day_of_week='ЧЕТВЕРГ' AND Subject IS NOT NULL AND WEEK = 'I'")
# 		vk.messages.send(user_id=message.user_id, message='Пары на четверг:\n\n' + create_message(req))
# 	else:
# 		req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM bbbo02 WHERE Day_of_week='ЧЕТВЕРГ' AND Subject IS NOT NULL AND WEEK = 'II'")
# 		vk.messages.send(user_id=message.user_id, message='Пары на четверг:\n\n' + create_message(req))

# def friday(message, vk, data):
# 	if get_week(data)%2!=0:
# 		req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM bbbo02 WHERE Day_of_week='ПЯТНИЦА' AND Subject IS NOT NULL AND WEEK = 'I'")
# 		vk.messages.send(user_id=message.user_id, message='Пары на пятницу:\n\n' + create_message(req))
# 	else:
# 		req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM bbbo02 WHERE Day_of_week='ПЯТНИЦА' AND Subject IS NOT NULL AND WEEK = 'II'")
# 		vk.messages.send(user_id=message.user_id, message='Пары на пятницу:\n\n' + create_message(req))

# def saturday(message, vk, data):
# 	if get_week(data)%2!=0:
# 		if get_week(data) in lecture_phisic:
# 			req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM bbbo02 WHERE Day_of_week='СУББОТА' AND Subject IS NOT NULL AND WEEK = 'I'")
# 		else:
# 			req = []
# 		vk.messages.send(user_id=message.user_id, message='Пары на субботу:\n\n' + create_message(req))
# 	else:
# 		if get_week(data) not in laba_phisic:
# 			req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM bbbo02 WHERE Day_of_week='СУББОТА' AND Subject IS NOT NULL AND WEEK = 'II' AND Type_lesson = 'пр'")
# 		else:
# 			req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM bbbo02 WHERE Day_of_week='СУББОТА' AND Subject IS NOT NULL AND WEEK = 'II'")
# 		vk.messages.send(user_id=message.user_id, message='Пары на субботу:\n\n' + create_message(req))


# def get_weekday(message, vk, day):
# 	if day.weekday()==0:
# 		tuesday(monday, vk, day)
# 	elif day.weekday()==1:
# 		tuesday(message, vk, day)
# 	elif day.weekday()==2:
# 		wednesday(message, vk, day)

# 	elif day.weekday()==3:
# 		thursday(message, vk, day)
# 	elif day.weekday()==4:
# 		friday(message, vk, day)
# 	elif day.weekday()==5:
# 		saturday(message, vk, day)
# 	vk.messages.send(user_id=message.user_id, message='Пары на XZ:\n\n' + message)

# def today(message, vk, data):
# 	get_weekday(message, vk, datetime.datetime.today())

# def tomorow(message, vk, data):
# 	data = datetime.datetime.today()+datetime.timedelta(days=1)
# 	get_weekday(message, vk, data)

# def for_week(message, vk, data):
# 	print('OKEY')
# 	for i in range(7):
# 		print(i)
# 		get_weekday(message, vk, data)
# 		data = data + datetime.timedelta(days=1) 


# def week(message, vk, data):
# 	vk.messages.send(user_id=message.user_id, message='Сейчас ' + str(get_week(data)) + ' неделя.')


# def start(message, vk, data):
#     vk.messages.send(user_id=message.user_id, message=u"Начнем, пожалуй")

# def random_habrahabr(message, vk, data):
#     vk.messages.send(user_id=message.user_id, message=u'https://habrahabr.ru/post/' + str(randint(100, 200000)) + u'/')

# if __name__ == '__main__':
#     queryset = [
#     [[u"Погнали", u"погнали", u"лол", u"Лол"], start], 
#     [[u"Хабрахабр", ], random_habrahabr],
#     [[u"Понедельник",], monday],
#     [[u"Вторник",], tuesday],
#     [[u"Среда",], wednesday],
#     [[u"Четверг",], thursday],
#     [[u"Пятница",], friday],
#     [[u"Суббота",], saturday],
#     [[u"Сегодня",], today],
#     [[u"Завтра",], tomorow],
#     [[u"Расписаниенанеделю",], for_week],
#     [[u"Неделя",], week]
#     ]
#     bot = VKBot(token='ad2782d4222562577747d80a4e616f6e8f9d566dfe73ca2e67656b3e2537e57c770fbce7bcc61073d86b5')
#     bot.run(query=queryset)
#     cur.close()
#     conn.close()


# # bot = VKBot(token='ad2782d4222562577747d80a4e616f6e8f9d566dfe73ca2e67656b3e2537e57c770fbce7bcc61073d86b5')

# # for event in bot.long_poll.listen():

# #     if event.type == VkEventType.MESSAGE_NEW:
# #         print('Новое сообщение:')

# #         if event.from_me:
# #             print('От меня для: ', end='')
# #         elif event.to_me:
# #             print('Для меня от: ', end='')

# #         if event.from_user:
# #             print(event.user_id)
# #         elif event.from_chat:
# #             print(event.user_id, 'в беседе', event.chat_id)
# #         elif event.from_group:
# #             print('группы', event.group_id)

# #         print('Текст: ', event.text)
# #         print()

# #     elif event.type == VkEventType.USER_TYPING:
# #         print('Печатает ', end='')

# #         if event.from_user:
# #             print(event.user_id)
# #         elif event.from_group:
# #             print('администратор группы', event.group_id)

# #     elif event.type == VkEventType.USER_TYPING_IN_CHAT:
# #         print('Печатает ', event.user_id, 'в беседе', event.chat_id)

# #     elif event.type == VkEventType.USER_ONLINE:
# #         print('Пользователь', event.user_id, 'онлайн', event.platform)

# #     elif event.type == VkEventType.USER_OFFLINE:
# #         print('Пользователь', event.user_id, 'оффлайн', event.offline_type)

# #     else:
# #         print(event.type, event.raw[1:])