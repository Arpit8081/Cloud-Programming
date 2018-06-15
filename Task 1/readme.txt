In this program I created three files to run this program.
1)	Read_csv.py
2)	Person.py
3)	Warehouse.py

1)	Read_csv.py
In read_csv.py file I imported library files such as sys (this is used for system specific paramiters), Pyro4 (these objects can talk with each other), person (this library imports person data for the .py file). I connected the host name with warehouse.py file (It means conncet with the server). After that, I defined each person’s name and their login details. Any number of people can be added to the program.

2)	Person.py
In this file I imported pprint, collection and sys libaraies. In line 6th, I define sys version. After that, I defined the function ‘convert’. This function converts all the data into items, then it does mapping and then returns the data. In line 19th, I created a class named as ‘Person’ and then I called main program function. In line 23, I created a new function ‘visit’. In this function I called ‘which statement you want to write’. In this function, I have to choose one function from ‘d, a, si, sy, ol and nl’. This function is called the warehouse function and performs according to the keyword you entered. In line 43, I defined the function called ‘addstore’. In this field, I have to add data of the book and call the warehouse function. I used same functions for further 4 times.  

3)	Warehouse.py
This warehouse means temp server is created using the home system. I imported the print function and collection, Pyro4, pprint, and csv libraries. In line 7th I created an object to open and write data fro csv file. Then I created an array and created the function ‘convert’ with same name as Person.py file. After that I executed the command to read all the lines and print them. In line 24th, I defined a class with the name ‘warehouse’. Then I displayed all the data from csv file and printed this data in server side and prints the book data name. I also used ‘store’ function to store the book data. This data has unique id, book name, isbn, year of publication and book author. After adding these details, the data will be stored in csv file and being shown on the server side. I also created ‘display_isbn’ function to display all the isbn data. From line 66 to 96, the program checks if the book is in loan or not in loan. In this function, all the for loops, if-else conditions remains same but only the data can change such as if the book being given in loan or  not in loan.

After this function, the function for lines 66 to 96% will be check if the book is in loan or not in loan. In this function all the for-loops, if-else condition remains same but only the data is in loan or not. Last two functions store print in server side and retrive all the data and prints in server side. Line 120 shows  the run pyro and displays the local host in program. And this can be called to the call objects. The output can be seen as below:



OUTPUT:
NOTE: THIS PROGRAM RUN IN PYTHON 2.7
 Open cmd and write: pyro4-ns 
1)	Open second cmd and write: python warehouse.py
2)	Open thired cmd and write: python read_csv.py
