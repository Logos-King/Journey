print("Welcome to my Game Player")
name = input("What is your name? ")
age = int(input("What is your age? "))

health = 10


if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are starting with", health, "health" ,name)
        print("Let's play!")
    
        left_or_right = input("First choice... Left or Right? (left/right)? ")
        if left_or_right == "left":
            ans = input("Nice, you followed the path and reach a lake... Do you swim across or go around (across/around)? " )

            if ans == "around":
                print("You went around and reached the other side of the lake")
            elif ans == "across":
                print("You managed to get across, but were bit by  a fish and lost 5 health")
                health -= 5         
            ans = input("You notice a house and a river. Which do you venture to (river/house)? ")
            if ans == "house":
                print("You go to the house and are greeted by the owner... He stabs you and you lose 5 health")
                health -= 5

                if health <= 0:
                    print("Game Over, You lost all your health")
                else:
                    print("You continue on")
                    ans = input("Bleeding heavily you notice two doors, one with a Bull Insignia and one with a Lion Insignia, which do you enter (bull/lion)? ")
                    if ans == "lion":
                        print("The Lion congratulates you on making it this far and crowns you victor of the game")
                    else:
                        print("A minotaur thunders out of the room and gores you taking 5 health and ending your life")
                        health -= 5
            else:
                print("You fell in the river and drown")
        else:
            print("You fell down a hole and died")
    else:
        print("Sorry to see you go!")
else:
    print("You are not old enough to play....")

