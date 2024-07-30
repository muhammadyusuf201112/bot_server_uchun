from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

rkm = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)


k1 = KeyboardButton(text='Haladilniklar')
k3 = KeyboardButton(text="Peleso`s")
k4 = KeyboardButton(text="Dishwasher")
k5 = KeyboardButton(text="Kir mashinalar")


rkm.add(k1, k3, k4, k5)


kiyim_menyu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

b1 = KeyboardButton(text='GR-RS780WE-PG22')
b2 = KeyboardButton(text='GR-RF532WE-PGJ(22)')
b3 = KeyboardButton(text='GR-RF532WE-PGJ(06)')
b4 = KeyboardButton(text='GR-RF610WE-PGS(22)')
b5 = KeyboardButton(text='GR-RF610WE-PMS(06)')
b6 = KeyboardButton(text='GR-RF610WE-PMS(37)')
b7 = KeyboardButton(text='GR-AG820U-C(X)')
b8 = KeyboardButton(text='GR-AG820U-C(PGB)')
b9 = KeyboardButton(text='GR-AG820U-C(GG)')
b10 = KeyboardButton(text='GR-AG820U-C(XK)')
b11 = KeyboardButton(text='GR-A820U-C(BS)')
b12 = KeyboardButton(text='GR-HG655UDZ-C(GG)')
b13 = KeyboardButton(text='GR-HG655UDZ-C(XK)')
b14 = KeyboardButton(text='GR-RT624WE-PMJ(06)')
b15 = KeyboardButton(text='GR-RT624WE-PMJ(37)')
b16 = KeyboardButton(text='GR-RT559WE-PMJ(06)')
b17 = KeyboardButton(text='GR-RT468WE-PMJ(06)')
b18 = KeyboardButton(text='GR-RT468WE-PMJ(37)')
b19 = KeyboardButton(text='GR-RB449WE-PMJ(51)')
b20 = KeyboardButton(text='GR-RB449WE-PMJ(49)')
b21 = KeyboardButton(text='GR-RB449WE-PMJ(06)')
b22 = KeyboardButton(text='GR-RB308WE-DGJ(06)')
orqaga = KeyboardButton(text='Qaytish')

kiyim_menyu.add(b1, b2, b3, b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b5,b16,b17,b18,b19,b20,b21,b22,orqaga)

fut_k = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

d1 = KeyboardButton(text='VC-DR200AC(B)')
d2 = KeyboardButton(text='VC-DR220AC(G)')
orqaga = KeyboardButton(text='Qaytish')
fut_k.add(d1, d2,orqaga)



fut = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

y1 = KeyboardButton(text='DW-14F2CIS(BS)-UZ')
y2 = KeyboardButton(text='DW-14F2CIS(SS)-UZ')
y3 = KeyboardButton(text='DW-10F1CIS(W)-UZ')
y4 = KeyboardButton(text='DW-10F1CIS(S)-UZ')
orqaga = KeyboardButton(text='Qaytish')
fut.add(y1, y2,y3,y4,orqaga )



kir_moshin = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

h1 = KeyboardButton(text='TW-BJ100M4GE(SK)')
h2 = KeyboardButton(text='TW-BJ100M4GE(WK)')
h3 = KeyboardButton(text='TW-BL70A2UZ(SS)')
h4 = KeyboardButton(text='TW-BL70A2UZ(WK)')
h5 = KeyboardButton(text='TW-BL80A2UZ(WK)')
h6 = KeyboardButton(text='TW-BL80A2UZ(SK)')
h7 = KeyboardButton(text='TW-BL90A4UZ(SS)')
h8 = KeyboardButton(text='TW-BL90A4UZ(WK)')
h9 = KeyboardButton(text='TW-BL100A4UZ(SS)')
h10 = KeyboardButton(text='TW-BL100A4UZ(WK)')
h11 = KeyboardButton(text='TW-BK90G4UZ(SK)')
h12 = KeyboardButton(text='TW-BK90G4UZ(WK)')
h13 = KeyboardButton(text='TW-BK90S2GUZ(WK)')
h14 = KeyboardButton(text='TW-BK100G4UZ(SK)')
h15 = KeyboardButton(text='TW-BK100G4UZ(WK)')
h16 = KeyboardButton(text='TW-BK100S2GUZ(SK)')
h17 = KeyboardButton(text='TW-BK100S2GUZ(WK)')
h18 = KeyboardButton(text='TW-BK110G4UZ(SK)')
h19 = KeyboardButton(text='TW-BK110G4UZ(WK)')
orqaga = KeyboardButton(text='Qaytish')


kir_moshin.add(h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,h19,orqaga)
