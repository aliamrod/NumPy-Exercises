# NumPy-Exercises

## What is NumPy?

NumPy ("Numerical Python") is a Python library used for working with arrays. It also has functions for working in the domain of Linear Algebra, Fourier Transforms, and matrices. NumPy was created in 2005 by Travis Oliphant and is an open-source project
you can utilize freely. 

## Why Use NumPy?

In Python we have lists that serve the purpose of arrays, but are slow to process. NumPy aims to provide an array object that is up to 50x faster than traditional Python lists. 


The array object in NumPy is called 'ndarray' and it provides multiple supporting functions that make working with ndarray very easy. Arrays are very frequently used in data science, where speed and resources are very important. 

## Why is NumPy faster than lists?

NumPy arrays are stored in one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently. This behavior is called 'locality of reference' in Computer Science. 

Originally, Python was not designed for numeric computation. As people started using Python for various tasks, the need for fast numeric computation(s) arose and NumPy was created to address this challenge. Today in the era of Artificial 
Intelligence, it would not have been possible to train Machine Learning algorithms without a fast numeric library such as NumPy. NumPy array is a collection of similar data-types that are densely packed in memory. Conversely, a Python list can have different 
data-types which places additional constraints while performing computations on it. NumPy is able to divide a task into multiple subtasks and process them parallelly. 

NumPy functions are implemented in C which again, makes it faster in comparison to Pythonic lists.
