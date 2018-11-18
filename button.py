from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import text
import keyboards as kb

from config_for_button import TOKEN
import sqlite3 as lite
import sys
import time

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=kb.great_kb)

@dp.message_handler(commands=['hi1'])
async def process_hi1_command(message: types.Message):
    await message.reply("Первое - изменяем размер клавиатуры", reply_markup=kb.great_kb1)


@dp.message_handler(commands=['hi2'])
async def process_hi2_command(message: types.Message):
    await message.reply("Женя і Саня, татко Вас кохає!!!)))", reply_markup=kb.great_kb2)


@dp.message_handler(commands=['hi3'])
async def process_hi3_command(message:types.Message):
    await message.reply("Третье - добавляем больше кнопок", reply_markup=kb.markup3)


@dp.message_handler(commands=['hi4'])
async def process_hi4_command(message: types.Message):
    await message.reply("Четвертое - расставляем кнопки в ряд", reply_markup=kb.markup4)


@dp.message_handler(commands=['hi5'])
async def process_hi5_command(message: types.Message):
    await message.reply("Пятое - добавляем ряды кнопок", reply_markup=kb.markup5)


@dp.message_handler(commands=['hi6'])
async def process_hi6_command(message:types.Message):
    await message.reply("Шестое - запрашиваем контакт и геолокацию\nЭти две кнопки не зависят друг от друга", reply_markup=kb.markup_request)


@dp.message_handler(commands=['hi7'])
async def process_hi7_command(message: types.Message):
    await message.reply('Седьмое - все методы вместе', reply_markup=kb.markup_big)

@dp.message_handler(commands=['rm'])
async def process_rm_command(message: types.Message):
    await message.reply("Убираем шаблоны сообщений", reply_markup=kb.ReplyKeyboardRemove())


@dp.message_handler(commands=['1'])
async def process_command_1(message: types.Message):
    await message.reply('First inline button', reply_markup=kb.inline_kb1)


@dp.callback_query_handler(func=lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Turn first button!!')


@dp.callback_query_handler(func=lambda c: c.data and c.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 2:
        await bot.answer_callback_query(callback_query.id, text='Нажата вторая кнопка')
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉', show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Нажата инлайн кнопка! code={code}')

@dp.message_handler(commands=['2'])
async def process_command_2(message: types.Message):
    await message.reply("Отправляю все возможные кнопки", reply_markup=kb.inline_kb_full)


help_message = text(
    "Это урок по клавиатурам.",
    "Доступные команды:\n",
    "/start - приветствие",
    "\nШаблоны клавиатур:",
    "/hi1 - авто размер",
    "/hi2 - скрыть после нажатия",
    "/hi3 - больше кнопок",
    "/hi4 - кнопки в ряд",
    "/hi5 - больше рядов",
    "/hi6 - запрос локации и номера телефона",
    "/hi7 - все методы"
    "/rm - убрать шаблоны",
    "\nИнлайн клавиатуры:",
    "/1 - первая кнопка",
    "/2 - сразу много кнопок",
    sep="\n"
)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message)


##########################################################################################################

#first_answer = text('Давай расчитаем стоимость страховки?')




@dp.message_handler(commands=['c'])



async def sp_oscpv(message: types.Message):
   # await message.reply(first_answer)
    await message.reply('Выберите желаемое действие', reply_markup=kb.start_menu)

    #await message.reply('Выбери тип транспортного средства', reply_markup=kb.car_type)
    sp.clear()

def koef_message(code, k):
    mes = f'Вы выбрали {code}, коеффициент - {k}'
    return mes

sp = []

@dp.callback_query_handler(func=lambda c: c.data)# and c.data.startswith('btn'))
async def choose_car_type(callback_query: types.CallbackQuery):
    code = callback_query.data[0:]
    #k1 = 0
    if code == 'calc':
        await bot.send_message(callback_query.from_user.id,'Выбери тип транспортного средства', reply_markup=kb.car_type)

    if code == 'A1':
        k = 0.34
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери город регистрации ТС', reply_markup=kb.gorod)
        save_k(k)
        print (sp)
    elif code == 'A2':
        k = 0.68
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери город регистрации ТС', reply_markup=kb.gorod)
        save_k(k)
        print(sp)
    elif code == 'B1':
        k = 1
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери город регистрации ТС', reply_markup=kb.gorod)
        save_k(k)
        print(sp)
    elif code == 'B2':
        k = 1.14
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери город регистрации ТС', reply_markup=kb.gorod)
        save_k(k)
        print(sp)
    elif code == 'B3':
        k = 1.18
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери город регистрации ТС', reply_markup=kb.gorod)
        save_k(k)
        print(sp)
    elif code == 'B4':
        k = 1.82
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери город регистрации ТС', reply_markup=kb.gorod)
        save_k(k)
        print(sp)
    elif code == 'C1':
        k = 2
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери город регистрации ТС', reply_markup=kb.gorod)
        save_k(k)
        print(sp)
    elif code == 'C2':
        k = 2.18
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери город регистрации ТС', reply_markup=kb.gorod)
        save_k(k)
        print(sp)
    elif code == 'D1':
        k = 2.55
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери город регистрации ТС', reply_markup=kb.gorod)
        save_k(k)
        print(sp)
    elif code == 'D2':
        k = 3
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери город регистрации ТС', reply_markup=kb.gorod)
        save_k(k)
        print(sp)
    elif code == 'E1':
        k = 0.34
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери город регистрации ТС', reply_markup=kb.gorod)
        save_k(k)
        print(sp)
    elif code == 'E2':
        k = 0.5
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери город регистрации ТС', reply_markup=kb.gorod)
        save_k(k)
        print(sp)


    elif code == 'Kyiv':
        k = 3.9
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери город регистрации ТС', reply_markup=kb.sfera)
        save_k(k)
        print(sp)
    elif code == 'Kyiv_obl':
        k = 2
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери город регистрации ТС', reply_markup=kb.sfera)
        save_k(k)
        print(sp)
    elif code == 'bolee_mln':
        k = 2.8
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери город регистрации ТС', reply_markup=kb.sfera)
        save_k(k)
        print(sp)
    elif code == 'g500_1000':
        k = 2.3
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери город регистрации ТС', reply_markup=kb.sfera)
        save_k(k)
        print(sp)
    elif code == 'g100_500':
        k = 1.7
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери город регистрации ТС', reply_markup=kb.sfera)
        save_k(k)
        print(sp)
    elif code == 'menee_100':
        k = 1
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери город регистрации ТС', reply_markup=kb.sfera)
        save_k(k)
        print(sp)
    elif code == 'eurobliahi':
        k = 3
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери город регистрации ТС', reply_markup=kb.sfera)
        save_k(k)
        print(sp)


    elif code == 'f_non_taxi':
        k = 1
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери стаж', reply_markup=kb.staz)
        save_k(k)
        print(sp)
    elif code == 'u_non_taxi':
        k = 1.1
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери стаж', reply_markup=kb.staz)
        save_k(k)
        print(sp)
    elif code == 'gruz':
        k = 1
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери стаж', reply_markup=kb.staz)
        save_k(k)
        print(sp)
    elif code == 'f_taxi':
        k = 1.1
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери стаж', reply_markup=kb.staz)
        save_k(k)
        print(sp)
    elif code == 'f_taxi':
        k = 1.2
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери стаж', reply_markup=kb.staz)
        save_k(k)
        print(sp)

    elif code == 'do_3':
        k = 1.75
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери период использования', reply_markup=kb.period)
        save_k(k)
        print(sp)
    elif code == 'ot_3':
        k = 1.35
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери период использования', reply_markup=kb.period)
        save_k(k)
        print(sp)
    elif code == 'ul':
        k = 1.2
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Выбери период использования', reply_markup=kb.period)
        save_k(k)
        print(sp)


    elif code == 'god':
        k = 1
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Были ли страховые события напротяжении года?', reply_markup=kb.strah_sob)
        save_k(k)
        print(sp)
    elif code == 'mes_11':
        k = 0.95
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Были ли страховые события напротяжении года?', reply_markup=kb.strah_sob)
        save_k(k)
        print(sp)
    elif code == 'mes_10':
        k = 0.9
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Были ли страховые события напротяжении года?', reply_markup=kb.strah_sob)
        save_k(k)
        print(sp)
    elif code == 'mes_9':
        k = 0.85
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Были ли страховые события напротяжении года?', reply_markup=kb.strah_sob)
        save_k(k)
        print(sp)
    elif code == 'mes_8':
        k = 0.8
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Были ли страховые события напротяжении года?', reply_markup=kb.strah_sob)
        save_k(k)
        print(sp)
    elif code == 'mes_7':
        k = 0.75
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Были ли страховые события напротяжении года?', reply_markup=kb.strah_sob)
        save_k(k)
        print(sp)
    elif code == 'mes_6':
        k = 0.7
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Были ли страховые события напротяжении года?', reply_markup=kb.strah_sob)
        save_k(k)
        print(sp)


    elif code == 'ss':
        k = 2
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Подсчет страховой премии',reply_markup=kb.sp)
        save_k(k)
        print(sp)
    elif code == 'non_ss':
        k = 1
        await bot.send_message(callback_query.from_user.id, koef_message(code, k))
        await bot.send_message(callback_query.from_user.id, f'Подсчет страховой премии', reply_markup=kb.sp)
        save_k(k)
        print(sp)

    elif code == 'count_sp':
        print(sp)
        await bot.send_message(callback_query.from_user.id, f'Страховая премия - {180*sp[0]*sp[1]*sp[2]*sp[3]*sp[4]*sp[5]} грн.')

    elif code == 'dogovora':
        await bot.send_message(callback_query.from_user.id, f'Выбери договор страхования', reply_markup=kb.choose_dog)

    elif code == 'dog_1':
        f = open('dogovor/dog1.doc', 'rb')
        await bot.send_document(callback_query.from_user.id, f, caption='Договор 1')
        time.sleep(3)
    elif code == 'dog_2':
        f = open('dogovor/dog2.doc', 'rb')
        await bot.send_document(callback_query.from_user.id, f, caption='Договор 2')
        time.sleep(3)
    elif code == 'dog_3':
        f = open('dogovor/dog3.doc', 'rb')
        await bot.send_document(callback_query.from_user.id, f, caption= 'Договор 3')
        time.sleep(3)


    return



'''@dp.message_handler(commands=['test'])
async def find_file_ids(message: types.Message):

    for file in os.listdir('dogovor/'):
        if file.split('.')[-1] == 'doc':
            f = open('dogovor/'+file, 'rb')
            user_id = message.from_user.id
            await bot.send_document(message.chat.id, f,None)
            #bot.send_message(message.chat.id, msg.)
            #msg = bot.send_voice(message.chat.id, f, None)
            # А теперь отправим вслед за файлом его file_id
            #bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(3)'''




def save_k(k):
    sp.append(k)






###########DataBase#############





##########################################################################################################
@dp.callback_query_handler(func=lambda c: c.data)# and c.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[0:]
    if code.isdigit():
        code = int(code)
    if code == 2:
        await bot.answer_callback_query(callback_query.id, text='Нажата вторая кнопка')
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉', show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Нажата инлайн кнопка! code={code}')


@dp.message_handler(commands=['2'])
async def process_command_2(message: types.Message):
    await message.reply("Отправляю все возможные кнопки", reply_markup=kb.inline_kb_full)


if __name__ == '__main__':
    executor.start_polling(dp)
