import datetime
import os
import pathlib

def main():

    dirpath = str(datetime.datetime.today().isoweekday())
    os.chdir(os.getcwd() + '/menu/' + dirpath)

    soups_s = ", ".join(soups())
    main_dish_s = ", ".join(main_dish())
    side_dish_s = ", ".join(side_dish())
    drinks_s = ", ".join(drinks())
    salads_s = ", ".join(salads())

    menu = [
       ['Супы: ', soups_s],
       ['Горячее: ', main_dish_s],
       ['Гарниры: ', side_dish_s],
       ['Напитки: ', drinks_s],
       ['Салаты: ', salads_s]
    ]
    
    os.chdir('..')
    os.chdir('..')

    return menu




def soups():
    soups = []
    with open('soups.txt', 'r', encoding='utf-8') as soups:
        soups = soups.read().split('\n')
    return soups

def main_dish():
    main_dish = []
    with open ('main_dish.txt', 'r', encoding='utf-8') as main_dish:
        main_dish = main_dish.read().split('\n')
    return main_dish

def side_dish():
    side_dish = []
    with open ('side_dish.txt', 'r', encoding='utf-8') as side_dish:
        side_dish = side_dish.read().split('\n')
    return side_dish

def drinks():
    drinks = []
    with open ('drinks.txt', 'r', encoding='utf-8') as drinks:
        drinks = drinks.read().split('\n')
    return drinks

def salads():
    salads = []
    with open ('salads.txt', 'r', encoding='utf-8') as salads:
        salads = salads.read().split('\n')
    return salads

if __name__ == '__main__':
    main()