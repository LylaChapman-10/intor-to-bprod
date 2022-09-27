def start():
    print("WELCOME TO THE WEST.")
    print(" YOU ARE LOOKING FOR YOUR FRIEND SANDRA, WHO WENT MISSING")
    a1 = input("Worker: Hello Traveler, what brings you to the Town house?\n 1. Im lost.. \n 2. Where should I go?\n 3. Do you know someone named Sandra?\n 4. Goodbye.\n")

    if a1 == "1":
        Imlost()
    elif a1 =="2":
        WTG()
    elif a1 =="3":
        Sandra()
    elif a1 =="4":
        Bye()
    else: 
        print("INVALID ANSWER")
      

def Imlost(): 
    print("Worker: Here's a map. YOU: Thank you\n YOU LEAVE THE TOWN HOUSE")
    a2 = input("1. Go to your INN \n 2. Go to the horse stables, \n 3. ask around about Sandra ")
    if a2 == "1":
        Inn()
    elif a2 == "2":
        Horse()
    elif a2 == "3":
        Ask()
    else:
        print("INVALID ANSWER")

    def Horse():
        print(" YOU WALK OVER TO THE STABLES..\n  YOU: Wow theres are some purty horses..\n YOU START TO PET THE HORSES\n do you know wh-\n HORSE KICKS YOU, YOU DIE")
    
    def Ask():
        print(" YOU ACCIDENTALY BUMP INTO A MAN..\n YOU: Hey! Im sorr-\n HE PUNCHES YOU IN THE FACE. YOU DIED")
   
    def Inn():
        print("YOU WALK TO THE INN YOUR STAYING AT, AS YOU GET TO THE FRONT DESK A TALL BUFFY MALE COMES UP TO YOU..\n Male: Who are you..\n HE SAYS IN A DARK GRUMPY VOICE.\n YOU: Im Y/N, Im here to check in?\n MALE: Oh yeah.. Y/N you are in room 41.")
    a3 = input("1. Go to your room.\n 2. talk to the male more.")
    if a3 == "1":
        room()
    elif a3 =="2":
        male()
    else:
        print("INVALID ANSWER")
def room():
    print("YOU WALK IN ROOM 41, A GOBLIN FIGHTS YOU, YOU LOSE.")

def male():
    print("YOU: Do you perhaps know someone named Sandra?\n Male: Yes. She came here earlier this week, she left abruptly saying she had buisness in the mountains or something...\n You: Really? What time did she leave at?!\n Male: Sorry I'm busy now..")




    
def WTG():
    print("Worker: The Icecream parolor is very good if you would like to go ..")
    a4 = input("YOU: 1. Thank you, I'll try it out\n 2. YOU: No thanks!")

    if a4 == "1":
        Try()
    elif a4 == "2":
        NO()
    else:
        print("INVALID ANSWER")
def NO():
    print("Worker: EXCUSE ME?? NO?? MY WONDERFUL DAUGHTER RUNS THAT ICECREAM PARLOR!!!\n WORKER MAN SOCCER PUNTS YOU...\n YOU DIED.")
   
def Try(): 
    print("YOU LEAVE THE TOWN HOUSE\n YOU WALK OVER TO THE INCECREAM PARLOR AND WALK IN.\n Worker: Hi! Welcome to Jan's Icecream Parlor! Thats me haha...What can I get ya?")
    a5 = input(" 1. Vanilla please!\n 2. Chocolate!\n 3. Have you heard of a lady named Sandra??")
    if a5 =="1":
        Van()
    elif a5 =="2":
        Choco()
    elif a5 == "3":
        Lady()
    else:
        print("INVALID ANSWER")
def Van():
    print("Worker: UGH! BASIC MAN EVER!!\n SHE THROWS ICECREAM AT YOU YOU GET A BRAINFREEZE AND FREEZE TO DEATH.")

def Choco():
    print("Worker: UGH! BASIC MAN EVER!!\n SHE THROWS ICECREAM AT YOU YOU GET A BRAINFREEZE AND FREEZE TO DEATH.")
    
def Lady():
    print("Worker: ....Yes! I remember she came into here a few days ago. I remeber seeing her a few days ago..\n She was telling me about how she was going to atempt to find gold hiden in the mountians.\n YOU: Thank you so much! YOU WALK TO THE DOOR AND ACIDENTALLY BUMP INTO A STRANGER\n Stranger: HEY YOU BUMPED INTO ME!\n YOU: I'm sorry! \n HE DROP KICKS YOU. DED ")








def Sandra():
    print("Worker: I've heard of someone with that name... I can't remember who.\n You: ...Thank you.\n YOU LEAVE THE TOWN HOUSE")
a6 = input( "1. Go to the icecream Palor\n 2. Go to the market\n 3. go talk to a coldminer by the mountian  ")
if a6 =="1":
    Palor() 
elif a6 == "2":
    Market()
elif a6 == "3":
    Mount()
else:
    print("INVALID ANSWER")
def Market():
    print("YOU WALK INTO THE MARKET, YOU SEE A CASHIER. YOU GO UP TO THEM \n YOU: Hve you seen a woman named Sandra? \n Worker: I don't think so... \n YOU: She has black hair.. 5'5? \n Worker: No sorry. \n YOU: Thanks anyway.   ")

def Palor():
    print("YOU WALK INTO  THE PARLOR, NO ONES IN THERE YOU GET IN LINE.\n Worker: Hello! What would you like Sr.? \n YOU: I would like plain ole Vanila\n Worker: Alright! It will be done in a few...")
a7 = input(" 1. Ask about Sandra\n 2. Don't say anything \\n 3. Hit on her")
if a7 == "1":
    Sand()
elif a7 =="2":
    Say()
elif a7 == "3":
    Hit()
else:
    print("INVALID ANSWER")
def Hit():
    print("YOU: you're like very pretty.. We could go on a icecream  date..? \n Worker: ugh, seriosuly I've had enough of men like you around here. You know what? I'm not giving you your icecream! Goodbye!!! \n WORKER ENDS YOU WITH ENTERNAL STARE")
def Say():
    print("Worker: your not going to talk to me? UGH SERIOSULY IV'E ALREADY HAVE HAD A BAD DAy. \n WORKER THROWS THE ICECREAM AT YOU, \n YOU FALL TO THE GROUND, \n HITTING YOUR HEAD AND DYING.")

def Sand():
    print(" Worker: Oh yeah! She came in here earlier this week saying something about going to find gold up in the mountian. \n I wonder where she got that myth from...\n YOUR REMEMBER A FEW MONTHS AGO SANDRA WAS TALKING ABOUT GOING TO THE MOUNTAINS TO LOOK FOR GOLD. \n YOU: Thank you so much I appreciate it. \n YOU GO OUT THE PARLOR TO THE MINE NEAR BY")










def Bye():
    print("...")

start()