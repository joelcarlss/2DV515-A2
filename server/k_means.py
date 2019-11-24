import numpy as np
from io import StringIO

# Create random places for cluster-thingies
# rand = np.random.randint(10, size=4)

# Create numpy array data from blogdata.txt
blog_names = np.genfromtxt('blogdata.txt', delimiter='\t', usecols=0, dtype=str) # Names of all blogs(column 0 in doc)
blog_data = np.genfromtxt('blogdata.txt', delimiter='\t', skip_header=1)[:, 1:] # Each blogs word freq. (rows in doc)
named_data = {label: row for label, row in zip(blog_names, blog_data)} # Pretty presentation (Blog name then word-freq)

blog_amount, word_amount = blog_data.shape

# Amount of clusters
k = 5

# Highest value in np arr. = is word china. Should return 11
# print(np.amax(data[:,0]))

# Lowest value in np arr. = is word china. Should return 0
# print(np.amin(data[:,0]))


# The highest amount of times each word exists
max_frequency = np.amax(blog_data, axis=0)

# The lowest amount of times each word exists
min_frequency = np.amin(blog_data, axis=0)

# Mock-values for easier testing
mock_max = np.array([2, 9, 2, 2, 2])
mock_min = np.array([0, 5, 0, 0, 0])
mock_centroids = np.random.randint(mock_min, mock_max+1, (k, len(mock_min)))

# Returns array with random integer between max and min frequency between each word
# rand = np.random.randint(min_frequency, max_frequency)

# K amount of arrays with random numbers between lowest and highest frequency of each word
# max_frequency + 1 because random value < max.
centroids = np.random.randint(min_frequency, max_frequency+1, (k, word_amount))


# Writes put pearson for every blog against every centroids.
# Will remove all values that are similarities between blog-data, and only similarities between clusters and blogs
# Indexing options explained: [(from start):(to blog_amount)(last k values)]
clusters = np.array(np.corrcoef(blog_data, centroids)[:blog_amount, -k::])


# print(np.corrcoef(blog_data[0], centroids)[0][1:])
# print(clusters[0])

# The most similar centroid for every blog
# or.. the index with the highest value on every element in clusters
matching_centroids = clusters.argmax(axis=1)
print(matching_centroids)

# TEST
# All indexes that matches a specified int
test_matching = np.where([matching_centroids]) ## TODO: return five arrays where every array is evvery blog that matches the current centroid
print(test_matching)
print(len(test_matching))

# All blogs that matches ints in test match
# blog_data[test_matching]

