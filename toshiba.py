import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode, InputFile
from buttons1 import rkm, kiyim_menyu,fut_k,fut,kir_moshin
from create import create_db
from inser import insert_user


API_TOKEN = '7373697818:AAE6fiw1_KPKRpiHlgDOhFPK2xE3POdzZVU'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
        create_db()
        try:
        # msg.from_id, msg.from_user.username
            insert_user(msg.from_id, msg.from_user.username)
        except:
            pass
        await msg.answer(f"Assalomu alekum {msg.from_user.full_name}", reply_markup=rkm)
@dp.message_handler(commands=['help'])
async def help(msg: types.Message):
    await msg.reply('Siz bu botda Haladinnik, Kirmoshina, Peleso`s, Dishwasher narxini ko`rasiz')


@dp.message_handler(text='Haladilniklar')
async def kiyimlar(msg: types.Message):
    await msg.answer("Haladilniklar bo'limiga xush kelibsiz!", reply_markup=kiyim_menyu)

@dp.message_handler(text='GR-RS780WE-PG22')
async def xadi(msg: types.Message):
    url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSZ503poD0aAEIHSPQn_z3RMXxjy8KPVCeOw&s'
    text = """
Litr: 545 l
Diller narxi: 1155$
Do`kon narxi: 1250$ 
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-RF532WE-PGJ(22)')
async def xudi(msg: types.Message):
    url = 'https://on-off.uz/wp-content/uploads/2023/10/b53b3a3d6ab90ce0268229151c9bde112021102110335850478ib3pbheann.jpg.jpg'
    text = """
Litr: 500 l
Diller narxi: 1420$
Do`kon narxi: 1500$ 
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-RF532WE-PGJ(06)')
async def xsdi(msg: types.Message):
    url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtXxp0DbtImGRmiayDkg7OTPJcdQbPN7ufLw&s'
    text = """
Litr: 500 l
Diller narxi: 1410$
Do`kon narxi: 1500$ 
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)


    
@dp.message_handler(text='GR-RF610WE-PGS(22)')
async def xidi(msg: types.Message):
    url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfE2J8svFeC-tsLnGAwl9w4unAoyh4EWwrBA&s'
    text = """
Litr: 470 l
Diller narxi: 1010$
Do`kon narxi: 1080$ 
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-RF610WE-PMS(06)')
async def xdi(msg: types.Message):
    url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSS3XwQBLfo8oNqWtToGMwqN1Ft6HD2KuRXWTT8pUiNgQ&s'
    text = """
Litr: 470 l
Diller narxi: 980$
Do`kon narxi: 1050$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-RF610WE-PMS(37)')
async def toshiba(msg: types.Message):
    url = 'https://aray.ge/wp-content/uploads/137169_Toshiba_GR-RF610WE-PMS37_1-600x600.webp'
    text = """
Litr: 470 l
Diller narxi: 970$
Do`kon narxi: 1040$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-AG820U-C(X)')
async def toshiba1(msg: types.Message):
    url = 'https://d1pjg4o0tbonat.cloudfront.net/content/dam/toshiba-aem/me/refrigerator/top-mount-freezer/toshiba-top-mount-freezer-608l-gr-ag820/ps-img-1.jpg'
    text = """
Litr: 608 l
Diller narxi: 1260$
Do`kon narxi: 1350$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-AG820U-C(PGB)')
async def toshiba2(msg: types.Message):
    url = 'https://bozorcom.ams3.cdn.digitaloceanspaces.com/media/1_7mHvkAL.jpg'
    text = """
Litr: 608 l
Diller narxi: 1220$
Do`kon narxi: 1300$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-AG820U-C(GG)')
async def toshiba3(msg: types.Message):
    url = 'https://allbest.ge/wp-content/uploads/2022/04/NF3833AF-600x600.png'
    text = """
Litr: 608 l
Diller narxi: 1220$
Do`kon narxi: 1300$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-AG820U-C(XK)')
async def toshiba4(msg: types.Message):
    url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpWOrGK5k1rRh0oAp8Nw5OpwowJDmIbQZmIw&s'
    text = """
Litr: 608 l
Diller narxi: 1155$
Do`kon narxi: 1250$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-A820U-C(BS)')
async def xodi(msg: types.Message):
    url = 'https://olcha.uz/image/600x600/products/2022-12-19/kholodilnik-toshiba-gr-a820u-cbs-183431-1.jpeg'
    text = """
Litr: 608 l
Diller narxi: 1155$
Do`kon narxi: 1250$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-HG655UDZ-C(GG)')
async def xrdi(msg: types.Message):
    url = 'https://www.discounteri.ge/images/thumbnails/550/450/detailed/7/GR-HG655UDZ-C_GG_-2.png'
    text = """
Litr: 505 l
Diller narxi: 1135$
Do`kon narxi: 1200$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-HG655UDZ-C(XK)')
async def toshiba5(msg: types.Message):
    url = 'https://olcha.uz/image/600x600/products/2022-12-19/kholodilnik-toshiba-gr-hg655udz-cxk-183481-1.jpeg'
    text = """
Litr: 505 l
Diller narxi: 1135$
Do`kon narxi: 1200$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-RT624WE-PMJ(06)')
async def toshiba6(msg: types.Message):
    url = 'https://on-off.uz/wp-content/uploads/2023/03/gr-rt624_open_.jpg'
    text = """
Litr: 463 l
Diller narxi: 705$
Do`kon narxi: 750$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-RT624WE-PMJ(37)')
async def toshiba0(msg: types.Message):
    url = 'https://on-off.uz/wp-content/uploads/2023/03/f495af2879569oswgga1.jpg'
    text = """
Litr: 463 l
Diller narxi: 695$
Do`kon narxi: 740$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-RT559WE-PMJ(06)')
async def toshiba7(msg: types.Message):
    url = 'https://on-off.uz/wp-content/uploads/2023/03/f495af2879569oswgga1.jpg'
    text = """
Litr: 411 l
Diller narxi: 700$
Do`kon narxi: 750$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-RT468WE-PMJ(06)')
async def toshiba8(msg: types.Message):
    url = 'https://olcha.uz/image/600x600/products/2022-12-19/kholodilnik-toshiba-gr-rt468we-pmj06-183545-1.jpeg'
    text = """
Litr: 338 l
Diller narxi: 660$
Do`kon narxi: 650$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-RT468WE-PMJ(37)')
async def toshiba9(msg: types.Message):
    url = 'https://olcha.uz/image/600x600/products/2022-12-19/kholodilnik-toshiba-gr-rt468we-pmj37-183553-0.jpeg'
    text = """
Litr: 338 l
Diller narxi: 660$
Do`kon narxi: 650$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-RB449WE-PMJ(51)')
async def toshiba10(msg: types.Message):
    url = 'https://on-off.uz/wp-content/uploads/2023/10/holodilnik-toshiba-gr-rb449we-pmj51.jpg'
    text = """
Litr: 320 l
Diller narxi: 660$
Do`kon narxi: 700$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-RB449WE-PMJ(49)')
async def toshiba11(msg: types.Message):
    url = 'https://on-off.uz/wp-content/uploads/2023/10/cq5dam.web_.5000.5000-1.jpeg'
    text = """
Litr: 320 l
Diller narxi: 660$
Do`kon narxi: 700$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-RB449WE-PMJ(06)')
async def toshiba12(msg: types.Message):
    url = 'https://api.radius.uz/storage/products/January2024/Ysw8o3Az4YMCTGZMqCRG.webp'
    text = """
Litr: 320 l
Diller narxi: 660$
Do`kon narxi: 700$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='GR-RB308WE-DGJ(06)')
async def toshiba13(msg: types.Message):
    url = 'https://olcha.uz/image/400x400/products/2022-12-19/kholodilnik-toshiba-gr-rb308we-dmj06-183508-2.jpeg'
    text = """
Litr: 295 l
Diller narxi: 680$
Do`kon narxi: 720$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)

@dp.message_handler(text='Qaytish')
async def sport(msg: types.Message):
    await msg.answer('Qatish', reply_markup=rkm)


@dp.message_handler(text='Peleso`s')
async def kiyimlar(msg: types.Message):
    await msg.answer("Peleso`slar bo'limiga xush kelibsiz!", reply_markup=fut_k)


@dp.message_handler(text='VC-DR200AC(B)')
async def pi(msg: types.Message):
    url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgKgoD7wuQLNKSfE9Bk14yU8PIqbfa3TPWVQ&s'
    text = """
Litr: 5 l
Diller narxi: 105$
Do`kon narxi: 120$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='VC-DR220AC(G)')
async def p(msg: types.Message):
    url = 'https://frankfurt.apollo.olxcdn.com/v1/files/6c6c431vcmxb3-UZ/image;s=2500x2500'
    text = """
Litr: 5 l
Diller narxi: 110$
Do`kon narxi: 125$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)

@dp.message_handler(text='Qaytish')
async def sport(msg: types.Message):
    await msg.answer('Qatish', reply_markup=rkm)

@dp.message_handler(text='Dishwasher')
async def dish(msg: types.Message):
    await msg.answer("Dishwashers bo'limiga xush kelibsiz!", reply_markup=fut)

@dp.message_handler(text='DW-14F2CIS(BS)-UZ')
async def pili(msg: types.Message):
    url = 'https://main-cdn.sbermegamarket.ru/big2/hlr-system/256/494/850/215/114/4/100028092467b3.jpg'
    text = """
Litr: 14 l
Diller narxi: 460$
Do`kon narxi: 520$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='DW-14F2CIS(SS)-UZ')
async def pil(msg: types.Message):
    url = 'https://images.uzum.uz/ck601vkjvf2qegt4bjvg/original.jpg'
    text = """
Litr: 14 l
Diller narxi: 445$
Do`kon narxi: 505$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='DW-10F1CIS(W)-UZ')
async def pi(msg: types.Message):
    url = 'https://images.uzum.uz/cmp1dmhs99ouqbfrsfr0/original.jpg'
    text = """
Litr: 10 l
Diller narxi: 305$
Do`kon narxi: 350$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='DW-10F1CIS(S)-UZ')
async def pili1(msg: types.Message):
    url = 'https://api.radius.uz/storage/products/February2024/FlpIdKrUqVmekaIVreoq.webp'
    text = """
Litr: 10 l
Diller narxi: 315$
Do`kon narxi: 365$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)

@dp.message_handler(text='Qaytish')
async def sport(msg: types.Message):
    await msg.answer('Qatish', reply_markup=rkm)


@dp.message_handler(text='Kir mashinalar')
async def kir(msg: types.Message):
    await msg.answer("Kir mashinalar bo'limiga xush kelibsiz!", reply_markup=kir_moshin)



@dp.message_handler(text='TW-BJ100M4GE(SK)')
async def pil2(msg: types.Message):
    url = 'https://on-off.uz/wp-content/uploads/2023/03/new-project-2hjgf_png.jpg'
    text = """
Litr: 6 l
Diller narxi: 300$
Do`kon narxi: 330$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='TW-BJ100M4GE(WK)')
async def pil3(msg: types.Message):
    url = 'https://vlv.am/public/uploads/images/21-02-2023/63f4d03ea5caa.webp'
    text = """
Litr: 6 l
Diller narxi: 285$
Do`kon narxi: 315$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='TW-BL70A2UZ(SS)')
async def pil4(msg: types.Message):
    url = 'https://catalog.milliykatalogi.uz/s3/med/69097d37-080b-4230-ae71-dab09615a713.jpg'
    text = """
Litr: 7 l
Diller narxi: 325$
Do`kon narxi: 355$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='TW-BL70A2UZ(WK)')
async def pil5(msg: types.Message):
    url = 'https://images.uzum.uz/co8e4p4qk7bc30trfth0/t_product_540_high.jpg'
    text = """
Litr: 7 l
Diller narxi: 340$
Do`kon narxi: 370$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='TW-BL80A2UZ(WK)')
async def pil6(msg: types.Message):
    url = 'https://catalog.milliykatalogi.uz/s3/300x200/c58be1b7-bba7-6a6a-3b1e-2bfeff5044a3.jpg'
    text = """
Litr: 8 l
Diller narxi: 400$
Do`kon narxi: 430$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='TW-BL80A2UZ(SK)')
async def pili7(msg: types.Message):
    url = 'https://s13emagst.akamaized.net/products/48265/48264531/images/res_80b7a73bc2bd5508670e8dff69b340ed.jpg'
    text = """
Litr: 8 l
Diller narxi: 385$
Do`kon narxi: 415$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='TW-BL90A4UZ(SS)')
async def pili8(msg: types.Message):
    url = 'https://catalog.milliykatalogi.uz/s3/med/519b2160-fc6b-174b-8ad2-7b41d2a1c8de.jpg'
    text = """
Litr: 9 l
Diller narxi: 430$
Do`kon narxi: 460$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='TW-BL90A4UZ(WK)')
async def pili9(msg: types.Message):
    url = 'https://vega.ge/image/cache/catalog/1Emil/1Toshiba/TW-BL90A4UZ(WK)-2000x1500.jpg'
    text = """
Litr: 9 l
Diller narxi: 415$
Do`kon narxi: 445$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='TW-BL100A4UZ(SS)')
async def pili10(msg: types.Message):
    url = 'https://vega.ge/image/cache/catalog/1HRACH/2020/2021/2023/Hunvar/Lvacqi%20Meqena/TW-BL100A4UZ(SS)-500x300.jpg'
    text = """
Litr: 8 l
Diller narxi: 435$
Do`kon narxi: 465$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='TW-BL100A4UZ(WK)')
async def pili11(msg: types.Message):
    url = 'https://on-off.uz/wp-content/uploads/2023/11/paltsfearyuyantoshibatw-bl100a4uzwkag.1-750x750-1.jpg'
    text = """
Litr: 8 l
Diller narxi: 425$
Do`kon narxi: 455$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='TW-BK90G4UZ(SK)')
async def pili12(msg: types.Message):
    url = 'https://sodda.uz/storage/product/I5KNw9WbRrIPXjraazo9LOWMW20m63uUHuDJCVCg.jpg'
    text = """
Litr: 8 l
Diller narxi: 420$
Do`kon narxi: 450$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='TW-BK90G4UZ(WK)')
async def pili13(msg: types.Message):
    url = 'https://sodda.uz/storage/product/zLIUMVZGeYUa7vqNZuysMVTANAmDkkf2GM1zgeCF.jpg'
    text = """
Litr: 9 l
Diller narxi: 490$
Do`kon narxi: 520$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='TW-BK90S2GUZ(WK)')
async def pili14(msg: types.Message):
    url = 'https://sodda.uz/storage/product/zLIUMVZGeYUa7vqNZuysMVTANAmDkkf2GM1zgeCF.jpg'
    text = """
Litr: 9 l
Diller narxi: 470$
Do`kon narxi: 500$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='TW-BK100G4UZ(SK)')
async def pili15(msg: types.Message):
    url = 'https://images.uzum.uz/cngpducu2hhlb05g5ihg/original.jpg'
    text = """
Litr: 9 l
Diller narxi: 530$
Do`kon narxi: 560$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='TW-BK100G4UZ(WK)')
async def pili16(msg: types.Message):
    url = 'https://sodda.uz/storage/product/F0cAboVm3U7c8jtukEyNH2tHySb6RIdimAufABYC.jpg'
    text = """
Litr: 9 l
Diller narxi: 515$
Do`kon narxi: 550$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='TW-BK100S2GUZ(SK)')
async def pili17(msg: types.Message):
    url = 'https://good-bt.ru/wa-data/public/shop/products/84/66/106684/images/215849/215849.970.jpeg'
    text = """
Litr: 10 l
Diller narxi: 510$
Do`kon narxi: 550$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)



@dp.message_handler(text='TW-BK110G4UZ(WK)')
async def pili18(msg: types.Message):
    url = 'https://avatars.mds.yandex.net/i?id=5c0fa3c3d94e4c91a41cefb8f493859e33d778aa-10637828-images-thumbs&n=13'
    text = """
Litr: 10 l
Diller narxi: 490$
Do`kon narxi: 530$
Bog'lanig: @toshiba_boy
    """
    await bot.send_photo(msg.chat.id, photo=url, caption=text)

@dp.message_handler(text='Qaytish')
async def sport(msg: types.Message):
    await msg.answer('Qatish', reply_markup=rkm)






if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)