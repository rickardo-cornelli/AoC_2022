"""This script solves the fifth day's advent of code problems"""
def prepare_piles(number_of_piles, filename):
    """ prepare the piles used at the end. the only hardcoded part is the number of piles
        and a small manipulation """
    
    list_of_piles = [ [] for _ in range(number_of_piles) ]
    with open(filename,'r',encoding='utf_8') as input_text:
        lines = input_text.readlines()
        i = 0
        while len(lines[i].split()) > 0:
            crates = lines[i].split()
            # print(crates)
            for index, crate in enumerate(crates):
                crate_content= crate.replace("[","").replace("]","")
                # use ord() to check ascii code of crate content
                if len(crate_content) > 0 and 65 <= ord(crate_content) <= 90:
                    list_of_piles[index].append(crate_content)
            i += 1
    input_text.close()
    print(list_of_piles)
    return list_of_piles

def process_instructions(list_of_piles, starting_line, filename):
    """Processes move instructions from filename. instructions start at starting_line"""
    with open(filename,'r',encoding='utf_8') as input_text:
        lines = input_text.readlines()
        print(lines[starting_line].split())
        for line in lines[starting_line:]:
            instruction = line.split()
            if instruction[0] == 'move':
                move_crate_content(int(instruction[1]), list_of_piles[int(instruction[3])-1], list_of_piles[int(instruction[5])-1])

def move_crate_content(number_of_objects, source, destination):
    """takes in a number of objects to move and moves them from destination to source"""
    boxes = []
    i = 0
    while i < number_of_objects:
        if len(source) > 0:
            box_to_move = source.pop(0)
            # push to the top of the stack
           # destination.insert(0,box_to_move)
            boxes.append(box_to_move)
        i +=1
    # put them in the order they were standing before
    for box in reversed(boxes):
        destination.insert(0,box)



def peek_at_boxes(piles):
    """retrieves top element of all non empty piles"""
    top_elements = ""
    for pile in piles:
        if len(pile) >0:
            print(pile[0])
            top_elements += pile[0]
    return top_elements


def main():
    piles = prepare_piles(9,'complete_input.txt')
    process_instructions(piles, 10, 'complete_input.txt')
    print(peek_at_boxes(piles))


if __name__ == "__main__":
    main()