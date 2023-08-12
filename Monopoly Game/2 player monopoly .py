import random

print("As soon as your money becomes 0 or -ve, u will Lose the game! ")
print("You have 50,000 rs cash at start of the game ")


def dice():
    a = random.randrange(1, 7)
    b = random.randrange(1, 7)
    return a + b


# print(dice())
# p1=[balance,position,cities,services,transportaion,rent earned,no of rounds,no. of houses]
p1 = [50000, 0, [], [], [], 0, 0, []]
p2 = [50000, 0, [], [], [], 0, 0, []]
p1id = 1
p2id = 2
list_ids = [0, p1, p2]


class sites:
    def __init__(self, name, pos, prce, ownr, huse, code):
        self.position = pos
        self.name = name
        self.price = prce
        self.owner = ownr
        self.house = huse
        self.code = code  # cities 0 , services 1, tax,rest house,club 2,  transportaion 3, chance 4, jail 6, community chest 8


Start = sites("Start", 0, 0, 0, 0, 7)
Mumbai = sites("Mumbai", 1, 8500, 0, 0, 0)
Water_works = sites("Water_works", 2, 3200, 0, 0, 1)
Railways = sites("Railways", 3, 9500, 0, 0, 3)
Ahmedabad = sites("Ahmedabad", 4, 4000, 0, 0, 0)
Income_tax = sites("Income_tax", 5, 0, 0, 0, 2)
Indore = sites("Indore", 6, 1500, 0, 0, 0)
Chance = sites("Chance", 7, 0, 0, 0, 4)
Jaipur = sites("Jaipur", 8, 3000, 0, 0, 0)
Jail = sites("Jail", 9, 0, 0, 0, 6)
Delhi = sites("Delhi", 10, 6000, 0, 0, 0)
Chandigarh = sites("Chandigarh", 11, 2500, 0, 0, 0)
Electric_company = sites("Electric_company", 12, 2500, 0, 0, 1)
Best = sites("Best", 13, 3500, 0, 0, 3)
Shimla = sites("Shimla", 14, 2200, 0, 0, 0)
Amritsar = sites("Amritsar", 15, 3300, 0, 0, 0)
Chest_community = sites("Community_chest", 16, 0, 0, 0, 8)
Srinagar = sites("Srinagar", 17, 5000, 0, 0, 0)
Club = sites("Club", 18, 200, 0, 0, 2)
Agra = sites("Agra", 19, 2500, 0, 0, 0)
Kanpur = sites("Kanpur", 21, 4000, 0, 0, 0)
Patna = sites("Patna", 22, 2000, 0, 0, 0)
Darjeeling = sites("Darjeeling", 23, 2500, 0, 0, 0)
Air_india = sites("Air_india", 24, 10500, 0, 0, 3)
Kolkata = sites("Kolkata", 25, 6500, 0, 0, 0)
Hyderabad = sites("Hyderabad", 26, 3500, 0, 0, 0)
Rest_house = sites("Rest_house", 27, 100, 0, 0, 2)
Chennai = sites("Chennai", 28, 7000, 0, 0, 0)
Bengaluru = sites("Bengaluru", 30, 4000, 0, 0, 0)
Wealth_tax = sites("Wealth_tax", 31, 200, 0, 0, 2)
Mysore = sites("Mysore", 32, 2500, 0, 0, 0)
Cochin = sites("Cochin", 33, 3000, 0, 0, 0)
Motor_boat = sites("Motor_boat", 34, 5500, 0, 0, 3)
Goa = sites("Goa", 35, 4000, 0, 0, 0)

list = [Start, Mumbai, Water_works, Railways, Ahmedabad, Income_tax, Indore, Chance, Jaipur, Jail, Delhi, Chandigarh,
        Electric_company, Best, Shimla, Amritsar, Chest_community, Srinagar, Club, Agra, Chance, Kanpur, Patna,
        Darjeeling,
        Air_india, Kolkata, Hyderabad, Rest_house, Chennai, Chest_community, Bengaluru, Wealth_tax, Mysore, Cochin,
        Motor_boat, Goa]
# print(len(list))
listloc = ["Start", "Mumbai", "Water_works", "Railways", "Ahmedabad", "Income_tax", "Indore", "Chance", "Jaipur",
           "Jail", "Delhi", "Chandigarh",
           "Electric_company", "Best", "Shimla", "Amritsar", "Chest_community", "Srinagar", "Club", "Agra", "Chance",
           "Kanpur", "Patna", "Darjeeling",
           "Air_india", "Kolkata", "Hyderabad", "Rest_house", "Chennai", "Bengaluru", "Wealth_tax", "Mysore", "Cochin",
           "Motor_boat", "Goa"]


# print(len(list))

def purchase(pos, ID):
    list[pos].owner = ID
    list_ids[ID][0] -= list[pos].price
    if list[pos].code == 0:
        list_ids[ID][2].append(list[pos].name)
    elif list[pos].code == 1:
        list_ids[ID][3].append(list[pos].name)
    elif list[pos].code == 3:
        list_ids[ID][4].append(list[pos].name)


# payment id1 to id2
def rent(pos, ID1, ID2):
    percent = 10
    if list[pos].house:
        percent = 20
    cash = (((percent * (list[pos].price)) / 100) // 100) * 100
    list_ids[ID1][0] -= cash
    list_ids[ID2][0] += cash
    # list_ids[ID1][5] -= cash
    list_ids[ID2][5] += cash
    print("Due to rent Player", ID1, "will give", cash, "to player", ID2)


def cashtobank(ID, cash):
    list_ids[ID][0] -= cash


def cashfrombank(ID, cash):
    list_ids[ID][0] += cash


# payment id1 to id2
def persontoperson(ID1, ID2, cash):
    list_ids[ID1][0] -= cash
    list_ids[ID2][0] += cash


def showall(ID):
    l = list_ids[ID]
    print("For Player", ID)
    print("Total Balance: ", l[0])
    print("Current Position: ", list[l[1]].name)
    print("Total Cities: ", l[2])
    print("Total Services: ", l[3])
    print("Total Transportaion: ", l[4])
    print("Total Rent Earned: ", l[5])
    print("Total Rounds: ", l[6])
    print("Houses made on: ", l[7])
    print("------------")


p1turn = True
p2turn = True


def chances(ID, roll):
    if roll == 2:
        print("Loss in share market Rs. 2000/-")
        cashtobank(ID, 2000)
    elif roll == 3:
        print("Lottery price Rs.2500")
        cashfrombank(ID, 2500)
    elif roll == 4:
        print("Fine for accident due to driving under liquor influence, Rs. 1000/-")
        cashtobank(ID, 1000)
    elif roll == 5:
        print("you have won the crossword competition prize Rs. 1000")
        cashfrombank(ID, 1000)
    elif roll == 6:
        print("House repairs Rs. 1500")
        cashtobank(ID, 1500)
    elif roll == 7:
        print("you have won a jackpot of Rs. 2000/-")
        cashfrombank(ID, 2000)
    elif roll == 8:
        print("Loss due to fire in godown, Rs. 3000/-")
        cashtobank(ID, 3000)
    elif roll == 9:
        print("Go back to Mumbai, if you have to pass starting point, collect Rs 1500/- and go to Darjeeling")
        cashfrombank(ID, 1500)
        list_ids[ID][6] += 1
        # self.rounds += 1
        list_ids[ID][1] = 23
        # self.position = 23
        # do we add +1 in rounds?
    elif roll == 10:
        print("Go to jail")
        cashtobank(ID, 1500)
        list_ids[ID][1] = 9
        print("You will now skip a chance as u landed on Jail. Also 1500 rs will be deducted.")
        # if ID==1:
        #     p1turn=False
        # else:
        #     p2turn = False
        # self.go_to_jail()
    elif roll == 11:
        print("Prize of best performance in Exports, Rs. 3000/-")
        cashfrombank(ID, 2500)
    elif roll == 12:
        print("Go to rest house, you cannot play next turn And 100 rs will get deducted.")
        list_ids[ID][1] = 27
        cashtobank(ID, 100)
        # self.position = 27
        # do we pay for going to rest house?
        # if ID==1:
        #     p1turn=False
        # else:
        #     p2turn = False
        # self.miss_turn()


def community_chest(ID, roll):
    if roll == 2:
        print("it is your birthday, collect from each player, Rs.500/-")
        cashfrombank(ID, 500)
        other = (ID % 2) + 1
        cashtobank(other, 500)
    elif roll == 3:
        print("Go to jail")
        cashtobank(ID, 1500)
        list_ids[ID][1] = 9
        print("You will now skip a chance as u landed on Jail. Also 1500 rs will be deducted.")
        # if ID == 1:
        #     p1turn = False
        # else:
        #     p2turn = False
        # self.go_to_jail()
    elif roll == 4:
        print("1st prize in reality TV show Rs. 2500/-")
        cashfrombank(ID, 2500)
    elif roll == 5:
        print("School & Medical Fees Rs.1000/-")
        cashtobank(ID, 1000)
    elif roll == 6:
        print("income tax refund Rs.2000/-")
        cashfrombank(ID, 2000)
    elif roll == 7:
        print("Marriage celebration Rs.2000/-")
        cashtobank(ID, 2000)
    elif roll == 8:
        print("Go to rest house, you cannot play next turn. And 100 rs will get deducted.")
        list_ids[ID][1] = 27
        cashtobank(ID, 100)
        # self.position = 27
        # do we pay for going to rest house?
        # if ID == 1:
        #     p1turn = False
        # else:
        #     p2turn = False
        # self.miss_turn()
    elif roll == 9:
        print("make general repair on all your properties: Each house pay Rs.50/-")
        cash = list_ids[ID][7] * 50
        cashtobank(ID, cash)

        # self.debit(len(self.houses) * 50)
    elif roll == 10:
        print("Receive interest on shares, Rs.1500/-")
        cashfrombank(ID, 1500)
    elif roll == 11:
        print("pay insurance premium, Rs.1500/-")
        cashtobank(ID, 1500)
    elif roll == 12:
        print("sale of stocks, collect Rs.3000/-")
        cashfrombank(ID, 3000)


def sell(ID):
    print("These are the locations available with u.")
    print("Cities: ", ', '.join(list_ids[ID][2]))
    print()
    print("Services: ", ', '.join(list_ids[ID][3]))
    print()
    print("Transportations: ", ', '.join(list_ids[ID][4]))
    print()
    a = input("Choose 1 for cities, 2 for services,3 for Transportations, 4 to exit: ")
    while (a != "1" and a != "2" and a != "3" and a != "4"):
        print("Invalid Input")
        a = input("Choose 1 for cities, 2 for services,3 for Transportations, 4 to exit: ")
    if a == "1" and len(list_ids[ID][2]) == 0:
        print("You can't choose this as it has no locations available ")
        a = "4"
    elif a == "2" and len(list_ids[ID][3]) == 0:
        print("You can't choose this as it has no locations available ")
        a = "4"
    elif a == "3" and len(list_ids[ID][4]) == 0:
        print("You can't choose this as it has no locations available ")
        a = "4"

    if a != "4":
        p = input("which location would u like to sell ? Enter the index starting from 1 : ")
        while (
                p != "1" and p != "2" and p != "3" and p != "4" and p != "5" and p != "6" and p != "7" and p != "8" and p != "9" and p != "10" and p != "11" and p != "12" and p != "13" and p != "14" and p != "15" and p != "16" and p != "17" and p != "18" and p != "19" and p != "20"):
            print("Invalid input")
            p = input("which location would u like to sell ? Enter the index starting from 1 : ")
        loc = ""

        if a == "1":
            l9 = []
            for d in range(1, len(list_ids[ID][2]) + 1):
                l9.append(str(d))
            while p not in l9:
                print("Invalid Input")
                p = input("which location would u like to sell ? Enter the index starting from 1 : ")
            p = int(p)
            loc = list_ids[ID][2][p - 1]
            list_ids[ID][2].remove(loc)
        elif a == "2":
            l9 = []
            for d in range(1, len(list_ids[ID][3]) + 1):
                l9.append(str(d))
            while p not in l9:
                print("Invalid Input")
                p = input("which location would u like to sell ? Enter the index starting from 1 : ")
            p = int(p)
            loc = list_ids[ID][3][p - 1]
            list_ids[ID][3].remove(loc)
        else:
            l9 = []
            for d in range(1, len(list_ids[ID][4]) + 1):
                l9.append(str(d))
            while p not in l9:
                print("Invalid Input")
                p = input("which location would u like to sell ? Enter the index starting from 1 : ")
            p = int(p)
            loc = list_ids[ID][4][p - 1]
            list_ids[ID][4].remove(loc)
        pos = listloc.index(loc)
        cash = ((list[pos].price // 2) // 100) * 100
        if list[pos].house:
            cash = (((list[pos].price + 500) // 2) // 100) * 100
        print("You will recieve", cash, "money.")
        cashfrombank(ID, cash)
        list[pos].owner = 0
    print("------------")
    showall(1)
    showall(2)


def house(ID, pos):
    if list_ids[ID][6] > 1:
        list[pos].house = ID
        print("You balance will get deducted by 500 rs")
        cashtobank(ID, 500)
        list_ids[ID][7].append(list[pos].name)
    else:
        print("You are not eligible to construct a house as u have not crossed the start location twice! ")


chance = 1

while list_ids[1][0] > 0 and list_ids[2][0] > 0:
    if chance % 2:
        if p1turn:
            print("Player 1 chance")
            if len(list_ids[1][2] + list_ids[1][3] + list_ids[1][4]) > 0:
                q = input("Do u want to sell any of ur property ? Press y for Yes and n for NO: ")
                while (q != "y" and q != "n"):
                    print("Invalid Input")
                    q = input("Do u want to sell any of ur property ? Press y for Yes and n for NO: ")
                if q == "y":
                    sell(1)
            print("Press enter to roll the dice")
            a = input()
            b = dice()
            print("You have scored : ", b)
            list_ids[1][1] = list_ids[1][1] + b
            if list_ids[1][1] > 35:
                list_ids[1][6] += 1
                print("You will recieve 1500 from the bank as u pass the start location")
                cashfrombank(1, 1500)
                list_ids[1][1] = (list_ids[1][1] % 36)
            pos = list_ids[1][1]
            print("You have landed on:", list[pos].name)
            if list[pos].code == 0 or list[pos].code == 3 or list[pos].code == 1:
                if list[pos].owner == 1:
                    if list[pos].code == 0:
                        if list_ids[1][6] < 2:
                            print(
                                "You are not eligible to construct a house as u have not crossed the start location twice! ")
                        else:
                            r = input("Do u want to make a house on this location ? Press y for Yes and n for NO: ")
                            while (r != "n" and r != "y"):
                                print("Invalid Input")
                                r = input("Do u want to make a house on this location ? Press y for Yes and n for NO")
                            if r == "y":
                                house(1, pos)
                    chance += 1
                elif list[pos].owner == 2:
                    rent(pos, 1, 2)
                    chance += 1
                else:
                    print("Do u want to purchase ", list[pos].name, "for price ", list[pos].price, " ? ")
                    print("Remember u will have to pay 1000 rs if u dont purchase it")
                    inp = input("Press y for YES and n for NO: ")
                    while (inp != "n" and inp != "y"):
                        print("Invalid Input")
                        inp = input("Press y for YES and n for NO: ")
                    if inp == "n":
                        list_ids[1][0] -= 1000
                        chance += 1
                    else:
                        purchase(pos, 1)
                        chance += 1
            else:
                if list[pos].code == 2:
                    if list[pos].name == "Club" or list[pos].name == "Wealth_tax":
                        print("Your 200 rs will get deducted due to ", list[pos].name)
                        cashtobank(1, 200)
                    elif list[pos].name == "Rest_house":
                        print("Your 100 rs will get deducted due to Rest House")
                        cashtobank(1, 100)
                    elif list[pos].name == "Income_tax":
                        cash = (((list_ids[1][5] * 10) / 100) // 100) * 100
                        print("Your", cash, "rs will get deducted due to Income tax")
                        cashtobank(1, cash)
                    chance += 1
                elif list[pos].code == 6:
                    cashtobank(1, 1500)
                    print("You will now skip a chance as u landed on Jail. Also 1500 rs will be deducted.")
                    p1turn = False
                    chance += 1
                else:
                    if list[pos].code == 4:
                        chances(1, b)
                        if b == 10 or b == 12:
                            p1turn = False
                        chance += 1
                    elif list[pos].code == 8:
                        community_chest(1, b)
                        if b == 3 or b == 8:
                            p1turn = False
                        chance += 1
        else:
            "Your chance has been skipped as u were in jail !!"
            a = input("Press Enter to proceed: ")
            p1turn = True
            chance += 1
    else:
        if p2turn:
            print("Player 2 chance")
            if len(list_ids[2][2]+list_ids[2][3]+list_ids[2][4])>0:
                q = input("Do u want to sell any of ur property ? Press y for Yes and n for NO: ")
                while (q != "y" and q != "n"):
                    print("Invalid Input")
                    q = input("Do u want to sell any of ur property ? Press y for Yes and n for NO: ")
                if q == "y":
                    sell(2)
            print("Press enter to roll the dice")
            a = input()
            b = dice()
            print("You have scored : ", b)
            list_ids[2][1] = list_ids[2][1] + b
            if list_ids[2][1] > 35:
                list_ids[2][6] += 1
                print("You will recieve 1500 from the bank as u pass the start location")
                cashfrombank(2, 1500)
                list_ids[2][1] = (list_ids[2][1] % 36)
            pos = list_ids[2][1]
            print("You have landed on:", list[pos].name)
            if list[pos].code == 0 or list[pos].code == 3 or list[pos].code == 1:
                if list[pos].owner == 2:
                    if list[pos].code == 0:
                        if list_ids[2][6] < 2:
                            print(
                                "You are not eligible to construct a house as u have not crossed the start location twice! ")
                        else:
                            r = input("Do u want to make a house on this location ? Press y for Yes and n for NO: ")
                            while (r != "n" and r != "y"):
                                print("Invalid Input")
                                r = input("Do u want to make a house on this location ? Press y for Yes and n for NO")
                            if r == "y":
                                house(2, pos)
                    chance += 1
                elif list[pos].owner == 1:
                    rent(pos, 2, 1)
                    chance += 1
                else:
                    print("Do u want to purchase ", list[pos].name, "for price ", list[pos].price, " ? ")
                    print("Remember u will have to pay 1000 rs if u dont purchase it")
                    inp = input("Press y for YES and n for NO: ")
                    while (inp != "n" and inp != "y"):
                        print("Invalid Input")
                        inp = input("Press y for YES and n for NO: ")
                    if inp == "n":
                        list_ids[2][0] -= 1000
                        chance += 1
                    else:
                        purchase(pos, 2)
                        chance += 1
            else:
                if list[pos].code == 2:
                    if list[pos].name == "Club" or list[pos].name == "Wealth_tax":
                        print("Your 200 rs will get deducted due to ", list[pos].name)
                        cashtobank(2, 200)
                    elif list[pos].name == "Rest_house":
                        print("Your 100 rs will get deducted due to Rest House")
                        cashtobank(2, 100)
                    elif list[pos].name == "Income_tax":
                        cash = (((list_ids[2][5] * 10) / 100) // 100) * 100
                        print("Your", cash, "rs will get deducted due to Income tax")
                        cashtobank(2, cash)
                    chance += 1
                elif list[pos].code == 6:
                    cashtobank(2, 1500)
                    print("You will now skip a chance as u landed on Jail. Also 1500 rs will be deducted.")
                    p2turn = False
                    chance += 1
                else:
                    if list[pos].code == 4:
                        chances(2, b)
                        if b == 10 or b == 12:
                            p2turn = False
                        chance += 1
                    elif list[pos].code == 8:
                        community_chest(2, b)
                        if b == 3 or b == 8:
                            p2turn = False
                        chance += 1
        else:
            "Your chance has been skipped as u were in jail !!"
            a = input("Press Enter to proceed: ")
            chance += 1
            p2turn = True

    print("------------")
    showall(1)
    showall(2)
if list_ids[1][0] <= 0:
    print("Player 2 Wins")
else:
    print("Player 1 Wins")

