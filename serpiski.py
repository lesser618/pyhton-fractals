import turtle

ruleInput = ['F','G']
ruleOutput = [" F-G+F+G-F",'GG']
start = "F-G"

front = 10
turn = 120
stack = []
dirstack = []
# turtle.left(90)
# turtle.mode("logo")
turtle.penup()
turtle.setpos(-200,-100)
turtle.pendown()
turtle.speed(200)


def generate(iteration):
	result = start
	temp = ""
	for i in range(iteration):
		for j in range(len(result)):
			for k in range(len(ruleInput)):
				if (result[j] == ruleInput[k]):
					temp += ruleOutput[k]
					break
				if (k == len(ruleInput)-1):
					temp += result[j]
		result = temp
		temp = ""
	return result


def draw(input):
	for x in input:
		if (x == 'F'):
			turtle.forward(front)
		elif (x == 'G'):
			turtle.forward(front)
		elif (x == '-'):
			turtle.left(turn)
		elif (x == '+'):
			turtle.right(turn)
		elif (x == '['):
			stack.append(turtle.pos())
			dirstack.append(turtle.heading())
		elif (x == ']'):
			turtle.penup()
			post = stack.pop()
			direc = dirstack.pop()
			turtle.setpos(post)
			turtle.setheading(direc)
			turtle.pendown()
	turtle.hideturtle()
	turtle.done()


draw(generate(5))