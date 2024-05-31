class RescueAnimal:
    def __init__(self, name, gender, age, weight,
                 acquisition_date, acquisition_country, training_status,
                 reserved, in_service_country):
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
        self.acquisition_date = acquisition_date
        self.acquisition_country = acquisition_country
        self.training_status = training_status
        self.reserved = reserved
        self.in_service_country = in_service_country


class Dog(RescueAnimal):
    def __init__(self, name, gender, age, weight,
                 acquisition_date, acquisition_country, training_status,
                 reserved, in_service_country, breed):
        super().__init__(name, gender, age, weight,
                 acquisition_date, acquisition_country, training_status,
                 reserved, in_service_country)
        
        # Dog-specific attributes
        self.breed = breed


class Monkey(RescueAnimal):
    def __init__(self, name, gender, age, weight, acquisition_date,
                 acquisition_country, training_status, reserved,
                 in_service_country, species, height, tail_length, body_length):
        super().__init__(name, gender, age, weight,
                         acquisition_date, acquisition_country, training_status,
                         reserved, in_service_country)
        
        
        # Monkey specific attributes
        self.species = species
        self.height = height
        self.tail_length = tail_length
        self.body_length = body_length
