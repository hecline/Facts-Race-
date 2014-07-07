import random

score = 0

print "Welcome! This game was made by Hannah Cline at table 16H. Remember, at any time you can press ctrl+C to quit.\n"
print "In this game you are playing a runner in a race. For each math fact you get right, your runner moves forward. Try to answer 10 math facts and win first place! To get extra practice, try both exercises!\n \n"
op = raw_input("Do you want to practice addition or subtraction? Type '+' for addition, and '-' for subtraction.\n")
if op == "+":
	while True:
		num1 = (random.randint(1, 5))
		num2 = (random.randint(1, 5))
		addanswer = (num1 + num2)

		response = raw_input("What is " + str(num1) + "+" + str(num2) + "?\n")

		response = str(response)
		addanswer = str(addanswer)

		if response == addanswer:
			print "Hooray, you got it right!"
			print "The answer was " + addanswer + "!"
			print "Let's move on to the next problem!"
			score = score + 1
			print "\nYour score is " + str(score) + "!"
			if score == 10:
				print "Congratulations! You got 10 math facts right, so your runner won in first place. Well done!\n"
				break
		else:
			print "Oops! That's incorrect. \nThe answer was " + addanswer + ". \nYour score is still " + str(score) + "."
			print "Let's try a different problem!  Remember, at any time you can press ctrl+C to quit.\n" 
if op == "-":
	while True:
		num1 = (random.randint(1, 5))
		num2 = (random.randint(1, 5))
		subanswer = (num1 - num2)

		response = raw_input("What is " + str(num1) + "-" + str(num2) + "?\n")

		response = str(response)
		subanswer = str(subanswer)

		if response == subanswer:
			print "Hooray, you got it right!"
			print "The answer was " + subanswer + "!"
			print "Let's move on to the next problem!"
			score = score + 1
			print "\nYour score is " + str(score) + "!"
			if score == 20:
				print "Congratulations! You got 20 math facts right, so your runner won in first place. Great job!\n"
				break
		else:
			print "Oops! That's incorrect. \nThe answer was " + subanswer + ". \nYour score is still " + str(score) + "."
			print "Let's try a different problem!  Remember, at any time you can press ctrl+C to quit.\n" 
#if op != "+" or "-":
#while(op != "+" and op != "-"):
	#op = raw_input("Do you want to practice addition or subtraction? Type '+' for addition, and '-' for subtraction.\n")
	#print "Uh oh! That response is not supported for this game."
	#print op
