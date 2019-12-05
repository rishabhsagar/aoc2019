from collections import Counter

def check_dd(n):
    # Check if the given number has atleast one adjacent
    n = str(n)

    if True in [n[x] == n[x+1] for x in range(len(n) - 1) ]:
        return True
    else:
        return False


def ascending_vals(n):
    n = str(n)
    # Check if the digits are in ascending order?
    if True in [n[x] > n[x+1] for x in range(len(n) - 1) ]:
        return False
    else:
        return True

def check_occurance_count(n):
    # Check for final condition
    nums = [int(i) for i in str(n)]
    li = Counter(nums)

    if 2 < max(li.values()) and 2 not in li.values():
        last_num = nums[0]
        run_length = 0
        for i in range(1, len(nums)):
            if last_num == nums[i]:
                run_length = run_length + 1
            else:
                run_length = 0
            last_num = nums[i]

            if run_length >= 2:
                return True

    return False

if __name__ == "__main__":
    possible_pass = list()
    for x in range(265275,781585):
        if (ascending_vals(x) and len(str(x)) == 6 and check_dd(x)):
            print(x)
            possible_pass.append(x)
    print("Total possibilities for part 1", len(possible_pass))

    poss = list()
    for x in range(265275,781585):
        if (ascending_vals(x) and len(str(x)) == 6 and check_dd(x)):
            if not check_occurance_count(x):
                poss.append(x)
    print("Total possibilities for part 2", len(poss))
        