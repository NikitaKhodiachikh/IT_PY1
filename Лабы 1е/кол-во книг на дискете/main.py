# TODO Найдите количество книг, которое можно разместить на дискете
one_symbol = 4
symbol_in_stroke = 25 * one_symbol
stroke_in_page = 50 * symbol_in_stroke
page_in_book = 100 * stroke_in_page
V_DiCKETbI = 1.44 * 1024 * 1024
Fin = V_DiCKETbI // page_in_book
print("Количество книг, помещающихся на дискету:", int(Fin))
