#initial dictionary
movie = {
    'title': 'Interestelar',
    'year': 2014,
    'director': 'Christopher Nolan'
}
# List dictionary values and keys
for keys in movie:
    print(f'{keys}: {movie[keys]}')

# Add new key value
movie['nota'] = 9

# Update existing key value
movie['year'] = 2015


print(movie)
