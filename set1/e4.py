import sys
import statistics

def sumStdDeviations(frequencyVectors):
	stdDev = 0
	for row in frequencyVectors:
		stdDev += statistics.stdev(row)
	
	return stdDev


def getColumnIdx(ch):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	return alphabet.find(ch)

def getFrequencyVectors(text, keySize) :
	idx = 0
	frequencyVectors = [[0 for i in range(26)] for j in range(keySize)] #2D array with keysize rows and 26 columns
	for ch in text: 
		row = idx % keySize
		column = getColumnIdx(ch)
		frequencyVectors[row][column] += 1
		idx += 1
	return frequencyVectors
	


def main() :
	with open('ex4_schneier.enc', 'r') as myfile:
			text = myfile.read()
	
	for keySize in range(5,16):
		frequencyVectors = getFrequencyVectors(text, keySize)
		stdDev = sumStdDeviations(frequencyVectors)
		print("sum of ", keySize, "std. devs: ", stdDev)
		# for row in frequencyVectors: 
		#  	print(row) 

if __name__ == "__main__":
    main()