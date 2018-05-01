from mrjob.job import MRJob

class Mr(MRJob):

	data=[]

	def mapper(self, key, line):
		line=line.split(',')
		self.data.append(line)
		yield 0,self.data

	def reducer(self, num, values):
		listval=list(values)
		number=len(listval)-1
		listval=listval[number]
		for i in listval:
			for j in listval:
				if (i != j and i[1]==j[0]):
					a=[i[0],i[1],j[1]]
					a=list(a)
					yield 'the output is ',tuple(a)

if __name__ == '__main__':
	Mr.run()