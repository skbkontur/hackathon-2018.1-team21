from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

roomname = 'Имение Элании'

def description():
    return"""Вы выходите из таверны и направляетесь в сторону имения Элании. Пройдя несколько кварталов на запад. 
    Подойдя ближе к богато украшенному большому дому, вы видите, что сюда стекаются гости. Дамы в шикарных платьях 
    и кавалеры в дорогих одеждах. Вы пытаетесь пройти в этом общем потоке, через главный вход, но вас останавливает 
    привратник. Худощавый мужчина с задранным подбородком и напомаженными волосами, собранным в тугой конский хвост."""

def dialog_start():
    return"""Привратник: Стойте! Кто вы? Совсем очевидно, что не один из гостей баронессы! *он брезгливо тыкает в вас 
    пальцем*"""

def dialog_answer_buttons_1():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="""Я по поручению мастера Торхилда, расследую дело об 
																  исчезновении лорда-протектора Винздора *показываете 
																  депешу*""")]])
	return keyboard

def dialog_1():
	return """Привратник: Хмм. Я конечно впущу вас, но вообще-то лучше не расстраивать сегодня баронессу, у нее 
	вообще-то праздник, разве вы не видете!"""

def dialog_answer_buttons_2():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="А что за праздник-то?")]])
	return keyboard

def dialog_2():
	return """Привратник: Как?! Помолвка с лордом конечно же!"""

def dialog_answer_buttons_3():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Оооок")]])
	return keyboard

def dialog_3():
	return """Привратник ведет вас, и вы попадаете в сад, музыканты играют легкую мелодию, ведутся светские беседы, 
	то тут, то там снуют слуги с подносами с едой и напитками. Внимательно осматриваясь, вы без труда выделяете среди 
	толпы лицо, той самой девушки с портрета в кабинете лорда. Леди Элания приветливо здоровается с вновь прибывшими, 
	непринуждённо перекидывается парой фраз с любыми гостями, мимо которых проходит. Но когда она отходит в сторону от 
	праздной суеты, вы замечаете, как сникают ее плечи, а взгляд потухает."""

def dialog_answer_buttons_4():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="подойти к Элании")]])
	return keyboard

def dialog_4():
	return """Вы подходите к девушке, и она не сразу обращает на вас внимание. вам кажется, что она сейчас где-то 
	глубоко в себе Леди Элания: *выпрямив спину и улыбаясь вам* Прощу прощения, я имею дурную привычку витать порой 
	в облаках! С Кем имею честь?"""

def dialog_answer_buttons_5():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="""Я хочу поговорить о пропаже вашего жениха. Вы 
                                                                    последняя видели его, за день, того как его 
                                                                  хватились. До меня доходят слухи, о том, что лорд 
                                                                  странно вел себя последнее время. Скажите, леди, он 
                                                                  не рассказывал вам что ни будь странное или пугающее 
                                                                  о своих планах?""")]])
	return keyboard

def dialog_5():
	return """Элания: *испуганно оглядевшись по сторонам* Боюсь, мне есть, что рассказать вам, но не здесь. *берет вас 
	за руку и уводит в дом* То, что произошло накануне с моим возлюбленным, это было настолько страшно и не похоже на 
	него, что я просто побоялась рассказать страже. Что подумают люди?! Он завязал мне глаза и сказал, что это 
	романтическая прогулка с сюрпризом, мы ехали какое-то время и там был этот храм.. Мне сразу не понравилось место, 
	я просила его уйти оттуда, но он как будто не слышал меня, сперва что-то нес о древних, что заточены здесь, что он 
	наконец-то разгадал загадку, как освободить могущество… и прочую оккультную чушь, в которой я никогда не была 
	сведуща... А потом, он взял меня за руку и стал нежно так просить, спуститься с ним в крипту. Когда я отказалась и 
	начала вырываться, клянусь, он силой хотел утащить меня туда! Мне чудом удалось сбежать! *на ее глаза наворачиваются
	 слезы* прощу вас, если вы найдете его там, в каком бы то не было виде, не говорите никому о том, что я вам сейчас 
	 поведала! Он не заслуживает такого очернения имени! А то, что было там у храма.. это был не мой Винздор.. """

def dialog_answer_buttons_6():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Можете не переживать на этот счет!")]])
	return keyboard

def dialog_6():
	return """Элания: *выпрямляет спину и хлоает себя по щекам* Я должна вернуться к гостям. Мы все верим, что 
	отсутствие нашего защитника — это лишь временно и я не могла отменить праздник. Она улыбается вам, вновь примерив 
	маску радушной хозяйки дома."""


def end_room_buttons():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Теперь я кажется понимаю о чем вы.. ")]])
	return keyboard