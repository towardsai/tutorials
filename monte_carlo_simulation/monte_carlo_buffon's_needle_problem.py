#Import required libraries :
import random
import math
import matplotlib.pyplot as plt

#Main function to estimate PI value :
def monte_carlo(runs,needles,n_length,b_width):
    #Empty list to store pi values :
    pi_values = []
    
    #Horizontal line for actual value of PI :
    plt.axhline(y=math.pi, color='r', linestyle='-')
    
    #For all runs :
    for i in range(runs):
        #Initialize number of hits as 0.
        nhits = 0
        
        #For all needles :
        for j in range(needles):
            #We will find the distance from the nearest vertical line :
            #Min = 0     Max = b_width/2
            x = random.uniform(0,b_width/2.0)
            
            #The theta value will be from 0 to pi/2 :
            theta = random.uniform(0,math.pi/2)
            
            #Checking if the needle crosses the line or not :
            xtip  = x - (n_length/2.0)*math.cos(theta)  
            if xtip < 0 :
                nhits += 1
                
        #Going with the formula :
        numerator = 2.0 * n_length * needles
        denominator = b_width * nhits
       
        #Append the final value of pi :
        pi_values.append((numerator/denominator))
    
    #Final pi value after all iterations :
    print(pi_values[-1])
    
    #Plotting the graph :
    plt.plot(pi_values)    
        
#Total number of runs :
runs = 100

#Total number of needles :
needles = 100000

#Length of needle :
n_length = 2  

#space between 2 verical lines :
b_width =2

#Calling the main function :
monte_carlo(runs,needles,n_length,b_width)
