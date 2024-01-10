import xml.etree.ElementTree as ET

# Parse XML File
tree = ET.parse('12-001 Data Sources/movie.xml')
root = tree.getroot()

# Initialize counters
favourite_count = 0
non_favourite_count = 0


# Print movie descriptions
print("Movie Descriptions:")
for movie in root.iter('movie'):
    for description in movie.iterfind('description'):
        print(description.text+"\n")

    # Check if the movie is a favourite or not and update counters
    favourite = movie.get('favorite').lower()
    if favourite == 'true':
        favourite_count += 1
    elif favourite == 'false':
        non_favourite_count += 1

# Print the number of favourites and non-favourites
print("Number of Favorite Movies:", favourite_count)
print("Number of Non-Favorite Movies:", non_favourite_count)
