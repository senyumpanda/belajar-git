class Say:
	def __init__(self):
		res = self.kata()
		Result(res)
	
	def kata(self):
		return "Hello"	

class Result:
	def __init__(self, word):
		res = self.print(word)
		print(res)

	def print(self, word):
		return word + " World"


Say()