from mrjob.job import MRJob

class MRWordCounter(MRJob):
	def mapper(self, key, line):
		for word in line.split():
			yield 0, max(line)

	def reducer(self, word, occurrences):
		yield 'max is', max(occurrences)

if __name__ == '__main__':
	MRWordCounter.run()