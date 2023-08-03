guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  while True:
    line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    
    value = yield name, age
    
    if value is not None:
      value=value.split(",")
      name = value[0]
      age = int(value[1])
      guests[name] = age
      yield name, age



object=read_guestlist("guest_list.txt")

""""for i in range(10):
  print(next(object))
  
print(object.send('Jane,35'))
for i in object:
  print(next(object))
"""
for i in range(199):
  try:
    if i == 10:
      print(object.send('Jane,35'))
    else:
      print(next(object))
  except StopIteration:
    print('it looks like the end of generator boss')
    break

print("\n\n\nlets see who can get hammered legally:\n")
print (guests)
over21 = ((key,value) for key, value in  guests.items() if value > 21)
for i in over21:
  print(i[0], "can drink because they are",i[1], " but prolly shouldnt")
print("\n\n\n")

def chickenTable():
  food = 'Chicken'
  table = 1
  for i in range(5):
    seat = i + 1
    yield f'Food: {food}'
    yield f'Table: {table}'
    yield f'Seat: {seat}'

def beefTable():
  food = 'Beef'
  table = 2
  for i in range(5):
    seat = i + 1
    yield f'Food: {food}'
    yield f'Table: {table}'
    yield f'Seat: {seat}' 

def fishTable():
  food = 'Fish'
  table = 3
  for i in range(5):
    seat = i + 1
    yield f'Food: {food}'
    yield f'Table: {table}'
    yield f'Seat: {seat}'

def iterate(num,gen):
  for i in range(num):
    yield gen

def meals(guests, t1, t2, t3):
  names = list(guests.keys())
  for i in range(5):
    yield (names[i],[next(t1) for i in range(3)])
  for i in range(5,10):
    yield (names[i],[next(t2) for i in range(3)])
  for i in range(10,15):
     yield (names[i],[next(t3) for i in range(3)])

meal_plans = meals(guests, chickenTable(), fishTable(), beefTable())

for i in meal_plans:
  print(i)
