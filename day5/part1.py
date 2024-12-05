file = open("input.txt", "r")
data = file.readlines()

for i in range(len(data)):
    if data[i][-1] == "\n":
        data[i] = data[i][:-1]

rules = data[:data.index('')]
updates = data[data.index('')+1:]


for i in range(len(rules)):
    rules[i].split("|")
    rules[i] = (int(rules[i][0:2]), int(rules[i][3:5]))


rule_dict = {}
for key, value in rules:
    if key not in rule_dict:
        rule_dict[key] = []
    rule_dict[key].append(value) 



updates = [list(map(int, string.split(','))) for string in updates]


def is_update_in_order(rule_dict, update):
    index_map = {page: i for i, page in enumerate(update)}
    for key, dependent_pages in rule_dict.items():
        if key in index_map:  
            for dependent_page in dependent_pages:
                if dependent_page in index_map:
                    if index_map[key] > index_map[dependent_page]:
                        return 0
    return update[len(update)//2]

results = [is_update_in_order(rule_dict, update) for update in updates]

print(sum(results))
