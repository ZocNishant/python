row1 = ["🕸️", "🕸️", "🕸️"]
row2 = ["🕸️", "🕸️", "🕸️"]
row3 = ["🕸️", "🕸️", "🕸️"]


map = [row1, row2, row3]
print(map)

print(f'{row1}\n{row2}\n{row3}')

position = input("Enter the position you want to hide your treasure.")

horizontal = int(position[0])
vertical = int(position[1])

selectedRow = map[vertical - 1]
selectedRow[horizontal - 1] = "X"

print(f'{row1}\n{row2}\n{row3}')