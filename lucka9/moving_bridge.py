import numpy as np
"""Solves the 9th day's problem in Advent of Code 2022"""

def prep_bridge():
    bridge = np.zeros([1000,1000])
    return bridge

def move_based_on_input(bridge):
    head = [499,499]
    tails = [[499,499],[499,499],[499,499],[499,499],[499,499],[499,499],[499,499],[499,499],[499,499]]
    with open('complete_input.txt', 'r', encoding='utf_8') as f:
       # print(f"\n bridge is at: {head}")
        #print(f"\n tail is at: {tail}")

        for line in f.readlines():
            instruction = line.split()
        #    print(f"\n head is before {instruction[1]} steps {instruction[0]} at: {head}")
        #    print(f"\n tail is before at: {tail}")
            head, tails, bridge = move_head(head, tails, bridge, instruction[0], int(instruction[1]))
        #    print(f"\n head is after at: {head}")
        #    print(f"\n tail is after at: {tail}")
       # print(bridge)
        print(np.count_nonzero(bridge))

def move_head(head, tails, bridge, direction, num_steps):
    steps_taken = 0
    while steps_taken < num_steps:
        if direction == 'U':
            head[0] -= 1
        elif direction == 'D':
            head[0] += 1
        elif direction == 'L':
            head[1] -= 1
        else:
            head[1] += 1
        for tail_number, current_tail in enumerate(tails):
            if tail_number == 0:
                update_tail_pos(head, current_tail)
            else:
                update_tail_pos(tails[tail_number -1], current_tail)
        bridge[tuple(tails[8])] += 1
        steps_taken += 1
    return head, tails, bridge

def update_tail_pos(head,tail):
    # same column but different rows
  #  print(f"\n head is at: {head}, tail is at: {tail}")
    vertical_difference = head[0] - tail[0]
    horizontal_difference = head[1] - tail[1]
    if not(abs(vertical_difference) + abs(horizontal_difference) <= 1 or abs(vertical_difference) == abs(horizontal_difference) == 1):

        if abs(vertical_difference) == 2 and horizontal_difference == 0:
            tail = move_tail_vertically(vertical_difference, tail)
        elif abs(horizontal_difference) == 2 and vertical_difference == 0:
            tail = move_tail_horizontally(horizontal_difference, tail)
        else:
   #         print(f"\n before diagonal move: hor_diff is {horizontal_difference} and ver_diff is {vertical_difference}")
   #         print(f" head is before diagonal at: {head} and tail is at: {tail}")
            tail = move_tail_diagonally(horizontal_difference, vertical_difference,tail)
    return tail

def move_tail_vertically(vertical_difference,tail):
    if vertical_difference == 2:
     #   print("\n moving down tail one step")
        tail[0] += 1
      #  print(f" tail is now at: {tail}")
    else: 
      #  print("\n moving up tail one step")
        tail[0] -= 1
      #  print(f" tail is now at: {tail}")
    return tail

def move_tail_horizontally(horizontal_difference,tail):
    if horizontal_difference == 2:
      #  print("\n moving tail to the right one step")
        tail[1] += 1
    else:
      #  print("\n moving tail to the left one step") 
        tail[1] -= 1
    return tail

def move_tail_diagonally(horizontal_difference, vertical_difference,tail):
    tail[1] += int(horizontal_difference/abs(horizontal_difference))
    tail[0] += int(vertical_difference/abs(vertical_difference))
  #  print(f"\n tail_x was moved: {int(horizontal_difference/abs(horizontal_difference))}")
  #  print(f" tail_y was moved: {int(vertical_difference/abs(vertical_difference))}")
  #  print(f"\n after diagonal: tail is at {tail}")
    return tail

def main():
    bridge = prep_bridge()
    move_based_on_input(bridge)

if __name__ == "__main__":
    main()