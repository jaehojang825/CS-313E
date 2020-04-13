#File: BabyNames.py

#Description: allows user to query a data base of 1000 most popular baby names in US

#Student Name: Jaeho Jang

#Student UT EID: jj36386

#Course Name: CS 313E

#Unique Number: 50300

#Date Created: 2/9/10

#Date Last Modified: 2/10/10

name_ranking = {}

with open('names.txt') as names_file:
    for names in names_file:
        (key,val) = names.rstrip('\n').split(' ',1)
        list = val.split()
        int_list = []
        for string_number in list:
            int_list.append(int(string_number))
        name_ranking[key] = int_list

def display_menu():
    menu = int(input('''
Options:
Enter 1 to search for names
Enter 2 to display data for one name
Enter 3 to display all names that appear in only one decade
Enter 4 to display all names that appear in all decade
Enter 5 to display all names that are more popular in every decade
Enter 6 to display all names that are less popular in every decade
Enter 7 to quit

Enter a choice:'''))
    return menu

def name_check(name_input):
    key_list = []
    for name in name_ranking.keys():
        key_list.append(name)

    if name_input in key_list:
        return True
    else:
        return False

def highest_ranking_decade(name):
    name_decade = name_ranking[name]
    index = 0
    minimum = 10000000
    for i in range(11):
        if name_decade[i] < minimum:
            minimum = name_decade[i]
            index = i
    index = index * 10 + 1900
    return index

def rankings_of_name():
    name_input = input('Enter a name:')

    rankings = name_ranking.get(name_input,0)

    print('\n'+name_input,':',end=' ')
    print(*rankings,sep=' ')
    index = 1900

    for i in rankings:
        print(index,':',i)
        index+=10

    return rankings

def app_one_decade():
    decade_input = int(input('Enter decade:'))
    list_of_names_and_ranks = []
    index = int((decade_input - 1900)/10);

    for key, value in name_ranking.items():
        if value[index] is not 0:
            list_of_names_and_ranks.append((value[index],key));

    return list_of_names_and_ranks


def all_decade_ex():
    list_of_names = []
    for key, value in name_ranking.items():
        is_in_all_decades = True
        for i in range(11):
            if value[i] is 0:
                is_in_all_decades = False
        if is_in_all_decades:
            list_of_names.append(key)

    return list_of_names

def increasing_pop_name():
    list_of_names = []
    for key, value in name_ranking.items():
        if_increasing = True
        for i in range(len(value)-1):
            if value[i] <= value[i+1]:
                if_increasing = False
        if if_increasing:
            list_of_names.append(key)

    return list_of_names

def decreasing_pop_name():
    list_of_names = []
    for key, value in name_ranking.items():
        if_increasing = True
        for i in range(len(value)-1):
            if i is 9 and value[i+1] is 0:
                break
            if value[i] >= value[i+1]:
                if_increasing = False
        if if_increasing:
            list_of_names.append(key)

    return list_of_names

def main():
    show_menu = 0
    while show_menu != 7:
        show_menu = display_menu()
        if show_menu == 1:
            name_input = input('Enter a name:')
            checking = name_check(name_input)
            if checking is True:
                decade_of_name = highest_ranking_decade(name_input)
                print('')
                print('The matches with their highest ranking decade are:')
                print(name_input,decade_of_name)
            if checking is False:
                print(name_input,'does not appear in any decade.')
        if show_menu == 2:
            rankings_of_name()
        if show_menu == 3:
            try:
                names_by_decade = app_one_decade()
                names_by_decade.sort()
                for i in names_by_decade:
                    print(i[1],i[0])
            except:
                print('Please enter a appropriate decade.')
        if show_menu == 4:
            name_in_all_decade = all_decade_ex()
            length_of_list = len(name_in_all_decade)
            print(length_of_list,'names appear in every decade. The names are:')
            for i in name_in_all_decade:
                print(i)
        if show_menu == 5:
            increasing_names = increasing_pop_name()
            length_of_list = len(increasing_names)
            print(length_of_list,'names are more popular in every decade.')
            for i in increasing_names:
                print(i)
        if show_menu == 6:
            decreasing_names = decreasing_pop_name()
            length_of_list = len(decreasing_names)
            print(length_of_list,'names are less popular in every decade.')
            for i in decreasing_names:
                print(i)
    print('')
    print('')
    print('Goodbye.')
main()
