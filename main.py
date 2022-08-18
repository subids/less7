
#
# with open('dish.txt', encoding='utf-8') as f:
#        rez = []
#        for line in f:
#         data = line.split(' | ')
#         rez.append({'name': data[0],
#                     'stock': data[1],
#                     'price': int(data[2])})
# print(rez)

#
import os

#  Ппрочитаем файл Recipes.txt
path = os.path.join(os.getcwd(), 'Recipes.txt')
with open(path, encoding='utf-8') as cook_file:
    cook_book = {}  # Создаем пустой словарь для поваренной книги
    for string in cook_file:
        dish = string.strip()
        #print(dish)# Выбираем из файла название блюда
        ingredients_count = int(cook_file.readline().strip())  # Выбираем из файла количество ингредиентов
        dish_dict = []  # Создаем пустой список для словарей с блюдами поваренной книги
        for item in range(ingredients_count):
            #  Выбираем из файла ингредиенты по разделителю '|'
            ingredient_name, quantity, measure = cook_file.readline().strip().split('|')
            #print(ingredient_name, quantity, measure)
            #  Добавляем в список словари с ингредиентами
            dish_dict.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[dish] = dish_dict  #  Добавляем в поваренную книгу блюда и их ингредиенты
        cook_file.readline()


    #print(cook_book)
#
#  Создаем функцию для получения списка покупок исходя из заказанных блюд и количества персон
def get_shop_list_by_dishes(dishes, person_count):
    grocery_dict = {}  # Создаем пустой словарь для хранения списка покупок
    for _dish in dishes:
        for ingredient in cook_book[_dish]:  # Выбираем ингредиенты для блюд из поваренной книги
            #  Добавляем ингредиеты, увеличивая их количество на число персон
            ingredient_list = dict([(ingredient['ingredient_name'],
                                     {'quantity': int(ingredient['quantity']) * person_count,
                                      'measure': ingredient['measure']})])
            print(ingredient_list)
            if grocery_dict.get(ingredient['ingredient_name']) == 'None':
                _merger = (int(grocery_dict[ingredient['ingredient_name']]['quantity']) +
                           int(ingredient_list[ingredient['ingredient_name']]['quantity']))
                grocery_dict[ingredient['ingredient_name']]['quantity'] = _merger
            else:
                grocery_dict.update(ingredient_list)
    return grocery_dict


get_shop_list_by_dishes(['Запеченный картофель',  'Омлет'], 2)