from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

infor = InlineKeyboardMarkup(row_width=1)
infor.add(InlineKeyboardButton("Назад", callback_data="back_main"))

theory = InlineKeyboardMarkup(row_width=1)
theory.add(InlineKeyboardButton("Справочные материалы", callback_data="sprav1"))
theory.add(InlineKeyboardButton("Алгебра", callback_data="algebra"))
theory.add(InlineKeyboardButton("Геометрия", callback_data="geometry"))
theory.add(InlineKeyboardButton("Назад", callback_data="back_main"))

urlkb = InlineKeyboardMarkup(row_width=1)
urlkb.add(InlineKeyboardButton("Справочные материалы", callback_data="sprav"))
urlkb.add(InlineKeyboardButton(text='Демоверсия, спецификация, кодификатор', url='https://fipi.ru/oge/demoversii-specifikacii-kodifikatory?ysclid=lpzxynp2uz878966881#!/tab/173801626-2'))
urlkb.add(InlineKeyboardButton(text='Банк задач ФИПИ', url='https://oge.fipi.ru/bank/index.php?proj=DE0E276E497AB3784C3FC4CC20248DC0'))
urlkb.add(InlineKeyboardButton(text='РЕШУ ОГЭ', url='https://math-oge.sdamgia.ru/?redir=&ysclid=lpzy7akewk187964325'))
urlkb.add(InlineKeyboardButton("Назад", callback_data="back_theory"))

algebra_theory = InlineKeyboardMarkup(row_width=1)
algebra_theory.add(InlineKeyboardButton("Формулы Сокр. Умножения", callback_data="sokr_umnozh"))
algebra_theory.add(InlineKeyboardButton("Свойства арифметического корня", callback_data="koren"))
algebra_theory.add(InlineKeyboardButton("Свойства степеней", callback_data="stepen"))
algebra_theory.add(InlineKeyboardButton("Решение уравнений", callback_data="uravn"))
algebra_theory.add(InlineKeyboardButton("Решение неравенств", callback_data="neravenstv"))
algebra_theory.add(InlineKeyboardButton("Функции", callback_data="funct"))
algebra_theory.add(InlineKeyboardButton("Теория Вероятностей", callback_data="veroyat"))
algebra_theory.add(InlineKeyboardButton("Прогрессия", callback_data="progr"))
algebra_theory.add(InlineKeyboardButton("Назад", callback_data="back_theory"))

geom_theory = InlineKeyboardMarkup(row_width=1)
geom_theory.add(InlineKeyboardButton("Углы", callback_data="ugl"))
geom_theory.add(InlineKeyboardButton("Треугольник", callback_data="treugolnik"))
geom_theory.add(InlineKeyboardButton("Теорема Пифагора", callback_data="t_pif"))
geom_theory.add(InlineKeyboardButton("Параллелограмм", callback_data="parallelogramm"))
geom_theory.add(InlineKeyboardButton("Трапеция", callback_data="trapet"))
geom_theory.add(InlineKeyboardButton("Окружность", callback_data="okru"))
geom_theory.add(InlineKeyboardButton("Многоугольники", callback_data="mnogougol"))
geom_theory.add(InlineKeyboardButton("Теоремы", callback_data="teorem"))
geom_theory.add(InlineKeyboardButton("Назад", callback_data="back_theory"))

inadd = InlineKeyboardMarkup(row_width=1)
inadd.add(InlineKeyboardButton("Справочные материалы", callback_data="sprav"))
inadd.add(InlineKeyboardButton("Формулы Сокр. Умножения", callback_data="sokr_umnozh"))
inadd.add(InlineKeyboardButton("Свойства арифметического корня", callback_data="koren"))
inadd.add(InlineKeyboardButton("Свойства степеней", callback_data="stepen"))
inadd.add(InlineKeyboardButton("Решение уравнений", callback_data="urav"))
inadd.add(InlineKeyboardButton("Решение неравенств", callback_data="neravenstv"))
inadd.add(InlineKeyboardButton("Функции", callback_data="funct"))
inadd.add(InlineKeyboardButton("Теория Вероятностей", callback_data="veroyat"))
inadd.add(InlineKeyboardButton("Прогрессия", callback_data="progr"))
inadd.add(InlineKeyboardButton("Углы", callback_data="ugl"))
inadd.add(InlineKeyboardButton("Треугольник", callback_data="treugolnik"))
inadd.add(InlineKeyboardButton("Теорема Пифагора", callback_data="t_pif"))
inadd.add(InlineKeyboardButton("Параллелограмм", callback_data="parallelogramm"))
inadd.add(InlineKeyboardButton("Трапеция", callback_data="trapet"))
inadd.add(InlineKeyboardButton("Окружность", callback_data="okru"))
inadd.add(InlineKeyboardButton("Многоугольники", callback_data="mnogougol"))
inadd.add(InlineKeyboardButton("Теоремы", callback_data="teorem"))

prog = InlineKeyboardMarkup(row_width=1)
prog.add(InlineKeyboardButton("Арифметическая прогрессия", callback_data="ar_prog"))
prog.add(InlineKeyboardButton("Геометрическая прогрессия", callback_data="ge_prog"))
prog.add(InlineKeyboardButton("Назад", callback_data="back_theme"))

func = InlineKeyboardMarkup(row_width=1)
func.add(InlineKeyboardButton("Минимум про все типы функций", callback_data="all_func"))
func.add(InlineKeyboardButton("Линейная функция", callback_data="lin_func"))
func.add(InlineKeyboardButton("Квадратная функция", callback_data="kva_func"))
func.add(InlineKeyboardButton("Назад", callback_data="back_theme"))

urav = InlineKeyboardMarkup(row_width=1)
urav.add(InlineKeyboardButton("Линейное", callback_data="lin_urav"))
urav.add(InlineKeyboardButton("Квадратное", callback_data="kvad_urav"))
urav.add(InlineKeyboardButton("Дробно-рациональное", callback_data="drob_urav"))
urav.add(InlineKeyboardButton("Система уравнений", callback_data="sis_urav"))
urav.add(InlineKeyboardButton("Назад", callback_data="back_theme"))

nerav = InlineKeyboardMarkup(row_width=1)
nerav.add(InlineKeyboardButton("Линейное", callback_data="lin_nerav"))
nerav.add(InlineKeyboardButton("Квадратное", callback_data="kvad_nerav"))
nerav.add(InlineKeyboardButton("Дробно-рациональное", callback_data="drob_nerav"))
nerav.add(InlineKeyboardButton("Система неравенств", callback_data="sis_nerav"))
nerav.add(InlineKeyboardButton("Назад", callback_data="back_theme"))


treug = InlineKeyboardMarkup(row_width=1)
treug.add(InlineKeyboardButton("Элементы", callback_data="elem_treug"))
treug.add(InlineKeyboardButton("Площадь", callback_data="S_treug"))
treug.add(InlineKeyboardButton("Признаки равенства", callback_data="prrav_treug"))
treug.add(InlineKeyboardButton("Признаки подобия", callback_data="prpod_treug"))
treug.add(InlineKeyboardButton("Прямоугольный треугольник", callback_data="prym_treug"))
treug.add(InlineKeyboardButton("Равнобедренный теугольник", callback_data="ravnobed_treug"))
treug.add(InlineKeyboardButton("Равносторонний треугольник", callback_data="ravnostor_treug"))
treug.add(InlineKeyboardButton("Назад", callback_data="back_theme1"))

parall = InlineKeyboardMarkup(row_width=1)
parall.add(InlineKeyboardButton("Свойства и признаки", callback_data="svoystv_parall"))
parall.add(InlineKeyboardButton("Площадь", callback_data="S_parall"))
parall.add(InlineKeyboardButton("Квадрат", callback_data="kvadr_parall"))
parall.add(InlineKeyboardButton("Прямоугольник", callback_data="prym_parall"))
parall.add(InlineKeyboardButton("Ромб", callback_data="romb_parall"))
parall.add(InlineKeyboardButton("Назад", callback_data="back_theme1"))

okr = InlineKeyboardMarkup(row_width=1)
okr.add(InlineKeyboardButton("Элементы окружности и формулы", callback_data="elem_okr"))
okr.add(InlineKeyboardButton("Вписанный и описанный треугольник", callback_data="vpis_okr"))
okr.add(InlineKeyboardButton("Вписанный и описанный четырёхугольник", callback_data="vpis1_okr"))
okr.add(InlineKeyboardButton("Вписанный и центральный угол", callback_data="ugol_okr"))
okr.add(InlineKeyboardButton("Свойства касательной и секущей", callback_data="cas_okr"))
okr.add(InlineKeyboardButton("Назад", callback_data="back_theme1"))

teo = InlineKeyboardMarkup(row_width=1)
teo.add(InlineKeyboardButton("Теорема Чевы", callback_data="chev_teo"))
teo.add(InlineKeyboardButton("Теорема Менелая", callback_data="men_teo"))
teo.add(InlineKeyboardButton("Теорема Фалеса", callback_data="fal_teo"))
teo.add(InlineKeyboardButton("Теорема Птолемея", callback_data="pto_teo"))
teo.add(InlineKeyboardButton("Пересечение медиан (центроид)", callback_data="centr_teo"))
teo.add(InlineKeyboardButton("Назад", callback_data="back_theme1"))

keyboard_inline = InlineKeyboardMarkup(row_width=1)
button1 = InlineKeyboardButton(text="Теория", callback_data="theory")
button3 = InlineKeyboardButton(text="Напоминания", callback_data="notify")
button4 = InlineKeyboardButton(text="Контакты", callback_data="info")
keyboard_inline.add(button1, button3, button4)

close = InlineKeyboardMarkup(row_with=1)
close.add(InlineKeyboardButton(text="Назад", callback_data="close"))