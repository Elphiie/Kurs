letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points.update({' ': 0})

# print(letter_to_points)
# print('\n \n')

def score_word(word):
  point_total = 0
  for letter in word.upper():
    points = letter_to_points.get(letter, 0)
    point_total += points
  return point_total

while True:
    points_check = input('Type a word: \n')
    print('\n')
    print(score_word(points_check))




