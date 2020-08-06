#Import required libraries :
import random
import matplotlib.pyplot as plt

#We are going with 3 doors :
#1 - Car
#2 - Goats
doors = ["goat","goat","car"]

#Empty lists to store probability values :
switch_win_probability = []
stick_win_probability = []

plt.axhline(y=0.66666, color='r', linestyle='-')
plt.axhline(y=0.33333, color='g', linestyle='-')

#Monte_Carlo Simulation :
def monte_carlo(n):
    
    #Calculating switch and stick wins :
    switch_wins = 0
    stick_wins = 0
    
    for i in range(n):
    
        #Randomly placing the car and goats behind the three doors :
        random.shuffle(doors) 
        
        #Contestant's choice :
        k = random.randrange(2)  

        #If the contestant doesn't get car :
        if doors[k] != 'car': 
            switch_wins += 1
            
        #If the contestant got car :
        else: 
            stick_wins += 1

        #Updating the list values :
        switch_win_probability.append(switch_wins/(i+1))
        stick_win_probability.append(stick_wins/(i+1))
        
        #Plotting the data :
        plt.plot(switch_win_probability)
        plt.plot(stick_win_probability)
        
    #Print the probability values :
    print('Winning probability if you always switch:',switch_win_probability[-1])
    print('Winning probability if you always stick to your original choice:', stick_win_probability[-1])


#Calling the function :
monte_carlo(1000)
