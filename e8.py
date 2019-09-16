import sys


# Function to check if the key provided is valid 
def check_mapping(mapping, text):
	return len(mapping) == len(text)

def encrypt(text, mapping):
	result = ""
	pointer = 0
	for ch in text:
		# XORing the ASCII values
		result += chr(ord(ch) ^ ord(mapping[pointer]))
		pointer += 1
		print(result)
		# print(ord(ch) ^ ord(mapping[pointer]))
	return result


def main():
	text = "informationsecurity"
	mapping1 = "vlaksjdhfgqodzmxncb"
	mapping2 = "tlftrffwmixor|{xbch"

	if not check_mapping(mapping1, text):
		print("inavlid mapping 1")
		sys.exit(0)

	if not check_mapping(mapping2, text):
		print("inavlid mapping 2")
		sys.exit(0)

	msg1 = encrypt(text, mapping1)
	# print(msg1)
	print(encrypt(msg1, mapping1))

if __name__ == "__main__":
    main()