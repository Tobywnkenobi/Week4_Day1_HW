
numbers = [1, 2, 2]

def square_sum(numbers):
    add_num = []
    for n in numbers:
        square = n**2
        add_num.append(square)
    return (sum(add_num))

answer = square_sum([4,4,6])

print(answer)