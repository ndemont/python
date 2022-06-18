import string
import sys

sys.tracebacklimit = 0

def text_analyzer(text):
	"""This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
	if TypeError:
		if (len(sys.argv) > 1):
			raise TypeError('One argument required')
		elif (len(sys.argv) < 1):
			print("What is the text to analyse?")
			text = input()
	upper = len([elem for elem in text if elem.isupper()])
	lower = len([elem for elem in text if elem.islower()])
	punctuation = len([elem for elem in text if elem in string.punctuation])
	space = len([elem for elem in text if elem == ' '])
	print("The text contains", len(text), "characters:")
	print("-", upper, "upper letters")
	print("-", lower, "lower letters")
	print("-", punctuation, "punctuation marks")
	print("-", space, "spaces")