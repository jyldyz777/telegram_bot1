from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = '5262339615:AAGr05IkW3UvkujYSdTDLRRq8Jea2Si_xTM'

bot = Bot(token=TOKEN)
'''
bot это переменная. Мы ее используем,как переменную для класса Bot,
т.к. ме не можем использовать класс напрямую.
dp тоже переменная для Dispatcher,который передает нам сообщения.

'''
dp = Dispatcher(bot)




'''@.dp это переменная Dispatcher,а message handler это встроенная функция.
 После нее мы даем команду,знак равно и пишем саму команду в квадратных скобках.
 затем пишем async и задаем любую функцию,в скобках пишем тип сообщения и ставим двоеточие.
 await msg.reply всегда есть в боте,т.к. мы должны ответить.
'''


@dp.message_handler(commands=["help"])
async def start_message(msg: types.Message):
    await msg.reply("can i help you?") \
 \
 \
@dp.message_handler(commands=["hello"])
async def say_answer(msg: types.Message):
    await msg.reply("I am glad to hear you ")


@dp.message_handler(commands=["Price"])
async def show_message(msg: types.Message):
    button = types.KeyboardButton('how much is it')
    user = types.ReplyKeyboardMarkup()
    user.add(button)
    await msg.reply("50$", reply_markup=user)


@dp.message_handler(commands=["keyboard"])
async def start_message(msg: types.Message):
    button = types.KeyboardButton("Life is good")
    button2 = types.ReplyKeyboardMarkup()
    button2.add(button)
    await msg.reply("Hello,batya", reply_markup=button2)


@dp.message_handler()
async def show(user_mes: types.message):
    if user_mes.text == 'png1':
        await bot.send_photo(user_mes.from_user.id,
                             photo="https://www.ixbt.com/img/n1/news/2021/3/2/MacBook-Air-MacBook-Pro-i-Mac-mini-Noutbuki-6_large.jpg")
    elif user_mes.text == "iphone":
        await bot.send_photo(user_mes.from_user.id,
                             photo='https://www.blog.motifphotos.com/wp-content/uploads/2020/01/Edit-photos.jpg')
        await user_mes.reply("it is the best phone ever you have")

@dp.message_handler()
async def repeat(msg: types.Message):
    if msg.text == 'png':
        await bot.send_photo(msg.from_user.id,
                             photo='https://media.istockphoto.com/photos/heart-and-soul-picture-id1216425366?k=20&m=1216425366&s=612x612&w=0&h=2DTHso4Ryo4bobdaKDuLgqArtrgHpAPIq-8-mVGtyHs=')
    elif msg.text == 'doc':
        await bot.send_document(msg.from_user.id, document=open("test.html", "rb"))
    else:
        await bot.send_message(msg.from_user.id, msg.text)


# Для того чтобы код запустился надо написать это:
executor.start_polling(dp)
