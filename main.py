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

if Answer == "C" or Answer == "c":
    score += 1
    print ("Correct")
else:
    print (f"{Answer} is Incorrect. The correct answer is C. LeBron James")

print ("")
print ("8.(Gian Rafael Roldan) Who is known as 'The Mamba' in the NBA?")
print ("A. Michael Jordan","  C. LeBron James") 
print ("B. Kobe Bryant","       D. Stephen Curry")
input ("Enter your answer: ")

if Answer == "B" or Answer == "b":
    score += 1
    print ("Correct")
else:
    print (f"{Answer} is Incorrect. The correct answer is B. Kobe Bryant")

if score >= 5:
    print (f"Congratulations! You got {score} out of 10 Items")
else: 
    print (f"Failed! you got {score} out of 10 Items")