import gc


class Animal:
    reference = ''
    name = ''
    weight = ''
    noise = ''
    male = 0  # 0-ж 1-м
    hungry = True
    eggs_count = 0
    last_get_milk = 0
    milk_count = 0
    last_shear = 0

    def __init__(self, reference, name, weight, male):
        self.reference = reference
        self.name = name
        self.weight = weight
        self.male = male

    def get_noise(self):
        return self.noise

    def get_feed(self):
        return self.hungry

    def do_feed(self):
        self.hungry = False

    def collect_tax(self, tax_kind):
        if tax_kind is 'eggs':
            if (self.male == 0) and (self.eggs_count > 0):
                cur_eggs_count = self.eggs_count
                self.eggs_count = 0

                return cur_eggs_count
            else:
                return 0
        elif tax_kind is 'milk':
            if self.last_get_milk > 12:
                cur_milk_count = self.milk_count
                self.last_get_milk = 0
                self.milk_count = 0
                return cur_milk_count

            else:
                return 0
        elif tax_kind is 'wool':
            if self.last_shear > 3:
                print("Ура, постригли")
            else:
                print("Слишком рано, еще шерсть не отросла")


class Birds(Animal):
    eggs_count = 1


class Livestock(Animal):  # класс заглушка, если потрбеуется добавление общих свойств для скота.
    get_hooves = True


class Cows(Livestock):
    reference = 'Корова'
    noise = 'МУУУ'
    milk_count = 8
    last_get_milk = 13  # сколько часов назад последний раз доили

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Goats(Livestock):
    reference = 'Коза'
    noise = 'МЕЕЕ'
    milk_count = 3
    last_get_milk = 13  # сколько часов назад последний раз доили

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Sheeps(Livestock):
    reference = 'Овца'
    noise = 'БЕЕЕ'
    last_shear = 1  # последний раз пострижена

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Gooses(Birds):
    reference = 'Гусь'
    noise = 'ГА-ГА-ГА'
    color = ''

    def __init__(self, name, weight, male, color):
        self.name = name
        self.weight = weight
        self.color = color
        self.male = male


class Chickens(Birds):
    reference = 'Курица'

    def __init__(self, name, weight, male, noise):
        self.name = name
        self.weight = weight
        self.male = male
        self.noise = noise


class Ducks(Birds):
    reference = 'Утка'
    noise = 'Кря'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


def lets_feed(animal_name):
    if animal_name.hungry:
        animal_name.get_feed()
        print('Покормили животное - ', animal_name.name)
    else:
        print('{} {} не хочет есть'.format(animal_name.reference, animal_name.name))


def lets_milk(animal_name):
    if animal_name.last_get_milk > 12:
        print('Доим {}, и получаем {} литров молока'.format(animal_name.name, animal_name.collect_tax('milk')))

    else:
        print('{} доили недавно, пока нет молока'.format(animal_name.name))


def lets_egg(animal_name):
    if animal_name.male == 0:
        print("Яйца собраны, животное {}-{}".format(animal_name.reference, animal_name.name))
    else:
        print('Мужики яца не высиживают, животное {}-{}'.format(animal_name.reference, animal_name.name))


def lets_shear(animal_name):
    print("Стрижем {}".format(animal_name.name))
    animal_name.collect_tax('wool')


goose1 = Gooses('Серый', '18', 'Серый', 1)
goose2 = Gooses('Белый', '15', 'Белый', 0)
chicken1 = Chickens('Ко-Ко', '10', 0, 'КО-КО-КО')
chicken2 = Chickens('Кукареку', '11', 1, 'Кукареку')
duck1 = Ducks('Кряква', 6)
cow = Cows("Маньку", 200)
goat1 = Goats("Рога", 30)
goat2 = Goats("Копыта", 32)
sheep1 = Sheeps("Барашек", 20)
sheep2 = Sheeps("Кудрявый", 20)


all_animals = [goose1, goose2, chicken1, chicken2, duck1, cow, goat1, goat2, sheep1, sheep2]

sheep2.hungry = False
cow.hungry = False
goat2.last_get_milk = 2
sheep2.last_shear = 5
for i in all_animals:
    lets_feed(i)# кормим
    if i.last_get_milk > 0:
        lets_milk(i)# доим
    if i.__class__.mro().__contains__(Birds):
        lets_egg(i)# собираем яйцы
    if i.__class__.mro().__contains__(Sheeps):
        lets_shear(i)# стрижем
print()

weight_sum = 0
heavy = 0
heavy_name = ''
for obj in gc.get_objects():
    if isinstance(obj, Animal):
        weight_sum += int(obj.__dict__['weight'])
        if int(obj.__dict__['weight']) > heavy:
            heavy = int(obj.__dict__['weight'])
            heavy_name = obj.__dict__['name']
print("Общий вес всех животных ", weight_sum)
print("Самое тяжелое животное - {}, вес - {}".format(heavy_name, heavy))
