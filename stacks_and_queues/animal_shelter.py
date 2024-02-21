# An animal shelter, which holds only dogs and cats,
# operates on a strictly "first in, first out" basis.
# People must adopt either the "oldest" (based on arrival
# time) of all animals at the shelter, or they can select
# whether they would prefer a dog or a cat (and will
# receive the oldest animal of that type).
# They cannot select which specific animal they would like.
# Create the data structures to maintain this system
# and implement operations such as enqueue, dequeueAny,
# dequeueDog, and dequeueCat. You may use the built-in
# LinkedList data structure.

class ListNode:
  def __init__(self, val):
      self.val = val
      self.next = None

class LinkedList:
  def __init__(self):
      self.head = None

  def append(self, val):
      new_node = ListNode(val)
      if not self.head:
          self.head = new_node
      else:
          curr_node = self.head
          while curr_node.next:
              curr_node = curr_node.next
          curr_node.next = new_node

class Animal:
  def __init__(self, species, name, timestamp):
      self.species = species
      self.name = name
      self.timestamp = timestamp

class Dog(Animal):
  dogs = LinkedList()

  def __init__(self, name, timestamp):
      super().__init__('dog', name, timestamp)
      Dog.dogs.append(self)

  @staticmethod
  def dequeueDog():
      if Dog.dogs.head is None:
          return None
      else:
          temp = Dog.dogs.head
          Dog.dogs.head = Dog.dogs.head.next
          return temp.val

class Cat(Animal):
  cats = LinkedList()

  def __init__(self, name, timestamp):
      super().__init__('cat', name, timestamp)
      Cat.cats.append(self)

  @staticmethod
  def dequeueCat():
      if Cat.cats.head is None:
          return None
      else:
          temp = Cat.cats.head
          Cat.cats.head = Cat.cats.head.next
          return temp.val

class AnimalShelter:
  def __init__(self):
      self.timestamp = 0

  def enqueue(self, animal):
      self.timestamp += 1
      if isinstance(animal, Dog):
          Dog(animal.name, self.timestamp)
      elif isinstance(animal, Cat):
          Cat(animal.name, self.timestamp)

  @staticmethod
  def dequeueAny():
      oldest_dog = Dog.dequeueDog()
      oldest_cat = Cat.dequeueCat()
      if oldest_dog is None:
          return oldest_cat
      elif oldest_cat is None:
          return oldest_dog
      else:
          return oldest_dog if oldest_dog.timestamp < oldest_cat.timestamp else oldest_cat