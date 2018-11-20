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




def save_k(k):
    sp.append(k)






###########DataBase##

if __name__ == '__main__':
    executor.start_polling(dp)
