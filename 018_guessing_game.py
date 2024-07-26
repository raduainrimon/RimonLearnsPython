sec_num = 5
guess_count = 0 #number of guesses
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess (1-10): "))
    guess_count += 1
    if guess == sec_num:
        print(f"Congratulations! {guess} is a correct guess.")
        break
else:
    print("Sorry, wrong guess!")
