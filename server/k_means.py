import numpy as np
from io import StringIO


# Create random places for cluster-thingies
# rand = np.random.randint(10, size=4)


blog_names = np.genfromtxt('blogdata.txt', delimiter='\t', usecols=0, dtype=str)
data = np.genfromtxt('blogdata.txt', delimiter='\t', skip_header=1)[:,1:]
named_data = {label: row for label, row in zip(blog_names, data)}


blog_amount, word_amount = data.shape

k = 4

# Highest value in np arr. = is word china. Should return 11
print(np.amax(data[:,0]))

# Lowest value in np arr. = is word china. Should return 0
print(np.amin(data[:,0]))