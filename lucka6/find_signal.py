"""This code solves the 6th day's problem in Advent of Code"""

def all_unique_letters(text):
    """Checks if all letters in text are unique"""
    # 128 possible characters
    char_set = [False] * 128
    # loop over all characters
    for letter in text:
        val = ord(letter)
        if char_set[val]:
            return False

        char_set[val] = True

    return True

def search_for_signal():
    with open('demo_input.txt', 'r', encoding='utf_8') as f:
        total_looped_letters = 0
        lines = f.readlines()
        print(len(lines))
        for line in lines:
            text = line.strip()
            i = 0
            # don't exceed maximum index
            # not sure if divided into lines or not
            while i + 3 < len(text) - 1:
                # if current chunk is a signal -> return i + 3 + 2
                 # add one to compensate for zero indexing. add three more since you read in chunks of 4
                if all_unique_letters(text[i:i+4]):
                    return total_looped_letters + i + 3 + 1
                i += 1
            total_looped_letters += i + 3 + 1
            #print(i + 4)
            #print(text[i:i+4])
    return total_looped_letters

def search_for_message():
    with open('demo_input.txt', 'r', encoding='utf_8') as f:
        total_looped_letters = 0
        lines = f.readlines()
        print(len(lines))
        for line in lines:
            text = line.strip()
            i = 0
            # don't exceed maximum index
            # not sure if divided into lines or not
            while i + 13 < len(text) - 1:
                # if current chunk is a signal -> return i + 3 + 2
                 # add one to compensate for zero indexing. add three more since you read in chunks of 4
                if all_unique_letters(text[i:i+14]):
                    return total_looped_letters + i + 13 + 1
                i += 1
            total_looped_letters += i + 13 + 1
            #print(i + 4)
            #print(text[i:i+4])
    return total_looped_letters

def main():
    """ main function"""
    number_of_letters = search_for_message()
    print(number_of_letters)

if __name__ == "__main__":
    main()
