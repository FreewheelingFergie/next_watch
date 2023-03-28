import spacy

# Import language model.
nlp = spacy.load('en_core_web_md')

'''
Read through the description of movies in 'movies.txt' and create a dictionary.
Use the colon to separate between Key and Value - the Key being the title of the movie
and the value being the movie description.
'''

# Create an empty dictionary called 'movies' as explained above.
movies = {}

# Loop through each line of 'movies.txt' and append Keys, Values to 'movies' dictionary.
# Reminder reference for creating a dict from a text file: https://www.tutorialspoint.com/How-to-create-a-Python-dictionary-from-text-file
with open('movies.txt', 'r') as f:
    for line in f.readlines():
        title, description = line.strip().split(':') # Remove any unecessary spaces with 'strip()' and split with ':'
        movies[title.strip()] = description.strip()


# Description of the movie Planet Hulk:
planet_hulk = ('''Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.''')




# Define function which compares the movie descriptions. 
'''
The function takes in 'description_for_comparison' (Planet Hulk) as a parameter.
Use 'similarity()' method by passing the processed description for comparison (doc1) and the processed movie description (doc2)
for each movie in the dictionary titled 'movies'.
All the calculated similarity scores are then stored in another dictionary, titled 'similarity_scores', 
where the Key is the movie title and Value is the similarity score.

'''
def most_similar_movie(description_for_comparison):
    # Process description which is to be compared against other descriptions.
    doc1 = nlp(description_for_comparison)

    # Obtain similarity scores for all movie titles in the dictionary titled 'movies' as described in above notes.
    # REF - L3T12 Course Notes
    # REF - https://spacy.io/usage/linguistic-features#vectors-similarity
    similarity_scores = {}
    for title, text in movies.items():
        doc2 = nlp(text)
        similarity_scores[title] = doc1.similarity(doc2)

    # Print similarity_scores dictionary content to confirm output of 'suggested next watch' below and comment out print statement when verified.
    # print(similarity_scores)
    
    ''' 
    Look up the value of each key in the 'similarity_scores' dictionary and return the Key
    with the maximum value.
    '''
    return max(similarity_scores, key=similarity_scores.get)

# Print message with suggested 'next watch'
x = most_similar_movie(planet_hulk)
print(f'The recommended movie to watch next is: {x}')

'''
The code was also tested by changing the planet_hulk description to be very identical to other movie descriptions 
which seemed to work.
'''