from stacks_and_queues.animal_shelter import Animal, AnimalShelter, Dog, Cat

# Create some dogs and cats
dog1 = Dog("Buddy", 1)
cat1 = Cat("Whiskers", 2)
dog2 = Dog("Max", 3)
cat2 = Cat("Mittens", 4)

# Create an animal shelter
shelter = AnimalShelter()

# Enqueue the dogs and cats into the shelter
shelter.enqueue(dog1)
shelter.enqueue(cat1)
shelter.enqueue(dog2)
shelter.enqueue(cat2)

# Dequeue the oldest animal regardless of species
oldest_animal = shelter.dequeueAny()
if oldest_animal:
    print(oldest_animal.name)  # Output: Buddy (oldest dog)
else:
    print("No animals left in the shelter")

# Dequeue the oldest dog
oldest_dog = Dog.dequeueDog()
if oldest_dog:
    print(oldest_dog.name)  # Output: Max
else:
    print("No dogs left in the shelter")

# Dequeue the oldest cat
oldest_cat = Cat.dequeueCat()
if oldest_cat:
    print(oldest_cat.name)  # Output: Whiskers
else:
    print("No cats left in the shelter")
