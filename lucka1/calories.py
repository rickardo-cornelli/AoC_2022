""" get groupby do to stuff """
from itertools import groupby



def get_calories_per_elf():
    """hello this is my hting"""
    calories_per_elf = []
    calories_per_elf_as_int =[]

    with open ('input.txt', 'r', encoding= 'UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            calories_per_elf.append(line.strip())
    f.close()

    list_of_calories_per_elf = [list(g) for k, g in groupby(calories_per_elf, key=bool) if k]
    for elf_list in list_of_calories_per_elf:
        res = [int(i) for i in elf_list]
        calories_per_elf_as_int.append(res)
    return calories_per_elf_as_int

def get_max_list_total(list_of_lists):
    """ make a list of the sums of lists and return the max"""
    sums = [sum(i) for i in list_of_lists]
    return max(sums)

def top_three_total_calories_per_elf(list_of_calories_per_elf):
    sums = [sum(i) for i in list_of_calories_per_elf]
    sums.sort(reverse= True)
    top_three = sums[:3]
    return sum(top_three)

def main():
    """snopp"""
    list_of_elf_calories = get_calories_per_elf()
    most_calories = get_max_list_total(list_of_elf_calories)
    print(top_three_total_calories_per_elf(list_of_elf_calories))
    
 
if __name__ == '__main__':
    main()