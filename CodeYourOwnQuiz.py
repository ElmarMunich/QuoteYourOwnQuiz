#level 1: Richard Paul Astley
#text
Rick = '''
Rick Astleys 1987 song ..1.. Gonna Give You Up was a No. 1 hit single
in 25 countries. The song won the 1988 Brit Award for Best British ..2.. .
Astley made a comeback in 2007, becoming an ..3.. phenomenon'. His music video
for "Never Gonna Give You Up" became integral to the meme known as ..4.. .
'''

#answers
l1 = {1:'Never',2:'Single',3:'Internet',4:'rickrolling'}

#level 2: Robyn Rihanna Fenty
#text
Rihanna = '''
Rihanna is a Barbadian-born singer, ..1.. and actress. In 2005,
Rihanna rose to fame with the release of her ..2.. studio album Music of the Sun
and its follow-up A Girl like Me (2006). Many of her songs rank among the
worlds best-selling singles of all time, including the single ..3..,
Among numerous awards and accolades, Rihanna has won nine Grammy Awards,
twelve American MusicAwards and twelve ..4..  Music Awards.
'''

#answers
l2 = {1:'songwriter',2:'debut',3:'Umbrella',4:'Billboard'}

#level 3: Madonna Louise Ciccone
#text
Madonna = '''
Madonna is an American singer, songwriter, actress, and ..1.. .
After performing as a ..2.., guitarist and vocalist in the music groups
Breakfast Club and Emmy, Madonna signed with Sire Records in 1982. Her other
ventures include fashion design, writing childrens books, opening of health
clubs, and filmmaking. She also contributed in various charities and founded
the ..3.. organization in 2006. Upon being confirmed in the Catholic Church in
1966, she adopted ..4.. as a confirmation name.
'''

#answers
l3 = {1:'businesswoman',2:'drummer',3:'Raising Malawi',4:'Veronica'}

def game_level():
    #user chooses his level
    #if the user input is not a number 1, 2 or 3 the user is prompted an error message and
    #the program jumpes back
    #the fuction fill_in_the_blank is called with the argument reflecting the chosen level

    print ('Welcome to the world of music. In this game you can shine with your music knowledge!!!')
    level = raw_input('Choose a level easy, medium or hard: ')
    # get level from user !!!! raw_input !!!
    if level == 'easy':
        print('You have chosen the easy level, Good luck!')
        fill_in_the_blank(Rick,l1)
    elif level == 'medium':
        print('You have chosen the medium level, Try your best!')
        fill_in_the_blank(Rihanna,l2)
    elif level == 'hard':
        print('You have chosen the hard level, You need more than luck!')
        fill_in_the_blank(Madonna,l3)
    else:
        print('--------------------------------------------------------')
        print ('You did not choose a possible level. Try again!')
        game_level()

def fill_in_the_blank(artist,level):
    ''' Input:
            artist and level as strings from user input
        Behavior:
            prints the text with the numbered blanks
            asks the user to fill the blanks (numbered by solution)
    '''
    blank_no = 1
    #blank number
    blank_max = 4
    #max number of blanks to fill
    print(artist)
    while blank_no <= blank_max:
        answer = raw_input('Fill the blank No'+ str(blank_no)+' : ')
        if answer.lower() == (level[blank_no]).lower():
            print(level[blank_no])
            artist = (artist.replace('..'+str(blank_no)+'..',(level[blank_no])))
            print (artist)
            blank_no = blank_no + 1

        else:
            print('Wrong answer. Try again:')

    nextlevel(artist)

def nextlevel(artist):
    #Congrats the user after finishing a level.
    #Lets user chose to play again
    #argument "artist"
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('Congratulations !!! You know a lot about the artist:')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    yes_no = raw_input('Do you want to play again? yes or no: ')
    if yes_no == 'yes':
        game_level()
    else:
        print('--------------------------------------------------------')
        print ('Good Bye!')
        return

game_level()
