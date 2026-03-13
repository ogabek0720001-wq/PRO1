import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from googletrans import Translator

# Bot tokeningizni shu yerga yozing
TOKEN = "8648334978:AAG8bC-uGMuvZk2NzhGIdU1FjOvQxBnFWWY"

bot = Bot(token=TOKEN)
dp = Dispatcher()
translator = Translator()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        f"Assalomu alaykum, {message.from_user.full_name}!\n"
        "Men o'zbekcha so'zlarni inglizchaga tarjima qiluvchi botman. "
        "Menga matn yuboring!"
    )

@dp.message()
async def translation_handler(message: types.Message):
    # Foydalanuvchi yuborgan matnni tarjima qilish
    # src='uz' - qaysi tildan, dest='en' - qaysi tilga
    try:
        translation = translator.translate(message.text, src='uz', dest='en')
        await message.reply(f"🇬🇧 Inglizcha tarjimasi:\n\n`{translation.text}`", parse_mode="Markdown")
    except Exception as e:
        await message.reply("Kechirasiz, tarjima qilishda xatolik yuz berdi.")

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi.")