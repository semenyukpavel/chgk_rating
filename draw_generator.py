import random

path = "C:\\Users\\pavel.semenyuk\\Desktop\\python\\rating\\"
group_num = 6
pot_num = 9

with open(path + "pots.txt") as f:
	f_pots = f.read()

pots = f_pots.split("\n")

groups_list = []
for i in range(group_num):
	s = "Группа " + str(i+1)
	l = [s]
	groups_list.append(l)

for j in range(pot_num):
	curr_pot = []
	for i in range(group_num):
		curr_pot.append(pots[group_num*j+i])
	random.shuffle(curr_pot)
	for i in range(group_num):
		groups_list[i].append(curr_pot[i])

for i in range(group_num):
	for j in range(len(groups_list[i])):
		print(groups_list[i][j])

