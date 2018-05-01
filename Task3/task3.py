from mrjob.job import MRJob

class Mr(MRJob):

	def mapper(self, key, value):
		key=0
		a=0
		num=0
		for i in value.split(','):
			a=float(i)+a
			num +=1
		yield key,(a,num)

	def reducer(self, key, values):
		a=0
		num=0
		for i in values:
			a +=i[0]
			num +=i[1]
		yield "Output is",a/num

if __name__ == '__main__':
	Mr.run()