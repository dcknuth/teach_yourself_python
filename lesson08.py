# Ask for input, check and loop if the input is not valid
while True:
  print('Enter your age:')
  age = input()
  try:
    age = int(age)
  except:
    print('Please use numeric digits.')
    continue
  if age < 1:
    print('Please enter a positive number.')
    continue
  break

print(f'Your age is {age}.')

# Random multiplication quiz with input checking
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(1, numberOfQuestions+1):
  # Pick two random numbers:
  num1 = random.randint(0, 9)
  num2 = random.randint(0, 9)
  # Create our question
  prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
  ans = input(prompt)
  try:
    ans = int(ans)
  except:
      print('Please use numeric digits.')
  else:
    # This block runs if no exceptions were raised in the try block.
    if ans == num1 * num2:
        print('Correct!')
        correctAnswers += 1
    else:
        print('Sorry, correct answer was', num1 * num2)
  time.sleep(2) # Brief pause to let user see the result
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
