def displayIntro():
    print('You are in a land full of dragons. In front of you \n '
          'you will see two caves. In one cave, the dragon is friendly \n' 
          ' in another cave he is not'
          )
def chooseCave():
    cave = ''
    while cave != '1' and cave !='2':
        print('Which cave will you go into? ')
        cave = input()
    return cave

def checkCave(chosencave)