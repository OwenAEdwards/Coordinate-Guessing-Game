def generate_location():
    x = int(input("Enter x-coordinate: "))
    while (x>100):
        x = int(input("Invalid input, x must be less than or equal to 100, re-enter x-coordinate: "))
    while (x<0):
        x = int(input("Invalid input, x must be greater than or equal to 0, re-enter x-coordinate: "))
    y = int(input("Enter y-coordinate: "))
    while (y>100):
        y = int(input("Invalid input, y must be less than or equal to 100, re-enter y-coordinate: "))
    while (y<0):
        y = int(input("Invalid input, y must be greater than or equal to 0, re-enter y-coordinate: "))
    return [x,y]

def generate_rand_location():
    import random
    # inclusive of both 0 and 100
    return [random.randint(0,100),random.randint(0,100)]

def make_direction(secret_location): 
    def direction(guess): # where guess is a list with coordinates [x,y]
        x,y=0,1 # indices for locations
        response=["Guess again, go"]
        # NOTE: we let the secret_location[y]==guess[y] and
        # secret_location[x]==guess[x] cases fall through
        if (secret_location[y]>guess[y]):
            response.append("north")
        elif (secret_location[y]<guess[y]):
            response.append("south")
        if (secret_location[x]>guess[x]):
            response.append("east")
        elif (secret_location[x]<guess[x]):
            response.append("west")
        response=" ".join(response) # joins the array elements
        response+="\n"
        return response
    return direction

status=1 # status of game starts on
game_number=0 # number of games starts at 0
# while the game's status is active...
while (status!=0):
    # prompts the user to continue the game or not
    status=int(input("Enter \'1\' for new game, \'0\' to exit: "))
    # if the user enters the wrong status, ask again
    while not (status==0 or status==1):
        print("Invalid input, enter again")
        status=int(input("Enter \'1\' for new game, \'0\' to exit: "))
    # if the game's status is active...
    if (status==1):
        game_number+=1
        print(f"\n\n=====Game number {game_number}=====\n")
        secret_location = generate_rand_location()
        direction = make_direction(secret_location)
        print("Enter guess location below\n")
        guess = generate_location()
        # guessing again
        while not (secret_location==guess):
            print(direction(guess))
            guess = generate_location()
    # if the game's status is not active...
        print(f"You found the secret location at {secret_location}!\n")
    elif (status==0):
        print("\nThank you for playing!\n")
        break
