def ooo():
    if "y" in "oreo":
        print "True"
        return True
    else:
        print "False"
        return False
    
     
#ooo()
def isColorOrPattern (word):
    '''Return True if if word is a recognized color or pattern'''
    word=str(word)
    known_colors = ['red','blue','green','yellow','purple']
    known_patterns = ['polkadot','striped','plaid']
    if word in known_colors:
        print True
        return True
    elif word in known_patterns:
        print True
        return True
    else:
        print False
        return False
    
isColorOrPattern('banana')
