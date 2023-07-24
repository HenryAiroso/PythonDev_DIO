T = input()

'''
TODO: Read the input variable and check if it has more or less than 140 characters.
If it's longer, print "MUTE", and if it's equal to or shorter, print "TWEET".
'''

Len_T = len(T)

if 1 <= Len_T <= 140:
    print("TWEET")
else:
    print("MUTE")
