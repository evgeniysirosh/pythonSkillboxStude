#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['мама,папа,сестра']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Наталья',160,'Сергей',180,'Катерина',150],
]
height_pather = int(my_family_height[0][my_family_height[0].index(180)])
height_mother = int(my_family_height[0][my_family_height[0].index(160)])
height_sister = int(my_family_height[0][my_family_height[0].index(150)])

print('Рост отца -', height_pather , 'ХХ см')

sum_family_height = height_sister + height_mother + height_sister
print('Общий рост моей семьи -' ,sum_family_height, 'ХХ см')

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
