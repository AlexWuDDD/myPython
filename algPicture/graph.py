
from collections import deque
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
    search_queue = deque() #创建一个队列
    search_queue += graph[name] #将你的邻居都加入到这个搜索队列中
    searched = []

    while search_queue: #只要队列不为空
        person = search_queue.popleft()  #就取出其中的第一个人
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False


def person_is_seller(name):
    return name[-1] == 'm'



search("you")