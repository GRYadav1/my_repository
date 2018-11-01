'''
Created on Nov 1, 2018

@author: gaurav
'''
'''
Created on Oct 18, 2018

@author: gaurav
'''
import random
import copy

board = [[]]
qholder= [[]]
heuholder = [[]]
nQueen = 0

class Queen:
    def _init_(self):
        self.h=0
        self.location=0,0

def restheuristic(qholderlist,board):
    sum=0
    qlist = copy.deepcopy(qholderlist)
    while(len(qlist)>0):
        q = qlist.pop(0)
        sum+=calHeuristic(q.location, board)
    return sum
        
def calHeuristic(queenLoc,board):    
    row,col=queenLoc
    countH=-1
    #horizontal
    for i in range(col,nQueen):
        if (board[row][i]=='Q'):      
            countH=countH+1
     
             
    #Left --> Right(up)
    countDiag1=-1
    while(row>=0 and col < nQueen):
        if(board[row][col]=='Q'):
             countDiag1+=1
        row-=1
        col+=1
    
    row,col = queenLoc     
    countDiag2=-1                      
    while(row<nQueen and col<nQueen):
        if(board[row][col]=='Q'):
             countDiag2+=1
        row+=1
        col+=1
    return (countH+countDiag1+countDiag2)
                           
def hillClimb(qholder):
   
   for k in range(0,nQueen):
       
        for i in range(0,nQueen):
            #listTemp=i,0
            tempqholder = copy.deepcopy(qholder)
            tempObj = tempqholder.pop(k)    
            boardcopy=copy.deepcopy(board)
            
            boardcopy[tempObj.location[0]][tempObj.location[1]]='-'

            boardcopy[i][k]='Q'
            colheu=calHeuristic([i,k],boardcopy)
            resth = restheuristic(tempqholder,boardcopy)       
            heuholder[i][k]=colheu+resth
            del(boardcopy)
            del(tempqholder)
         

    #for i in range(0,8):
    #   print(heuholder[i])  
   
   #print()
       
def findminat(L):
    '''Return indices of the first minimum value in a list of lists.'''
    return min(
        (n, i, j)
            for j, L2 in enumerate(L)
            for i, n in enumerate(L2)
               )[0:]

def findIndexes(num,heuholder):
    indexlist =[]
    for i in  range(0,nQueen):
        for j in range(0,nQueen):
            if(heuholder[i][j]==num):
                indexlist.append([i,j])
                
    return indexlist        
def makeMoves(qholder,heuholder):
    
    ''' find minimum number and its indexes'''
    minnum,j,i=findminat(heuholder)
    ''' find all locations on that min number'''
    indexlist = findIndexes(minnum, heuholder);
    ''' select random row, col from indexlist'''
    rand_row,rand_col = indexlist[random.randint(0,len(indexlist)-1)]
    
    tempQueen = qholder.pop(rand_col)
    board[tempQueen.location[0]][tempQueen.location[1]]='-'
    board[rand_row][rand_col]='Q'    
    tempQueen.location=rand_row,rand_col
    #qholder.append(tempQueen)
    qholder.insert(rand_col,tempQueen)
        #qholder = sorted(qholder, key=lambda p: p.location[1])
    
    
def initializearray(nQueen):
    global board
    board = [[ '-' for i in range(1,nQueen+1)] for j in range(1,nQueen+1)]
       
    global qholder
    qholder.clear()
    
    global heuholder
    heuholder = [[ 0 for i in range(1,nQueen+1)] for j in range(1,nQueen+1)]
     
  
def main():
   
    qholder=[]
    stepsuccess = 0
    stepfailure = 0
    # hardcode list
    global nQueen 
    nQueen = int(input("Enter number of queens:"))
    #nQueen = 9
    initializearray(nQueen)
    '''tempL =[4,5,6,3,4,5,6,5]
    for i in range(0,8):
         
         if (board[tempL[i]][i]== '-'):
                board[tempL[i]][i] = 'Q'
                q = Queen();
                q.location=tempL[i],i
                qholder.append(q)
    '''
    #    for l in range(0,1):    
    #initializearray() 
        
    for i in range(0,nQueen):
        rand_row = random.randint(0,nQueen-1)
        if (board[rand_row][i]== '-'):
             board[rand_row][i] = 'Q'
             q = Queen();
             q.location=rand_row,i
             qholder.append(q)
    
      
    for i in range(0,nQueen):
         print(board[i])              
    print("=========")           
        #print(calHeuristic(tempObj.location,board))
        #hillClimb(qholder)
    hprev = -999
    stepcount = 0
       
    #print("TIMES DONE :-",l,"\n\n") 
    while(1):
        '''perform hill climb and populate heuristic table (heuholder)'''
        hillClimb(qholder)
        stepcount+=1
        '''Makemove to the minimum heuristic number block'''
        makeMoves(qholder,heuholder)
        ''' Recalcuate heuristic of all queens'''
        h = restheuristic(qholder, board)
              
        for i in range(0,nQueen):
            print(board[i])
        print("================")    
        
        '''if heursitc is 0, bravo! we found a solution'''     
        if (h==0):
            print("\nFound it in ",stepcount-1, "Steps..!!\n")
            for i in range(0,nQueen):
                print(board[i])
            print("-----------------")     
            stepsuccess+=1
                     
            break;
        
        else:              #Else check if previous heurstic is same as current
                           # if it is, well unfortunately we failed!!!  
            if(hprev == h and stepcount < 500):
                print("Failure steps-,",stepcount-1)
                stepfailure+=1
                for i in range(0,nQueen):
                    print(heuholder[i])
        
                break;
        hprev = h
        
    print("Success:",stepsuccess,"Failure:",stepfailure)


main()