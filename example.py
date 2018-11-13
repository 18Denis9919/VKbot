## -*- coding: utf-8 -*-
from bot import VKBot
from random import randint
from importlib import reload
import pymysql
import datetime
import re
import postgresql
import psycopg2
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
# conn = pymysql.connect(host='127.0.0.1', port=3307, user='root', passwd='denis', db='timetable')
# cur = conn.cursor()
conn = psycopg2.connect("host='ec2-50-19-127-158.compute-1.amazonaws.com' dbname='da3vvps6qv9fpc' user='cgbvbzntdxveul' password='f5fdf70c6d5fe8fed9dc9e0ff1430ea6e99f18ef27896797401db2f6b5f7f47e'")
cur = conn.cursor()

lecture_phisic = [1, 5, 9, 13]
laba_phisic = [2, 6, 10, 14]


def get_group(vk_id):
	req = cur.execute("""SELECT * FROM users WHERE vk_id = '{0}'""".format(str(vk_id)))
	for el in cur:
		group = el[2]
	return group


def get_week(data):
	time = data.isocalendar()[1]
	time1 = datetime.datetime(2018, 9, 1).isocalendar()[1]
	week = time - time1
	return week


def create_message(request, data):
	mes = ''
	for row in request:
		if str(get_week(data)) in row[4]:
			mes = mes + str(row[0])+' пара ('+ str(row[1]) + ', с ' + str(row[2]) + ' до ' + str(row[3]) + '): \n' + str(row[4]) + ', ' + str(row[5])+'\n\n'
		elif not bool(re.search(r'\d', row[4])):
			mes = mes + str(row[0])+' пара ('+ str(row[1]) + ', с ' + str(row[2]) + ' до ' + str(row[3]) + '): \n' + str(row[4]) + ', ' + str(row[5])+'\n\n'
	
	if mes=='':
		mes = 'Занятий нет.\n\n'

	return mes


def monday(data, vk_id, mes_date=''):
	if get_week(data)%2!=0:
		cur.execute("""SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ПОНЕДЕЛЬНИК' AND Subject IS NOT NULL AND WEEK = 'I' AND Group_ID = '{0}'""".format(get_group(vk_id)))
		# cur.execute(u"""SELECT Class FROM time_table WHERE Group_ID != '????-02-17'""")
	else:
		cur.execute("""SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ПОНЕДЕЛЬНИК' AND Subject IS NOT NULL AND WEEK = 'II' AND Group_ID = '{0}'""".format(get_group(vk_id)))
	message = 'Пары на понедельник ' + mes_date + ':\n\n' + create_message(cur, data)	
	return message



def tuesday(data, vk_id, mes_date=''):
	if get_week(data)%2!=0:
		cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ВТОРНИК' AND Subject IS NOT NULL AND WEEK = 'I' AND Group_ID = '{0}'".format(get_group(vk_id)))
	else:
		cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ВТОРНИК' AND Subject IS NOT NULL AND WEEK = 'II' AND Group_ID = '{0}'".format(get_group(vk_id)))
	message = 'Пары на вторник ' + mes_date + ':\n\n' + create_message(cur, data)	
	return message

def wednesday(data, vk_id, mes_date=''):
	if get_week(data)%2!=0:
		cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='СРЕДА' AND Subject IS NOT NULL AND WEEK = 'I' AND Group_ID = '{0}'".format(get_group(vk_id)))
	else:
		cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='СРЕДА' AND Subject IS NOT NULL AND WEEK = 'II' AND Group_ID = '{0}'".format(get_group(vk_id)))
	message = 'Пары на среду ' + mes_date + ':\n\n' + create_message(cur, data)	
	return message	

def thursday(data, vk_id, mes_date=''):
	if get_week(data)%2!=0:
		cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ЧЕТВЕРГ' AND Subject IS NOT NULL AND WEEK = 'I' AND Group_ID = '{0}'".format(get_group(vk_id)))
	else:
		cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ЧЕТВЕРГ' AND Subject IS NOT NULL AND WEEK = 'II' AND Group_ID = '{0}'".format(get_group(vk_id)))
	message = 'Пары на четверг ' + mes_date + ':\n\n' + create_message(cur, data)	
	return message

def friday(data, vk_id, mes_date=''):
	if get_week(data)%2!=0:
		cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ПЯТНИЦА' AND Subject IS NOT NULL AND WEEK = 'I' AND Group_ID = '{0}'".format(get_group(vk_id)))
	else:
		cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ПЯТНИЦА' AND Subject IS NOT NULL AND WEEK = 'II' AND Group_ID = '{0}'".format(get_group(vk_id)))
	message = 'Пары на пятницу ' + mes_date + ':\n\n' + create_message(cur, data)	
	return message

def saturday(data, vk_id, mes_date=''):
	if get_week(data)%2!=0:
		cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='СУББОТА' AND Subject IS NOT NULL AND WEEK = 'I' AND Group_ID = '{0}'".format(get_group(vk_id)))
	else:
		cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='СУББОТА' AND Subject IS NOT NULL AND WEEK = 'II' AND Group_ID = '{0}'".format(get_group(vk_id)))
	message = 'Пары на субботу ' + mes_date + ':\n\n' + create_message(cur, data)	
	return message

def send_monday(message, vk, correct_mes=''):
	vk.messages.send(user_id=message.user_id, message=correct_mes + monday(datetime.datetime.utcnow(), message.user_id))

def send_tuesday(message, vk, correct_mes=''):
	vk.messages.send(user_id=message.user_id, message=correct_mes + tuesday(datetime.datetime.utcnow(), message.user_id))

def send_wednesday(message, vk, correct_mes=''):
	vk.messages.send(user_id=message.user_id, message=correct_mes + wednesday(datetime.datetime.utcnow(), message.user_id))

def send_thursday(message, vk, correct_mes=''):
	vk.messages.send(user_id=message.user_id, message=correct_mes + thursday(datetime.datetime.utcnow(), message.user_id))

def send_friday(message, vk, correct_mes=''):
	vk.messages.send(user_id=message.user_id, message=correct_mes + friday(datetime.datetime.utcnow(), message.user_id))

def send_saturday(message, vk, correct_mes=''):
	vk.messages.send(user_id=message.user_id, message=correct_mes + saturday(datetime.datetime.utcnow(), message.user_id))


def get_weekday(day, mes_date, vk_id):
	if day.weekday()==0:
		return monday(day, vk_id, mes_date)
	elif day.weekday()==1:
		return tuesday(day, vk_id, mes_date)
	elif day.weekday()==2:
		return wednesday(day, vk_id, mes_date)
	elif day.weekday()==3:
		return thursday(day, vk_id, mes_date)
	elif day.weekday()==4:
		return friday(day, vk_id, mes_date)
	elif day.weekday()==5:
		return saturday(day, vk_id, mes_date)
	else:
		mes_sun = 'В воскресенье выходной день!'
		return mes_sun

def on_date(message, vk, date):
	mes_date = '(' + str(date.day) + '.' + str(date.month) + ')'
	vk.messages.send(user_id=message.user_id, message=get_weekday(date, mes_date,message.user_id))

def today(message, vk, correct_mes=''):
	mes_date = '(' + str(datetime.datetime.today().day) + '.' + str(datetime.datetime.today().month) + ')'
	vk.messages.send(user_id=message.user_id, message=correct_mes + get_weekday(datetime.datetime.today(), mes_date, message.user_id))

def tomorow(message, vk, correct_mes=''):
	date = datetime.datetime.today()+datetime.timedelta(days=1)
	mes_date = '(' + str(date.day) + '.' + str(date.month) + ')'
	vk.messages.send(user_id=message.user_id, message=correct_mes + get_weekday(date, mes_date, message.user_id))

def for_week(message, vk, correct_mes=''):
	data = datetime.datetime.today()
	mes_week = 'Пары на неделю:\n_________________________\n\n'
	for i in range(7):
		mes_date = '(' + str(data.day) + '.' + str(data.month) + ')'
		if get_weekday(data, mes_date, message.user_id)!='В воскресенье выходной день!':
			mes_week += get_weekday(data, mes_date, message.user_id)  + '_________________________\n\n'
		data = data + datetime.timedelta(days=1) 
	vk.messages.send(user_id=message.user_id, message=correct_mes + mes_week)


def week(message, vk, correct_mes=''):
	vk.messages.send(user_id=message.user_id, message=correct_mes + 'Сейчас ' + str(get_week(datetime.datetime.utcnow())) + ' неделя.')

def teachers(message, vk, correct_mes=''):
	req = cur.execute("SELECT DISTINCT Teachers FROM time_table WHERE Group_ID = '{0}' AND Teachers IS NOT NULL".format(get_group(message.user_id)))
	teacher_list = ''
	for row in cur:
		teacher_list += row[0] + '\n'
	vk.messages.send(user_id=message.user_id, message=correct_mes + teacher_list)

def test(message, vk, correct_mes=''):
	vk.messages.send(user_id=message.user_id, message=correct_mes + u"Работает")

def hello(message, vk, correct_mes=''):
	vk.messages.send(user_id=message.user_id, message=correct_mes + u'Тебя нет в базе, введи свою группу!\n Группы, которые поддреживает бот:\n БББО-01-17\nБББО-02-17 ')

def list_comand(message, vk, correct_mes=''):
	list_message = '''Вот что я умею:
		-Выводить расписание на определенный день недели
		-Выводить расписание на сегодня и завтра
		-Выводить расписание на всю неделю
		-Выводить номер недели
		-Выводить список преподавателей
		________________________________________________

		Для того чтобы посмотореть расписание другой группы напиши мне "Сменить" и затем введи нужную тебе группу!

	'''
	vk.messages.send(user_id=message.user_id, message=correct_mes + list_message)

def start(message, vk, correct_mes=''):
	vk_id = message.user_id
	group = message.text
	try:
		cur.execute(u"""INSERT INTO users (vk_id, group_id) VALUES ('{0}', '{1}') ON CONFLICT DO NOTHING""".format(str(vk_id), group))
		conn.commit()
		vk.messages.send(user_id=message.user_id, message=correct_mes + u'Я добавил тебя в базу, можешь приступать к работе!')
		list_comand(message, vk)
	except:	
		conn.rollback()
		vk.messages.send(user_id=message.user_id, message=correct_mes + u'Упс, что то пошло не так!')


def delete_user(message, vk, correct_mes=''):
	vk_id = message.user_id
	try:
		cur.execute("""DELETE FROM users WHERE vk_id = '{0}'""".format(str(message.user_id)))
		conn.commit()
		vk.messages.send(user_id=message.user_id, message=correct_mes + u'Смена группы произошла успешно!')
		hello(message, vk)
	except:	
		conn.rollback()
		vk.messages.send(user_id=message.user_id, message=correct_mes + u'Упс, что то пошло не так!')

if __name__ == '__main__':
	bot = VKBot(token='ad2782d4222562577747d80a4e616f6e8f9d566dfe73ca2e67656b3e2537e57c770fbce7bcc61073d86b5')
	bot.get_user_id()
	user_id = bot.vk_id
	while True:
		# user_id = bot.vk_id
		cur.execute("""SELECT vk_id, group_id FROM users WHERE vk_id = '{0}'""".format(str(user_id)))

		user_id_db = 1
		for el in cur:
			user_id_db = el[0]	
		if int(user_id_db) == user_id:
			queryset = [
			[[u"Понедельник", "пн","понедельник",], send_monday],
			[[u"Вторник", "вт", "вторник",], send_tuesday],
			[[u"Среда", "ср", "среда", "среду", "Среду",], send_wednesday],
			[[u"Четверг", "чт", "четверг",], send_thursday],
			[[u"Пятница", "пт", "пятницу", "пятница", "Пятинцу",], send_friday],
			[[u"Суббота", "суб", "суббота", "Субботу", "субботу", "сб",], send_saturday],
			[[u"Сегодня", "сегодня",], today],
			[[u"Завтра", "завтра"], tomorow],
			[[u"Неделю", "неделю"], for_week],
			[[u"Сменить",], delete_user],
			[[r"[A-Z]{1}[a-z]{1}", r'\d+/\d+/\d+', r"1\s"], test],
			[[u"Неделя", "неделя", "нед"], week],
			[[u"преподы",], teachers],
			[[u"info","Инфо","инфо","команды", "Комнадны"], list_comand],
			[['1'], on_date]
			]
		else:
			queryset = [
			[[u'Привет',], hello],
			[[u'БББО-02-17', 'БББО-01-17'], start]
			]
		bot.run(query=queryset)
	cur.close()
	conn.close()


# 5432