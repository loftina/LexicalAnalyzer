def main():
	file = open('front.in', 'r')
	for line in file:
		current_line = unicode(line)

		index = 0
		while (index < len(current_line)):
			if current_line[index].isalpha():
				current_ident = current_line[index]
				index = index + 1
				while (current_line[index].isalpha() or current_line[index].isnumeric()):
					current_ident = current_ident + current_line[index]
					index = index + 1
				report('ident', current_ident)
			elif current_line[index].isnumeric():
				current_ident = current_line[index]
				index = index + 1
				while (current_line[index].isnumeric()):
					current_ident = current_ident + current_line[index]
					index = index + 1
				report('int_lit', current_ident)
			else:
				if (current_line[index] != ' '):
					current_ident = current_line[index]
					report('unknown', current_ident)
				index = index + 1

def report(type, value):
	if type == 'ident':
		token = 11
	if type == 'int_lit':
		token = 10
	if type == 'unknown':
		if value == '=':
			token = 20
		elif value == '+':
			token = 21
		elif value == '-':
			token = 22
		elif value == '*':
			token = 23
		elif value == '/':
			token = 24
		elif value == '(':
			token = 25
		elif value == ')':
			token = 26
		else:
			token = -1
	print('Next Token is: {0}, Next lexeme is {1}'.format(token, value))

if __name__ == "__main__":
	main()