'''
Created on Oct 19, 2017

@author: emilydutile
'''

import sys

# TODO
# input a list, output the mean
def mean(l):
    if l != []:
        newl = [float(i) for i in l]
        average = sum(newl) / float(len(newl))
        return average
    return 0

##
    
def mean_test(l, expected):
    print("mean({})={:.5f}, expected={:.5f}".format(str(l), mean(l), expected))
    
    
def scovariance(l1, l2):
    x_mean = mean(l1)
    y_mean = mean(l2)
    data = [(l1[i] - x_mean) * (l2[i] - y_mean) for i in range(len(l1))]
    return sum(data) / (len(data)-1)
    #return 0


# input a list, output the sample variance
# equal to the self-covariance
def svariance(l):
    m = mean(l)
    varRes = sum([(xi - m)**2 for xi in l]) / len(l)
    return scovariance(l,varRes)

##

def svariance_test(l, expected):
    print("svariance({})={:.5f}, expected={:.5f}".format(str(l), svariance(l), expected))
    
svariance_test([1, 2, 3], 1.)
svariance_test([1, 2, 3, 4], 5./3.)
svariance_test([600, 470, 170, 430, 300], 27130)

##

def scovariance_test(l1, l2, expected):
    print("scovariance({}, {})={:.5f}/{:.5f}, expected={:.5f}".format(str(l1), str(l2), scovariance(l1, l2), scovariance(l2, l1), expected))
    


def main(argv):    
    scovariance_test([2.1, 2.5, 3.6, 4.0], [8, 10, 12, 14], 8./3.)



if __name__ == "__main__":
    main(sys.argv[1:])