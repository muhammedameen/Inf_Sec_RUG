import argparse
import sys

def transform(ch, mapping, alpha):
	# return chth elemant of mapping
	i = alpha.find(ch)
	# print("Mapped ", ch, i, mapping[i])
	return mapping[i]

def check_mapping(mapping, alpha):
	string = ''.join(sotred(list(mapping)))
	return string == alpha

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

	parser = argparse.ArgumentParser(description="where:")
	parser.add_argument("mapping", help = "26 letter char-mappig \n or an int-value")
	parser.add_argument("-o", help = "keep non-letters as is, honor letter casing", action = "store_true")
	parser.add_argument("-d", help = "decrypt", action = "store_true")
	try:
	    args = parser.parse_args()
	except:
	    parser.print_help()
	    sys.exit(0)
	# print(args.mapping)
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	# mapping = "yxzwvtsqpnrmlkjgfdchbuoaie"
	# string = "QwertyuioP1234"
	mapping = args.mapping
	if args.o is True:
		mode_o = 1
	else:
		mode_o = 0
	if args.d is True:
		mode_d = 1
	else:
		mode_d = 0
	
	with open('2019.enc', 'r') as myfile:
  		data = myfile.read()
	
	if mode_d == 0:
  		print(string_transform(data, mapping, alpha, mode_o))
	elif mode_d == 1:
  		print(string_transform(data, alpha, mapping, mode_o))


if __name__ == "__main__":
    main()





