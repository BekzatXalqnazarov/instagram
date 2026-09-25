from aiogram.fsm.state import State,StatesGroup
import logging
import asyncio
from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command
from aiogram.types import FSInputFile
from api import instagram
import os
from dotenv import load_dotenv
load_dotenv()
api = os.getenv('api_key')
bot = Bot(api)
dp=Dispatcher()

@dp.message(Command('start'))
async def baslaw(sms:types.Message):
    await sms.answer(text=f'Assalomu Aleykum {sms.from_user.first_name} Qanday Jardem Kerek?')
@dp.message()
async def juwap(sms:types.Message):
    txt=sms.text
    answer=await instagram(smstext=txt)
    await sms.answer_video(video=answer)
    await sms.answer(text=juwap)

async def main():
    await dp.start_polling(bot)

    


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
