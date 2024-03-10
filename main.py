def findMinNumber(filename):
    with open(filename, "r") as file:
        line = file.readline().strip()
        min_number = int(line)

        for line in file:
            number = int(line.strip())
            if number < min_number:
                min_number = number

    return min_number

def findMaxNumber(filename):
    with open(filename, "r") as file:
        line = file.readline().strip()
        max_number = int(line)

        for line in file:
            number = int(line.strip())
            if number > max_number:
                max_number = number

    return max_number

def findMedian(filename):
    with open(filename, "r") as file:
        numbers = [int(line.strip()) for line in file]
        length = len(numbers)

        if length % 2 == 0:
            median = (numbers[length//2 - 1] + numbers[length//2]) / 2
        else:
            median = numbers[length//2]
        
    return median

def arithmeticMean(filename):
    with open(filename, "r") as file:
        numbers = [int(line.strip()) for line in file]
        length = len(numbers)
        sum = 0
        for number in numbers:
            sum += number
        mean = sum / length
    return mean

def findLongPositiveSequence(filename):
    with open(filename, 'r') as file:
        numbers = [int(num) for num in file.read().split()]
    longest_sequence = []
    current_sequence = [numbers[0]]

    for i in range(1, len(numbers)):
        if numbers[i] > current_sequence[-1]:
            current_sequence.append(numbers[i])
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = [numbers[i]]

    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence

    return longest_sequence

def findLongNegativeSequence(filename):
    with open(filename, 'r') as file:
        numbers = [int(num) for num in file.read().split()]
    
    longest_sequence = []
    current_sequence = [numbers[0]]

    for i in range(1, len(numbers)):
        if numbers[i] < current_sequence[-1]:
            current_sequence.append(numbers[i])
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = [numbers[i]]

    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence

    return longest_sequence    

filename = "10m.txt"

minNumber = findMinNumber(filename)
maxNumber = findMaxNumber(filename)
median = findMedian(filename)
mean = arithmeticMean(filename)
positive = findLongPositiveSequence(filename)
negative = findLongNegativeSequence(filename)

print("Minimum Number:",minNumber)
print("Maximum Number:", maxNumber)
print("Median:", median)
print("Arithmetic Mean:", mean)
print("Longest Positive Sequence:", positive)
print("Longest Negative Sequence:", negative)