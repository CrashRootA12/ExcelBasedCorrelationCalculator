"""
Correlation Calculator by Jaskirat Singh Grewal
"""
# Using Numpy library
import numpy as np
import xlrd
from collections import Counter as cTr
import math
from matplotlib import pyplot as plt


# Numpy Arrays is used in this script rather than using Numpy Matrices since it will be deprecated soon.
first_data_set = []
second_data_set = []


# Calculating Measures of Central Tendency and Standard Deviation
def calculate_central_tendency(the_data_set):
    mean = np.mean(the_data_set)
    median = np.median(the_data_set)
    mode = cTr(the_data_set).most_common(1)
    std_deviation = np.std(the_data_set)
    variance = np.var(the_data_set)
    print("------------------------------------------------")
    print("The mean of data-set {ds} is {m}".format(ds=the_data_set, m=mean))
    print("The median of data-set {ds} is {M}".format(ds=the_data_set, M=median))
    print("The mode of data-set {ds} is {z}".format(ds=the_data_set, z=mode))
    print("The variance of data-set {} is {}".format(the_data_set, variance))
    print("The standard deviation of data-set {ds} is {sd}".format(ds=the_data_set, sd=std_deviation))
    print("-------------------------------------------------")


def calculate_covariance(data_set_one, data_set_2, n)->float:
    arr_xy = data_set_one * data_set_2
    sum_x = np.sum(data_set_one)
    sum_y = np.sum(data_set_2)

    sum_xy = np.sum(arr_xy)
    sum_x_square = sum_x*sum_x
    sum_y_square = sum_y*sum_y
    num = n*sum_xy-sum_x*sum_y
    denom_t1 = n*sum_x_square-sum_x*sum_x
    denom_t2 = n*sum_y_square-sum_y*sum_y
    denom = math.sqrt(denom_t1*denom_t2)
    return num/denom


def calculate_pearson_coefficient(set_x, set_y)->float:
    mean_x = np.mean(set_x)
    mean_y = np.mean(set_y)
    den1 = np.sum((set_x - mean_x) * (set_x - mean_x))
    den2 = np.sum((set_y - mean_y) * (set_y - mean_y))
    num = np.sum((set_x - mean_x) * (set_y - mean_y))
    den = math.sqrt(den1)*math.sqrt(den2)
    return num/den


def sketch(ds1, ds2):
    data = (ds1, ds2)
    colors = ("red", "green")
    groups = ("Data Set I", "Data Set II")
    # Create plot
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, axisbg="1.0")
    for data, color, group in zip(data, colors, groups):
        ds1, ds2 = data
        ax.scatter(ds1, ds2, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
    plt.title('Data-Sets Scatter Plot')
    plt.show()


# Main Script
print("Welcome to Correlation Calculator by Jaskirat Singh Grewal")
xl_address = input("Enter the address of excel file containing the data-sets")
wb = xlrd.open_workbook(xl_address)
sheet = wb.sheet_by_index(0)
for i in range(sheet.nrows):
    first_data_set= np.append(first_data_set,float(sheet.cell_value(i, 0)))
for i in range(sheet.nrows):
    second_data_set = np.append(second_data_set, float(sheet.cell_value(i, 1)))
calculate_central_tendency(first_data_set)
calculate_central_tendency(second_data_set)
calculate_pearson_coefficient(first_data_set,second_data_set)
sketch(first_data_set, second_data_set)
