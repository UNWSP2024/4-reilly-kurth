#Program #2: Movie Tix
#Reilly Kurth
#2/12/2025

total = 0.0

another_movie = True

while another_movie:
    movies = input("What movie would you like to see? ")
    tickets = int(input("How many tickets would you like? "))
    total += tickets

    answer = input("What to watch another movie? ")
    if answer == "yes":
        another_movie = True
    else:
        another_movie = False

print("Your total number of tickets is", total)


