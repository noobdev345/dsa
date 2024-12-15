class Solution:
	def sumOfDivisors(self, n):
		total = 0
		for i in range(1, n + 1):
			total += (i * (n // i))
		return total
