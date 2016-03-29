__author__ = 'Evan'

phrase = ""

#program keeps asking for phrases until command quit

while phrase != "quit":
    #type a phrase (or quit to exit program)

    phrase = input("Type a phrase (or quit to exit program):\n").lower()
    if phrase == "quit":
        print("End of Program")
    else:
        #find the amount each vowel appears
        #each one of these variables represents each vowel and counts the amount of times it appears
        vowel_a = phrase.count("a")
        vowel_e = phrase.count("e")
        vowel_i = phrase.count("i")
        vowel_o = phrase.count("o")
        vowel_u = phrase.count("u")

        #Display amount of each vowel

        print("Letter A count:", vowel_a)
        print("Letter E count:", vowel_e)
        print("Letter I count:", vowel_i)
        print("Letter O count:", vowel_o)
        print("Letter U count:", vowel_u)

        #program keeps asking for phrases until command quit
