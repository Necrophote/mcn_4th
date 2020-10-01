class PrefixCodeTree:

	def __init__(self):
		self.root = {}

	def insert(self, codeword, symbol):
		current = self.root
		for i in codeword:
			if i not in current:
				current[i] = {}
			current = current[i]
		current[2] = symbol

	def decode(self, encodedData, datalen):
		l = 0
		s = ''
		current = self.root
		for b in encodedData:
			for i in reversed(range(8)):
				l+=1
				if l > datalen:
					return s
				current = current[(b>>i)&1]
				if 2 in current:
					s = s + current[2]
					current = self.root
