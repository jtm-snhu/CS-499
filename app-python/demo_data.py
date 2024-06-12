from random import randint
from models import Animal

def create_dogs(n):
    # Create list of n dogs for testing
    dogs = []
    print('Creating dogs...')
    for i in range(n):
        name = f'DogName{i}'
        animal = 'Dog'
        if i%2 == 0:
            gender = 'Male'
        else:
            gender = 'Female'
        age = randint(2,20)
        weight = randint(2,50)
        acquisition_date = f'{randint(1,30)}/{randint(1,12)}/{randint(2000, 2024)}'
        acquisition_country = 'USA'
        training_status = 'Trained'
        reserved = False
        if i%3 == 0:
            in_service_country = 'UK'
        elif i%2 == 0:
            in_service_country = 'Canada'
        else:
            in_service_country = 'USA'
        breed = f'Breed{i}'
        # Add entry to list
        dogs.append(Animal(name=name,
                        animal=animal,
                        gender=gender,
                        age=age,
                        weight=weight,
                        acquisition_date=acquisition_date,
                        acquisition_country=acquisition_country,
                        training_status=training_status,
                        reserved=reserved,
                        in_service_country=in_service_country,
                        breed=breed))
  
    for x in range(10):
        print(dogs[x])

    print(f'Dogs Length: {len(dogs)}')
    return dogs

def create_monkeys(n):
    # Create list of n monkeys for testing
    monkeys = []
    print('Creating Monkeys...')
    for i in range(n):
        name = f'MonkeyName{i}'
        animal = 'Monkey'
        if i%2 == 0:
            gender = 'Male'
        else:
            gender = 'Female'
        age = randint(2,20)
        weight = randint(2,50)
        acquisition_date = f'{randint(1,30)}/{randint(1,12)}/{randint(2000, 2024)}'
        acquisition_country = 'United States'
        training_status = 'In Progress'
        reserved = False
        in_service_country = 'United States'
        breed = f'breed{i}'
        height = randint(6,28)
        tail_length = randint(2,36)
        body_length = randint(12,24)
        
        # Add entry to list
        monkeys.append(Animal(name=name,
                              animal=animal,
                              gender=gender,
                              age=age,
                              weight=weight,
                              acquisition_date=acquisition_date,
                              acquisition_country=acquisition_country,
                              training_status=training_status,
                              reserved=reserved,
                              in_service_country=in_service_country,
                              breed=breed,
                              height=height,
                              tail_length=tail_length,
                              body_length=body_length))
  
    for x in range(10):
        print(monkeys[x])

    print(f'Monkey Length: {len(monkeys)}')
    return monkeys


#Create n list for search demo
#n should be an even number
def create_search_data():
    demo_list = []
    for item in create_dogs(50000):
        demo_list.append(item)
    for item in create_monkeys(50000):
        demo_list.append(item)
    for x in range(len(demo_list)):
        demo_list[x].id = x
    
    return demo_list

