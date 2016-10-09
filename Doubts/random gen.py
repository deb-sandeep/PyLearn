# First, it is a good practice not to name python files with the same name
# as that of system libraries. This makes importing standard libraries difficult.
import random

for i in range(10):
    x = random.random() # why did they use random twice?
    # [Sandy] - When you import random, the file defines an instance of the 
    # random class assigned against the 'random' variable. In the above line
    # you are calling the random() method on the random class instance.

    print (x) # how can i print integers?
    # [Sandy] - Not sure if I understood the question. 
