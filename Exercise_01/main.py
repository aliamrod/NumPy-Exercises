import numpy as np
from operationsclass import IntArray

def productivity_of_company(order, data_frame):
    return np.sum(data_frame[order])

def max_productivity(data_frame):
    i = 0
    best_company = i + 1
    num_of_products = 0

    for i in range(len(data_frame)):
        result = productivity_of_company(i, data_frame)
        if result > num_of_products:
            num_of_products = result
            best_company = i + 1

            print(f"The best company is the {best_company}. company with {num_of_products} products made")

def min_productivity(data_frame):
    i = 0
    worst_company = i + 1
    num_of_products = productivity_of_company(0, data_frame)

    for i in range(len(data_frame)):
        result = productivity_of_company(i, data_frame)
        if result <= num_of_products:
            num_of_products = result
            worst_company = i + 1
    print(f"The worst company is the {worst_company}. company with {num_of_products} products made.")

def mean_products(data_frame):
    for i in range(len(data_frame)):
        average = np.mean(data_frame[i])
        print(f"On average, one human from {i}. company produced {average} products.")

    total_sum = 0
    num_elements = 0

    for row in data_frame:
        for element in row:
            num_elements += 1
    for row in range(len(data_frame)):
        row_sum = sum(data_frame[row])
        total_sum += row_sum

    total_mean = total_sum / num_elements

    print(f"Mean of the entire conglomerate is {total_mean} per employee.")

def file_handling():
    lines = []
    # Transform into 2D NumPy array of integers
    with open('/Users/aliamahama-rodriguez/numpy/company.txt', 'r') as file: # 'r'=> read mode and outputs error message if no such file exists
        for line in file:
            values = line.strip().split(',')
            #print(type(values))
            int_values = [int(val) for val in values]
            lines.append(int_values)
    data_frame = np.array([np.array(row) for row in lines], dtype='object')
    return data_frame

def main():
    data_frame = file_handling()
    print(data_frame)

    first_branch = IntArray(data_frame[0])
    first_branch.display()
    first_branch.salary()
    first_branch.show_data()

    max_productivity(data_frame)
    min_productivity(data_frame)
    mean_products(data_frame)

if __name__ == "__main__":
    main()
