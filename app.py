#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import *
import random
from random import shuffle
import sqlite3

from peewee import *

DATABASE = 'quiz.db'
DEBUG = True
SECRET_KEY = 'FENWOEINOObfwe'
database = SqliteDatabase(DATABASE)

#ROOT = path.dirname(path.realpath(__file__))
#database = sqlite3.connect(path.join(ROOT, "blog.db"))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

class Quiz(Model):
	ja_vocab = TextField(null = False)
	en_vocab = TextField(null = False)

	class Meta:
		database = database


def initialize():
    database.connect()
    database.create_tables([Quiz], safe=True)

@app.before_request
def before_request():
    g.db = database
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

"""
def parseDate(dateData):
    return dt(
        dateData.tm_year,
        dateData.tm_mon,
        dateData.tm_mday,
        dateData.tm_hour,
        dateData.tm_min,
        dateData.tm_sec
    )

d = datetime.datetime.now() + datetime.timedelta(-30)

"""

numCorrect = 0
numIncorrect = 0

@app.route('/ja', methods=["GET", "POST"])
def eiken1_quiz():
	quizzes = Quiz.select()
	num = random.randrange(1, 100)
	num1 = random.randrange(1, 100)
	num2 = random.randrange(1, 100)
	num3 = random.randrange(1, 100)
	ja_vocab = quizzes[num].ja_vocab
	en_answer = quizzes[num].en_vocab
	en_option1 = quizzes[num1].en_vocab
	en_option2 = quizzes[num2].en_vocab
	en_option3 = quizzes[num3].en_vocab

	option_list = [en_answer, en_option1, en_option2, en_option3]
	list_num = [0, 1, 2, 3]
	shuffle(list_num)

	correct = "正解!"
	incorrect = "不正解!"

	return render_template('index.html', quizzes=quizzes, ja_vocab=ja_vocab, en_answer=en_answer, en_option1=en_option1, en_option2=en_option2, en_option3=en_option3, option_list=option_list, list_num=list_num, correct=correct, incorrect=incorrect)

@app.route('/ja/quiz', methods=["GET", "POST"])
def eiken1_quiz_next():
	quizzes = Quiz.select()
	num = random.randrange(1, 100)
	num1 = random.randrange(1, 100)
	num2 = random.randrange(1, 100)
	num3 = random.randrange(1, 100)
	ja_vocab = quizzes[num].ja_vocab
	en_answer = quizzes[num].en_vocab
	en_option1 = quizzes[num1].en_vocab
	en_option2 = quizzes[num2].en_vocab
	en_option3 = quizzes[num3].en_vocab

	option_list = [en_answer, en_option1, en_option2, en_option3]
	list_num = [0, 1, 2, 3]
	shuffle(list_num)

	correct = "正解!"
	incorrect = "不正解!"

	return render_template('quiz.html', quizzes=quizzes, ja_vocab=ja_vocab, en_answer=en_answer, en_option1=en_option1, en_option2=en_option2, en_option3=en_option3, option_list=option_list, list_num=list_num, correct=correct, incorrect=incorrect)

if __name__ == "__main__":
    initialize()
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
