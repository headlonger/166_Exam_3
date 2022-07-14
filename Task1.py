# 1. Напишите функцию, которая запрашивает у пользователя номер карты, CVC-код и PIN-код. После этого выводит на экран
# номер карты с первыми четырьмя цифрами, остальные заменены на звездочки, CVC-код в виде
# ###, и PIN-код в виде &&&0 (вместо 0 последняя цифра).
# 1234567891011121

def card(cardnum, cvc, pin):
    print(f'\nНомер карты: {cardnum[0:4] + " **** **** ****"}\nCVC-код: ###\nPIN-код: {"&&&" + pin[3]}')


cardnum = ''
cvc = ''
pin = ''

# while cardnum != 16:
#     cardnum = input('Введите номер карты: ')
#
#     if len(cardnum) == 16 and cardnum.isdigit():
#         cvc = input('Введите CVC: ')
#         if len(cvc) == 3 and cvc.isdigit():
#             pin = input('Введите PIN: ')
#         else:
#             print('Вы ввели неверный cvc карты!')
#             if len(pin) == 4 and pin.isdigit():
#                 card(cardnum, cvc, pin)
#             else:
#                 print('Вы ввели неверный pin карты!')
#     else:
#         print('Вы ввели неверный номер карты!')

while len(cardnum) != 16:
    cardnum = input('Введите номер карты: ')

while len(cvc) != 3:
    cvc = input('Введите CVC: ')

while len(pin) != 4:
    pin = input('Введите PIN: ')

card(cardnum, cvc, pin)
