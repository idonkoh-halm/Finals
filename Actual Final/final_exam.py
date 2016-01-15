import traceback, inspect, random, math
### Dear students, 
### 
### Here is a final test. There are 8 questions. I will grade your
### performance on all 8 of them. Honors students, I expect you to be
### able to get 7/8 or 8/8 correct.
###
### Regular students, 5/8 or 6/8 constitutes a strong score.
###
###
### Here is a breakdown of how I anticipate the grades being
### calculated:
###
### 0/8 - F 
### 1/8 - D / Honors F
### 2/8 - C- / Honors D- 
### 3/8 - C / Honors D
### 4/8 - B- / Honors C
### 5/8 - B / Honors C+
### 6/8 - B+ / Honors B-
### 7/8 - A / Honors A-
### 8/8 - A / Honors A
###
### I'm terribly sorry I've been unable to be in class this week. As I
### imagine you've been told, I broke my ankle in multiple
### places. I've already had one surgery and I'll be facing another
### one before I'm able to even think about coming back to work.
###
### Those of you continuing on in Application Development, I'll be
### planning to work with you virtually until I'm able to come in the
### building, via google docs, google hangouts, YouTube, etc. It will
### be a strange start to the semester, but I think it will be fun --
### if you have a chance to switch into the class and you haven't
### requested it yet, please do. We could use a few more students.
###
### I've had a fun semester working with you all. You should know that
### programming is challenging, frustrating stuff, but that you've
### done strong work. I'd love to keep working with any and all of you
### to build your programming skills, and I look forward to asking you
### questions in the years to come as you go onto careers in computers
### and come to know more than I do.
###
### Thank you for your hard work, and my sincere apologies for being unable
### to end the semester in class with you.
###
### Mr. H
### 
######################################################
######################################################
###                                                                        ###
###                     VARIABLES AND DATA TYPES                      ###
###                                                                        ###
######################################################
######################################################


# Store a list of 7 names in the variable first_names

# Store the number 3.14 in the variable myPi



######################################################
######################################################
###                                                                        ###
### bug fixes -- Fix the error in each of the following functions.   ###
###                                                                        ###
######################################################
######################################################

def isColorOrPattern (word):
    '''Return True if if word is a recognized color or pattern'''
    known_colors = ['red','blue','green','yellow','purple']
    known_patterns = ['polkadot','striped','plaid']
    if word in known_colors or known_patterns:
        return True
    else:
        return False

def count_vowels (word):
    '''Count the vowels in word.
    '''
    word = word.lower() # lower or upper case
    vowels = 'aeiou' # no sometimes y for us
    for letter in word:
        vowel_count = 0
        if letter in vowels:
            vowel_count += 1
    return vowel_count

######################################################
######################################################
###                                                                        ###
###                                 FUNCTIONS                            ###
###                                                                        ###
######################################################
######################################################

# Create functions to do the following...

# Write a function titled startsWithVowel that returns True if the
# argument starts with a vowel and returns False otherwise.

# Write a function called every_other that returns every other item from a sequence,
# starting with the first item.
# 
# For example
# every_other(['Tom','Mary','Bob','Basil'])
#  --> ['Tom','Bob']


######################################################
######################################################
###                                                                        ###
###                                 OBJECTS                              ###
###                                                                        ###
######################################################
######################################################


# Fix the reproduce method below to address the
# misunderstanding/syntax errors and correctly create a child with the
# person and their partner as parents

class Person:

    population = []
    
    def __init__ (self, parents=[]):
        self.children = []
        self.partner = None
        self.parents = parents
        for p in parents:
            p.children.append(self)
        self.population.append(self)

    def makePartner (self, partner):
        self.partner = partner

    def reproduce (self):
        if self.partner:
            p = Person
            self.children.append(p)
            p.parents = self + self.partner
            
    def tick (self):
        if not self.partner:
            if random.randint(1,10) < 3:
                for p in self.population:
                    if (not p.partner # no polygamy
                        and                        
                        p not in self.parents # no incest
                    ):
                        self.makePartner(p)
                        return
        if random.randint(1,10) < 2:
            self.reproduce()

# Now create a function called run_sim that creates an initial
# population of 100 Person objects, then runs through the "tick"
# function for 50 generations.



################################################
################################################
####                                                            ####
####       GRADING CODE - DO NOT MODIFY CODE BELOW     ####
####                                                            ####
################################################
################################################

# DO NOT MODIFY THE LINES BELOW THIS
# THIS IS HOW THE TEST RUNS
class TestProblem:

    def __init__ (self, tests, description):
        self.description = description
        self.tests = tests
    
    def run_tests (self):
        for test in self.tests:
            if not run_test(*test):
                print 'Failed test # ',self.tests.index(test)+1,
                print ': ',inspect.getsource(test[0])
                return False
        return True

global all
all = False

def userEndTest ():
    global all
    if all:
        return False
    answer = raw_input('You got one wrong. Should we keep grading the rest of the questions or not? \n y (yes, continue)\n n (no, stop now) \na (grade all questions)')
    while answer not in ['y','n','a']:
        raw_input('Please type y or n (for yes, continue grading, or no, stop grading):')
    if answer == 'y':
        return False
    elif answer == 'n':
        return True
    elif answer == 'a':
        all = True
        return False
class UserEndedEvaluation (Exception):
    pass

def run_test (f, testval):
    try:
        result = f()
    except:
        'Error in test'
        print 'Test code: ',inspect.getsource(f)
        traceback.print_exc()
        if userEndTest():
            raise UserEndedEvaluation()
    else:
        if result==testval:
            return True
        else:
            print 'Test code: ',inspect.getsource(f)
            print 'Incorrect result.'
            print 'Expected : ',testval
            print 'Got value: ',result
            if userEndTest():
                raise UserEndedEvaluation()

all_tests = [
    TestProblem(
        tests=[
            (lambda *args: type(first_names),list), # names are a list
            (lambda *args: len(first_names),7), # there are 7 names
            (lambda *args: set([type(n)==str for n in first_names])==set([True]),True), # names are strings
        ],
        description='Store a list of 7 names in the variable first_names'
        ),
    TestProblem(
        tests=[(lambda *args: myPi==3.14,True),
        ],
        description='Store the number 3.14 in the variable myPi'
        ),
    TestProblem(
        tests=[(lambda *args: isColorOrPattern('red'),True),
               (lambda *args: isColorOrPattern('green'),True),
               (lambda *args: isColorOrPattern('striped'),True),
               (lambda *args: isColorOrPattern('banana'),False),
               (lambda *args: isColorOrPattern(1231),False),
               ],
        description='Fix the bug in isColorOrPattern'
        ),
    TestProblem(
        tests=[(lambda *args: count_vowels('four'),2),
               (lambda *args: count_vowels('COOPERATE'),5),
               (lambda *args: count_vowels('Oranges'),3)],
        description='Fix the bug in count_vowels',
        ),
    TestProblem(
        tests=[(lambda *args: startsWithVowel('Apple'),True),
               (lambda *args: startsWithVowel('Toast'),False),
               (lambda *args: startsWithVowel('orange'),True),
               (lambda *args: startsWithVowel('nobody'),False),
               (lambda *args: startsWithVowel('123abc'),False),
               ],
        description='Create a function called startsWithVowel',
    ),
    TestProblem(
        tests=[
            (lambda *args: tuple(every_other(range(10))),(0,2,4,6,8)),
            (lambda *args: tuple(every_other(['a','b','c','d','e'])),
             ('a','c','e')),
               ],
        description='Create a function called every_other that returns every other item in a list',
        ),
]

# Class tests...

class PersonTestProblem (TestProblem):

    def __init__ (self):
        self.description = 'Fix reproduce method for Person class'
        self.tests = [
            (self.setup,None),
            (self.populationIncrease,3),
            (self.parentsSetProperly,True),
            ]

    def setup (self):
        self.p1 = Person([])
        self.p2 = Person([])
        
    def populationIncrease (self):
        self.p1.makePartner(self.p2)
        self.p1.reproduce()
        return len(Person.population)

    def parentsSetProperly (self):
        assert(self.p1 in Person.population[-1].parents)
        assert(self.p2 in Person.population[-1].parents)
        return True
        
    def multipleChildren (self):
        self.p1.reproduce()
        self.p1.reproduce()
        self.p1.reproduce()
        return len(Person.population)


def test_simulation (sim_function):
    Person.population = []
    counts = {}

    def count_calls (f):
        def decorated_method (*args, **kwargs):
            if counts.has_key(f):
                counts[f] += 1
            else:
                counts[f] = 1
            return f(*args,**kwargs)
        return decorated_method
    reproduce_orig = Person.reproduce
    tick_orig = Person.tick
    init_orig = Person.__init__
    Person.reproduce = count_calls(Person.reproduce)
    Person.tick = count_calls(Person.tick)
    Person.__init__ = count_calls(Person.__init__)
    sim_function()
    try:
        assert(counts[init_orig] >= 100) # Make sure we created enough people
        assert(counts[tick_orig] > 5000) # Make sure we ticked enough times
        assert(counts[reproduce_orig] > 50) # Make sure we reproduced
        assert(counts[init_orig] > 150) # Make sure we created and reproduced
    except:
        print init_orig,'was called',counts[init_orig],'times'
        print tick_orig,'was called',counts[tick_orig],'times'
        print reproduce_orig,'was called',counts[reproduce_orig],'times'
        raise
    else:
        print 'Looks like we ran the simulation'
    
all_tests.extend([
    PersonTestProblem(),
    TestProblem(
        [(lambda *args: test_simulation(run_sim),None)],
        'Create simulation that creates population of Person objects.'
        ),
    ])

def run_all_tests ():
    ftot = 0; fscore = 0
    for tp in all_tests:
        print 'Running: ',tp.description
        ftot += 1
        try:
            if tp.run_tests():
                fscore += 1
                print 'Passed!',fscore,'/',ftot
        except UserEndedEvaluation:
            print 'User ended evaluation early'
            print 'Score at that point was ',fscore,'/',ftot
            return 
    print 'Final Score: ',fscore,'/',ftot


run_all_tests()
