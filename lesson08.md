# Python Lesson 8
This will be a short lesson on input validation. When we ask a user for input or read from a file, we might need to see if the input we are getting is in the right format. One simple way to do this is with a “try” block and/or if statements
```
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
```
We could also use the module pyinputplus to do some checking for us, but since this is not part of the standard distribution and is not included with Anaconda, I am not going to go over this. Instead let’s make a multiplication quiz and use standard methods to check if we are getting good input
```
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
```
[Python Lesson 9](lesson09.md) - Reading and Writing Files
