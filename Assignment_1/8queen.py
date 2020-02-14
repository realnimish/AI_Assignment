TITLE = '''
    Name : Nimish Agrawal
    Roll Number : 1801113
    Problem Statement : Implement 8-Queen problem using UCS
'''


def isValidState(board, row, col):
    '''
        Checks whether we can insert queen at row,col 
        position without getting into any attacking position.

        @param board : Current State Tuple
        @param row : Specifies the row being tested
        @param col : Specifies the col being tested
        @returns bool : 1 if no attacking position generated else 0
    '''
    
    N = len(board) # Size of the board

    # Checking no vertical attack formation
    for i in xrange(row):
        if board[i] == col: return 0

    # Checking no main diagonal attack formation
    for i in xrange(1, min(row,col) + 1):
        if board[row-i] == col-i: return 0

    # Checking no secondary diagonal attack formation
    for i in xrange(1, min(row,N - col -1) + 1):
        if board[row-i] == col+i: return 0

    return 1


def findSolutionUsingUCS(size = 8):
    '''
        Finds solution to N-Queen problem using Uniform Cost Search
        State Space :: <c1,c2,c3,...,c_n>
        Start State :: <-1,-1,-1,....,-1>
        Action :: AssignQueenInRow(i)
        Goal Test :: No Attacking Position generated
        Cost   :: Number of times to assign queens

        @param size : Solves N-Queen problem with default value = 8
        @returns tuple of length 'size' if a solution exists else -1
    '''
    
    initialBoard = [-1]*size
    Q = [initialBoard]

    while Q != []:
        board = Q[0]    # Expanding Node with min cost
        Q = Q[1:]
        
        row = board.index(-1)   # Finding the next empty row
        # Checking for all possible column
        for col in xrange(size):
            
            if isValidState(board,row,col) == 1:
                possibleState = list(board)
                possibleState[row] = col    # Adding Queen at (row,col)

                # Checking if all Queens placed
                if size == row+1: return possibleState
                else: Q.append(possibleState)

    return -1


def printBoard(board):
    '''
        Outputs a tuple belonging to Space Set followed by 
        2D matrix where Q denotes the position of queen placed
    '''

    tupl = ','.join(map(str,board))
    print '\nTuple Form : <%s>' % tupl
    print 'Matrix Form : '
    N = len(board)

    for i in xrange(N):
        row = ['#']*N
        row[board[i]] = 'Q'
        print ''.join(row)
    print
    

def main():
    print 'N- Queen Problem using UCS '

    while True:
        print '-'*50
        N = int(raw_input('Enter Size in range [4,10] : '))
        if N <= 3 or N  > 10:
            print '-'*50
            print TITLE
            print '-'*50
            print 'Exiting...'
            return
        ans = findSolutionUsingUCS(N)
        printBoard(ans)

# Driver Code
main()
