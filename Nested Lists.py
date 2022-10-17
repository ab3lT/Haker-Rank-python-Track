if __name__ == '__main__':
    records = []
    score_arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        if not score in score_arr:
            score_arr.append(score)
score_arr.sort()
second_lowest = score_arr[1]

new_names_list = []
for r in records:
    if r[1] == second_lowest:
        new_names_list.append(r[0])
new_names_list.sort()
for name in new_names_list:
    print(name)