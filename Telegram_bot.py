import os
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from datetime import datetime
import re
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import db_map as db
from random import randint
from config import API_TOKEN
import markups as m

bot = Bot(API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class Add (StatesGroup):
    theme = State()
    wait_dop = State()
    photo = State()

class Reminder(StatesGroup):
    time = State()

async def on_startup(_):
    await db.db_start()
    asyncio.create_task(send_daily_reminders())
    print('Бот запущен!')

@dp.callback_query_handler(lambda query: query.data == "notify")
async def set_reminder(query: types.CallbackQuery):
    user_id = query.from_user.id
    user = await db.user_already_set_reminder(user_id)
    print(user)
    if user == False:
        await query.message.answer("Пожалуйста, введите время для напоминания в формате ЧЧ:ММ")
        await Reminder.time.set()
    else:
        await query.message.answer("Вы уже поставили время!")

@dp.message_handler(state=Reminder.time)
async def save_reminder_time(message: types.Message, state: FSMContext):
    reminder_time = message.text
    if re.match(r'^\d{2}:\d{2}$', reminder_time):
        user_id = message.from_user.id
        await db.add_reminder(user_id, reminder_time)
        await message.answer("Время напоминания установлено!")
        await state.finish()
    else:
        await message.answer("Пожалуйста, введите время в правильном формате (ЧЧ:ММ)")

async def send_daily_reminders():
    while True:
        current_time = datetime.now().strftime("%H:%M")
        users_to_notify = await db.get_users_for_reminder(current_time)
        for user_id in users_to_notify:
            print(user_id)
            await bot.send_message(user_id, "Ты успел сегодня порешать задачки?")
        await asyncio.sleep(60)

@dp.callback_query_handler(lambda query: query.data == "info")
async def info(query: types.CallbackQuery):
    await bot.edit_message_text(
        chat_id=query.message.chat.id,
        message_id=query.message.message_id,
        text="По всем вопросам, предложениям и найденым ошибкам пишите разработчику @Kengamath 💌",
        reply_markup = m.infor
    )

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Привет! \U0001F44B Я бот,который поможет тебе с подготовкой к ОГЭ по математике! \U0001F4DD"
                        "\n\n\U0001F4D2 Кнопка <b>'Теория'</b> отвечает за все необходимые формулы, теоремы, определения, признаки и свойства, которые тебе могут понадобиться на экзамене "
                        "\n\n\U000023F0 Нажав на <b>'Напоминания'</b>, ты сможешь установить ежедневные уведомления, чтобы не забрасывать свою подготовку"
                        "\n\n\U0001F4F1 Если ты нашёл ошибку или хочешь предложить новую задачку или теорию, то смело переходи в <b>'Контакты'</b>", parse_mode='HTML', reply_markup=m.keyboard_inline
    )

@dp.callback_query_handler(lambda query: query.data == "theory")
async def theory(query: types.CallbackQuery):
    await bot.edit_message_text(
        chat_id=query.message.chat.id,
        message_id=query.message.message_id,
        text="Рад видеть тебя в отделе теории 📚"
             "\nЧто тебя интересует?",
        reply_markup=m.theory
    )


@dp.callback_query_handler(lambda query: query.data == "sprav1")
async def sprav(query: types.CallbackQuery):
    await bot.edit_message_text(
        chat_id=query.message.chat.id,
        message_id=query.message.message_id,
        text="Ого! А вот и наши любимые справочные материалы, которые тебе будут доступны на экзамене \U0001F60F "
             "\nТакже здесь есть ссылочки на кодификатор, спецификацию и демоверсию экзамена 2024 года:",

        reply_markup=m.urlkb
    )



@dp.callback_query_handler(lambda query: query.data == "algebra")
async def alg(query: types.CallbackQuery):
    await bot.edit_message_text(
        chat_id=query.message.chat.id,
        message_id=query.message.message_id,
        text="Алгебра раздел не маленький \U0001F914 "
             "\n Что конкретно ты ищещь? ",
        reply_markup=m.algebra_theory
    )


@dp.callback_query_handler(lambda query: query.data == "geometry")
async def alg(query: types.CallbackQuery):
    await bot.edit_message_text(
        chat_id=query.message.chat.id,
        message_id=query.message.message_id,
        text="Добро пожаловать в страну 'Геометрия' \U0001F3F0"
             "\nКакой район планируешь изучить?' ",
        reply_markup=m.geom_theory
    )


@dp.callback_query_handler(lambda query: query.data == "back_main")
async def alg(query: types.CallbackQuery):
    await bot.edit_message_text(
        chat_id=query.message.chat.id,
        message_id=query.message.message_id,
        text="Привет! \U0001F44B Я бот,который поможет тебе с подготовкой к ОГЭ по математике! \U0001F4DD"
                        "\n\n\U0001F4D2 Кнопка <b>'Теория'</b> отвечает за все необходимые формулы, теоремы, определения, признаки и свойства, которые тебе могут понадобиться на экзамене "
                        "\n\n\U000023F0 Нажав на <b>'Напоминания'</b>, ты сможешь установить ежедневные уведомления, чтобы не забрасывать свою подготовку"
                        "\n\n\U0001F4F1 Если ты нашёл ошибку или хочешь предложить новую задачку или теорию, то смело переходи в <b>'Контакты'</b>", parse_mode='HTML',
        reply_markup=m.keyboard_inline
    )


@dp.callback_query_handler(lambda query: query.data == "back_theory")
async def alg(query: types.CallbackQuery):
    await bot.edit_message_text(
        chat_id=query.message.chat.id,
        message_id=query.message.message_id,
        text="Выберите предмет: ",
        reply_markup=m.theory
    )

@dp.callback_query_handler(lambda query: query.data == "back_theme")
async def alg(query: types.CallbackQuery):
    await bot.edit_message_text(
        chat_id=query.message.chat.id,
        message_id=query.message.message_id,
        text="Выберите тему: ",
        reply_markup=m.algebra_theory
    )

@dp.callback_query_handler(lambda query: query.data == "back_theme1")
async def alg(query: types.CallbackQuery):
    await bot.edit_message_text(
        chat_id=query.message.chat.id,
        message_id=query.message.message_id,
        text="Выбери интересующий тебя раздел: ",
        reply_markup=m.geom_theory
    )

@dp.message_handler(commands=['add'])
async def add_photo_command(message: types.Message):
    await message.reply("Выбери тему , для которой хочешь добавить фотографию:", reply_markup=m.inadd)
    await Add.theme.set()

# Function to handle choosing a topic
@dp.callback_query_handler(state=Add.theme)
async def choose_topic(query: types.CallbackQuery, state: FSMContext):
    theme = query.data
    if theme == "uravn":
        await query.message.answer("Что хочешь добавить?", reply_markup=m.urav)
        await Add.wait_dop.set()
        @dp.callback_query_handler(state=Add.wait_dop)
        async def waitt(query: types.callback_query, state: FSMContext):
            theme = query.data
            await state.update_data(theme=theme)
            await Add.photo.set()
            print(theme)
            await query.message.answer("Отлично! Отправьте фото!")
    elif theme == "neravenstv":
        await query.message.answer("Что хочешь добавить?", reply_markup=m.nerav)
        await Add.wait_dop.set()
        @dp.callback_query_handler(state=Add.wait_dop)
        async def waitt(query: types.callback_query, state: FSMContext):
            theme = query.data
            await state.update_data(theme=theme)
            await Add.photo.set()
            print(theme)
            await query.message.answer("Отлично! Отправьте фото!")
    elif theme == "funct":
        await query.message.answer("Что хочешь добавить?", reply_markup=m.func)
        await Add.wait_dop.set()
        @dp.callback_query_handler(state=Add.wait_dop)
        async def waitt(query: types.callback_query, state: FSMContext):
            theme = query.data
            await state.update_data(theme=theme)
            await Add.photo.set()
            print(theme)
            await query.message.answer("Отлично! Отправьте фото!")
    elif theme == "progr":
        await query.message.answer("Что хочешь добавить?", reply_markup=m.prog)
        await Add.wait_dop.set()
        @dp.callback_query_handler(state=Add.wait_dop)
        async def waitt(query: types.callback_query, state: FSMContext):
            theme = query.data
            await state.update_data(theme=theme)
            await Add.photo.set()
            print(theme)
            await query.message.answer("Отлично! Отправьте фото!")
    elif theme == "treugolnik":
        await query.message.answer("Что хочешь добавить?", reply_markup=m.treug)
        await Add.wait_dop.set()
        @dp.callback_query_handler(state=Add.wait_dop)
        async def waitt(query: types.callback_query, state: FSMContext):
            theme = query.data
            await state.update_data(theme=theme)
            await Add.photo.set()
            print(theme)
            await query.message.answer("Отлично! Отправьте фото!")
    elif theme == "parallelogramm":
        await query.message.answer("Что хочешь добавить?", reply_markup=m.parall)
        await Add.wait_dop.set()
        @dp.callback_query_handler(state=Add.wait_dop)
        async def waitt(query: types.callback_query, state: FSMContext):
            theme = query.data
            await state.update_data(theme=theme)
            await Add.photo.set()
            print(theme)
            await query.message.answer("Отлично! Отправьте фото!")
    elif theme == "okru":
        await query.message.answer("Что хочешь добавить?", reply_markup=m.okr)
        await Add.wait_dop.set()
        @dp.callback_query_handler(state=Add.wait_dop)
        async def waitt(query: types.callback_query, state: FSMContext):
            theme = query.data
            await state.update_data(theme=theme)
            await Add.photo.set()
            print(theme)
            await query.message.answer("Отлично! Отправьте фото!")
    elif theme == "teorem":
        await query.message.answer("Что хочешь добавить?", reply_markup=m.teo)
        await Add.wait_dop.set()
        @dp.callback_query_handler(state=Add.wait_dop)
        async def waitt(query: types.callback_query, state: FSMContext):
            theme = query.data
            await state.update_data(theme=theme)
            await Add.photo.set()
            print(theme)
            await query.message.answer("Отлично! Отправьте фото!")
    else:
        theme = query.data
        await state.update_data(theme=theme)
        await Add.photo.set()
        print(theme)
        await query.message.answer("Отлично! Отправьте фото!")


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Add.photo)
async def receive_photo(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    topic = user_data.get('theme')
    file_id = message.photo[-1].file_id
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path
    await bot.download_file(file_path, f"{topic}_{file_id}.jpg")
    photo_path = f"{topic}_{file_id}.jpg"
    await db.add_photo(topic, photo_path)
    await message.reply(f"Фотография сохранена для темы: {topic}")
    await state.finish()

@dp.callback_query_handler(lambda query: query.data == "close")
async def close_button(query: types.CallbackQuery):
    if query.message.text:
        topic = query.message.text.split(":")[1].strip()
        photo_path = await db.get_photo(topic)
        if isinstance(photo_path, tuple) and len(photo_path) > 0:
            photo_path = photo_path[0]
            os.remove(photo_path)
    await bot.delete_message(chat_id=query.message.chat.id, message_id=query.message.message_id)

@dp.callback_query_handler()
async def query_get(query: types.CallbackQuery):
    topic = query.data
    if topic == "urav":
        await query.message.answer("Уравнения бывают разные. Какой тип тебя интересует? \U0001F914", reply_markup=m.urav)
        photo_path = await db.get_photo(topic)
        print(f"Photo Path: {photo_path}")

        if isinstance(photo_path, tuple) and len(photo_path) > 0:
            photo_path = photo_path[0]  # Извлекаем строку из кортежа
            await bot.send_photo(query.from_user.id, open(photo_path, 'rb'), reply_markup=m.close)
    elif topic == "neravenstv":
        await query.message.answer(f"Неравенства бывают разных типов. Какие тебя интересуют? \U0001F914", reply_markup=m.nerav)
        photo_path = await db.get_photo(topic)
        print(f"Photo Path: {photo_path}")

        if isinstance(photo_path, tuple) and len(photo_path) > 0:
            photo_path = photo_path[0]  # Извлекаем строку из кортежа
            await bot.send_photo(query.from_user.id, open(photo_path, 'rb'), reply_markup=m.close)
    elif topic == "funct":
        await query.message.answer(f"Функции бывают разных типов. Какие тебя интересуют? \U0001F914", reply_markup=m.func)
        photo_path = await db.get_photo(topic)
        print(f"Photo Path: {photo_path}")

        if isinstance(photo_path, tuple) and len(photo_path) > 0:
            photo_path = photo_path[0]  # Извлекаем строку из кортежа
            await bot.send_photo(query.from_user.id, open(photo_path, 'rb'), reply_markup=m.close)
    elif topic == "progr":
        await query.message.answer("Прогрессии бывают разных типов. Какие тебя интересуют? \U0001F914", reply_markup=m.prog)
        photo_path = await db.get_photo(topic)
        print(f"Photo Path: {photo_path}")

        if isinstance(photo_path, tuple) and len(photo_path) > 0:
            photo_path = photo_path[0]  # Извлекаем строку из кортежа
            await bot.send_photo(query.from_user.id, open(photo_path, 'rb'), reply_markup=m.close)
    elif topic == "treugolnik":
        await query.message.answer("Что ты хочешь узнать про треугольники? \U0001F914", reply_markup=m.treug)
        photo_path = await db.get_photo(topic)
        print(f"Photo Path: {photo_path}")

        if isinstance(photo_path, tuple) and len(photo_path) > 0:
            photo_path = photo_path[0]  # Извлекаем строку из кортежа
            await bot.send_photo(query.from_user.id, open(photo_path, 'rb'), reply_markup=m.close)
    elif topic == "parallelogramm":
        await query.message.answer("Хмм, какой раздел тебя заинтересовал? \U0001F914", reply_markup=m.parall)
        photo_path = await db.get_photo(topic)
        print(f"Photo Path: {photo_path}")

        if isinstance(photo_path, tuple) and len(photo_path) > 0:
            photo_path = photo_path[0]  # Извлекаем строку из кортежа
            await bot.send_photo(query.from_user.id, open(photo_path, 'rb'), reply_markup=m.close)
    elif topic == "okru":
        await query.message.answer("Рад видеть тебя в данном отделе! С чем подсказать? \U0001F914", reply_markup=m.okr)
        photo_path = await db.get_photo(topic)
        print(f"Photo Path: {photo_path}")

        if isinstance(photo_path, tuple) and len(photo_path) > 0:
            photo_path = photo_path[0]  # Извлекаем строку из кортежа
            await bot.send_photo(query.from_user.id, open(photo_path, 'rb'), reply_markup=m.close)
    elif topic == "teorem":
        await query.message.answer("А кто это тут у нас? С чем могу помочь? \U0001F914", reply_markup=m.teo)
        photo_path = await db.get_photo(topic)
        print(f"Photo Path: {photo_path}")

        if isinstance(photo_path, tuple) and len(photo_path) > 0:
            photo_path = photo_path[0]  # Извлекаем строку из кортежа
            await bot.send_photo(query.from_user.id, open(photo_path, 'rb'), reply_markup=m.close)
    else:
        photo_path = await db.get_photo(topic)
        print(f"Photo Path: {photo_path}")

        if isinstance(photo_path, tuple) and len(photo_path) > 0:
            photo_path = photo_path[0]  # Извлекаем строку из кортежа
            await bot.send_photo(query.from_user.id, open(photo_path, 'rb'), reply_markup=m.close)







if __name__ == "__main__":
    executor.start_polling(dp,on_startup=on_startup, skip_updates=True)
