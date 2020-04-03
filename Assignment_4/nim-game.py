import random
child = {}
payoff = {}

def reset_game():
    global child,payoff
    child = {1:0,-1:0}
    payoff = {1:0,-1:1}

def maxNode(n,k):
    if n <=0: return 1
    if payoff.get(n):
        return payoff[n]
    
    child[n] = n-random.randint(1,min(n,k))
    payoff[n] = 0
    
    for ch in xrange(1,min(n,k)+1):
        if minNode(n-ch,k) == 1:
            child[n] = n-ch
            payoff[n] = 1
            return 1
    return 0

def minNode(n,k):
    if n<=0: return 0
    if payoff.get(-n):
        return payoff[-n]
    
    child[-n] = n-random.randint(1,min(n,k))
    payoff[-n] = 1
    
    for ch in xrange(1,min(n,k)+1):
        if maxNode(n-ch,k) == 0:
            child[-n] = n-ch
            payoff[-n] = 0
            return 0
    return 1

# 1 -> maxNode
# 0 -> minNode
def solve(n,k,typ):
    if typ: maxNode(n,k)
    else: minNode(n,k)

def player(n,k,turn = None):
    
    def check_move(num,limit):
        try:
            n = int(num)
            if n < 1 or n > limit:
                return 0
            return n
        except:
            return 0
        
    if turn == None:
        txt = 'Player move : '
    else:
        txt = 'Player %d move : '%(turn+1)
        
    while 1:
        print '\nSticks left : ',n
        x = raw_input(txt)
        x = check_move(x,min(n,k))
        if x != 0: return n-x
        print  'Invalid Move!!!\n'
        
# 1 -> minNode
# 0 -> maxNode
def robot(n,k,typ,turn = None):
    solve(n,k,typ^1)
    if typ: x = child[-n]
    else: x = child[n]
    if turn==None:
        print 'Robot Move --> %d\n'%(n-x)
    else:
        print 'Robot %d Move --> %d'%(turn+1,n-x)
    return x


def game1(n,k):
    turn = 0
    while n>0:
        n = player(n,k,turn)
        turn ^= 1
    print 'Winner is Player %d\n'%(turn+1)

def game2(n,k):
    state = ['Player','Robot']
    turn = random.randint(0,1)
    print 'First Move : ',state[turn]
    typ = turn^1

    while n>0:
        if turn:
            n = robot(n,k,typ)
        else:
            n = player(n,k)
        turn ^= 1
    print 'Winner : ',state[turn]

def game3(n,k):        
    verdict = maxNode(n,k)
    turn = 0
    
    while n>0:
        n = robot(n,k,turn,turn)
        turn ^= 1
    print 'Winner is Robot %d\n'%(turn+1)


def game_mode():
    print 'Options :  1. User v/s User'
    print '\t 2. User v/s AI'
    print '\t 3. AI v/s AI'
    
    ch = raw_input('Enter your Choice(1-3) : ')
    n = int(raw_input('N = '))
    k = int(raw_input('K = '))
    assert n>0 and k>0,'Invalid Input'
    reset_game()
    if ch=='1': game1(n,k)
    elif ch=='2': game2(n,k)
    elif ch=='3': game3(n,k)
    else: print 'Invalid Choice!!!'
    
        
def main():
    while True:
        print '\n1. New Game'
        print '0. Exit'
        ch = raw_input('Choice : ')
        if ch != '1': return
        game_mode()

if __name__ == "__main__":
    main()
    
        
