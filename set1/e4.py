import sys
import math
import numpy
import statistics

def threeMostFrequentLetters(array):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	frequentLetters = ['','','']
	for count in range(0,3):
		idx = array.index(max(array))
		array[idx] = 0

		#shift the letter 22 steps to the right (same as 4 steps left)
		frequentLetters[count] = alphabet[(idx + 22) % 26] 
	return frequentLetters

def standardDeviation(array):
	sumXX = 0
	sumX = 0
	for num in array: 
		sumXX += num*num
		sumX += num
	return math.sqrt(sumXX / 26 - math.pow(sumX/26, 2))


def sumStdDeviations(frequencyVectors):
	stdDev = 0
	
	for row in frequencyVectors:
		stdDev += standardDeviation(row)
		#stdDev += numpy.std(row)
	
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
	
	#part one, showing the most likely key size
	bigStDev = 0
	for keySize in range(5,16):
		frequencyVectors = getFrequencyVectors(text, keySize)
		stdDev = sumStdDeviations(frequencyVectors)
		if (stdDev > bigStDev):
			bigStDev = stdDev 
			bestFrequencyVectors = frequencyVectors
		print("sum of ", keySize, "std. devs: ", stdDev)
		# for row in frequencyVectors: 
		#  	print(row) 
	
	for row in bestFrequencyVectors:
		frequentLetters = threeMostFrequentLetters(row)
		print(frequentLetters)

if __name__ == "__main__":
    main()