## PART 1 -------------------------------->

# reading the file
data = ""
with open('day_1/input.txt', 'r') as file:
    data = file.read().split('\n')

elves = {}
tmp_elf = []
max_elf = 0
for d in data:
    # if we find an empty element
    if d == '':
        sum_cals = sum(tmp_elf)
        elves[sum_cals] = tmp_elf
        tmp_elf = []

        # check for the maximum
        if sum_cals > max_elf:
            max_elf = sum_cals
        continue
    # add the calory to the list
    tmp_elf.append(int(d))

print("The maxium elf has", max_elf, "calories")

## PART 2 -------------------------------->
import collections

# order the previous elves dictionary
ordered_elves = collections.OrderedDict(sorted(elves.items()))

# calculate the sum of the last three elves
sum_top_three = sum(list(ordered_elves.keys())[-3:])

# print the sum
print("The top three elves have", sum_top_three, "calories")
