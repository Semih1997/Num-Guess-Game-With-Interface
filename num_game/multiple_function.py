import time

def with_friend():
    def all_include(num,feed_backs,feed_backs_inputs,counting,func,control): #control True if we need to take another input and func is int if we sure about the num is absulutely an integer.
        input_or_not = control
        num = func(num)
        print(feed_backs)
        if input_or_not == True:
            num = input(feed_backs_inputs)
            counting += 1
            print("Analyzing your num..")
        time.sleep(1)
        return num , counting

    guess_count = 1
    random_num = input("Give your num between the range of (0,250) and you have to give a integer: ") # a is string defaultly.

    while True:
        if not random_num.replace('-','',1).isdigit():
            random_num = input("Please give a valid INTEGER. Don't try againg lie to me: ")

        elif not int(random_num) in range(0,251) :
            random_num = input("Your num is not in RANGE(0,250). You can't lie to me: ")

        elif int(random_num) in range(0,251):
            random_num = int(random_num)
            print("Get your num succesfully. Give me to your friend!! After 3 second.")
            print("See you! I will hide your num :))")
            time.sleep(2)
            for i in range(30):
                print("")
            break

    a = input("Write your {}. guess between the range of (0,250): ".format(guess_count))
    guess_count += 1
    print("Analyzing your num..")
    time.sleep(0.5)

    while True:
        feed_backs=["WTF Write Numeric!!","Out of RANGE","Try BIGGER!!","Try LOWER!!",("Congrulation your {}. guess is the answer.".format(guess_count) , a)]
        feed_backs_inputs = ["Give your {}. guess: ".format(guess_count), "Please make your {}. guess between the range(0,250): ".format(guess_count)]

        if not a.replace('-','',1).isdigit():
            a , guess_count = all_include(a,feed_backs[0],feed_backs_inputs[0],guess_count,str,True)

        elif not int(a) in range(0,251):
            a , guess_count = all_include(a,feed_backs[1],feed_backs_inputs[1],guess_count,int,True)

        elif int(a) < random_num:
            a , guess_count = all_include(a,feed_backs[2],feed_backs_inputs[0],guess_count,int,True)

        elif random_num < int(a):
            a , guess_count = all_include(a,feed_backs[3],feed_backs_inputs[0],guess_count,int,True)

        else :
            all_include(a,feed_backs[4],None,guess_count,int,False)
            break

        if guess_count == 11:
            if int(a) == random_num: # a is a string defaultly.
                print("THAT'S THE ANSWER!")
                break 
            else:
                print("You can not find the number!! LOSER, YOU BORN TO DIE FOR NOTHING!! The answer was: ", random_num ,a)
                time.sleep(2)
                break