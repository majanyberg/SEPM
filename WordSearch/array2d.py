import numpy as np
from numpy import array
import itertools
import random
import string

class Array2D:
    def __init__(self,rows,cols):
        self.theRows=[]
        for i in range(rows):
            self.theRows.append([0 for _ in range(cols)])

    def numrows(self):
        #print(len(self.theRows))
        return (len(self.theRows))

    def numcols(self):
        return (len(self.theRows[0]))

    def clear(self,value):
        for i in range(self.numrows()):
            self.theRows[i].clear(value)

    def __getitem__(self,pos):
        assert len(pos)==2,"Two subscripts required."
        i=pos[0]
        j=pos[1]
        assert i>=0 and i<self.numrows()\
               and j>=0 and j<self.numcols(),\
        "Invalid element subscript"
        return self.theRows[i][j]

    def __setitem__(self,pos,value):
        assert len(pos)==2,"Two subscripts required."
        i=pos[0]
        j=pos[1]
        assert i>=0 and i<self.numrows()\
               and j>=0 and j<self.numcols(),\
        "Invalid element subscript"
        self.theRows[i][j]=value

    def traverse(self):
        x=self.numrows()
        y=self.numcols()
        for i in range(x):
            for j in range(y):
                print(self.theRows[i][j], end=" ")
            print()
    
    def place_word(self, word, direction,start_cord_x,start_cord_y):
        placements_x = [start_cord_x]
        placements_y = [start_cord_y]

        dx = direction[0]
        dy = direction[1]

        start_x=start_cord_x
        start_y=start_cord_y
        for _ in range(len(word)-1):
            #letter = word[letter_index]
            start_x+=dx
            start_y+=dy
            print(start_x, start_y)
            if start_x>9 or start_x<0 or start_y>9 or start_y<0:
                return False
            if self.theRows[start_x][start_y]!=0:
                return False
            placements_x.append(start_x)
            placements_y.append(start_y)

        for letter_index in range(len(word)):
            letter = word[letter_index]
            x = placements_x[letter_index]
            y = placements_y[letter_index]
            self.theRows[x][y]= letter
        return True

        


    def populate(self):
        x=self.numrows()
        y=self.numcols()
        words_to_add = ['morot', 'potatis', 'fisk']
        # rand_row_col = [random.uniform(0,1) for _ in range(8)]

        for index in range(len(words_to_add)):
            word = words_to_add[index]
            placed = False

            long = len(word)

            directions = [[1,1],[-1,-1], [1,-1], [-1,1],
                          [0,1],[1,0], [0,-1], [-1,0]]

            while not(placed):
                start_cord_x = random.randint(0, 9)
                start_cord_y = random.randint(0, 9)
                rand_dir_probs = [random.random() for i in range(len(directions))]
                rand_dir_index = rand_dir_probs.index(max(rand_dir_probs))
                rand_dir = directions[rand_dir_index]
                placed = self.place_word(word, rand_dir,start_cord_x,start_cord_y)
                if placed:
                    print('params word,x,y,dir: \n',word,start_cord_x,start_cord_y,rand_dir)
        
        x=self.numrows()
        y=self.numcols()
        for i in range(x):
            for j in range(y):
                if self.theRows[i][j]==0:
                    self.theRows[i][j] = random.choice(string.ascii_uppercase)
        

                

                    


        
                
           

    
    def SelectedTraversal(self,From,To):
        assert type(From)==tuple and type(To)==tuple,"Two subscripts required."
        lst=[]
        #For vertical traversal
        if From[1] == To[1]:
            if From[0]>To[0]:
                direct = -1
            else:
                direct = 1
            for i in range(From[0],To[0],direct):
                lst.append(self.theRows[i][From[1]])
        #For horizontal traversal
        elif From[0] == To[0]:
            if From[1]>To[1]:
                direct = -1
            else:
                direct = 1
            for j in range(From[1],To[1],direct):
                lst.append(self.theRows[From[0]][j])
        #For diagnol traversal
        #elif To[0]-From[0] == To[1]-From[1]:
        else:
            if From[0]>To[0]:
                direct1 = -1
            else:
                direct1 = 1
            if From[1]>To[1]:
                direct2 = -1
            else:
                direct2 = 1
            for i,j in zip(range(From[0],To[0],direct1),range(From[1],To[1],direct2)):
                lst.append(self.theRows[i][j])
        return lst
    #def SelectedTraversal(self,From,To):
    #    if From[0] > To[0]:
    #        direct1 = -1
    #    else:
    #        direct1 = 1
    #    if From[1] > To[1]:
    #        direct2 = -1
    #    else:
    #        direct2 = 1
    #    for i,j in itertools.zip_longest(range(From[0],To[0],direct1),range(From[1],To[1],direct2)):
    #       pass

