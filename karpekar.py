HELP = """This script attempts to recreate karpekar's number

The logic is:
1. Take any four-digit number, using at least two different digits (leading zeros are allowed).
2. Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros if necessary.
3. Subtract the smaller number from the bigger number.
4. Go back to step 2 and repeat.

Eventually you will reach kaprekar's number => 6174
"""

KaprekarsConstant = 6174

from random import randint

def getdigits(input):
	digits = [int(i) for i in list(str(input))]
	diff = 4 - len(digits)
	if diff > 0:
		return [0] * diff + digits
	return digits

def sorted_digits(digits):
	return sorted(digits), sorted(digits, reverse=True)

def to_number(digits):
	return int("".join([str(i) for i in digits]))

def run_rules(input):
	err = {'msg' : ''}
	def set_err(msg):
		err['msg'] = msg
		return False
	def IsFourDigit(input):
		result = input <= 9999
		return result or set_err('Input "{}" is not four digit number'.format(input))
	def HasTwoDiffDigits(input):
		result = getdigits(input)
		return result or set_err('Input "{}" does not have two different digits'.format(input))
	
	if not all(rule(input) for rule in [IsFourDigit, HasTwoDiffDigits]):
		raise RuntimeError(err['msg'])

def main(input):
	print('-------------------------------')
	print('Input is: {}'.format(input))

	run_rules(input)

	idx = 1
	while True:
		digits = getdigits(input)
		lower, higher = sorted_digits(digits)
		input = to_number(higher) - to_number(lower)
		if input == KaprekarsConstant:
			print('Found Kaprekars Constant in {} iterations'.format(idx))
			break
		idx += 1


def genRandom4Digits():
	max = randint(2, 4)
	digits = [str(randint(0, 9)) for _ in range(max)]
	return int(''.join(digits))

if __name__ == "__main__":
	for _ in range(10):
		number = genRandom4Digits()
		main(number)
