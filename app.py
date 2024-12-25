from functions import *
import csv
from colorama import Fore, Style


data_list = []



if __name__ == '__main__':
    with open('diamonds.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            data_list.append(lines)
    # Separates the header from data table
    headers = data_list.pop(0)

    while True:
        try:
            users_choise = Actions(int(menu()))
        except ValueError:
            print("Incorrect choise")
            continue
        if users_choise is Actions.EXIT: break
        elif users_choise is Actions.HIGEST_PRICE:
            clear_terminal()
            print(f"The most expensive dimond`s price is:{Fore.GREEN} {(highest_price(data_list))}{Style.RESET_ALL} \n")
        elif users_choise is Actions.AVERAGE_PRICE:
            clear_terminal()
            print(f"The average price for diamond is:{Fore.GREEN} {average_price(data_list)}{Style.RESET_ALL}\n")
        elif users_choise is Actions.IDEAL_QUANTITY:
            clear_terminal()
            print(f"The amount of diamond with ideal cut is:{Fore.GREEN} {ideal_cut(data_list)}{Style.RESET_ALL}\n")
        elif users_choise is Actions.COLORS_NAME_AND_QUANTITY:
            clear_terminal()
            print(colors_names_and_quantity(data_list))
        elif users_choise is Actions.MEDIAN_CARAT_FOR_PREMIUM:
            clear_terminal()
            print(f"The median carat for premium cut is: {Fore.GREEN}{median_karat_for_premium_cut(data_list)} {Style.RESET_ALL}\n")
        elif users_choise is Actions.CARAT_AVERAGE_FOR_EACH_CUT:
            clear_terminal()
            print(carat_average_for_each_cut(data_list))
            
        elif users_choise is Actions.PRICE_AVERAGE_FOR_EACH_CARAT:
            clear_terminal()
            print(price_average_for_each_carat(data_list))
        
    
    

    
