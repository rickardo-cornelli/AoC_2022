import numpy as np

def prep_data():
    with open('complete_input.txt', 'r', encoding = 'utf_8') as f:
        with open('complete_enhanced_input.txt', 'w', encoding='utf_8') as w:
            for line in f.readlines():
                # text = " ".join(line)
                new_text = line.replace("", " ")
                w.write(new_text)  
    w.close()
    f.close()
    return

def prep_array():
  #  tree_heights = np.loadtxt('complete_enhanced_input.txt', dtype=int)
    tree_heights = np.loadtxt('complete_enhanced_input.txt', dtype=int)
    return tree_heights

def visible_from_above(i,j, array):
    elements_above = array[:i, j]
    return array[i,j] > np.max(elements_above)

def visible_from_below(i,j,array):
    elements_below = array[(i+1):, j]
    return array[i,j] > np.max(elements_below)

def visible_from_left(i,j,array):
    elements_to_the_left = array[i, :j]
    return array[i,j] > np.max(elements_to_the_left)

def visible_from_right(i,j,array):
    elements_to_the_right = array[i, j+1:]
    return array[i,j] > np.max(elements_to_the_right)

def visible_from_any_direction(i,j,array):
    from_above = visible_from_above(i,j,array)
    from_below = visible_from_below(i,j,array)
    from_left = visible_from_left(i,j,array)
    from_right = visible_from_right(i,j,array)
    """if(from_above):
        print(f"\n {array[i,j]} at {i},{j} is visible from above")
    if(from_below):
        print(f"\n {array[i,j]} at {i},{j} is visible from below")
    if(from_left):
        print(f"\n {array[i,j]} at {i},{j} is visible from left")
    if(from_right):
        print(f"\n {array[i,j]} at {i},{j} is visible from right")"""
    return from_above or from_below or from_left or from_right

def check_all_trees(tree_array):
    visible_trees = 0
    rows = tree_array.shape[0]
    cols = tree_array.shape[1]
    visible_trees += 2*(rows) + 2*(cols) -4
    ## only check internal trees i.e. not on edge
    # that is: rows from (1 -> cols -1)
    # cols from (1 to cols -1)
    # trees on the edge are: 
    # print(tree_array)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if visible_from_any_direction(i,j,tree_array):
                visible_trees += 1
    return visible_trees

def scenic_score_above(i,j,array):
    elements_above = array[:i, j]
    score = 0
    for elem in np.flip(elements_above):
        if array[i,j] > elem:
        #    print(f"\n elem above is: {elem}")
       #     print(f"\n {array[i,j]} is bigger than {elem}")
            score += 1
        else:
            score += 1
            break
    #print(f"\n scenic above är: {score}")
    return score 

def scenic_score_below(i,j,array):
    elements_below = array[(i+1):, j]
    score = 0
    for elem in elements_below:
        if array[i,j] > elem:
           # print(f"\n elem below is: {elem}")
            #print(f"\n {array[i,j]} is bigger than {elem}")
            score += 1
        else:
            score += 1
            break
   # print(f"\n scenic below är: {score}")
    return score 

def scenic_score_left(i,j,array):
    elements_to_the_left = array[i, :j]
    score = 0
    for elem in np.flip(elements_to_the_left):
        if array[i,j] > elem:
       #     print(f"\n elem to left is: {elem}")
      #      print(f"\n {array[i,j]} is bigger than {elem}")
            score += 1
        else:
            score += 1
            break
    #print(f"\n scenic left är: {score}")
    return score 

def scenic_score_right(i,j,array):
    elements_to_the_right = array[i, j+1:]
    score = 0
    for elem in elements_to_the_right:
        if array[i,j] > elem:
       #     print(f"\n elem to the right is: {elem}")
      #      print(f"\n {array[i,j]} is bigger than {elem}")
            score += 1
        else:
            score += 1
            break
    #print(f"\n scenic right är: {score}")
    return score 

def get_scenic_score(i,j,array):
    above = scenic_score_above(i,j,array)
    below = scenic_score_below(i,j,array)
    left = scenic_score_left(i,j,array)
    right = scenic_score_right(i,j,array)
    """
    print(f"\n array elem {array[i,j]} at {i},{j} has scenic score above {above}")
    print(f"\n array elem {array[i,j]} at {i},{j} has scenic score below {below}")
    print(f"\n array elem {array[i,j]} at {i},{j} has scenic score left {left}")
    print(f"\n array elem {array[i,j]} at {i},{j} has scenic score right {right}")
    """
    return above* below * left * right

def get_max_scenic_score(array):
    current_max = 0
    rows = array.shape[0]
    cols = array.shape[1]
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            scenic = get_scenic_score(i,j,array)
            if scenic > current_max:
                current_max = scenic
    return current_max

# def compare_above(i,j, arr):
def main():
    trees = prep_array()
    #get_scenic_score(3,2,trees)
    # get_scenic_score(1,2,trees)
    #scenic_score_right(1,2,trees)
    # scenic_score_left(1,2,trees)
    print(get_max_scenic_score(trees))
if __name__ == "__main__": 
    main()