from math import floor
def prepare_data():
    """Take input data, divide each line into two lists and find their intersection
        add the intersecting elements to a new list """
    total_priority = 0
    with open('input.txt', 'r', encoding='utf_8') as f:
        lines = f.readlines()
        for line in lines:
            whole_rucksack = list(line.rstrip())
            length = len(whole_rucksack)
           # print("\n")
           # print(length)
            middle_index = floor(length /2)
          #  print("\n")
            #print(middle_index)
            #print("\n")
            first_compartment = whole_rucksack[:middle_index]
            # print(first_compartment)
         #   print("\n")
            second_compartment = whole_rucksack[middle_index:]
          #  print(second_compartment)
            shared_elements = set(first_compartment).intersection(second_compartment)
           # print("\n")
            #print(shared_elements)
            for element in shared_elements:
                total_priority += get_priority_level(element)
                
    f.close()
    return total_priority

def alternative_prepare_data():
    total_priority = 0
    with open('input.txt','r', encoding='utf_8') as f:
        lines = f.readlines()
        i = 0
        # iterate through line, take 
        # [0 1 2] [3 4 5] [6 7 8] 9 
        while i + 2 < len(lines):
            # iterate through the list and make groups of three of elfs
            first_elf = list(lines[i].rstrip())
            second_elf = list(lines[i+1].rstrip())
            third_elf = list(lines[i+2].rstrip())
            # find the intersection of the three elfs and determine the priority level of the 
            # shared elements
            shared_elements = set(first_elf).intersection(second_elf, third_elf)
            for element in shared_elements:
                total_priority += get_priority_level(element)
        
            # increment i to proceed in the list
            i = i + 3
    f.close()
    return total_priority






def get_priority_level(s):
    """use ascii to get priority level
        a-z: 97-122     A-Z: 65-90  """
    num = ord(s)
    if  97 <= num <= 122:
        priority_level = num - 96
    if  65 <= num <= 90:
        priority_level = num - 38
    return priority_level


def main():
    print("hej")
    print(alternative_prepare_data())



if __name__ == "__main__":
    main()