def start():
    print("WELCOME TO THE WEST.\n")
    print(" YOU ARE LOOKING FOR YOUR FRIEND SANDRA, WHO WENT MISSING \n ")
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
        print("INVALID ANSWER \n")
      

def Imlost(): 
    print("Worker: Here's a map. YOU: Thank you\n YOU LEAVE THE TOWN HOUSE. \n ")
    a2 = input("1. Go to your INN \n 2. Go to the horse stables, \n 3. ask around about Sandra. \n ")
    if a2 == "1":
        Inn()
    elif a2 == "2":
        Horse()
    elif a2 == "3":
        Ask()
    else:
        print("INVALID ANSWER  \n ")

def Horse():
    print(" YOU WALK OVER TO THE STABLES..\n  YOU: Wow theres are some purty horses..\n YOU START TO PET THE HORSES\n do you know wh-\n HORSE KICKS YOU, YOU DIE.  \n  ")
    a11 = input(" 1. Ohno! I ded. \n 2. NOOOOOOOOOOOOOOOOOO \n")
    if a11 == "1":
        Oh()
    elif a11 == "2":
        NOOO()
    else:
        print("INVALID ANSWER\n")
def NOOO():
    print ("LOL REKT  DO NOT MESS WITH HORSES \n")
    a13 = input(" 1. Seesh mean much\n 2. I like your humor \n ")
    if  a13 == "1":
        seesh()
    elif a13 == "2":
        humor()
    else:
        print("INVALID ANSWER \n")

def humor():
    print(" Hey thanks man, nobody else likes my humor \n ")
    a15 =input(" 1. Yeah I like it. \n 2. NO SIKEEE \n ")
    if a15 == "1":
        yeahh()
    elif a15 == "2":
        SIKE()
    else:
        print("INVALID ANSWER \n ")
def yeahh():
    print("Hermm, maybe ill revive you huh? just rerun alrighty. \n")
def SIKE():
    print(" Woah dude, low blow. GET OUTTA HERE \n ")
def seesh():
    print("No humor huh? \n")
    a14 = input("1. I do have humor!! \n 2. Nah dude ur madd. \n")
    if a14 == "1":
        do()
    elif a14 == "2":
        mad()
    else:
        print("INVALID ANSWER \n")
def do():
    print(" Yeah yeah get outta here man. \n ")
def mad():
    print("bro what get out. \n")
def Oh():
    print(" Sucks to suck bozo")
    a12 = input("1. RUDE! \n 2. LOL\n")
    if a12 == "1":
        rude()
    elif a12 == "2":
        lol()
    else:
        print("INVALID ANSWER \n")

def rude():
    print("NOBODY CARES BYE \n")
def lol():
    print("Ikr, im so funny hahahah \n")

def Ask():
    print(" YOU ACCIDENTALY BUMP INTO A MAN..\n YOU: Hey! Im sorr-\n HE PUNCHES YOU IN THE FACE. YOU DIED \n")
    a30 = input( "1. NO WAY \n 2. How rude.. \n")
    if a30 == "1":
        NOWAYD()
    elif a30  == "2":
        rudde()
    else:
        print("INVALID ANSWER \n")
def NOWAYD():
    print(" LOL REKT RETRY \n")
def rudde():
    print("FRR LOL \n")
def Inn():
    print("YOU WALK TO THE INN YOUR STAYING AT, AS YOU GET TO THE FRONT DESK A TALL BUFFY MALE COMES UP TO YOU..\n Male: Who are you..\n HE SAYS IN A DARK GRUMPY VOICE.\n YOU: Im Y/N, Im here to check in?\n MALE: Oh yeah.. Y/N you are in room 41. \n")
    a3 = input("1. Go to your room.\n 2. talk to the male more. \n")
    if a3 == "1":
        room()
    elif a3 =="2":
        male()
    else:
        print("INVALID ANSWER \n")
def room():
    print("YOU WALK IN ROOM 41, A GOBLIN FIGHTS YOU, YOU LOSE. \n")

def male():
    print("YOU: Do you perhaps know someone named Sandra?\n Male: Yes. She came here earlier this week, she left abruptly saying she had buisness in the mountains or something...\n YOU: Really? What time did she leave at?!\n Male: Sorry I'm busy now.. \n YOU: Please \n Male; DUDE REALLY I SAID IM BUSY!!! \n HE PUNCHES YOU IN THE FACE YOU DED \n  ")




    
def WTG():
    print("Worker: The Icecream parolor is very good if you would like to go .. \n")
    a4 = input("YOU: 1. Thank you, I'll try it out\n 2. YOU: No thanks! \n")

    if a4 == "1":
        Try()
    elif a4 == "2":
        NO()
    else:
        print("INVALID ANSWER \n")
def NO():
    print("Worker: EXCUSE ME?? NO?? MY WONDERFUL DAUGHTER RUNS THAT ICECREAM PARLOR!!!\n WORKER MAN SOCCER PUNTS YOU...\n YOU DIED.")
   
def Try(): 
    print("YOU LEAVE THE TOWN HOUSE\n YOU WALK OVER TO THE INCECREAM PARLOR AND WALK IN.\n Worker: Hi! Welcome to Jan's Icecream Parlor! Thats me haha...What can I get ya? \n")
    a5 = input(" 1. Vanilla please!\n 2. Chocolate!\n 3. Have you heard of a lady named Sandra?? \n")
    if a5 =="1":
        Van()
    elif a5 =="2":
        Choco()
    elif a5 == "3":
        Lady()
    else:
        print("INVALID ANSWER \n")
def Van():
    print("Worker: UGH! BASIC MAN EVER!!\n SHE THROWS ICECREAM AT YOU YOU GET A BRAINFREEZE AND FREEZE TO DEATH. \n")

def Choco():
    print("Worker: UGH! BASIC MAN EVER!!\n SHE THROWS ICECREAM AT YOU YOU GET A BRAINFREEZE AND FREEZE TO DEATH. \n")
    
def Lady():
    print("Worker: ....Yes! I remember she came into here a few days ago. I remeber seeing her a few days ago..\n She was telling me about how she was going to atempt to find gold hiden in the mountians.\n YOU: Thank you so much! YOU WALK TO THE DOOR AND ACIDENTALLY BUMP INTO A STRANGER\n Stranger: HEY YOU BUMPED INTO ME!\n YOU: I'm sorry! \n HE DROP KICKS YOU. DED. \n ")








def Sandra():
    print("Worker: I've heard of someone with that name... I can't remember who.\n You: ...Thank you.\n YOU LEAVE THE TOWN HOUSE")
    a6 = input( "1. Go to the icecream Palor\n 2. Go to the market\n 3. go talk to a coldminer by the mountian \n ")
    if a6 =="1":
        Palor() 
    elif a6 == "2":
        Market()
    elif a6 == "3":
        Mount()
    else:
        print("INVALID ANSWER \n")
def Market():
    print("YOU WALK INTO THE MARKET, YOU SEE A CASHIER. YOU GO UP TO THEM \n YOU: Have you seen a woman named Sandra? \n Worker: I don't think so... \n YOU: She has black hair.. 5'5? \n Worker: No sorry. \n YOU: Thanks anyway. \n  ")
    a38 = input(" 1. Go ask someone else \n 2. Walk out of market ")
    if a38 == "1":
        elseu()
    elif a38 =="2":
        Walkoit()
    else:
        print("INVALID ANSWER")
def elseu():
    print(" YOU: Uh hello? Do you- \n A MAN PUNCHED YOU U DED")
def Walkoit():
    print(" YOU WALK OUT OF THE STORE AND FALL DOWN A MANHOLE. u ded")
def Mount():
    print(" YOU GO TO A MINER TO TALK TO THEM BUT GOT HIT IN THE HEAD WITH A SHOVEL AND DED.")
def Palor():
    print("YOU WALK INTO  THE PARLOR, NO ONES IN THERE YOU GET IN LINE.\n Worker: Hello! What would you like Sr.? \n YOU: I would like plain ole Vanila\n Worker: Alright! It will be done in a few...\n")
    a7 = input(" 1. Ask about Sandra\n 2. Don't say anything \n 3. Hit on her \n")
    if a7 == "1":
        Sand()
    elif a7 =="2":
        Say()
    elif a7 == "3":
        Hit()
    else:
        print("INVALID ANSWER \n")
def Hit():
    print("YOU: you're like very pretty.. We could go on a icecream  date..? \n Worker: ugh, seriosuly I've had enough of men like you around here. You know what? I'm not giving you your icecream! Goodbye!!! \n WORKER ENDS YOU WITH ENTERNAL STARE")
def Say():
    print("Worker: your not going to talk to me? UGH SERIOSULY IV'E ALREADY HAVE HAD A BAD DAY. \n WORKER THROWS THE ICECREAM AT YOU, \n YOU FALL TO THE GROUND, \n HITTING YOUR HEAD AND DYING.")

def Sand():
    print(" Worker: Oh yeah! She came in here earlier this week saying something about going to find gold up in the mountian. \n I wonder where she got that myth from...\n YOUR REMEMBER A FEW MONTHS AGO SANDRA WAS TALKING ABOUT GOING TO THE MOUNTAINS TO LOOK FOR GOLD. \n YOU: Thank you so much I appreciate it. \n YOU GO OUT THE PARLOR TO THE MINE NEAR BY \n")
    a8 = input(" 1. Go into mine\n 2. Talker to Miners\n 3. Go to the big crater in the mine. \n")
    if a8 == "1": 
        Mine()
    elif a8 == "2":
        Miner()
    elif a8 == "3":
        Crater()
    else:
        print("INVALID ANSWER \n")

def Mine():
    print(" YOU  WALK INTO THE MINE.. AS YOU GO IN FURTHER YOU HEAR A RUMBILING BEHIND YOU. ROCKS SUDDENLY SLIP TOWARDS YOU. DED \n")
def Crater():
    print(" AS YOU WALKTO THE CRATER YOU SUDDENLY GET SCARED BY BATS FLYING PASTY YOU, YOU  SLIP INTO THE CRATER. DED \n")
def Miner():
    print(" YOU: Hello, I'm wondering if you know someone named Sandra? \n Worker: Yes! She came  into this mine a few days ago. She said she was searching for something.. \n YOU: Did she come out of the mine orr??\n Worker: I haven't seen her since, I was a little worried but she did say she hadfood and water packed with her. \n YOU: Thanks. Is it alrightif I go down into the mine also? \n Worker: Yeah sure, make sure you come out with her lad. \n AS YOU ENTER AND WALK DOWN THE MINE THERE ARE THREE TUNNELS. \n ")
    a9 = input("1. Left tunnel \n 2. Middle tunnel \n 3. Right tunnel \n ")
    if a9 == "1":
        Left()
    elif a9 == "2":
        Middle()
    elif a9 == "3":
        Right()
    else:
        print("INVALID ANSWER \n")

def Left():
    print(" AS YOU WALK INTO THE TUNNEL A WORKER SUDDENLY HITS YOU IN THE HEAD WITH A SHOVEL YOU HIT YOUR HEAD AND DIE. \n")
    a16 =  input(" 1. How is that possible?? \n 2. Okay \n ")
    if a16 == "1":
        HOWW()
    elif a16 == "2":
        Oker()
    else:
        print("INVALID ANSWER \n")

def Oker():
    print(" wow your chill like that \n YOU: yer \n")
def HOWW():
    print("dude are you mad???")
    a17 = input(" 1. No.. \n 2. Who even are you? \n")
    if a17 == "1":
        bruhh()
    elif a17 == "2":
        Who()
    else:
        print("INVALID ANSWER \n")
def bruhh():
    print(" Imagine dying from a shovel LOL, get outta here \n ")
def Who():
    print(" I am the god of death..")
    a18 = input(" 1. Wait seriously? \n2. Na bro don't believe you haha\n")
    if a18=="1":
        Waut()
    elif a18 =="2":
        believe()
    else:
        print ("INVALID ANSWER \n")

def believe():
    print(" DEATH: Okay well.. \n HE SUMMONS YOU \n DEATH: Bye I'm banning you- \n DEATH BANS YOU FROM EXISTANCE ")
def Waut():
    print("DEATH: Yeah, you wanna be my sidekick? \n")
    a19 = input("1. YES! \n 2. No\n")
    if a19 == "1":
        sis()
    elif a19 == "2":
        ermm()
    else:
        print("INVALID ANSWER \n")
def sis():
    print(" DEATH: Alright  \n DEATH SUMMONS YOU TO THE UNDERWORLD\n YOU: Dang this is cool man. \n YOU LIVE WITH DEATH FOR FOREVER IT WAS AWESOME \n ")
def ermm():
    print("DEATH: well ur loss. \n DEATH BANS YOUR EXISTANCE\n")

def Middle():
    print(" YOU WALK INTO THE TUNNEL AND FALL INTO A SMALL NEVER ENDING CRATER. DED \n")
    a20 = input("1. Yowchies \n 2. Rip me \n")
    if a20 == "2":
        Yoww()
    elif a20 == "20":
        RIPaE()
    else:
        print("INVALID ANSWER \n")
def RIPaE():
    print(" LOL REKT. deeed \n")
def Yoww():
    print(" That hurt? BOZO \n")
    a21 = input(" 1. No.. 2. Yes it did!!\n ")
    if a21 =="1":
        UHUH()
    elif a21 == "2":
        did()
    else:
        print("INVALID ANSWER \n")
def did():
    print(" Na dude go workout.. \n")
def UHUH():
    print("Ur weak boi \n")
    a22 =  input(" 1. IM NOT \n 2. I guess.. \n ")
    if a22== "1":
        BRUUR()
    elif a22 == "2":
        Guessy()
    else:
        print("INVALID ANSWER \n")
def BRUUR():
    print(" UR BAD. DED \n")
def Guessy():
    print(" Hit the gym my guy.. \n")

def Right():
    print("YOU WALK INTO THE TUNNEL, YOU HEAR A DISTANCE VOICE.. YOU RUN TO THE VOICE. \n UNKNOWN: Help me!!!! \n YOU: Sandra..?? \n SANDRA: Yes! Y/N? \n YOU: are you alright? Whats wrong?? \n AS YOU WALK TO SANDRA YOU SEE HER LIMPING  \n SANDRA: I twisted my Ankle back there. I found the gold atleast! \n SHE MOVES HER BODY TO THE SIDE AND A STASH OF COINS SUDDENLY APPEAR. \n YOU: Seriosuly? How! \n SANDRA: I found it in a well a few miles down. I twisted my ankle climbing back up by slipping and falling back into the well. \n YOU: Jeesh, lets get you out of here so we can fix your leg. \n SANDRA: Alright. \n YOU HELP SANDRA AND GO OUT OF THE TUNNEL. SUDDENLY ROCKS START TUMBULING TOWARDS YOU.. \n  ")
    a10 =input(" 1. Run towards rocks. \n 2. Safe yourself. \n 3. Hide in a creves with Sandra")
    if a10 == "1":
        Ruaa()
    elif a10 == "2":
        Savee()
    elif a10 == "3":
        HIDE()
def Ruaa(): 
    print(" YOU RUN TOWARDS THE ROCKS WITH SANDRA, YOU GET HIT BY THE ROCKS AND DIE.\n ")
    a23 = input("1. bro I should have hid.. \n 2. Seriously \n ")
    if a23 == "1":
        BROW()
    elif a23 == "2": 
        Seriosu()
    else:
        print("INVALID ANSWER \n")
def BROW():
    print(" L L L REKT \n ")
def Seriosu():
    print(" LOL REKT REKT \n ")
def Savee():
    print("YOU RUN OUT OF THE MINE UNHARMED. YOU DIE OF GUILT OF LEAVING SANDRA BEHIND \n")
    a24 = input("1. Dude I saved myself how can I die of guilt..? \n 2. I guess thats alright.. \n")
    if a24 =="1":
        selff()
    elif a24 == "2":
        alrights()
    else:
        print("INVALID ANSWER \n ")

def alrights():
    print("Yeah thats what I thought \n") 

def selff():
    (" That's what you get for being  a horrible person. \n ")
    a25 = input(" 1. RUDE \n 2. Yeah.. \n")
    if a25 == "1":
        RUDEYS()
    elif a25 == "2":
        Yeahhh()
    else:
        print(" INVALID ANSWER \n")
def Yeahhh():
    print(" See now you get it \n")
def RUDEYS():
    print(" Bro I'm bannishing you for being a bad person \n ")
def HIDE():
    print(" YOU GRAB SANDRA AND THE GOLD AND RUN THE THE CREVES. THE ROCKS SLOWLY STOP TUMBLING AT YOU. \n SANDRA: Thank god.. Now lets get out of here! \n YOU AND SANDRA MOVE THE ROCKS AWAY AND LIMP TOWARDS THE EXIT. \n YOU: We're out! \n SANDRA: Great, lets get to a hospital now, huh? \n SANDRA RECOVERS FROM HER FRACTURED LEG AND YOU BOTH LIVE HAPPILY EVER AFTER WITH YOUR RICHES. \n ")
def Bye():
    print("... \n")

start()