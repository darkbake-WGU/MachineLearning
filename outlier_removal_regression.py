#!/usr/bin/python

import pickle

import matplotlib.pyplot as plt
import numpy
from sklearn.linear_model import LinearRegression

from outlier_cleaner import outlierCleaner

### load up some practice data with outliers in it
ages = pickle.load( open("practice_outliers_ages.pkl", "rb") )
net_worths = pickle.load( open("practice_outliers_net_worths.pkl", "rb") )



### ages and net_worths need to be reshaped into 2D numpy arrays
### second argument of reshape command is a tuple of integers: (n_rows, n_columns)
### by convention, n_rows is the number of data points
### and n_columns is the number of features
ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))
from sklearn.model_selection import train_test_split
ages_train, ages_test, net_worths_train, net_worths_test = train_test_split(ages, net_worths, test_size=0.1, random_state=42)

# ## fill in a regression here!  Name the regression object reg so that
# ## the plotting code below works, and you can see what your regression looks like

reg = LinearRegression().fit(ages_train, net_worths_train)

print(reg.coef_)

try:
    plt.plot(ages, reg.predict(ages), color="blue")
except NameError:
    pass
plt.scatter(ages, net_worths)
plt.show()


### identify and remove the most outlier-y points
cleaned_data = []*100
predictionNet_Worths = reg.predict(net_worths_train)
cleaned_data = outlierCleaner(predictionNet_Worths, ages_train, net_worths_train)

print(cleaned_data)






### only run this code if cleaned_data is returning data
if len(cleaned_data) > 0:
    ages, net_worths, errors = list(zip(*cleaned_data))
    ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
    net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))
    ages_train, ages_test, net_worths_train, net_worths_test = train_test_split(ages, net_worths, test_size=0.1,
                                                                                random_state=42)

    ### refit your cleaned data!
    try:
        reg.fit(ages_train, net_worths_train)
        plt.plot(ages_train, reg.predict(ages_train), color="blue")
    except NameError:
        print("you don't seem to have regression imported/created,")
        print("   or else your regression object isn't named reg")
        print("   either way, only draw the scatter plot of the cleaned data")

    plt.scatter(ages, net_worths)
    plt.xlabel("ages")
    plt.ylabel("net worths")
    plt.show()
else:
    print("outlierCleaner() is returning an empty list, no refitting to be done")






