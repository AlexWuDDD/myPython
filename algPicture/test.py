print("Alex is cool")


def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


def count(list):
    if list == []:
        return 0
    else:
        return 1 + count(list[1:])


def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    else:
        sub_max = max(list[1:])
        return list[0] if list[0] > sub_max else sub_max


myList = [2, 4, 6]
print(sum(myList))
myList = [2, 4, 6]
print(count(myList))
myList = [2, 4, 6]
print(max(myList))
