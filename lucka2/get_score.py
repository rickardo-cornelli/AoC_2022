from encodings import utf_8


def get_score():
    """ get total score"""
    score = 0
    with open('input.txt','r', encoding= 'utf_8') as f:
        for line in f.readlines():
            outcome = line.split()
            # score += determine_score_from_round(outcome)
            score += alternative_score(outcome)
    f.close()
    return score

# (1 for Rock, 2 for Paper, and 3 for Scissors)
# A for Rock, B for Paper, and C for Scissors

def alternative_score(outcome):
    round_result = 0
    if outcome[1] == 'X':
        if outcome[0] == 'A':
            # need to lose and enemy picks rock -> pick scissor
            round_result += 3
        elif outcome[0] == 'B':
            # need to lose and enemy picks paper -> you pick rock
            round_result += 1
        else:
            round_result += 2

    elif outcome[1] =='Y':
        if outcome[0] == 'A':
            round_result += 4
        elif outcome[0] == 'B':
            round_result += 5
        else:
            round_result += 6
    else:
        if outcome[0] == 'A':
            round_result += 8
        elif outcome[0] == 'B':
            round_result += 9
        else:
            round_result += 7

    return round_result

def determine_score_from_round(chosen_moves):
    """ Get result from individual round"""
    round_result = 0
    # If you choose rock
    if chosen_moves[1] == 'X':
        round_result += 1
        if chosen_moves[0] == 'C':
            round_result += 6
        elif chosen_moves[0] == 'A':
            round_result += 3
    # If you choose paper
    if chosen_moves[1] == 'Y':
        round_result += 2
        if chosen_moves[0] == 'A':
            round_result += 6
        elif chosen_moves[0] =='B':
            round_result += 3
    # if you choose scissor
    if chosen_moves[1] == 'Z':
        round_result += 3
        if chosen_moves[0] =='B':
            round_result += 6
        elif chosen_moves[0] == 'C':
            round_result += 3
    
    return round_result





def main():
    """ poop """
    # total_score = get_score()
    total_score = get_score()
    print(total_score)


if __name__ == "__main__":
    main()


