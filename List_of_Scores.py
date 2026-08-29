scores = [15, 18, 12, 20, 17,9]

print("Number of students:", len(scores))
print("Highest score:", max(scores))
print("Lowest score:", min(scores))

average = sum(scores) / len(scores)

print("Average:", average)

print("Scores above 15:")

for score in scores:
    if score > 15:
        print(score)
    if score < 10:
        print("There are scores below 10.",f"Score is: {score}")