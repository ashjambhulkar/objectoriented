# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:
import collections

class Solution:
	def read(self, buf: List[str], n: int) -> int:
		def __init__(self):
			self.queue = collections.deque([])

		def read(self, buf, n):
				total_read = 0

				while self.queue and n > 0:
					buf[total_read] = self.queue.popleft()
					total_read += 1
					n -= 1

				while n > 0:
					buf4 = [""]*4
					current_read = read4(buf4)
					if current_read == 0:
						return total_read

					if current_read > n:
						self.queue += buf4[n:current_read]

					for i in range(min(current_read, n)):
						buf[total_read] = buf4[i]
						total_read += 1
						n -= 1
				return total_read
