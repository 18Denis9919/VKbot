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

conn = psycopg2.connect("host='ec2-50-19-127-158.compute-1.amazonaws.com' dbname='da3vvps6qv9fpc' user='cgbvbzntdxveul' password='f5fdf70c6d5fe8fed9dc9e0ff1430ea6e99f18ef27896797401db2f6b5f7f47e'")
cur = conn.cursor()


def get_group(vk_id):
	req = cur.execute("""SELECT * FROM users WHERE vk_id = '{0}'""".format(str(vk_id)))
	group = 0
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
		if (str(get_week(data)) in row[4]) or ('кр.' in row[4]) or (not bool(re.search(r'\d', row[4]))):
			mes = mes + str(row[0])+' пара ('+ str(row[1]) + ', ' + str(row[2]).replace('-', ':') + '-' + str(row[3]).replace('-', ':') + '): \n' + str(row[4]) + ', ' + str(row[5])+'\n\n'
	
	if mes=='':
		mes = 'Занятий нет.\n\n'

	return mes


def monday(data, vk_id, mes_date=''):
	if get_group(vk_id)!=0:
		if get_week(data)%2!=0:
			cur.execute("""SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ПОНЕДЕЛЬНИК' AND Subject IS NOT NULL AND WEEK = 'I' AND Group_ID = '{0}'""".format(get_group(vk_id)))
		else:
			cur.execute("""SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ПОНЕДЕЛЬНИК' AND Subject IS NOT NULL AND WEEK = 'II' AND Group_ID = '{0}'""".format(get_group(vk_id)))
		message = 'Пары на понедельник ' + mes_date + ':\n\n' + create_message(cur, data)
	else:
		message = 'Тебя нет в базе, введи свою группу!\n Группы, которые поддреживает бот:\nБББО-01-17 \nБББО-02-17'	
	return message



def tuesday(data, vk_id, mes_date=''):
	if get_group(vk_id)!=0:
		if get_week(data)%2!=0:
			cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ВТОРНИК' AND Subject IS NOT NULL AND WEEK = 'I' AND Group_ID = '{0}'".format(get_group(vk_id)))
		else:
			cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ВТОРНИК' AND Subject IS NOT NULL AND WEEK = 'II' AND Group_ID = '{0}'".format(get_group(vk_id)))
		message = 'Пары на вторник ' + mes_date + ':\n\n' + create_message(cur, data)	
	else:
		message = 'Тебя нет в базе, введи свою группу!\n Группы, которые поддреживает бот:\nБББО-01-17 \nБББО-02-17'	
	return message

def wednesday(data, vk_id, mes_date=''):
	if get_group(vk_id)!=0:
		if get_week(data)%2!=0:
			cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='СРЕДА' AND Subject IS NOT NULL AND WEEK = 'I' AND Group_ID = '{0}'".format(get_group(vk_id)))
		else:
			cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='СРЕДА' AND Subject IS NOT NULL AND WEEK = 'II' AND Group_ID = '{0}'".format(get_group(vk_id)))
		message = 'Пары на среду ' + mes_date + ':\n\n' + create_message(cur, data)	
	else:
		message = 'Тебя нет в базе, введи свою группу!\n Группы, которые поддреживает бот:\nБББО-01-17 \nБББО-02-17'	
	return message	

def thursday(data, vk_id, mes_date=''):
	if get_group(vk_id)!=0:
		if get_week(data)%2!=0:
			cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ЧЕТВЕРГ' AND Subject IS NOT NULL AND WEEK = 'I' AND Group_ID = '{0}'".format(get_group(vk_id)))
		else:
			cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ЧЕТВЕРГ' AND Subject IS NOT NULL AND WEEK = 'II' AND Group_ID = '{0}'".format(get_group(vk_id)))
		message = 'Пары на четверг ' + mes_date + ':\n\n' + create_message(cur, data)	
	else:
		message = 'Тебя нет в базе, введи свою группу!\n Группы, которые поддреживает бот:\nБББО-01-17 \nБББО-02-17'	
	return message

def friday(data, vk_id, mes_date=''):
	if get_group(vk_id)!=0:
		if get_week(data)%2!=0:
			cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ПЯТНИЦА' AND Subject IS NOT NULL AND WEEK = 'I' AND Group_ID = '{0}'".format(get_group(vk_id)))
		else:
			cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='ПЯТНИЦА' AND Subject IS NOT NULL AND WEEK = 'II' AND Group_ID = '{0}'".format(get_group(vk_id)))
		message = 'Пары на пятницу ' + mes_date + ':\n\n' + create_message(cur, data)	
	else:
		message = 'Тебя нет в базе, введи свою группу!\n Группы, которые поддреживает бот:\nБББО-01-17 \nБББО-02-17'	
	return message

def saturday(data, vk_id, mes_date=''):
	if get_group(vk_id)!=0:
		if get_week(data)%2!=0:
			cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='СУББОТА' AND Subject IS NOT NULL AND WEEK = 'I' AND Group_ID = '{0}'".format(get_group(vk_id)))
		else:
			cur.execute("SELECT Number_lesson, Class, Start_lesson, End_lesson, Subject, Type_lesson  FROM time_table WHERE Day_of_week='СУББОТА' AND Subject IS NOT NULL AND WEEK = 'II' AND Group_ID = '{0}'".format(get_group(vk_id)))
		message = 'Пары на субботу ' + mes_date + ':\n\n' + create_message(cur, data)	
	else:
		message = 'Тебя нет в базе, введи свою группу!\n Группы, которые поддреживает бот:\nБББО-01-17 \nБББО-02-17'	
	return message

def send_monday(message, vk):
	vk.messages.send(user_id=message.user_id, message= monday(datetime.datetime.utcnow(), message.user_id))

def send_tuesday(message, vk):
	vk.messages.send(user_id=message.user_id, message=tuesday(datetime.datetime.utcnow(), message.user_id))

def send_wednesday(message, vk):
	vk.messages.send(user_id=message.user_id, message= wednesday(datetime.datetime.utcnow(), message.user_id))

def send_thursday(message, vk):
	vk.messages.send(user_id=message.user_id, message= thursday(datetime.datetime.utcnow(), message.user_id))

def send_friday(message, vk):
	vk.messages.send(user_id=message.user_id, message= friday(datetime.datetime.utcnow(), message.user_id))

def send_saturday(message, vk):
	vk.messages.send(user_id=message.user_id, message= saturday(datetime.datetime.utcnow(), message.user_id))


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

def today(message, vk):
	mes_date = '(' + str(datetime.datetime.today().day) + '.' + str(datetime.datetime.today().month) + ')'
	vk.messages.send(user_id=message.user_id, message=get_weekday(datetime.datetime.today(), mes_date, message.user_id))

def tomorow(message, vk):
	date = datetime.datetime.today()+datetime.timedelta(days=1)
	mes_date = '(' + str(date.day) + '.' + str(date.month) + ')'
	vk.messages.send(user_id=message.user_id, message=get_weekday(date, mes_date, message.user_id))

def for_week(message, vk):
	if get_group(message.user_id)!=0:
		data = datetime.datetime.today()
		mes_week = 'Пары на неделю:\n_________________________\n\n'
		for i in range(7):
			mes_date = '(' + str(data.day) + '.' + str(data.month) + ')'
			if get_weekday(data, mes_date, message.user_id)!='В воскресенье выходной день!':
				mes_week += get_weekday(data, mes_date, message.user_id)  + '_________________________\n\n'
			data = data + datetime.timedelta(days=1) 
	else:
		mes_date = 'Тебя нет в базе, введи свою группу!\n Группы, которые поддреживает бот:\nБББО-01-17 \nБББО-02-17'
	vk.messages.send(user_id=message.user_id, message=mes_week)


def week(message, vk):
	if get_group(message.user_id)!=0:
		num_week = str(get_week(datetime.datetime.utcnow()))
	else:
		num_week = 'Тебя нет в базе, введи свою группу!\n Группы, которые поддреживает бот:\nБББО-01-17 \nБББО-02-17'
	vk.messages.send(user_id=message.user_id, message='Сейчас ' + num_week + ' неделя.')

def teachers(message, vk):
	if get_group(message.user_id)!=0:
		req = cur.execute("SELECT DISTINCT Teachers FROM time_table WHERE Group_ID = '{0}' AND Teachers IS NOT NULL".format(get_group(message.user_id)))
		teacher_list = ''
		for row in cur:
			teacher_list += row[0] + '\n'
	else:
		teacher_list = 'Тебя нет в базе, введи свою группу!\n Группы, которые поддреживает бот:\nБББО-01-17 \nБББО-02-17'
	vk.messages.send(user_id=message.user_id, message=teacher_list)



def list_comand(message, vk):
	if get_group(message.user_id)!=0:
		list_message = '''Вот что я умею:
			- Выводить расписание на определенный день недели
			- Выводить расписание на сегодня 
			- Выводить расписание на завтра
			- Выводить расписание на всю неделю
			- Выводить расписание на определенную дату
			- Выводить номер недели
			- Выводить список преподавателей
			________________________________________________

			Для того чтобы посмотореть расписание другой группы напиши мне "Сменить"!
		'''
	else:
		list_message = 'Тебя нет в базе, введи свою группу!\n Группы, которые поддреживает бот:\nБББО-01-17 \nБББО-02-17'
	vk.messages.send(user_id=message.user_id, message=list_message)

def delete_user(message, vk):
	if get_group(message.user_id)!=0:
		vk_id = message.user_id
		try:
			cur.execute("""DELETE FROM users WHERE vk_id = '{0}'""".format(str(message.user_id)))
			conn.commit()
			vk.messages.send(user_id=message.user_id, message=u'Смена группы произошла успешно!')
			hello(message, vk)
		except:	
			conn.rollback()
			vk.messages.send(user_id=message.user_id, message=u'Упс, что то пошло не так!')
	else:
		vk.messages.send(user_id=message.user_id, message=u'Тебя нет в базе, введи свою группу!\n Группы, которые поддреживает бот:\nБББО-01-17 \nБББО-02-17')



def today_auto(vk_id, vk):
	mes_auto = 'Привет хочу напомнить пары на сегодня:\n\n'
	mes_auto_info = 'Чтобы отключить уведомления, напиши мне "уведомления".'
	mes_date = '(' + str(datetime.datetime.today().day) + '.' + str(datetime.datetime.today().month) + ')'
	vk.messages.send(user_id=vk_id, message=mes_auto+get_weekday(datetime.datetime.today(), mes_date, vk_id)+mes_auto_info)


def notifications(message, vk):	
	if get_group(message.user_id)!=0:
		# notification = 0
		cur.execute(u"""SELECT notifications, group_id FROM users WHERE vk_id='{0}'""".format(str(message.user_id)))
		for el in cur:
			notification = el[0]
		if notification=='no':
			cur.execute(u"""UPDATE users SET notifications='yes' WHERE vk_id='{0}'""".format(str(message.user_id)))
			conn.commit()
			vk.messages.send(user_id=message.user_id, message=u'Теперь тебе будет приходить уведомление о парах в 6:45 с понедельника по субботу!\n Чтобы отключить уведомление напиши мне "уведомление".')
		else:
			cur.execute(u"""UPDATE users SET notifications='no' WHERE vk_id='{0}'""".format(str(message.user_id)))
			conn.commit()
			vk.messages.send(user_id=message.user_id, message=u'Теперь тебе не будет приходить уведомление о парах утром! Чтобы включть уведомление напиши мне "уведомление"')
	else:
		vk.messages.send(user_id=message.user_id, message=u'Тебя нет в базе, введи свою группу!\n Группы, которые поддреживает бот:\nБББО-01-17 \nБББО-02-17')


def start(message, vk):
	vk_id = message.user_id
	group = message.text.upper()
	if get_group(vk_id)==0:
		try:
			cur.execute(u"""INSERT INTO users (vk_id, group_id, notifications) VALUES ('{0}', '{1}', 'no') ON CONFLICT DO NOTHING""".format(str(vk_id), group))
			conn.commit()
			vk.messages.send(user_id=message.user_id, message=u'Я добавил тебя в базу, можешь приступать к работе!')
			list_comand(message, vk)
		except:	
			conn.rollback()
			vk.messages.send(user_id=message.user_id, message=u'Упс, что то пошло не так!')
	else:
		vk.messages.send(user_id=message.user_id, message=u'Ты уже есть в базе! Твоя группа: {0}'.format(get_group(vk_id)))

def hello(message, vk):
	if get_group(message.user_id)==0:
		vk.messages.send(user_id=message.user_id, message=u'Тебя нет в базе, введи свою группу!\n Группы, которые поддреживает бот:\nБББО-01-17 \nБББО-02-17 ')
	else:
		vk.messages.send(user_id=message.user_id, message=u'Ну привет, чувак из {0}'.format(get_group(message.user_id)))


if __name__ == '__main__':
	bot = VKBot(token='ad2782d4222562577747d80a4e616f6e8f9d566dfe73ca2e67656b3e2537e57c770fbce7bcc61073d86b5')	
	while True:
		if datetime.datetime.now().strftime('%H:%M:%S')=='14:48:00' and datetime.datetime.now().weekday()!=6:
			print('WORK!')
			cur.execute(u"""SELECT vk_id, group_id FROM users WHERE notifications='yes'""")
			for el in cur:
				today_auto(int(el[0]), bot.vk)
		queryset = [
		[[u"пн", "понедельник",], send_monday],
		[[u"вт", "вторник",], send_tuesday],
		[[u"ср", "среда", "среду",], send_wednesday],
		[[u"чт", "четверг",], send_thursday],
		[[u"пт", "пятницу", "пятница",], send_friday],
		[[u"суб", "суббота", "субботу", "сб",], send_saturday],
		[[u"сегодня",], today],
		[[u"завтра",], tomorow],
		[[u"неделю",], for_week],
		[[u"сменить",], delete_user],
		[[u"неделя", "нед"], week],
		[[u"преподы", "преподавтаели"], teachers],
		[[u"уведомление", "уведомления",], notifications],
		[[u"info","инфо","команды"] , list_comand],
		[[u''], on_date],
		[[u'Привет',], hello],
		[[u'бббо-02-17', 'бббо-01-17'], start]
		]
		bot.run(query=queryset)
	cur.close()
	conn.close()


