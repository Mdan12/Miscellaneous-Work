import random



class Money():

    def Housechoices(self):
        houses = ["0", "1", "2", "3", "4", "5"]
        firsthouse = [1, 2, 3, 4, 5]
        moneyFirstHouse = random.choice(list(firsthouse))
        moneyNextHouses = []
        houses[moneyFirstHouse] = "Money"
        moneyMovement = random.randint(1,2)
        guesses = 0
        

        while True:
                FirstGuess = int(input("First Guess: "))
                if FirstGuess not in (1, 2, 3, 4, 5):
                    print("Only numbers between 1 and 5")
                else:
                    break

        if FirstGuess == moneyFirstHouse:
            print("you win.")
            quit()
        else:
            print("wrong pick.")
            guesses += 1
            print(guesses)

        
        while True:
            houses = ["0", "1", "2", "3", "4", "5"]
            moneyMovement = random.randint(1,2)
            if moneyMovement == 1:
                if moneyFirstHouse == 1:
                    moneyFirstHouse = 2
                    houses[moneyFirstHouse] = "money"
                else:
                    moneyFirstHouse = moneyFirstHouse - 1
                    houses[moneyFirstHouse] = "money"

            if moneyMovement == 2:
                if moneyFirstHouse == 5:
                    moneyFirstHouse = 4
                    houses[moneyFirstHouse] = "money"
                else:
                    moneyFirstHouse = moneyFirstHouse + 1
                    houses[moneyFirstHouse] = "money"
            while True:
                nextguess = int(input("Next guess: "))
                if nextguess not in (1, 2, 3, 4, 5):
                    print("Only numbers between 1 and 5")
                else:
                    break
                
              
            if nextguess == moneyFirstHouse:
                print("you win")
                quit()
            else:
                print("wrong")
                guesses += 1
                if guesses == 6:
                        quit()
                
                         
while True:
    houses = ["0", "1", "2", "3", "4", "5"]
    moneyMovement = random.randint(1,2)
    moneyhouse = Money()
    moneyhouse.Housechoices()






