# 💡 Abstract: 

The Young Tableau is a versatile and efficient data structure that offers a compact 
representation for maintaining a matrix of elements. It excels in scenarios where 
ordering and retrieval of the elements are critical operations. In this implementation, 
the Young Tableau represents a matrix using a row-major layout. This means that the elements 
in the matrix are stored in a linear array, with each row of the matrix placed consecutively in the array. Each element in each 
row is less than the number to it's right and greater then the number to it's left. Similarly, 
each number is less than the number above it (in the same column) and greater than the number
below it.
By utilizing this row-major representation, efficient algorithms can be implemented for element 
insertion, minimum element extraction, and other operations. 
This implementation showcases the power of the Young Tableau as a 
valuable tool in various applications requiring ordered collections. 📊💪
# How to run the code
Run the `Young_Diagram_Tester.py` file, 
input the number of all elements and the number of rows and columns of your desired 2D matrix. Remeber that
n shal equal the number of input rows times the number of input columns. Then the program will create a 1D array of size n 
with random numbers from 10 to 99, 
and print it in a 2D style with taken number of rows and columns. At last, it will sort the elements and
print the diagram again.
I shall mention that the `Young_Diagram.py` module contains all the codes and functions needed to implement the
Young diagram and the `Young_Diagram_Tester.py` file is a tester file for that module.
# Resources
_Introduction To Algorithms_, 3rd edition: Chapter6, Heapsort: Problem 6-3


	
