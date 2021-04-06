# -*- coding: utf-8 -*-
"""seven-planets-riddle.ipynb

#Seven Planets Riddle

* Tutorial: https://news.towardsai.net/spr
* Github: https://github.com/towardsai/tutorials/tree/master/logic/seven_planets_riddle.py
"""

#Importing required libraries for calculations:
import numpy as np

#Lists of possible routes without any combinations:

#Routes starting with 1:
list1 = ["12","121","1232","12343","123454","12363","123676"]

#Routes starting with 2:
list2 = ["212","232","2343","23454","2363","23676","23","21"]

#Routes starting with 3:
list3 = ["32","343","3454","363","3676","34","3212","323","36"]

#Routes starting with 4:
list4 = ["43","454","434","43212","4323","4363","43676","45"]

#Routes starting with 5:
list5 = ["54","545","543212","5434","54363","543676","54323"]

#Routes starting with 6:
list6 = ["63","676","63212","6323","63454","636","67","6343"]

#Routes starting with 7:
list7 = ["76","767","763212","76323","763454","76343","7636"]

#Empty lists to store the routes with combinations:
one = []
two = []
three = []
four = []
five = []
six = []
seven = []


#Finding combinations for list1:
for i in range(len(list1)):
  if(list1[i][-1] == "1"):
    for j in range(len(list1)):
      one.append(list1[i]+list1[j][1:])

  elif(list1[i][-1] == "2"):
    for j in range(len(list2)):
      one.append(list1[i]+list2[j][1:])

  elif(list1[i][-1] == "3"):
    for j in range(len(list3)):
      one.append(list1[i]+list3[j][1:])

  elif(list1[i][-1] == "4"):
    for j in range(len(list4)):
      one.append(list1[i]+list4[j][1:])

  elif(list1[i][-1] == "5"):
    for j in range(len(list5)):
      one.append(list1[i]+list5[j][1:])

  elif(list1[i][-1] == "6"):
    for j in range(len(list6)):
      one.append(list1[i]+list6[j][1:])

  elif(list1[i][-1] == "7"):
    for j in range(len(list7)):
      one.append(list1[i]+list7[j][1:])

#Finding combinations for list2:
for i in range(len(list2)):
  if(list2[i][-1] == "1"):
    for j in range(len(list1)):
      two.append(list2[i]+list1[j][1:])

  elif(list2[i][-1] == "2"):
    for j in range(len(list2)):
      two.append(list2[i]+list2[j][1:])

  elif(list2[i][-1] == "3"):
    for j in range(len(list3)):
      two.append(list2[i]+list3[j][1:])

  elif(list2[i][-1] == "4"):
    for j in range(len(list4)):
      two.append(list2[i]+list4[j][1:])

  elif(list1[i][-1] == "5"):
    for j in range(len(list5)):
      two.append(list2[i]+list5[j][1:])

  elif(list2[i][-1] == "6"):
    for j in range(len(list6)):
      two.append(list2[i]+list6[j][1:])

  elif(list2[i][-1] == "7"):
    for j in range(len(list7)):
      two.append(list2[i]+list7[j][1:])

#Finding combinations for list3:
for i in range(len(list3)):
  if(list3[i][-1] == "1"):
    for j in range(len(list1)):
      three.append(list3[i]+list1[j][1:])

  elif(list3[i][-1] == "2"):
    for j in range(len(list2)):
      three.append(list3[i]+list2[j][1:])

  elif(list3[i][-1] == "3"):
    for j in range(len(list3)):
      three.append(list3[i]+list3[j][1:])

  elif(list3[i][-1] == "4"):
    for j in range(len(list4)):
      three.append(list3[i]+list4[j][1:])

  elif(list3[i][-1] == "5"):
    for j in range(len(list5)):
      three.append(list3[i]+list5[j][1:])

  elif(list3[i][-1] == "6"):
    for j in range(len(list6)):
      three.append(list3[i]+list6[j][1:])

  elif(list3[i][-1] == "7"):
    for j in range(len(list7)):
      three.append(list3[i]+list7[j][1:])


#Finding combinations for list4:
for i in range(len(list4)):
  if(list4[i][-1] == "1"):
    for j in range(len(list1)):
      four.append(list4[i]+list1[j][1:])

  elif(list4[i][-1] == "2"):
    for j in range(len(list2)):
      four.append(list4[i]+list2[j][1:])

  elif(list4[i][-1] == "3"):
    for j in range(len(list3)):
      four.append(list4[i]+list3[j][1:])

  elif(list4[i][-1] == "4"):
    for j in range(len(list4)):
      four.append(list4[i]+list4[j][1:])

  elif(list4[i][-1] == "5"):
    for j in range(len(list5)):
      four.append(list4[i]+list5[j][1:])

  elif(list4[i][-1] == "6"):
    for j in range(len(list6)):
      four.append(list4[i]+list6[j][1:])

  elif(list4[i][-1] == "7"):
    for j in range(len(list7)):
      four.append(list4[i]+list7[j][1:])


#Finding combinations for list5:
for i in range(len(list5)):
  if(list5[i][-1] == "1"):
    for j in range(len(list1)):
      five.append(list5[i]+list1[j][1:])

  elif(list5[i][-1] == "2"):
    for j in range(len(list2)):
      five.append(list5[i]+list2[j][1:])

  elif(list5[i][-1] == "3"):
    for j in range(len(list3)):
      five.append(list5[i]+list3[j][1:])

  elif(list5[i][-1] == "4"):
    for j in range(len(list4)):
      five.append(list5[i]+list4[j][1:])

  elif(list5[i][-1] == "5"):
    for j in range(len(list5)):
      five.append(list5[i]+list5[j][1:])

  elif(list5[i][-1] == "6"):
    for j in range(len(list6)):
      five.append(list5[i]+list6[j][1:])

  elif(list5[i][-1] == "7"):
    for j in range(len(list7)):
      five.append(list5[i]+list7[j][1:])

#Finding combinations for list6:
for i in range(len(list6)):
  if(list6[i][-1] == "1"):
    for j in range(len(list1)):
      six.append(list6[i]+list1[j][1:])

  elif(list6[i][-1] == "2"):
    for j in range(len(list2)):
      six.append(list6[i]+list2[j][1:])

  elif(list6[i][-1] == "3"):
    for j in range(len(list3)):
      six.append(list6[i]+list3[j][1:])

  elif(list6[i][-1] == "4"):
    for j in range(len(list4)):
      six.append(list6[i]+list4[j][1:])

  elif(list6[i][-1] == "5"):
    for j in range(len(list5)):
      six.append(list6[i]+list5[j][1:])

  elif(list6[i][-1] == "6"):
    for j in range(len(list6)):
      six.append(list6[i]+list6[j][1:])

  elif(list6[i][-1] == "7"):
    for j in range(len(list7)):
      six.append(list6[i]+list7[j][1:])


#Finding combinations for list7:
for i in range(len(list7)):
  if(list6[i][-1] == "1"):
    for j in range(len(list1)):
      seven.append(list7[i]+list1[j][1:])

  elif(list7[i][-1] == "2"):
    for j in range(len(list2)):
      seven.append(list7[i]+list2[j][1:])

  elif(list7[i][-1] == "3"):
    for j in range(len(list3)):
      seven.append(list7[i]+list3[j][1:])

  elif(list7[i][-1] == "4"):
    for j in range(len(list4)):
      seven.append(list7[i]+list4[j][1:])

  elif(list7[i][-1] == "5"):
    for j in range(len(list5)):
      seven.append(list7[i]+list5[j][1:])

  elif(list7[i][-1] == "6"):
    for j in range(len(list6)):
      seven.append(list7[i]+list6[j][1:])

  elif(list7[i][-1] == "7"):
    for j in range(len(list7)):
      seven.append(list7[i]+list7[j][1:])


#Storing only unique elements:
one = np.unique(one)
two = np.unique(two)
three = np.unique(three)
four = np.unique(four)
five = np.unique(five)
six = np.unique(six)
seven = np.unique(seven)

#Output with lengths of lists:

print("Length of List one is",len(one),"\n")
print("Elements of List one:\n")
print(one)
print("=========================================================================")
print("\n")



print("Length of List two is",len(two),"\n")
print("Elements of List two:\n")
print(two)
print("=========================================================================")
print("\n")

print("Length of List three is",len(three),"\n")
print("Elements of List three:\n")
print(three)
print("=========================================================================")
print("\n")

print("Length of List four is",len(four),"\n")
print("Elements of List four:\n")
print(four)
print("=========================================================================")
print("\n")

print("Length of List five is",len(five),"\n")
print("Elements of List five:\n")
print(five)
print("=========================================================================")
print("\n")

print("Length of List six is",len(six),"\n")
print("Elements of List six:\n")
print(six)
print("=========================================================================")
print("\n")

print("Length of List seven is",len(seven),"\n")
print("Elements of List seven:\n")
print(seven)

#Program to generate more combinations of possible routes:

#Empty lists to store the possible routes:
Fone = []
Ftwo = []
Fthree = []
Ffour = []
Ffive = []
Fsix = []
Fseven = []


#Finding combinations for list one:
for i in range(len(one)):
  if(one[i][-1] == "1"):
    for j in range(len(one)):
      Fone.append(one[i]+one[j][1:])

  elif(one[i][-1] == "2"):
    for j in range(len(two)):
      Fone.append(one[i]+two[j][1:])

  elif(one[i][-1] == "3"):
    for j in range(len(three)):
      Fone.append(one[i]+three[j][1:])

  elif(one[i][-1] == "4"):
    for j in range(len(four)):
      Fone.append(one[i]+four[j][1:])

  elif(one[i][-1] == "5"):
    for j in range(len(five)):
      Fone.append(one[i]+five[j][1:])

  elif(one[i][-1] == "6"):
    for j in range(len(six)):
      Fone.append(one[i]+six[j][1:])

  elif(one[i][-1] == "7"):
    for j in range(len(seven)):
      Fone.append(one[i]+seven[j][1:])


#Finding combinations for list two:
for i in range(len(two)):
  if(two[i][-1] == "1"):
    for j in range(len(one)):
      Ftwo.append(two[i]+one[j][1:])

  elif(two[i][-1] == "2"):
    for j in range(len(two)):
      Ftwo.append(two[i]+two[j][1:])

  elif(two[i][-1] == "3"):
    for j in range(len(three)):
      Ftwo.append(two[i]+three[j][1:])

  elif(two[i][-1] == "4"):
    for j in range(len(four)):
      Ftwo.append(two[i]+four[j][1:])

  elif(two[i][-1] == "5"):
    for j in range(len(five)):
      Ftwo.append(two[i]+five[j][1:])

  elif(two[i][-1] == "6"):
    for j in range(len(six)):
      Ftwo.append(two[i]+six[j][1:])

  elif(two[i][-1] == "7"):
    for j in range(len(seven)):
      Ftwo.append(two[i]+seven[j][1:])

#Finding combinations for list three:
for i in range(len(three)):
  if(three[i][-1] == "1"):
    for j in range(len(one)):
      Fthree.append(three[i]+one[j][1:])

  elif(three[i][-1] == "2"):
    for j in range(len(two)):
      Fthree.append(three[i]+two[j][1:])

  elif(three[i][-1] == "3"):
    for j in range(len(three)):
      Fthree.append(three[i]+three[j][1:])

  elif(three[i][-1] == "4"):
    for j in range(len(four)):
      Fthree.append(three[i]+four[j][1:])

  elif(three[i][-1] == "5"):
    for j in range(len(five)):
      Fthree.append(three[i]+five[j][1:])

  elif(three[i][-1] == "6"):
    for j in range(len(six)):
      Fthree.append(three[i]+six[j][1:])

  elif(three[i][-1] == "7"):
    for j in range(len(seven)):
      Fthree.append(three[i]+seven[j][1:])


#Finding combinations for list four:
for i in range(len(four)):
  if(four[i][-1] == "1"):
    for j in range(len(one)):
      Ffour.append(four[i]+one[j][1:])

  elif(four[i][-1] == "2"):
    for j in range(len(two)):
      Ffour.append(four[i]+two[j][1:])

  elif(four[i][-1] == "3"):
    for j in range(len(three)):
      Ffour.append(four[i]+three[j][1:])

  elif(four[i][-1] == "4"):
    for j in range(len(four)):
      Ffour.append(four[i]+four[j][1:])

  elif(four[i][-1] == "5"):
    for j in range(len(five)):
      Ffour.append(four[i]+five[j][1:])

  elif(four[i][-1] == "6"):
    for j in range(len(six)):
      Ffour.append(four[i]+six[j][1:])

  elif(four[i][-1] == "7"):
    for j in range(len(seven)):
      Ffour.append(four[i]+seven[j][1:])

#Finding combinations for list five:
for i in range(len(five)):
  if(five[i][-1] == "1"):
    for j in range(len(one)):
      Ffive.append(five[i]+one[j][1:])

  elif(five[i][-1] == "2"):
    for j in range(len(two)):
      Ffive.append(five[i]+two[j][1:])

  elif(five[i][-1] == "3"):
    for j in range(len(three)):
      Ffive.append(five[i]+three[j][1:])

  elif(five[i][-1] == "4"):
    for j in range(len(four)):
      Ffive.append(five[i]+four[j][1:])

  elif(five[i][-1] == "5"):
    for j in range(len(five)):
      Ffive.append(five[i]+five[j][1:])

  elif(five[i][-1] == "6"):
    for j in range(len(six)):
      Ffive.append(five[i]+six[j][1:])

  elif(five[i][-1] == "7"):
    for j in range(len(seven)):
      Ffive.append(five[i]+seven[j][1:])

#Finding combinations for list six:
for i in range(len(six)):
  if(six[i][-1] == "1"):
    for j in range(len(one)):
      Fsix.append(six[i]+one[j][1:])

  elif(six[i][-1] == "2"):
    for j in range(len(two)):
      Fsix.append(six[i]+two[j][1:])

  elif(six[i][-1] == "3"):
    for j in range(len(three)):
      Fsix.append(six[i]+three[j][1:])

  elif(six[i][-1] == "4"):
    for j in range(len(four)):
      Fsix.append(six[i]+four[j][1:])

  elif(six[i][-1] == "5"):
    for j in range(len(five)):
      Fsix.append(six[i]+five[j][1:])

  elif(six[i][-1] == "6"):
    for j in range(len(six)):
      Fsix.append(six[i]+six[j][1:])

  elif(six[i][-1] == "7"):
    for j in range(len(seven)):
      Fsix.append(six[i]+seven[j][1:])


#Finding combinations for list seven:
for i in range(len(seven)):
  if(seven[i][-1] == "1"):
    for j in range(len(one)):
      Fseven.append(seven[i]+one[j][1:])

  elif(seven[i][-1] == "2"):
    for j in range(len(two)):
      Fseven.append(seven[i]+two[j][1:])

  elif(seven[i][-1] == "3"):
    for j in range(len(three)):
      Fseven.append(seven[i]+three[j][1:])

  elif(seven[i][-1] == "4"):
    for j in range(len(four)):
      Fseven.append(seven[i]+four[j][1:])

  elif(seven[i][-1] == "5"):
    for j in range(len(five)):
      Fseven.append(seven[i]+five[j][1:])

  elif(seven[i][-1] == "6"):
    for j in range(len(six)):
      Fseven.append(seven[i]+six[j][1:])

  elif(seven[i][-1] == "7"):
    for j in range(len(seven)):
      Fseven.append(seven[i]+seven[j][1:])

#Storing only the unique elements:
Fone = np.unique(Fone)
Ftwo = np.unique(Ftwo)
Fthree = np.unique(Fthree)
Ffour = np.unique(Ffour)
Ffive = np.unique(Ffive)
Fsix = np.unique(Fsix)
Fseven = np.unique(Fseven)

#Lengths of the final lists:
print("Length of the Final List One:",len(Fone))
print("Length of the Final List Two:",len(Ftwo))
print("Length of the Final List Three:",len(Fthree))
print("Length of the Final List Four:",len(Ffour))
print("Length of the Final List Five:",len(Ffive))
print("Length of the Final List Six:",len(Fsix))
print("Length of the Final List Seven:",len(Fseven))
print("\n")

#Printing first 5 elements of each lists:
print(Fone[:5])
print(Ftwo[:5])
print(Fthree[:5])
print(Ffour[:5])
print(Ffive[:5])
print(Fsix[:5])
print(Fseven[:5])

#Getting routes with exactly 10 movements:

#Empty list to store the routes:
List_one = []
List_two = []
List_three = []
List_four = []
List_five = []
List_six = []
List_seven = []

#List of routes starting with "1" with 10 movements:
for i in range(len(Fone)):
  if(len(Fone[i])>=10):
    List_one.append(Fone[i][:10])

#List of routes starting with "2" with 10 movements:
for i in range(len(Ftwo)):
  if(len(Ftwo[i])>=10):
    List_two.append(Ftwo[i][:10])

#List of routes starting with "3" with 10 movements:
for i in range(len(Fthree)):
  if(len(Fthree[i])>=10):
    List_three.append(Fthree[i][:10])

#List of routes starting with "4" with 10 movements:
for i in range(len(Ffour)):
  if(len(Ffour[i])>=10):
    List_four.append(Ffour[i][:10])

#List of routes starting with "5" with 10 movements:
for i in range(len(Ffive)):
  if(len(Ffive[i])>=10):
    List_five.append(Ffive[i][:10])

#List of routes starting with "6" with 10 movements:
for i in range(len(Fsix)):
  if(len(Fsix[i])>=10):
    List_six.append(Fsix[i][:10])

#List of routes starting with "7" with 10 movements:
for i in range(len(Fseven)):
  if(len(Fseven[i])>=10):
    List_seven.append(Fseven[i][:10])

#Getting only unique elements:
List_one = np.unique(List_one)
List_two = np.unique(List_two)
List_three = np.unique(List_three)
List_four = np.unique(List_four)
List_five = np.unique(List_five)
List_six = np.unique(List_six)
List_seven = np.unique(List_seven)

#Lengths of the final lists:
print("Length of the Final List One:",len(List_one))
print("Length of the Final List Two:",len(List_two))
print("Length of the Final List Three:",len(List_three))
print("Length of the Final List Four:",len(List_four))
print("Length of the Final List Five:",len(List_five))
print("Length of the Final List Six:",len(List_six))
print("Length of the Final List Seven:",len(List_seven))
print("\n")

#Printing first 5 elements of each lists:
print(List_one[:5])
print(List_two[:5])
print(List_three[:5])
print(List_four[:5])
print(List_five[:5])
print(List_six[:5])
print(List_seven[:5])

#Verifying our solution route for Routes starting with 1:

#b is the solution route:
b = "2343623436"

#Empty list to store the matching routes:
list_1 = []

#To check for all the elements in the list:
for i in range(len(List_one)):
  a = List_one[i]

#Append the route if at least one element match with the solution list:
  for j in range(10):
    if(a[j] == b[j]):
      list_1.append(a)

#Get the unique elements only:
list_1 = np.unique(list_1)

#Comparing the list with original list:
if(len(List_one) == len(list_1)):
  print("Congratulations!!")
  print("Solution route is successful on possible routes starting with 1")

else:
  print("Solution route may not work universally.")

#Combining all the lists:

List_all = []

for i in range(len(List_one)):
  List_all.append(List_one[i])

for i in range(len(List_two)):
  List_all.append(List_two[i])

for i in range(len(List_three)):
  List_all.append(List_three[i])

for i in range(len(List_four)):
  List_all.append(List_four[i])

for i in range(len(List_five)):
  List_all.append(List_five[i])

for i in range(len(List_six)):
  List_all.append(List_six[i])

for i in range(len(List_seven)):
  List_all.append(List_seven[i])

#Verifying our solution route (Universal):

#b is the solution route:
b = "2343623436"

def verify(solution_route, list_name):
  b = solution_route

  if (list_name == "List_one"):
    List_name = List_one
  elif (list_name == "List_two"):
    List_name = List_two
  elif (list_name == "List_three"):
    List_name = List_three
  elif (list_name == "List_four"):
    List_name = List_four
  elif (list_name == "List_five"):
    List_name = List_five
  elif (list_name == "List_six"):
    List_name = List_six
  elif (list_name == "List_seven"):
    List_name = List_seven
  elif (list_name == "List_all"):
    List_name = List_all

  #Empty list to store the matching routes:
  list_new = []

  #To check for all the elements in the list:
  for i in range(len(List_name)):
    a = List_name[i]

  #Append the route if at least one element match with the solution list:
    for j in range(10):
      if(a[j] == b[j]):
        list_new.append(a)

  #Get the unique elements only:
  list_new = np.unique(list_new)

  #Comparing the list with original list:
  if(len(List_name) == len(list_new)):
    print("Congratulations!!")
    print("The provided solution route is successful on possible routes starting with",list_name[5:])

  else:
    print("The provided solution route may not work universally.")

print("List Names:")
print("List_one")
print("List_two")
print("List_three")
print("List_four")
print("List_five")
print("List_six")
print("List_seven")
print("\n")

#List of list namesL
L_N = ["List_one","List_two","List_three","List_four","List_five","List_six","List_seven","List_all"]

#Taking input from user:
solution_route = input("Enter the solution route you want to verify: ")
list_name = input("Enter the name of the list you want to verify: ")
print("\n")

#Verifying inputs:
if((len(solution_route) != 10)):
  print("Please enter a solution route with 10 movements.")

  if(list_name not in L_N):
    print("Please enter a valid list name.")

else:
  if(list_name not in L_N):
    print("Please enter a valid list name.")

  else:
    verify(solution_route,list_name)
