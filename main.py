import pprint as pprint

recip_file = "D:\\pycharmTests\\HW_cook_book\\recipes.txt"
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

class cook_book:
    def read_cook_book(self):
        with open(recip_file, encoding='utf-8') as file:
            new_cook_book = {}
            for dish in file.read().split('\n\n'):
                dish_name, ingr_cnt, *ingridients = dish.split('\n')
                cur_dish = []
                for ingridient in ingridients:
                    if ingridient != '':                        
                        ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, ingridient.split(' | '))
                        cur_dish.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
                new_cook_book[dish_name] = cur_dish            
        return new_cook_book

    def get_shop_list_by_dishes(self, dishes, person_count):
        cook_book = self.read_cook_book()
        ingridients_list = {}
        for dish in dishes:
            cur_item = cook_book[dish]           
            for cur_ingr in cur_item:                
                if cur_ingr.get('ingredient_name') in ingridients_list.keys():
                    ingridients_list[cur_ingr.get('ingredient_name')] += cur_ingr.get('ingredient_name')
                else:    
                    tmp_dict = {'measure': cur_ingr.get('measure'), 'quantity': person_count*cur_ingr.get('quantity')}
                    ingridients_list.update({cur_ingr.get('ingredient_name'): tmp_dict})                
        pprint.pprint(ingridients_list)

my_book = cook_book()
my_book.get_shop_list_by_dishes(dishes, person_count)