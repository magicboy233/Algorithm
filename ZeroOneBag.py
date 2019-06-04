
n = 5
totalWeight = 100
weight = [10, 20, 30, 40, 50]
value = [20, 30, 65, 40, 60]

maxWeight = 0
maxValue = 0
bag = [0, 0, 0, 0, 0]
bags = []
best_answer = None



def conflict(k):
    global bag, weight, totalWeight
    if sum([y[0] for y in filter(lambda x: x[1] == 1, zip(weight[:k + 1], bag[:k + 1]))]) > totalWeight:
        return True
    return False



def backpack(k):
    global bag, maxValue, maxWeight, best_answer
    if k == n:
        current_value = get_value(bag)
        current_weight = get_weight(bag)

        if current_value > maxValue:
            maxValue = current_value
            best_answer = bag[:]

        if current_value == maxValue and current_weight < maxWeight:
            maxWeight = current_weight
            best_answer = bag[:]
    else:
        for i in [1, 0]:
            bag[k] = i
            if not conflict(k):
                backpack(k + 1)


def get_weight(bag):
    global weight
    return sum([y[0] for y in filter(lambda x: x[1] == 1, zip(weight, bag))])


def get_value(bag):
    global value
    return sum([y[0] for y in filter(lambda x: x[1] == 1, zip(value, bag))])


backpack(0)
print(best_answer)
print('total weight:')
print(get_value(best_answer))