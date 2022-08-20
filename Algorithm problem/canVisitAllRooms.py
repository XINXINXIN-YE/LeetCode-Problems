rooms = [[1],[2],[3],[]]
count = 0
length = len(rooms)

queue = []

queue.append(rooms[0])
rooms[0] = None
while queue:
    room = queue.pop()
    for key in room:
        if rooms[key] != None:
            queue.insert(0,rooms[key])
            rooms[key] = None
    count += 1
if count == length:
    print(True)
else:
    print(False)
