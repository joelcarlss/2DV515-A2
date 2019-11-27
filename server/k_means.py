import numpy as np


def k_means(blog_data):
    blog_amount, word_amount = blog_data.shape

    # Amount of clusters
    k = 5

    # The highest amount of times each word exists
    max_frequency = np.amax(blog_data, axis=0)

    # The lowest amount of times each word exists
    min_frequency = np.amin(blog_data, axis=0)

    # Create Centroids
    # K amount of arrays with random numbers between lowest and highest frequency of each word
    # max_frequency + 1 because random value < max. Making it float for better precision
    centroids = np.random.randint(min_frequency, max_frequency+1, (k, word_amount)).astype(float)

    matching_centroids = np.array([])
    best_matching_indexes = {}

    while True:

        # Writes out pearson for every blog against every centroids.
        # Will remove all values that are similarities between blog-data, and only similarities between clusters and blogs
        # Indexing options explained: [(from start):(to blog_amount)(last k values)]
        similarities = np.array(np.corrcoef(blog_data, centroids)[:blog_amount, -k::])

        if np.array_equal(similarities.argmax(axis=1), matching_centroids):
            return best_matching_indexes
        else:
            # The most similar centroid for every blog
            # or.. the index with the highest value on every element in clusters
            matching_centroids = similarities.argmax(axis=1)

        # All indexes that matches a specified int
        for i in range(k):  # For each centroid, get all blogs and create an new centroid in the middle
            best_matching_indexes[i] = np.where(matching_centroids == i)[0]  # Indexes that is most similar with centroid i
            best_matching_blogs = blog_data[best_matching_indexes[i]]  # Blogs that are most similar with centroid i
            centroids[i] = np.sum(best_matching_blogs, axis=0) / len(best_matching_indexes)  # Average blog. = new centroid



