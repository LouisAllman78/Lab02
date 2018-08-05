def find_reverse(numbers):
    #TODO: find the reverse of the list
    return list(reversed(numbers))

def find_max(numbers):
    #TODO: find the maximum of the list
    return max(numbers)

def find_min(numbers):
    #TODO: find the minimum of the list
    return min(numbers)

def find_sum(numbers):
    #TODO: find the sum of all the numbers in the list
    return sum(numbers)

def find_average(numbers):
    #TODO: find the average of all the numbers in the list
    return sum(numbers) / len(numbers)

def find_descending(numbers):
    #TODO: numbers sorted in descending order
    return list(reversed(sorted(numbers)))
    

def second_smallest(numbers):
    #TODO: find the second smallest
    numbers.sort()
    i = 0
    while numbers[i] == numbers[0]:
        i += 1
    
    return numbers[i]



'''
 bonus task:
 a function that takes in a list of numbers, and an index 'k' 
 and prints the kth smallest number in the list
'''
def kth_smallest(numbers, k):
    #TODO: find the kth smallest number in the list
    numbers.sort()
    i = 0
    num = numbers[0]
    j = 0
    counter = 1
    while i < len(numbers) and counter != k:
        if numbers[i] != num:
            num = numbers[i]
            counter += 1
            if counter == k:
                j = i
        i += 1

    return numbers[j]
