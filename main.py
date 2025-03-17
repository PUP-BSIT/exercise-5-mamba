score = 0

print ("YUGI-OH Quiz")
print ("")
print ("1.(Ernesto Bernas) What is the name of the main character in Yugi-Oh?")
print ("A. Yugi Muto","                     C. Joey Wheeler") 
print ("B. Seto Kaiba","                    D. Maximillian Pegasus")

answer = input("Enter your answer: ")

if answer == "A" or answer == "a":
    score += 1
    print ("Correct")
else:
    print (f"{answer} is Incorrect. The correct answer is A. Yugi Muto")
    
print ("")
print ("2.(Ernesto Bernas) Who originally owns the Blue-Eyes White Dragon card?")
print ("A. Main Character's Grandfather","  C. Main Character's Mom") 
print ("B. Main Character's Sister","       D. Main Character's Dad")
input ("Enter your answer: ")

if answer == "A" or answer == "a":
    score += 1
    print ("Correct")
else:
    print (f"{answer} is Incorrect. The correct answer is A. Main Character's Grandfather")

print ("")
print ("3. (Ernesto Bernas) What is Maximillian Pegasus’ claim to fame?")
print ("A. The creator of Duel Monsters","  C. The creator of Duel Monsters Battle City") 
print ("B. The creator of the Duel Arena"," D. The creator of Duel Monsters Duelist Kingdom")
input ("Enter your answer: ")

if answer == "A" or answer == "a":
    score += 1
    print ("Correct")
else:
    print (f"{answer} is Incorrect. The correct answer is A. He is the creator of Duel Monsters")

print ("")
print ("7.(Gian Rafael Roldan) Who is known as 'The King' in the NBA?")
print ("A. Michael Jordan","  C. LeBron James") 
print ("B. Kobe Bryant","       D. Stephen Curry")
input ("Enter your answer: ")

if answer == "C" or answer == "c":
    score += 1
    print ("Correct")
else:
    print (f"{answer} is Incorrect. The correct answer is C. LeBron James")

print ("")
print ("8.(Gian Rafael Roldan) Who is known as 'The Mamba' in the NBA?")
print ("A. Michael Jordan","  C. LeBron James") 
print ("B. Kobe Bryant","       D. Stephen Curry")
input ("Enter your answer: ")

if answer == "B" or answer == "b":
    score += 1
    print ("Correct")
else:
    print (f"{answer} is Incorrect. The correct answer is B. Kobe Bryant")

if score >= 5:
    print (f"Congratulations! You got {score} out of 10 Items")
else: 
    print (f"Failed! you got {score} out of 10 Items")
score = 0

print("(Altheno Mari L. Tero) 9. Who holds the record for the most points scored in a single NBA game?")
print(" ")
print("a. Wilt Chamberlain")
print("b. Michael Jordan")
print("c. Kobe Bryant")
print("d. LeBron James")
print("")

answer = "a"
user_answer = input("Enter your answer: ").lower().strip()

if user_answer == answer:
    print("Correct!")
    score += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is {answer}.")
    
print("(Altheno Mari L. Tero) 10. 3. What is the regulation height of a basketball hoop from the floor?")
print(" ")
print("a. 9 feet")
print("b. 10 feet")
print("c. 11 feet")
print("d. 12 feet")
print("")

answer = "b"
user_answer = input("Enter your answer: ").lower().strip()

if user_answer == answer:
    print("Correct!")
    score += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is {answer}.")
    

print("Congratulations! You got {score} out of 10:", score)
