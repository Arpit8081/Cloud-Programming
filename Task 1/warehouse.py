from __future__ import print_function
import collections
import Pyro4
import pprint 
import csv
pp = pprint.PrettyPrinter(indent=2)
reader = csv.DictReader(open('sample.csv', 'rb'))
dict_list = []
def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data
for line in reader:
    line=convert(line)
    print(line)
    dict_list.append(line)
@Pyro4.expose

class Warehouse(object):
    def __init__(self):
        self.contents = dict_list

    def list_contents(self):
        books=[]
        pp.pprint(self.contents)
        for val in self.contents:
            books.append(val['bookName'])
        return books
    def store(self,name, item): 
        bookObj=["bookAuthor","bookIsbn","bookName","YOP"]
        obj={}
        books=[]
        item=item.split('a,')
        print ("the item test ",item)
        for i in item:
            item=i.split(",")
            obj = dict(zip(bookObj, item))
            obj["BookId"]=len(self.contents)
            obj["loan"]="no"
        print("coverting and adding your book to Database", obj)
        self.contents.append(obj)
        pp.pprint(self.contents)
        for val in self.contents:
            books.append(val['bookName'])

        print("The new Added on the list",books)
        return books

    def queryisbn(self,name,item):
        books=[]
        item=item.split("si,")
        for i in item:
            if(len(i)>1):
                for val in self.contents:
                    if(str(val["bookIsbn"])== i):
                        pp.pprint(val)
                        books.append(val["bookName"])
        print("{0} stored the {1}.".format(name, books))
        return books
    
    def noLoan(self,name,item):
        books = []
        item = item.split("nl,")
        for i in item:
            if (len(i) > 1):
                for val in self.contents:
                    if (str(val["bookIsbn"]) == i):
                        pp.pprint(val)
                        load = {"loan": "no"}
                        val.update(load)
                        books.append(val)
        if (len(books) < 1):
            print("no books on this ISBN In the library")
        print("This particular book is set no to the loan with this ISBN ", books)
        return books

    def onLoan(self, name, item):
        books = []
        item = item.split("ol,")
        for i in item:
            if (len(i) > 1):
                for val in self.contents:
                    if (str(val["bookIsbn"]) == i):
                        pp.pprint(val)
                        load={"loan":"yes"}
                        val.update(load)
                        books.append(val)
        if (len(books) < 1):
            print("no books on this ISBN In the library")
        print("This particular book is set to the loan with this ISBN ", books)
        return books
    
    def store1(self, name, item):
        self.contents.append(item)
        print("{0} stored the {1}.".format(name, item))

    def retrieveBookYOP(self, name, item):
        bookArr=[]
        fromyear=0
        toyear=1
        item = item.split("sy,")
        for i in item:
            if(len(i)>0):
                i = i.split(",")
                fromyear=int(i[0])
                toyear=int(i[1])
                for val in self.contents:
                    if(int(val["YOP"])<=int(i[1]) and int(val["YOP"])>=int(i[0])):
                        bookArr.append(val["bookName"])
                        pp.pprint(val)
        return bookArr
        
        

def main():
    warehouse = Warehouse()
    Pyro4.Daemon.serveSimple(
        {
            warehouse: "example.warehouse"
        },
        ns=True)

if __name__ == "__main__":
    main()
