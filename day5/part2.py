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
                        update[index_map[key]], update[index_map[dependent_page]] = update[index_map[dependent_page]], update[index_map[key]]
                        return True
    return False

wrongs = [update if is_update_in_order(rule_dict, update) else None for update in updates]
wrongs = [update for update in wrongs if update is not None]
print(wrongs)
corrected = []
for update in wrongs:
    while is_update_in_order(rule_dict, update):
        pass
    corrected.append(update)
print(corrected)
print(sum([update[len(update)//2] for update in corrected]))

