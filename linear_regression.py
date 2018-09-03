from __future__ import division
from matplotlib import pyplot as plot
import numpy
import csv

# data points
X, Y = [], []

# populate the coordinates with data from the csv file
with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        X.append(float(row[0]))
        Y.append(float(row[1]))

class LinearRegression:
    def __init__(self, X, Y):
        # initialize weights
        self.w0 = 0     # slope-intercept / bias
        self.w1 = 0     # slope
        # initialize data set
        self.X = X
        self.Y = Y
        # data set means
        self.mean_X = self.mean(X)
        self.mean_Y = self.mean(Y)

    def mean(self, nums):
        return sum(nums) / len(nums)

    def calulate_weights(self):
        self.w1 = self.calculate_w1()
        self.w0 = self.calculate_w0()

    def calculate_w1(self):
        sum_1, sum_2 = 0, 0

        for i in range(len(X)):
            sum_1 += (self.X[i] - self.mean_X) * (self.Y[i] - self.mean_Y)
            sum_2 += pow((self.X[i] - self.mean_X), 2)

        # divide after finished summing up
        return sum_1 / sum_2

    def calculate_w0(self):
        return self.mean_Y - self.w1 * self.mean_X

    def graph(self):
        # widen range of x and y axes on the graph
        max_x = numpy.max(X) + 3
        min_x = numpy.min(X) - 3

        # set x axis values
        x = numpy.linspace(min_x, max_x)
        # set y axis values
        y = self.w0 + self.w1 * x

        # equation format: y = w0 + w1 * x,
        final_equation = "y = " + str(round(linearRegression.w0, 4)) + " + " + str(round(linearRegression.w1, 4)) + " * x"

        # plot data points
        plot.scatter(X, Y, color = 'blue', label = 'Data points', marker = 'D')

        # plot line
        plot.plot(x, y, color = 'red', label = final_equation)

        # customize the plot
        plot.title('Linear Regression')
        plot.xlabel('x')
        plot.ylabel('y')
        plot.legend()
        plot.grid(True)
        plot.show()

linearRegression = LinearRegression(X, Y)
linearRegression.calulate_weights()
linearRegression.graph()
