import argparse
import sys

# Function to encrypt/decrypt an alphabet
def transform(ch, mapping, alpha):
	# return chth elemant of mapping
	i = alpha.find(ch)
	# print("Mapped ", ch, i, mapping[i])
	return mapping[i]

# Function to check if the key provided is valid 
def check_mapping(mapping, alpha):
	string = ''.join(sorted(list(mapping)))
	return string == alpha

# Function to encrypt/decrypt a string
# Mapping - key for encryption
# alpha - the set of aplphabets in language
# mode 0 when -o not present , mode 1 when -o present 
def string_transform(string, mapping, alpha, mode):
	string1 = ''
	if mode == 1:
	# -o is present
		for ch in string:
			if(ch.isalpha()):
				# print(ch)
				ech = ch.lower()
				dch = transform(ech, mapping, alpha)
				if ch.isupper():
					string1 = string1 + dch.upper()
				else:
					string1 = string1 + dch
			else:
				string1 = string1 + ch

		return string1
	elif mode == 0:	
		# -o is absent
		for ch in string:
			if(ch.isalpha()):
				string1 = string1 + transform(ch.lower(), mapping, alpha)
		return string1
	else:
		print("Invalid Mode")
		return ''

def main():

	# checking if all required parameters present
	parser = argparse.ArgumentParser(description="where:")
	parser.add_argument("mapping", help = "26 letter char-mappig \n or an int-value")
	parser.add_argument("-o", help = "keep non-letters as is, honor letter casing", action = "store_true")
	parser.add_argument("-d", help = "decrypt", action = "store_true")
	try:
	    args = parser.parse_args()
	except:
	    parser.print_help()
	    sys.exit(0)
		
	# english alphabets
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	# mapping = "yxzwvtsqpnrmlkjgfdchbuoaie"
	# string = "QwertyuioP1234"
	mapping = args.mapping

	# check if key is a valid mapping 
	if check_mapping(mapping, alpha) is False:
		print("Key Invalid")
		sys.exit(0)

	# setting mode -o
	if args.o is True:
		mode_o = 1
	else:
		mode_o = 0

	# setting decryption mode
	if args.d is True:
		mode_d = 1
	else:
		mode_d = 0
	
	# opening the file to be decrypted
	with open('2019.enc', 'r') as myfile:
  		data = myfile.read()
	
	if mode_d == 0:
  		print(string_transform(data, mapping, alpha, mode_o))
	elif mode_d == 1:
  		print(string_transform(data, alpha, mapping, mode_o))


if __name__ == "__main__":
    main()





