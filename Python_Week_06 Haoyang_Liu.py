def find_unique_objects(object_array):

    frequency = {}
    for obj in object_array:
        if obj in frequency:
            frequency[obj] += 1
        else:
            frequency[obj] = 1
    

    unique_objects = [item for item, count in frequency.items() if count == 1]
    return unique_objects



game_objects = ["apple", "banana", "apple", "cherry", "date", "banana", "fig", "grape", "fig"]


result = find_unique_objects(game_objects)
print("Unique objects (appear only once):", result)
