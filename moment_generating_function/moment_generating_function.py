#1-Dimensional Data:

#Import required libraries:
from scipy import stats

#Dataset:
d = [1,2,3,4,5]

#Finding 0th moment:
print("0th Moment = ",stats.moment(d,moment=0))

#Finding 1st moment:
print("1st Moment = ",stats.moment(d,moment=1))

#Finding 2nd moment:
print("2nd Moment = ",stats.moment(d,moment=2))

#Finding 3nd moment:
print("3nd Moment = ",stats.moment(d,moment=3))

#Finding 4th moment:
print("4th Moment = ",stats.moment(d,moment=4))


#============================================================


#2-Dimensional Data:

#Import required libraries:
from scipy import stats

#Dataset:
d = [[5,6,9,11,3],[21,4,8,15,2]]

#Finding 0th moment:
print("0th Moment = ",stats.moment(d,moment=0))

#Finding 1st moment:
print("1st Moment = ",stats.moment(d,moment=1))

#Finding 2nd moment:
print("2nd Moment = ",stats.moment(d,moment=2))

#Finding 3nd moment:
print("3nd Moment = ",stats.moment(d,moment=3))

#Finding 4th moment:
print("4th Moment = ",stats.moment(d,moment=4))


#============================================================


#2-Dimensional Data:
#Set axis=1 (Horizonatal):

#Import required libraries:
from scipy import stats

#Dataset:
d = [[5,6,9,11,3],[21,4,8,15,2]]

#Finding 0th moment:
print("0th Moment = ",stats.moment(d,moment=0,axis=1))

#Finding 1st moment:
print("1st Moment = ",stats.moment(d,moment=1,axis=1))

#Finding 2nd moment:
print("2nd Moment = ",stats.moment(d,moment=2,axis=1))

#Finding 3nd moment:
print("3nd Moment = ",stats.moment(d,moment=3,axis=1))

#Finding 4th moment:
print("4th Moment = ",stats.moment(d,moment=4,axis=1))


#============================================================


#Multi-Dimensional Data:

#Import required libraries:
from scipy import stats

#Dataset:
d = [[5,6,9,11,3],
     [21,4,8,15,2],
    [15,23,42,1,36]]

#Finding 0th moment:
print("0th Moment = ",stats.moment(d,moment=0))

#Finding 1st moment:
print("1st Moment = ",stats.moment(d,moment=1))

#Finding 2nd moment:
print("2nd Moment = ",stats.moment(d,moment=2))

#Finding 3nd moment:
print("3nd Moment = ",stats.moment(d,moment=3))

#Finding 4th moment:
print("4th Moment = ",stats.moment(d,moment=4))


#============================================================


#2-Dimensional Data:
#Set axis=1 (Horizonatal):
#Higher Order Moments:

#Import required libraries:
from scipy import stats

#Dataset:
d = [[5,6,9,11,3],[21,4,8,15,2]]

#Finding 10th moment:
print("10th Moment = ",stats.moment(d,moment=10,axis=1))

#Finding 12th moment:
print("12th Moment = ",stats.moment(d,moment=12,axis=1))
