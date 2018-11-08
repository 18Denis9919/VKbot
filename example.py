from bot import VKBot
from random import randint
from importlib import reload
import pymysql
import datetime
import re

conn = pymysql.connect(host='127.0.0.1', port=3307, user='root', passwd='denis', db='timetable')
cur = conn.cursor()

data_now = datetime.datetime.utcnow()

lecture_phisic = [1, 5, 9, 13]
laba_phisic = [2, 6, 10, 14]


def get_group(vk_id):
	req = cur.execute("""SELECT * FROM users WHERE vk_id = (%s)""", str(vk_id))	
	print(req)
	for el in cur:
		group = el[2]
	print(group)
	return group


def get_week(data):
	time = data.isocalendar()[1]
	time1 = datetime.datetime(2018, 9, 1).isocalendar()[1]
	week = time - time1
	return week


def create_message(request):
	mes = ''
	for row in cur:
		mes = mes + str(row[0])+' пара ('+ str(row[1]) + ', с ' + str(row[2]) + ' до ' + str(row[3]) + '): \n' + str(row[4]) + ', ' + str(row[5])+'\n\n'
	
	if mes=='':
		mes = 'Занятий нет.\n\n'

	return mes


def monday(data, vk_id):
	if get_week(data)%2!=0:
		req = cur.execute("""SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ПОНЕДЕЛЬНИК' AND Subject IS NOT NULL AND WEEK = 'I' AND Group_ID = %s""", get_group(vk_id))
	else:
		req = cur.execute("""SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ПОНЕДЕЛЬНИК' AND Subject IS NOT NULL AND WEEK = 'II' AND Group_ID = %s""", get_group(vk_id))
	message = 'Пары на понедельник (' + str(data.day) + '.' + str(data.month) + ')' + ':\n\n' + create_message(req)	
	return message



def tuesday(data, vk_id):
	if get_week(data)%2!=0:
		req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ВТОРНИК' AND Subject IS NOT NULL AND WEEK = 'I' AND Group_ID = %s", get_group(vk_id))
	else:
		req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ВТОРНИК' AND Subject IS NOT NULL AND WEEK = 'II' AND Group_ID = %s", get_group(vk_id))
	message = 'Пары на вторник (' + str(data.day) + '.' + str(data.month) + ')' + ':\n\n' + create_message(req)	
	return message

def wednesday(data, vk_id):
	if get_week(data)%2!=0:
		req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='СРЕДА' AND Subject IS NOT NULL AND WEEK = 'I' AND Group_ID = %s", get_group(vk_id))
	else:
		req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='СРЕДА' AND Subject IS NOT NULL AND WEEK = 'II' AND Group_ID = %s", get_group(vk_id))
	message = 'Пары на среду (' + str(data.day) + '.' + str(data.month) + ')' + ':\n\n' + create_message(req)	
	return message	

def thursday(data, vk_id):
	if get_week(data)%2!=0:
		req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ЧЕТВЕРГ' AND Subject IS NOT NULL AND WEEK = 'I' AND Group_ID = %s", get_group(vk_id))
	else:
		req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ЧЕТВЕРГ' AND Subject IS NOT NULL AND WEEK = 'II' AND Group_ID = %s", get_group(vk_id))
	message = 'Пары на четверг (' + str(data.day) + '.' + str(data.month) + ')' + ':\n\n' + create_message(req)	
	return message

def friday(data, vk_id):
	if get_week(data)%2!=0:
		req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ПЯТНИЦА' AND Subject IS NOT NULL AND WEEK = 'I' AND Group_ID = %s", get_group(vk_id))
	else:
		req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ПЯТНИЦА' AND Subject IS NOT NULL AND WEEK = 'II' AND Group_ID = %s", get_group(vk_id))
	message = 'Пары на пятницу (' + str(data.day) + '.' + str(data.month) + ')' + ':\n\n' + create_message(req)	
	return message

def saturday(data, vk_id):
	if get_week(data)%2!=0:
		if get_week(data) in lecture_phisic:
			req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='СУББОТА' AND Subject IS NOT NULL AND WEEK = 'I' AND Group_ID = %s", get_group(vk_id))
		else:
			req = []
	else:
		if get_week(data) not in laba_phisic:
			req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='СУББОТА' AND Subject IS NOT NULL AND WEEK = 'II' AND Type_lesson = 'пр' AND Group_ID = %s", get_group(vk_id))
		else:
			req = cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='СУББОТА' AND Subject IS NOT NULL AND WEEK = 'II' AND Group_ID = %s", get_group(vk_id))
	message = 'Пары на субботу (' + str(data.day) + '.' + str(data.month) + ')' + ':\n\n' + create_message(req)	
	return message

def send_monday(message, vk):
	vk.messages.send(user_id=message.user_id, message=monday(data_now, str(message.user_id)))

def send_tuesday(message, vk):
	vk.messages.send(user_id=message.user_id, message=tuesday(data_now, str(message.user_id)))

def send_wednesday(message, vk):
	vk.messages.send(user_id=message.user_id, message=wednesday(data_now, str(message.user_id)))

def send_thursday(message, vk):
	vk.messages.send(user_id=message.user_id, message=thursday(data_now, str(message.user_id)))

def send_friday(message, vk):
	vk.messages.send(user_id=message.user_id, message=friday(data_now, str(message.user_id)))

def send_saturday(message, vk):
	vk.messages.send(user_id=message.user_id, message=saturday(data_now, str(message.user_id)))


def get_weekday(day, vk_id):
	if day.weekday()==0:
		return monday(day, vk_id)
	elif day.weekday()==1:
		return tuesday(day, vk_id)
	elif day.weekday()==2:
		return wednesday(day, vk_id)
	elif day.weekday()==3:
		return thursday(day, vk_id)
	elif day.weekday()==4:
		return friday(day, vk_id)
	elif day.weekday()==5:
		return saturday(day, vk_id)
	else:
		mes_sun = 'В воскресенье выходной день!'
		return mes_sun

def today(message, vk):
	# get_weekday(datetime.datetime.today())
	vk.messages.send(user_id=message.user_id, message=get_weekday(datetime.datetime.today(), str(message.user_id)))

def tomorow(message, vk):
	# data = datetime.datetime.today()+datetime.timedelta(days=1)
	vk.messages.send(user_id=message.user_id, message=get_weekday(datetime.datetime.today()+datetime.timedelta(days=1), str(message.user_id)))

def for_week(message, vk):
	data = datetime.datetime.today()
	mes_week = '_________________________\n\n'
	for i in range(7):
		if get_weekday(data, str(message.user_id))!='В воскресенье выходной день!':
			mes_week += get_weekday(data, str(message.user_id))  + '_________________________\n\n'
		data = data + datetime.timedelta(days=1) 
	vk.messages.send(user_id=message.user_id, message=mes_week)


def week(message, vk):
	vk.messages.send(user_id=message.user_id, message='Сейчас ' + str(get_week(data_now)) + ' неделя.')


def start(message, vk):
    vk.messages.send(user_id=message.user_id, message=u"Начнем, пожалуй")

def random_habrahabr(message, vk):
    vk.messages.send(user_id=message.user_id, message=u'https://habrahabr.ru/post/' + str(randint(100, 200000)) + u'/')

def test(message, vk):
	vk.messages.send(user_id=message.user_id, message=u"Работает")

def hello(message, vk):
	vk.messages.send(user_id=message.user_id, message=u'Тебя нет в базе, введи свою группу')


def start(message, vk):
	vk_id = message.user_id
	group = message.text
	try:
		cur.execute("""INSERT INTO users VALUES (NULL, %s, %s)""", ( vk_id, group))
		conn.commit()
		vk.messages.send(user_id=message.user_id, message=u'Я добавил тебя в базу, можешь приступать к работе!')
	except:	
		conn.rollback()
		vk.messages.send(user_id=message.user_id, message=u'Упс, что то пошло не так!')

		# vk.messages.send(user_id=message.user_id, message=u'Я добавил тебя в базу, можешь приступать к работе!')

def delete_user(message, vk):
	vk_id = message.user_id
	try:
		cur.execute("""DELETE FROM users WHERE vk_id = (%s)""", str(message.user_id))
		conn.commit()
		vk.messages.send(user_id=message.user_id, message=u'Смена группы произошла успешно!')
	except:	
		conn.rollback()
		vk.messages.send(user_id=message.user_id, message=u'Упс, что то пошло не так!')







if __name__ == '__main__':
	bot = VKBot(token='')
	user_id = bot.get_user_id()
	while True:
		req = cur.execute("""SELECT vk_id FROM users WHERE vk_id = (%s)""", str(user_id))
		if req==1:
			for el in cur:
				user_id_db = el[0]
		else:
			user_id_db = 0		
		if int(user_id_db) == user_id:
			queryset = [
			[[u"Погнали", u"погнали", u"лол", u"Лол"], start], 
			[[u"Хабрахабр", ], random_habrahabr],
			[[u"Понедельник", "пн","понедельник",], send_monday],
			[[u"Вторник", "вт", "вторник",], send_tuesday],
			[[u"Среда", "ср", "среда", "среду", "Среду",], send_wednesday],
			[[u"Четверг", "чт", "четверг",], send_thursday],
			[[u"Пятница", "пт", "пятницу", "пятница", "Пятинцу",], send_friday],
			[[u"Суббота", "суб", "суббота", "Субботу", "субботу",], send_saturday],
			[[u"Сегодня", "сегодня",], today],
			[[u"Завтра", "завтра"], tomorow],
			[[u"Неделю", "неделю"], for_week],
			[[u"Сменить",], delete_user],
			[[r"[A-Z]{1}[a-z]{1}", r'\d+/\d+/\d+', r"1\s"], test],
			[[u"Неделя", "неделя", "нед"], week],
			[[u""], week]
			]
		else:
			queryset = [
			[[u'Привет',], hello],
			[[u'БББО-02-17', 'БББО-01-17'], start]
			]
		bot.run(query=queryset)
	cur.close()
	conn.close()


