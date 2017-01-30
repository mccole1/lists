#Exercise 2: Shopping List

shopping_list = []

def add_to_list(item):
    item = item.lower()
    if item not in shopping_list:
        shopping_list.append(item)
        print "%s added to your shopping list!" % item.upper()
    else:
        print "Item already on list."
    return sorted_shopping_list()

def sorted_shopping_list():
    shopping_list.sort()
    return shopping_list

def remove_from_list(item):
    item = item.lower()
    if item in shopping_list:
        shopping_list.remove(item)
        print "%s was removed from your shopping list." % item
    else:
        print "Item not on list."
    return sorted_shopping_list()

def main():
    #Test1
    print add_to_list("pears")
    print add_to_list("apples")
    print add_to_list("peppers")
    print add_to_list("butter")

    #Test2
    print add_to_list("pears")

    #Test3
    print remove_from_list("pears")

if __name__ == '__main__':
    main()


#Exercise 2:

primes = [2, 3]

#primes.append(5, 7, 11)

#print primes #error: append() only takes one argument

primes.append([5, 7, 11])

print primes

primes.pop()

print primes

primes.append(5)
primes.append(7)
primes.append(11)

print primes

# primes.extend(13, 17)

# print primes #error: extend() only takes one argument

primes.extend([13, 17])

print primes




