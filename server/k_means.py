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

# The highest amount of times each word exists
max_frequency = np.amax(blog_data, axis=0)

# The lowest amount of times each word exists
min_frequency = np.amin(blog_data, axis=0)

# Create Centroids
# K amount of arrays with random numbers between lowest and highest frequency of each word
# max_frequency + 1 because random value < max.
centroids = np.random.randint(min_frequency, max_frequency+1, (k, word_amount))

matching_centroids = np.array([])

while True:

    # Writes out pearson for every blog against every centroids.
    # Will remove all values that are similarities between blog-data, and only similarities between clusters and blogs
    # Indexing options explained: [(from start):(to blog_amount)(last k values)]
    similarities = np.array(np.corrcoef(blog_data, centroids)[:blog_amount, -k::])

    if np.array_equal(similarities.argmax(axis=1), matching_centroids):
        break
    else:
        # The most similar centroid for every blog
        # or.. the index with the highest value on every element in clusters
        matching_centroids = similarities.argmax(axis=1)

    # All indexes that matches a specified int
    for i in range(k):  # For each centroid, get all blogs and create an new centroid in the middle
        best_matching_indexes = np.where(matching_centroids == i)[0]  # Indexes that is most similar with centroid i
        best_matching_blogs = blog_data[best_matching_indexes]  # Blogs that are most similar with centroid i
        centroids[i] = np.sum(best_matching_blogs, axis=0) / len(best_matching_indexes)  # Average blog. = new centroid

    print(matching_centroids)



print("----------------------------------------")

# centroid_indexes = np.linspace(0, k-1, k)  # Indexes of every centroid (0,1,2,3....)
# print(np.where(np.equal.outer(matching_centroids, [0]))[0])
# indices = np.where(matching_centroids == centroid_indexes[:, None])
# print(np.unique(indices[0], return_counts=True)[1])
# test = np.split(indices[1], (np.unique(indices[0], return_counts=True)[1]))
# print(test)


# All blogs that matches ints in test match
# blog_data[test_matching]

