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
