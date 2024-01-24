questions = [["Current Railway Minister of India is" , "mamta banarjee" , "Ram vilash" , "Ashwini Vaishnaw" , "Piyush Goyal" , "c"] ,
            ["Which god is also known as Gauri Nandan" , "Agni" , "Indra" , "Hanuman" , "Ganesha" , "d"] ,
            ["What does not grow on tree according to a popular Hindi saying?" , "money" , "flowers" , "leaves" , "fruits" , "a"]  ,
            ["which city is known as pink city in india " , "Banglore" , "Maysore" , "Jaipur" , "kochi" , "c"] ,
            ["who wrote india's national anthem" , "Rabindranath tagore" , "lal bahadur shastri" , "chetan bhagat" , "rk narayan" , "a"] ,
            ["how many religians in india" , "6" , "7" , "8" , "9" , "a"] ,
            ["when is national hindi diwas celebrated ?" , "13 september" , "14 september" , "14 july" , "15 august" , "b"] ,
            ["how many states are there in india" , "28" , "29" , "31" , "30" , "a"] ,
            ["where is india gate located " , "agra" , "punjab" , "mumbai" , "new delhi" , "d"] ,
            ["Who wrote vande matram " , "Sarat Chandra Chattopadhyay" , "rabindranath tagore" , "Bankim Chandra Chatterjee" , "ishwar chandra vidyasagar" , "c"] ,
            ["which of the following places is famous for the great vishnu temple" , "indonesia" , "afganistan" , "pakistan" , "cambodia" , "d"] ,
            ["where is largest bhuddhist monastry located " , "uttar pradesh" , "arunachal pradesh" , "himachal pradesh" , "sikkim" , "b"] ,
            ["which musical instrument is not a foreign origin" , "tabla" , "flute" , "sitar" , "voilin" , "b"] ,
            ["who was killed during 'opertaion bluestar' of 1984" , "baba santa singh" , "haji mastan" , "Jarnail Singh Bhindrawale" , "Homi Jehangir Bhabha" , "c"] ,
            ["which formar indian president died as a result of road accidnent" , "rajendra prasad" , "Faqruddin Ali Ahmed" , "Giani Zail Singh" , "R. venkatraman" , "c"]]


prize = [1000 , 2000 , 3000 , 4000 , 5000 , 10000 , 20000 , 40000 , 80000 , 160000 , 320000 , 640000 , 1250000 , 2500000 , 5000000 , 10000000]
for i in range(len(questions)):
    print(questions[i][0])
    print(f"a. {questions[i][1]}   b. {questions[i][2]}   c. {questions[i][3]}   d. {questions[i][4]} \n")
    userinput = input("enter your option \n")
    if(userinput in questions[i][5]):
        print(f"you won {prize[i]} rupees \n")
    elif(prize[i] < 320000 and prize[i] >= 10000):
        print("congo !! you won 10000 ✨ \n")
        break
    elif(prize[i] >= 320000 ):
        print("congo !! you won 320000 🎉\n")
        break
    else:
        print("oops !! better luck next time \n ")
        break
    