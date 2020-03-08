import random
RS = raw_input
RI = lambda x=int: map(x,RS().split())
RN = lambda x=int: x(RS())


class Student:
    '''
        Represents a point in m-dimension
    '''
    
    def __init__(self,_marks):
        self.marks = list(_marks)
        self.avg = 1.0*sum(_marks)/len(_marks)
        self.group = -1

    def getDistance(self, node):
        assert type(node) == Student, "Class type doesn't match"
        assert len(self.marks) == len(node.marks), "Subject count doesn't match"
        
        m = len(self.marks)
        dis = 0
        for i in xrange(m):
            dis += (self.marks[i] - node.marks[i])**2
        return dis

    def getDistanceByAvg(self, node):
        assert type(node) == Student, "Class type doesn't match"

        return (self.avg - node.avg)**2


class Leaders:
    
    def __init__(self):
        self.rep = tuple()
        self.fitness = -1

    def offspring(self, par2):

        child = Leaders()
        for i in xrange(len(par2.rep)):
            prob = random.random()

            if prob < 0.45:
                    child.rep += (self.rep[i],)
            elif prob < 0.90:
                    child.rep += (par2.rep[i],)
            else:
                    child.rep += (Leaders.mutation(),)

        return child	# Fitness value not calculated yet!

    @staticmethod
    def mutation():
        seed = 100*random.random()
        delta = 0.01 * random.randint(0,1)
        return min(100.0,seed+delta)


    def electRep(self,points,k):
        n = len(points)
        representative = []
        for i in xrange(k):
            genesisNode = points[random.randint(0,n-1)]
            representative.append(genesisNode.avg)
        
        self.rep = tuple(representative)
        self.calcFitness(points)

    def calcFitness(self,points):
        fitness = 0
        
        for point in points:
            minDistance = -1
            for rep in self.rep:
                dis = (rep - point.avg)**2
                if minDistance == -1 or dis < minDistance:
                    minDistance = dis
            fitness += minDistance
            
        self.fitness = fitness
        return fitness

def output(students, center):
        sid = 1
        #group = []
        for student in students:
            idx = 0
            dif = abs(student.avg - center.rep[0])
            for i in xrange(1,len(center.rep)):
                val = abs(student.avg - center.rep[i])
                if val < dif:
                    dif = val
                    idx = i

            #group.append([idx+1,sid])
            print 'Student %d belongs to group-%d'%(sid,idx+1)
            sid += 1
    #group.sort()

def getInput():
    n = int(RS('Number of students : '))
    m= int(RS('Number of subjects : '))
    k = int(RS('Number of groups : '))      # Assuming k <= n
    assert n>0 and m>0 and k>0, 'Invalid Input'

    myClass = []
    
    for i in xrange(n):
        print 'Marks obtained by student %d : '%(i+1),
        arr = RI()
        assert len(arr) == m,'Subject count not valid'
        assert min(arr)>=0 and max(arr) <=100, 'Marks range not valid'

        stud = Student(arr)
        myClass.append(stud)

    return (n,m,k,myClass)

def main():
    '''
            Gene :- Mean (Initially)
            Chromosome :- k-group (collection of genes)
            Population :- collection of Chromosomes
    '''

    POP_SIZE = 100
    MAX_GENX = 100
    n,m,k,students = getInput()
    population = []

    for x in xrange(POP_SIZE):
        individual = Leaders()
        individual.electRep(students,k)
        population.append(individual)

    genx = 1
    flag = 1
    while flag and genx <= MAX_GENX:
        population.sort(key = lambda x:x.fitness)
        if population[0].fitness == 0:
            flag = 0
            break

        carryAhead = int(0.1*POP_SIZE)
        future = population[:carryAhead]
        rem = POP_SIZE - carryAhead

        for i in xrange(rem):
            par1 = random.randint(0,POP_SIZE/2)
            par2 = random.randint(0,2*POP_SIZE/3)
            child = population[par1].offspring(population[par2])
            child.calcFitness(students)
            future.append(child)

        population = future
        genx+=1

    # Select parents
    # Do crossover
    # Do mutation
    # Repeat

    output(students,population[0])

# Driver Code
main()
        
