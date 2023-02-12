def draw_punch_card(rows, columns):
    border_line = f"..{'+-'*(columns-1)}+"
    card_line = f"..{'|.'*(columns-1)}|"

    print(border_line)
    print(card_line)

    border_line = "+-" + border_line[2:]
    card_line = "|." + card_line[2:]

    print(border_line)

    for r in range(0, rows-1):
        print(card_line)
        print(border_line)



test_cases = int(input())
rows = list()
columns = list()

for t in range(0, test_cases):
    r, c = input().split(" ")

    rows.append(int(r))
    columns.append(int(c))

for t in range(0, test_cases):
    print(f"Case #{t+1}:")
    draw_punch_card(rows[t], columns[t])
