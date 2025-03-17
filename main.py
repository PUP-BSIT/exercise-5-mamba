# BERNAS, ERNESTO
score = 0

print ("Mamba Quiz")
print ("")
print ("1.(Ernesto Bernas) What is the name of the main character in Yugi-Oh?")
print ("")
print ("A. Yugi Muto","                     C. Joey Wheeler") 
print ("B. Seto Kaiba","                    D. Maximillian Pegasus")

answer = "a"
user_answer = input("Enter your answer: ").lower()

if user_answer == answer:
    score += 1
    print ("Correct")
else:
    print (f"{user_answer} is Incorrect. The correct answer is {answer}. Yugi Muto")
    
print ("")
print ("2.(Ernesto Bernas) Who originally owns the Blue-Eyes White Dragon card?")
print ("")
print ("A. Main Character's Grandfather","  C. Main Character's Mom") 
print ("B. Main Character's Sister","       D. Main Character's Dad")

answer = "a"
user_answer = input("Enter your answer: ").lower()

if user_answer == answer:
    score += 1
    print ("Correct")
else:
    print (f"{answer} is Incorrect. The correct answer is {answer}. Main Character's Grandfather")

print("")
print ("3. (Ernesto Bernas) What is Maximillian Pegasus’ claim to fame?")
print(" ")
print ("A. The creator of Duel Monsters","  C. The creator of Duel Monsters Battle City") 
print ("B. The creator of the Duel Arena"," D. The creator of Duel Monsters Duelist Kingdom")

answer = "a" 
user_answer = input("Enter your answer: ").lower()

if user_answer == answer:
    score += 1
    print ("Correct!")
else:
    print (f"{user_answer} is Incorrect. The correct answer is {answer} He is the creator of Duel Monsters")

# BUENACIFRA, ABRIANNE
print ("")
print ("4.(Abrianne Buenacifra) Who is the main character in Tangled?")
print ("")
print ("A. Rapunzel","                      C. Eugene") 
print ("B. Gothel","                        D. Maximus")

answer = "a"
user_answer = input("Enter your answer: ").lower()

if user_answer == answer:
    score += 1
    print ("Correct!")
else:
    print (f"{user_answer} is Incorrect. The correct answer is {answer}. Rapunzel")

print ("")
print ("5.(Abrianne Buenacifra) What are the floating lights called?")
print ("")
print ("A. Fireflies","                      C. Stars") 
print ("B. Lanterns","                       D. Sun")

answer = "b"
user_answer = input("Enter your answer: ").lower()

if user_answer == "b":
    score += 1
    print ("Correct!")
else:
    print (f"{user_answer} is Incorrect. The correct answer is {answer}. Lanterns")

print ("")
print ("6.(Abrianne Buenacifra) What is the name of the chameleon in Tangled?")
print ("")
print ("A. Pascual","                        C. Pascal") 
print ("B. Pascul","                         D. Pasqual")

answer = "c"
user_answer = input("Enter your answer: ").lower()

if user_answer == "c":
    score += 1
    print ("Correct!")
else:
    print (f"{user_answer} is Incorrect. The correct answer is {answer}. Pascal")

# ROLDAN, GIAN RAFAEL
print(" ")
print("7. (Gian Rafael Roldan) Who is known as 'The King' in the NBA?")
print(" ")
print("A. Wilt Chamberlain","               C. Michael Jordan")
print("B. Kobe Bryant","                    D. LeBron James")
print("")

answer = "d"
user_answer = input("Enter your answer: ").lower()

if user_answer == answer:
    print("Correct!")
    score += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is {answer}.")

print(" ")
print("8. (Gian Rafael Roldan) Who is known as 'The Mamba' in the NBA?")
print(" ")
print("A. Wilt Chamberlain","               C. Michael Jordan")
print("B. Kobe Bryant","                    D. LeBron James")
print("")

answer = "b"
user_answer = input("Enter your answer: ").lower()

if user_answer == answer:
    print("Correct!")
    score += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is {answer}.")


# TERO, ALTHENO MARI
print(" ")
print("9. (Altheno Mari Tero) Who holds the record for the most points scored in a single NBA game?")
print(" ")
print("A. Wilt Chamberlain","               C. Michael Jordan")
print("B. Kobe Bryant","                    D. LeBron James")
print("")

answer = "a"
user_answer = input("Enter your answer: ").lower()

if user_answer == answer:
    print("Correct!")
    score += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is {answer}.")
 
print(" ")
print("10. (Altheno Mari Tero) What is the regulation height of a basketball hoop from the floor?")
print(" ")
print("A. 9 feet","                         C. 10 feet")
print("B. 11 feet","                        D. 12 feet")
print("")

answer = "c"
user_answer = input("Enter your answer: ").lower()

if user_answer == answer:
    print("Correct!")
    score += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is {answer}.")
    
#Total Score
if score >=5:
    print(f"Congratulations! You got {score} out of 10")
else:
    print(f"Failed! You got {score} out of 10")