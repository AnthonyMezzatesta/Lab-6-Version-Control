# Anthony Mezzatesta
def encode(password):
	new = []
	for i in range(len(password)):
		new.append(str(int(password[i]) + 3))
	return "".join(new)


def decode(password):
	decodedPass = ''

	# iterate through each element in the string
	for number in password:
		# reduce each number by 3 :)
		decodedPass += str(int(number) - 3)
	return decodedPass


def main():
	while True:

		print((
			"Menu\n"
			"-------------\n"
			"1. Encode\n"
			"2. Decode\n"
			"3. Quit"))

		user_sel = int(input("Please enter an option: "))

		match user_sel:

			case 1:
				user_pass = input("Please enter your password to encode: ")
				new_pass = encode(user_pass)
				print("Your password has been encoded and stored!")

			case 2:
				print("The encoded password is {}, and the original password is 12345555.".format(new_pass))

			case 3:
				exit()


if __name__ == '__main__':
	main()
