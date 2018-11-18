from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, types
import keyboards as kb



button_hi = KeyboardButton('То для Вас))')

great_kb = ReplyKeyboardMarkup()
great_kb.add(button_hi)
great_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)

great_kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_hi)


button1 = KeyboardButton('1️⃣')
button2 = KeyboardButton('2️⃣')
button3 = KeyboardButton('3️⃣')

markup3 = ReplyKeyboardMarkup().add(button1).add(button2).add(button3)

markup4 = ReplyKeyboardMarkup().row(button1, button2, button3)

markup5 = ReplyKeyboardMarkup().row(button1, button2, button3).add(KeyboardButton('Middle row'))

button4 = KeyboardButton('4️⃣')
button5 = KeyboardButton('5️⃣')
button6 = KeyboardButton('6️⃣')
markup5.row(button4, button5)
markup5.insert(button6)


markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Send your contact ☎️', request_contact=True))\
                                                        .add(KeyboardButton('Send your location 🗺️', request_location=True))


markup_big = ReplyKeyboardMarkup()
markup_big.add(button1, button2, button3, button4, button5, button6)
markup_big.row(button1, button2, button3, button4, button5, button6)

markup_big.row(button4, button2)
markup_big.add(button3, button2)
markup_big.insert(button1)
markup_big.insert(KeyboardButton('9️⃣'))



inline_btn_1 = InlineKeyboardButton('First button', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)


inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1)
inline_kb_full.add(InlineKeyboardButton('Вторая кнопка', callback_data='btn2'))
inline_btn_3 = InlineKeyboardButton('кнопка 3', callback_data='btn3')
inline_btn_4 = InlineKeyboardButton('кнопка 4', callback_data='btn4')
inline_btn_5 = InlineKeyboardButton('кнопка 5', callback_data='btn5')
inline_kb_full.add(inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full.row(inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full.insert(InlineKeyboardButton("query=''", switch_inline_query=''))
inline_kb_full.insert(InlineKeyboardButton("query='qwerty'", switch_inline_query='qwerty'))
inline_kb_full.insert(InlineKeyboardButton("Inline в этом же чате", switch_inline_query_current_chat='wasd'))
inline_kb_full.add(InlineKeyboardButton('Уроки aiogram', url='https://surik00.gitbooks.io/aiogram-lessons/content/'))

######################################################################

dogovor = InlineKeyboardButton('Договора страхования', callback_data='dogovora')

dog_1 = InlineKeyboardButton('Договор 1', callback_data='dog_1')
dog_2 = InlineKeyboardButton('Договор 2', callback_data='dog_2')
dog_3 = InlineKeyboardButton('Договор 3', callback_data='dog_3')
choose_dog = InlineKeyboardMarkup(row_width=1)
choose_dog.add(dog_1, dog_2, dog_3)

adress = InlineKeyboardButton('Адрес дирекции', callback_data='adress')
calc_oscpv = InlineKeyboardButton('Калькулятор ОСАГО', callback_data='calc')
dogovor = InlineKeyboardButton('Договора страхования', callback_data='dogovora')

car_type_legk = InlineKeyboardMarkup(row_width=3)
# Заголовки типов ТС
legkovoe_ts = InlineKeyboardButton('Легковые ТС', callback_data='forma')
gruzovue_ts = InlineKeyboardButton('Грузовое ТС', callback_data='forma')
avtobusu = InlineKeyboardButton('Автобус', callback_data='forma')
pricepu = InlineKeyboardButton('Прицеп', callback_data='forma')
moto = InlineKeyboardButton('Мотоцикл', callback_data='forma')
#Легковые ТС
typeB1 = InlineKeyboardButton('B1', callback_data='B1')
typeB2 = InlineKeyboardButton('B2', callback_data='B2')
typeB3 = InlineKeyboardButton('B3', callback_data='B3')
typeB4 = InlineKeyboardButton('B4', callback_data='B4')
#Грузовые ТС
typeC1 = InlineKeyboardButton('C1', callback_data='C1')
typeC2 = InlineKeyboardButton('C2', callback_data='C2')
#Автобусы
typeD1 = InlineKeyboardButton('D1', callback_data='D1')
typeD2 = InlineKeyboardButton('D2', callback_data='D2')
#Автобусы
typeA1 = InlineKeyboardButton('A1', callback_data='A1')
typeA2 = InlineKeyboardButton('A2', callback_data='A2')
#Прицепы
typeE1 = InlineKeyboardButton('E1', callback_data='E1')
typeE2 = InlineKeyboardButton('E2', callback_data='E2')

#Город регистрации
gorod_reg = InlineKeyboardButton('Город регистрации', callback_data='forma')

Kyiv = InlineKeyboardButton('Киев', callback_data='Kyiv')
Kyiv_obl = InlineKeyboardButton('Киевская обл.', callback_data='Kyiv_obl')
bolee_mln = InlineKeyboardButton('Города более 1 млн.', callback_data='bolee_mln')
g500_1000 = InlineKeyboardButton('Города от 500 тис до 1 млн', callback_data='g500_1000')
g100_500 = InlineKeyboardButton('Города от 100 тис до 500 тис', callback_data='g100_500')
menee_100 = InlineKeyboardButton('Города менее 100 млн', callback_data='menee_100')
eurobliahi = InlineKeyboardButton('ТС зарегистрированы в других странах', callback_data='eurobliahi')

#sp = InlineKeyboardButton('Страховая премия', callback_data='sp')

sum_sp = InlineKeyboardButton('Подсчитать страговую премию', callback_data='count_sp')



start_menu = InlineKeyboardMarkup(row_width=1)
start_menu.add(adress, calc_oscpv, dogovor)

car_type = InlineKeyboardMarkup(row_width=3)

car_type.add(legkovoe_ts)
car_type.row(typeB1, typeB2, typeB3, typeB4)
car_type.add(gruzovue_ts)
car_type.row(typeC1, typeC2)
car_type.add(avtobusu)
car_type.row(typeD1, typeD2)
car_type.add(moto)
car_type.row(typeA1, typeA2)
car_type.add(pricepu)
car_type.row(typeE1, typeE2)

gorod = InlineKeyboardMarkup(row_width=2)
gorod.add(gorod_reg)
gorod.add(Kyiv, Kyiv_obl)
gorod.add(bolee_mln, g500_1000)
gorod.add(g100_500, menee_100)
gorod.add(eurobliahi)
#gorod.add(sp)

sp = InlineKeyboardMarkup(row_width=1)
sp.add(sum_sp)

f_non_taxi = InlineKeyboardButton('ТС физ. лиц (не такси)', callback_data='f_non_taxi')
u_non_taxi = InlineKeyboardButton('ТС юр. лиц (не такси)', callback_data='u_non_taxi')
gruz = InlineKeyboardButton('Груговые ТС, автобусы и прицепы', callback_data='gruz')
f_taxi = InlineKeyboardButton('ТС ф.л. с использованием в комерческих целях', callback_data='f_taxi')
u_taxi = InlineKeyboardButton('ТС ю.л. с использованием в комерческих целях', callback_data='f_taxi')

sfera = InlineKeyboardMarkup(row_width=1)
sfera.add(f_non_taxi, u_non_taxi,gruz, f_taxi, u_taxi)

do_3_let = InlineKeyboardButton('Любой стаж (ф.л.)', callback_data='do_3')
ot_3_let = InlineKeyboardButton('от 3 лет (ф.л.)', callback_data='ot_3')
ul = InlineKeyboardButton('Юридическое лицо', callback_data='ul')

staz = InlineKeyboardMarkup(row_width=1)
staz.add(do_3_let, ot_3_let, ul)


god = InlineKeyboardButton('1 год', callback_data='god')
mes_11 = InlineKeyboardButton('11 песяцев', callback_data='mes_11')
mes_10 = InlineKeyboardButton('10 песяцев', callback_data='mes_10')
mes_9 = InlineKeyboardButton('9 песяцев', callback_data='mes_9')
mes_8 = InlineKeyboardButton('8 песяцев', callback_data='mes_8')
mes_7 = InlineKeyboardButton('7 песяцев', callback_data='mes_7')
mes_6 = InlineKeyboardButton('6 песяцев', callback_data='mes_6')

period = InlineKeyboardMarkup(row_width=1)
period.add(god, mes_11, mes_10, mes_9, mes_8, mes_7, mes_6)

ss = InlineKeyboardButton('Да', callback_data='ss')
non_ss = InlineKeyboardButton('Нет', callback_data='non_ss')
strah_sob = InlineKeyboardMarkup(row_width=1)
strah_sob.add(ss, non_ss)