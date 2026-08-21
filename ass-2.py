import math as m


#Q.1) Lists []
roll_no= int(input("Enter your roll number"))
num_digits=m.log10(roll_no)+1
L=[]

for i in range(num_digits):
  digit=roll_no%10
  L.append(digit*10)
  roll_no//=10

#Appending elements
print(L)
L.append(0)
print(L)
L.insert(0,0)
print(L)

#Deleting elements
L.remove(8)
print(L)
L.pop(1)
print(L)

#Sorting
sorted_list=L.sort()
print(sorted_list)
print(L)


L.sort(reverse=True)
print(L)

#Slicing
print("First three elements of the list:",L[:3])
print("Last three elements of the list:",L[-3:])

#Making a new list
new_L=[] 
average=sum(L)/len(L)

for i in range(len(L)):
  if L[i]>average:
    new_L.append(L[i])


#Q.2) Tuples ()

#Creating scores tuple from first 8 elements in above list
scores=tuple(L[:8])

#part (i) 
highest=max(scores)
print(highest)
highest_idx=scores.index(highest)     # first index where highest occurs
print(highest_idx)
hi_idx=scores.find(highest)
print(hi_idx)

lowest=min(scores)
print(lowest)
freq_lowest=scores.count(lowest)
print(freq_lowest)

#part (ii)
# Tuples are immutable, so they cannot be reversed in place; slicing creates a reversed tuple instead.

reversed_scores=list(scores[::-1])
print(reversed_scores)

#part (iii)
aScore= int(input("Enter a score to search for: "))

if aScore in scores:
  print("First occurance of aScore is at index:", scores.index(aScore))
else:
  print("Score not found")

#part (iv)
scores[0]=100 #This will raise an error because tuples are immutable and cannot be modified after creation.
#Tuple differs from a list because they are immutable, meaning their elements cannot be changed, added, or removed after the tuple is created. Lists, on the other hand, are mutable and allow for modifications.
print(L)


#part (v) Tuple unpacking using *
first,second, *remaining=scores
print("First score:", first)
print("Second score:", second)
print("Remaining scores:", remaining) 
#Note: Although scores is a tuple, remaining is a list because of the unpacking syntax used. The * operator collects all remaining elements into a list.


#Q.3) #random module
import random
random.seed(roll_no) #seed with roll number

#part (i) genrating random numbers in a given range
random_list= list(random.randint(100,900) for _ in range(100))

 
#part (ii) 

odd_numbers= list(x for x in random_list if x%2!=0) #all odd numbers in the list
print(odd_numbers)
print(len(odd_numbers))

#part (iii)
even_numbers=[x for x in random_list if x%2==0] #all even numbers in the list
print("Even_numbers: ",even_numbers)
# another method to find even numbers:
even_nos= [x for x in random_list if x not in odd_numbers] #all even numbers in the list
print("Even_numbers: ",even_nos)  

#part (iv) finding all prime numbers in the list
 
def isPrime(n):
  if n<=1:
    return False
  
  for i in range(2, int(m.sqrt(n))+1):
    if n%i==0:
      return False
    

  return True


prime_nos=[x for x in random_list if isPrime(x)] 
print("Prime_numbers: ",prime_nos)
print("No of prime numbers: ",len(prime_nos))

# part(v) Most frequent number and its frequency

most_frequent= max(set(random_list), key=random_list.count) #explanation: set(random_list) creates a set of unique numbers from the list, and max() finds the number with the highest count in the original list using random_list.count as the key function.
print(random_list.count(most_frequent))


#Q.4) Sets

roll_no= input("Enter your roll number (8 digit)")

digits=[int(d) for d in roll_no] #list of digits in roll number

A={d*7 for d in digits}
B={d*9 for d in digits}

#part(i) Union of A and B
union_set= A.union(B)
print(union_set)

#part(ii) Intersection of A and B
intersection_set= A.intersection(B)
print(intersection_set)

#part(iii) difference



