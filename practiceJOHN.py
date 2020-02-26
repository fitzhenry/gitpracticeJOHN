# Partner 1: John Robert Fitzlovely
# partner 2: Ethan Bankowski
######################
# Assignment Name: GitHub practice - 2/26/20 - 10 points

import random as rand
def getNRandom(n):
	'''takes in an integer and returns a list of n random integers between 1 and 10, inclusive'''
    number_list = []
    for i in range(n):
        number_list.append(rand.randint(1,10)
    return number_list

def multiplyRandom(numbers):
	'''takes in a list of n numbers and returns the product of the numbers'''
    pass
        product = 1
        for i in numbers:
            product = product*i
        return product

def main():
	print(multiplyRandom(getNRandom(10))

if __name__ == "__main__":
	main()
