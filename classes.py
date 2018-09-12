import gc

class animal:
    reference = ''
    name = ''
    weight = ''
    noise = ''
    male = 0  # 0-ж 1-м
    hungry = True

    def get_noise(self):
        return self.noise

    def get_feed(self):
        return self.hungry

    def do_feed(self):
        self.hungry = False


class birds(animal):
    eggs_count = 1

    def get_egg(self):
        if (self.male == 0) and (self.eggs_count > 0):
            return self.eggs_count
            self.eggs_count = 0
        else:
            return 0


class livestock(animal): # класс заглушка, если потрбеуется добавление общих свойств для скота.
    get_hooves = True


class cows(livestock):
    reference = 'Корова'
    noise = 'МУУУ'
    milk_count=8
    last_get_milk = 13 #сколько часов назад последний раз доили

    def get_milk(self):
        if self.last_get_milk >12:
            return self.milk_count
            self.milk_count = 0
            self.last_get_milk = 0
        else:
            return 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class goats(livestock):
    reference = 'Коза'
    noise = 'МЕЕЕ'
    milk_count = 3
    last_get_milk = 13  # сколько часов назад последний раз доили

    def get_milk(self):
        if self.last_get_milk > 12:
            return self.milk_count
            self.milk_count = 0
            self.last_get_milk = 0
        else:
            return 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class sheeps(livestock):
    reference = 'Овца'
    noise = 'БЕЕЕ'
    last_shear = 1  # последний раз пострижена

    def do_shear(self):
        if self.last_shear > 3:
            print("Ура, постригли")
        else:
            print("Слишком рано, еще шерсть не отросла")


    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class gooses(birds):
    reference = 'Гусь'
    noise = 'ГА-ГА-ГА'
    color = ''

    def __init__(self, name, weight, male,color):
        self.name = name
        self.weight = weight
        self.color = color
        self.male = male


class chickens(birds):
    reference = 'Курица'
    def __init__(self, name, weight,male,noise):
        self.name = name
        self.weight = weight
        self.male = male
        self.noise = noise


class ducks(birds):
    reference = 'Утка'
    noise = 'Кря'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


def lets_feed(animal_name):
    if animal_name.hungry == True:
        animal_name.get_feed()
        print('Покормили животное - ', animal_name.name)
    else:
        print('{} {} не хочет есть'.format(animal_name.reference,animal_name.name))


def lets_milk(animal_name):
    # return animal_name.get_milk()
    if animal_name.last_get_milk >12:
        print('Доим {}, и получаем {} литров молока'.format(animal_name.name, animal_name.get_milk()))
    else:
        print('{} доили недавно, пока нет молока'.format(animal_name.name))


def lets_egg(animal_name):
    if animal_name.male == 0:
        print("Яйца собраны, животное {}-{}".format(animal_name.reference,animal_name.name))
    else:
        print('Мужики яца не высиживают, животное {}-{}'.format(animal_name.reference,animal_name.name))

def lets_shear(animal_name):
    print("Стрижем {}".format(animal_name.name))
    animal_name.do_shear()
    print()

goose1 = gooses('Серый', '18', 'Серый', 1)
goose2 = gooses('Белый', '15', 'Белый', 0)
chicken1 = chickens('Ко-Ко', '10', 0, 'КО-КО-КО')
chicken2 = chickens('Кукареку', '11', 1, 'Кукареку')
duck1 = ducks('Кряква', 6)
cow = cows("Маньку",200)
goat1=goats("Рога", 30)
goat2=goats("Копыта", 32)
sheep1=sheeps("Барашек", 20)
sheep2=sheeps("Кудрявый", 20)

print('Корм животных:')
sheep2.hungry = False
cow.hungry=False

lets_feed(goose1)
lets_feed(goose2)
lets_feed(chicken1)
lets_feed(chicken2)
lets_feed(duck1)
lets_feed(cow)
lets_feed(goat1)
lets_feed(goat2)
lets_feed(sheep1)
lets_feed(sheep2)



print()
print("Дойка:")
# print('Доим {}, и получаем {} литров молока'.format(cow.name, cow.get_milk()))
# print('Доим {}, и получаем {} литров молока'.format(goat1.name, goat1.get_milk()))
goat2.last_get_milk = 2
# print('Доим {}, и получаем {} литров молока'.format(goat2.name, goat2.get_milk()))

lets_milk(cow)
lets_milk(goat1)
lets_milk(goat2)

lets_egg(goose1)
lets_egg(goose2)
lets_egg(chicken1)
lets_egg(chicken2)
lets_egg(duck1)
print()
print("Стрижка:")
sheep2.last_shear=5
lets_shear(sheep2)
lets_shear(sheep1)


weight_sum = 0
heavy=0
heavy_name=''
for obj in gc.get_objects():
    if isinstance(obj, animal):
        # print(obj.__dict__)
        weight_sum+=int(obj.__dict__['weight'])
        if int(obj.__dict__['weight']) > heavy:
            heavy=int(obj.__dict__['weight'])
            heavy_name = obj.__dict__['name']
print("Общий вес всех животных ", weight_sum)
print("Самое тяжелое животное - {}, вес - {}".format(heavy_name,heavy))