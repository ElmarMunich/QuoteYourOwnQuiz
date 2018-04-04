'''
#level 1: Richard Paul Astley
#text
Rick = 'Rick Astleys 1987 song ..1.. Gonna Give You Up was a No. 1 hit single
in 25 countries. The song won the 1988 Brit Award for Best British ..2.. .
Astley made a comeback in 2007, becoming an ..3.. phenomenon'. His music video
for "Never Gonna Give You Up" became integral to the meme known as ..4..'.

#answers
{'never':'Never','single':'Single','internet':'Internet',
'rickrolling':'rickrolling'}

#level 2: Robyn Rihanna Fenty
#text
Rihanna = 'Rihanna is a Barbadian-born singer, ..1.. and actress. In 2005,
Rihanna rose to fame with the release of her ..2.. studio album Music of the Sun
and its follow-up A Girl like Me (2006). Many of her songs rank among the
worlds best-selling singles of all time, including the single ..3..,
Among numerous awards and accolades, Rihanna has won nine Grammy Awards,
twelve American MusicAwards and twelve ..4..  Music Awards.'

#answers
{'songwriter':'songwriter','debut':'debut','umbrella':'Umbrella',
'billboard':'Billboard'}

#level 3: Madonna Louise Ciccone
#text
Madonna = 'Madonna is an American singer, songwriter, actress, and ..1.. .
After performing as a ..2.., guitarist and vocalist in the music groups
Breakfast Club and Emmy, Madonna signed with Sire Records in 1982. Her other
ventures include fashion design, writing childrens books, opening of health
clubs, and filmmaking. She also contributed in various charities and founded
the ..3.. organization in 2006. Upon being confirmed in the Catholic Church in
1966, she adopted ..4.. as a confirmation name.'

#answers
{'businesswoman':'businesswoman','drummer':'drummer',
'raising malawi':'Raising Malawi','veronica': 'Veronica'}
'''

level = 0
def game_level():
    #user chooses his level
    #if the user input is not a number 1, 2 or 3 the user is prompted an error message and
    #the program jumpes back
    #the fuction fill_in_the_blank is called with the argument reflecting the chosen level

    print ('Welcome to the world of music. In this game you can shine with your music knowledge!!!')
    level = raw_input('Choose your level: easy, medium or hard')
    if level == 'easy':
        print('You have chosen the easy level, Good luck!')
        fill_in_the_blank(Rick)
    elif level == 'medium':
        print('You have chosen the medium level, Try your best!')
        fill_in_the_blank(Rihanna)
    elif level == 'hard':
        print('You have chosen the hard level, You need more than luck!')
        fill_in_the_blank(Madonna)
    else:
        print('--------------------------------------------------------')
        print ('You did not choose a level. Try again!')
        game_level()
'''
def fill_in_the_blank(artist):
    blank_fill=1
    #Prompts a sentence to the user with a blank to fill and loops to the next
    #sentence if the answer is correct, jumps back otherwise
    #argument "artist" defined by the chosen level in "game_level"
    #blank_fill: defines the number of loops (sentences with blanks)
    #pos: choses the sentence to prompt in the appropriate list
    while blank_fill <= 4:
        print('--------------------------------------------------------')
        print(artist)
        answer = raw_input('Fill the blank >>> use only lower cases <<< : ')
        if answer == (artist[pos+1]):
            print(artist[pos+2])
            pos = pos + 3
            blank_fill = blank_fill + 1
        else:
            print(not_correct)
'''

game_level()
