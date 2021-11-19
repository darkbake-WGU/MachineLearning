#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []
    data = []*100
    n = 0

    ### your code goes here

    for prediction, net_worth, age in zip(predictions, net_worths, ages):
        data[n] = [(ages, net_worth, abs(prediction - net_worth)]

    data.sort(key=lambda y: y[2])

    cleaned_data = data[0:(81)]

    return cleaned_data
