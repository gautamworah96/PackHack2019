#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kzphy
#
# Created:     13/04/2019
# Copyright:   (c) kzphy 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os

def main():

##    h = open('G:/My Drive/NCSU/PackHacks2019/movie_names.txt','r')
##    names = h.readlines()
##    new_names = [r.strip() for r in names]
##    new_names_txt = [i+'.txt' for i in new_names]

    #files = os.listdir()
    files = ['SpiderMan.txt', 'SpiderMan2.txt', 'X-MenTheLastStand.txt', 'SpiderMan3.txt', 'IronMan.txt', 'IronMan2.txt', 'TheAvengers.txt', 'IronMan3.txt', 'TheAmazingSpider-Man2.txt', 'Avengers_AgeofUltron.txt', 'CaptainAmericaCivilWar.txt', 'Deadpool.txt', 'GuardiansoftheGalaxy 2.txt', 'ThorRagnarok.txt', 'Spider-ManHomecoming.txt', 'AvengersInfinityWar.txt', 'BlackPanther.txt']
    directory = 'G:/My Drive/NCSU/PackHacks2019/MovieScripts/'
    #files = files[len(files)-5:]
    f = (open(directory + '1_17.txt','a+'))
    for i in files:
        g = open(directory+i,'r')
        lines = g.readlines()
        f.write(''.join(lines)+'\n')
        g.close()
    f.close()

if __name__ == '__main__':
    main()
