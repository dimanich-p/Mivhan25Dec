from enum import Enum
import os
from colorama import Fore,Style

class Actions(Enum):
    HIGEST_PRICE = 1
    AVERAGE_PRICE = 2
    IDEAL_QUANTITY = 3
    COLORS_NAME_AND_QUANTITY = 4
    MEDIAN_CARAT_FOR_PREMIUM = 5
    CARAT_AVERAGE_FOR_EACH_CUT = 6
    PRICE_AVERAGE_FOR_EACH_CARAT = 7
    EXIT = 8

def clear_terminal():
    os.system("cls")

# presents the menu and gets user choise
def menu():
    for act in Actions:
        print(f"{Fore.RED}{act.value}{Style.RESET_ALL} - {Fore.BLUE}{act.name}{Style.RESET_ALL}")
    return input("Your selection: ")

# all functions bellow, perfoming analisis of data file as their.names
def highest_price(data):
    highest = "0"
    for item in data:
        if item[6] > highest: highest = item[6]
    return highest

def average_price(data):
    prices_count = 0
    sum = 0
    for item in data:
        prices_count +=1
        sum += int(item[6])
    return sum/prices_count

def ideal_cut(data):
    counter = 0
    for item in data:
        if item[1] == 'Ideal':
            counter +=1
    return counter

def colors_names_and_quantity(data):
    colors_set = set()
    ret_dict = {}
    ret_string =""
    for item in data:
        colors_set.add(item[2])
    for color in colors_set:
        counter = 0
        for item in data:
            if color == item[2]:counter +=1
        ret_dict.update({color:counter})
    for key,value in ret_dict.items():
        ret_string += f"Color:{Fore.GREEN}{key}{Style.RESET_ALL} has quantity of {Fore.YELLOW}{value}.{Style.RESET_ALL} \n"
    return ret_string

def median_karat_for_premium_cut(data):
    carat_list = []
    for item in data:
        if item[1] == 'Premium':carat_list.append(item[0])
    carat_list.sort()
    return carat_list[len(carat_list)//2]

def carat_average_for_each_cut(data):
    cuts_set = set()
    ret_dict = {}
    ret_string = ""
    for item in data:
        cuts_set.add(item[1])
    for cut in cuts_set:
        carat_total = 0
        counter = 0
        for item in data:
            if item[1] == cut:
                counter += 1
                carat_total += float(item[0])
        ret_dict.update({cut:carat_total/counter})
    for key,value in ret_dict.items():
        ret_string += f"Cut {Fore.GREEN}{key}{Style.RESET_ALL} has average of: {Fore.YELLOW}{value}{Style.RESET_ALL}. \n"
    return ret_string

def price_average_for_each_carat(data):
    carat_set = set()
    ret_dict = {}
    ret_string = ""
    for item in data:
        carat_set.add(item[0])
    for carat in carat_set:
        counter = 0
        price_total = 0
        for item in data:
            if item[0] == carat:
                counter += 1
                price_total += int(item[6])
        ret_dict.update({carat:price_total/counter})
    for key,value in ret_dict.items():
        ret_string += f"Carat of:{Fore.GREEN}{key}{Style.RESET_ALL} has average price of {Fore.YELLOW}{value}{Style.RESET_ALL}. \n"
    return ret_string

 
    