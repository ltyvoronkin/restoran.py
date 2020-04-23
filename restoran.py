class Restoran():
    def __init__(self, restoran_name, cuisine_type):
        self.restoran_name = restoran_name
        self.cuisine_type = cuisine_type
        self.number_served=0

    def describe_restoran(self):
        print("My favorite restoran is " + self.restoran_name.title() +
              ". Its has  " + self.cuisine_type + " cuisine!!!")

    def open_restoran(self):
        print("Restoran " + self.restoran_name.title() +
              " is open now, welcome!!!")

    def read_served(self):
        print("served today - ".title()+str(self.number_served))    

    def increment_number_people(self,number):
    	self.number_served +=number

    def update_served(self,new):
    	self.number_served=new



favorite_restoran = Restoran('apple', 'russian')
favorite_restoran.describe_restoran()
favorite_restoran.open_restoran()
favorite_restoran.increment_number_people(300)
favorite_restoran.read_served()

favorite_restoran2 = Restoran('friends plays', 'italian')
favorite_restoran2.describe_restoran()
favorite_restoran2.open_restoran()
favorite_restoran2.increment_number_people(243)
favorite_restoran2.read_served()

favorite_restoran3 = Restoran('hookah plays', 'russian')
favorite_restoran3.describe_restoran()
favorite_restoran3.open_restoran()
favorite_restoran3.increment_number_people(400)
favorite_restoran3.read_served()