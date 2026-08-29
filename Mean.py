def calculate_average(scores):

    total = sum(scores)

    average = total / len(scores)

    return average


scores = [15, 18, 17, 20]

print(calculate_average(scores))