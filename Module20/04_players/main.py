players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

lst = list()
for i_name, i_scores in players.items():
    lst.append(i_name + i_scores)
print(lst)
