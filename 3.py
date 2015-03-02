# -*- code:utf-8 -*-
# language: python 3.4
# author: Chantisnake


def rearrange(data):
    elements = []
    temp = data.split('\n')
    for string in temp:
        if temp != '':  # in case there is change line at the end or in the middle
            elements.append(string.split(" "))
    for i in elements:
        i.insert(0, len(i[0]))
        i[1] = i[1].lower()
    elements = sorted(elements, key=lambda element: element[0], reverse=True)
    print("here is the rearranged list:")
    print(elements)
    print()
    return elements


def read(filename):
    f = open(filename, 'r')
    data = f.read()
    return data


def match(name, data):
    name = name.lower()
    print("Running the frontward analysis: ")
    print()
    front = frontwardanlysis(name, data)
    print()
    print("Running the backward analysis: ")
    print()
    back = backwardanlysis(name, data)
    out = compare(front, back)
    return out


def frontwardanlysis(name, data):
    breaked = False  # controller
    used = []
    unused = []
    while len(name) > 0:
        # find whether this has been detected
        # this can be better if the trash is erased
        print("examine whether this has been found before...")
        for thing in unused:
            if thing[1] == 0:
                print("find the element:")
                # renew
                used.append(thing[0])
                print(used[-1])
                # renew name
                name = name[thing[0][0]:]
                print("name renewed:")
                print(name)
                # renew unused
                for all in unused:
                    all[1] -= thing[0][0]
                breaked = True
                break
        if breaked:
            breaked = False
            continue
        else:
            print("nothing found running regular analysis: ")
        # regular analysis
        for element in data:
            # print(element)
            # if the pointer haven't been detected.
            # if this is at the beginning, save it
            if name.find(element[1]) == 0:
                used.append(element)
                print("find the element and saved:")
                print(used[-1])
                name = name[element[0]:]
                print("name renewed")
                print(name)
                # renew unused
                for all in unused:
                    all[1] -= element[0]
                break
            # if this is not at the pointer, save it for later use
            elif name.find(element[1]) != -1:
                print("find the element save for later")
                unused.append([element, name.find(element[1])])
                print(unused[-1])
            # if all the choice cannot satisfy
            elif element == data[-1]:
                # find approximation
                print("no element found, finding approximation...")
                used.append(approximate(name, 'f', data))
                # renew name
                name = name[1:]
                print("name has been renewed:")
                print(name)
                # renew unused
                for all in unused:
                    all[1] -= 1
                break
    print()
    print("frontward analysis ends and here is the value we found: ")
    print(used)
    return used


def backwardanlysis(name, data):
    breaked = False  # controller
    used = []  # the element actually using to consist of the name
    unused = []  # found the element inside name, save for later use
    while len(name) > 0:
        # find whether this has been detected
        # this can be better if the trash is erased
        print("examine whether this has been found before...")
        for thing in unused:
            if thing[1] == len(name):
                print("find the element:")
                # renew
                used.insert(0, thing[0])
                print(used[-1])
                # renew name
                name = name[:len(name) - thing[0][0]]
                print("name renewed:")
                print(name)
                # no need to renew unused
                breaked = True
                break
        if breaked:
            breaked = False
            continue
        else:
            print("nothing found running regular analysis: ")
        # regular analysis
        for element in data:
            # print(element)
            # if the pointer haven't been detected.
            # if this is at the biginning, save it
            if name.rfind(element[1]) == len(name) - 1:
                used.append(element)
                print("find the element and saved:")
                print(used[-1])
                name = name[:len(name) - element[0]]
                print("name renewed")
                print(name)
                # no need renew unused
                break
            # if this is not at the pointer, save it for later use
            elif name.rfind(element[1]) != -1:
                print("find the element save for later")
                unused.append([element, name.rfind(element[1]) + element[0]])
                # save the element and the position of the end of the element
                print(unused[-1])
            # if all the choice cannot satisfy
            elif element == data[-1]:
                # find approximation
                print("no element found, finding approximation...")
                used.insert(0, approximate(name, 'b', data))
                # renew name
                name = name[:len(name) - 1]
                print("name has been renewed:")
                print(name)
                # no need to renew unused
    print()
    print("backward analysis ends and here is the value we found: ")
    print(used)
    return used


def compare(a, b):
    nulla = nullb = False
    for all in a:
        if all == "null":
            nulla = True
    for all in b:
        if all == "null":
            nullb = True

    if nulla and nullb:
        print('we cannot find a appropriate combination to suit your need, if you think this is wrong please leave a comment')
        return ""
    if nulla:
        return b
    if nullb:
        return a
    if len(a) > len(b):
        return b
    return a


def approximate(name, test, data):
    if test == 'f':
        # this can be made faster by not searching the one with only one letter
        for element in data:
            if element[1][0] == name[0]:
                print("find the following approximation: ")
                print(element)
                return element
    if test == 'b':
        lenname = len(name)
        for element in data:
            try:
                if element[1][0] == name[lenname - element[0]]:
                    print("find the following approximation: ")
                    print(element)
                    return element
            except:
                pass
    print("Error: nothing found, return null")
    return "null"


if __name__ == "__main__":
    Data = read("read")
    Data = rearrange(Data)
    Name = input("input the name: ")
    out = match(Name, Data)
    if out != '':
        print("\n\nhere is the solution we found:")
        for element in out:
            for i in range(1, len(element)):
                print(element[i], end='\t')
            print()
