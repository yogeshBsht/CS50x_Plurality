# Plurality

max_candidates = 5
candidates = ['Lincoln', 'Kennedy', 'Bush', 'Obama', 'Trump', 'Biden']

# Taking number of candidates as input
flag = 1
while flag:
    num_candidates = int(float(input("Enter number of candidates: ")))
    if num_candidates < 2:
        print("Value Error! At least 2 candidates must contest the election.")
    elif num_candidates > max_candidates:
        print(f"Value Error! Number of candidates must not exceed {max_candidates}.")
    else: 
        flag = 0

# Randomly selecting contestants from candidates list
import random      
contestants = [*random.sample(candidates, num_candidates)]
print("Contestants are: ", end=" ")
print(*contestants, sep=", ")

# Taking number of voters as input
voters = int(float(input("Enter number of voters: ")))

# Random voting based on number of voters
dict = {}
for _ in range(voters):
    val = random.sample(contestants,1)[0]
    if val in dict:
        dict[val] += 1
    else:
        dict[val] = 1
        
# Winner selection based on vote count
winner, count = [], 0
for cont in dict:
    if dict[cont] == count:
        winner.append(cont)
        count = dict[cont]
    elif dict[cont] > count:
        winner = [cont]
        count = dict[cont]

if len(winner) == 1:        
    print(f"Winner {winner[0]} secured {count} votes out of {voters} votes.")
else:
    print("Election tied among: ", end=" ")
    print(*winner, sep = ", ")