def find_completely_overlapping_pairs():
    completely_overlapping_pairs = 0
    with open('input.txt','r', encoding='utf_8') as f:
        lines = f.readlines()
        for line in lines:
            both_elfs_task_range= line.rstrip().split(',')
            first_elfs_task_range = both_elfs_task_range[0].split('-')
            second_elfs_task_range = both_elfs_task_range[1].split('-')
            #print(first_elfs_task_range)
            #print("\n second elf's task range is: ")
            #print(second_elfs_task_range)
            first_elfs_tasks = set(range(int(first_elfs_task_range[0]),int(first_elfs_task_range[1])+1))
            #print("\n first elfs tasks is: ")
            #print(first_elfs_tasks)
            second_elfs_tasks = set(range(int(second_elfs_task_range[0]),int(second_elfs_task_range[1]) +1))
            #print("\n second elf's tasks are: ")
            #print(second_elfs_tasks)
            overlapping_tasks = first_elfs_tasks.intersection(second_elfs_tasks)
            #print(overlapping_tasks)
            if overlapping_tasks == first_elfs_tasks or overlapping_tasks == second_elfs_tasks:
                completely_overlapping_pairs += 1
    f.close()
    return completely_overlapping_pairs

def find_overlapping_pairs():
    overlapping_pairs = 0
    with open('input.txt','r', encoding='utf_8') as f:
        lines = f.readlines()
        for line in lines:
            both_elfs_task_range= line.rstrip().split(',')
            first_elfs_task_range = both_elfs_task_range[0].split('-')
            second_elfs_task_range = both_elfs_task_range[1].split('-')
            first_elfs_tasks = set(range(int(first_elfs_task_range[0]),int(first_elfs_task_range[1])+1))
            second_elfs_tasks = set(range(int(second_elfs_task_range[0]),int(second_elfs_task_range[1]) +1))
            overlapping_tasks = first_elfs_tasks.intersection(second_elfs_tasks)
            #print(overlapping_tasks)
            if len(overlapping_tasks) > 0:
                overlapping_pairs += 1
    f.close()
    return overlapping_pairs

def main():
    print(find_overlapping_pairs())

if __name__ == "__main__":
    main()