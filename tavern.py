def description():
    return 'Вы входите в таверну и вам в нос сразу же бьет приятный запах жаркого и свежей выпечки. В дальней части от вас расположена стойка, которую протирает крупный рыжебородый дварф в переднике и с засученными рукавами, завидев вас, он делает приветственный жест рукой, приглашая присесть за стойкой. В ближнем темном углу спиной к вам сидит широкоплечий мужчина, темный волосы и зеленая жилетка на нем подсказывает вам, что это может быть слуга лорда Логен. Надо сказать, что в столь ранний час он тут единственный посетитель.'
def initiate():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Подойти к мужчине за столом")]])
	return keyboard

def dialog_start():
    return 'Вы подходите ближе и видите, что даже сидеть ему трудновато, приятный запах жаркого перебивает запах дешевого алкоголя, исходящий из стакана в руке у человек. Он резким движением опрокидывает стакан в себя и с грохотом ставит на стол.Логен: Чего тебе? Я нынче безработный.. могу себе позволить!'


def dialog_answer_buttons_1():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Воу-воу! Палехчи, приятель! Я вообще-то тут, чтобы вернуть тебе уверенность в завтрашнем дне, т.е. твою работу, в общем, лорда ищу. Я знаю, что ты уже все рассказал городским стражам, но может, я угощу стаканчиком и мы побеседуем по душам. Обещаю, что только между нами!")]])
	return keyboard

def dialog_1():
	return 'Логен: *тяжело роняет голову на руки и начинает причать, раскачиваясь в стороны*. Я ведь говорил ему! А какой человек! Человечище! Он как с похода того вернулся, сам не свой стал, не ест не пьет и одну только книгу, потрёпанную из рук, не выпускает! Тьфу! Я говорю, хозяин вы б сходили свежим воздухом подышали что ли! И правда смотрю на следующий день - засобирлся! Я увидал, вышел радостный, говорю ну вот, мол, давайте коня вам поседлаю! И верно, что отличный день, для прогулки! А он обернулся, посмотрел на меня как-то дико, какими-то не своими глазами и я вдруг остолбенел ничего сделать не могу, видел только, что он пошел к Южным воротам. Я когда отошел, решил, что никому рассказывать не буду.. слишком это странно для лорда нашего Винздора..'
def dialog_answer_buttons_2():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Ясно. не переживай, я никому не скажу тоже")]])
	return keyboard
def end_room():
	return 'Вы выходите из таверны и направляетесь в сторону имения Элании. Пройдя несколько кварталов на запад. Подойдя ближе к богато украшенному большому дому, вы видите, что сюда стекаются гости. Дамы в шикарных платьях и кавалеры в дорогих одеждах. Вы пытаетесь пройти в этом общем потоке, через главный вход, но вас останавливает привратник. Худощавый мужчина с задранным подбородком и напомаженными волосами, собранным в тугой конский хвост. Привратник: Стойте! Кто вы? Совсем очевидно, что не один из гостей баронессы! *он брезгливо тыкает в вас пальцем*'