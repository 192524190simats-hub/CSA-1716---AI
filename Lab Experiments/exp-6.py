rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

position = 'A'

while True:
    print("Vacuum is in room", position)

    if rooms[position] == 'Dirty':
        print("Cleaning room", position)
        rooms[position] = 'Clean'
    else:
        print("Room", position, "is already clean")

    if position == 'A':
        position = 'B'
    else:
        position = 'A'

    if rooms['A'] == 'Clean' and rooms['B'] == 'Clean':
        print("All rooms are clean!")
        break
