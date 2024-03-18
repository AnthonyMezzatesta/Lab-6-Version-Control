# Anthony Mezzatesta
def encode(password):
	new = []
	for i in range(len(password)):
		new.append(str(int(password[i]) + 3))
	return "".join(new)


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
				pass

			case 3:
				exit()


if __name__ == '__main__':
	main()
