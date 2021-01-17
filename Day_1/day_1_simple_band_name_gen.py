print("Helo everyone!!!\n")
city = input("enter your home_town: \n")
nike_name = input("enter your nike_name: \n")

random_Adjective = ("Angry", "Bashful", "Crazy", "Deadly", "Evil", "Fierce", "Grizzly", "Happy", "Indigo", "Jealous", "Kicking", "Lonely", "Mysterious", "New", "Old", "Pretty", "Quiet", "Raving", "Secret", "Tidy", "Untidy", "Vicious", "Whispering", "X-Rated", "Yellow", "Zany")

random_animals = ("Alligators", "Bats", "Cats", "Dolphins", "Eagles", "Frogs", "Gerbils", "Horses", "Iguanas", "Jackals", "Kangaroos", "Leopards", "Meerkats", "Nighthawks", "Ocelots", "Panthers", "Quails", "Reptiles", "Shrews", "Turtles", "Unicorns", "Vipers", "Whales", "X-Rays", "Yaks", "Zebras")
#mix the name and nike name by using ord function
f_city = city[2]
ord_city = ord(f_city)-90 # eliminate out_of_range error help by minus large number 
f_nike_name = nike_name[2]
ord_nike_name = ord(f_nike_name)-90 # eliminate out_of_range error help by minus large number 

print("Your band name should be\n")

print("The "+random_Adjective[ord_city] + " " +random_animals[ord_nike_name])
