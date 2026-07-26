#learning loops

# for i in range(16,0,-1):
#     print(i)

# a = "Kenta Sherpa"
# print(len(a))
# for i in range(len(a)):
#     if i==4:
#         continue    
#     else:
#         print(a[i])
# n = 5
# # for i in range(n):
# #     print(i)
# n=int(input("Enter a number: "))
# count = 0
# sum = 0
# for i in range(1,n+1):
#     if n % i ==0:
#         count+=1
# if count == 2:
#     print("is",n,"a prime number")
# else:
#     print(n,"is not a prime number")
        
import random



for i in range(3):
    x = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == x:
        print("Congratulations! You guessed the correct number.")
    else:
        print("Sorry, that's not the correct number.The correct number was", x)

