import random

def hospital():
    number = input("Input a number: ")
    timemeasure = input("Input an measure of time(hour/min/sec): ")
    transportmode = input("Input a transport mode(car/metro/plane): ")
    adj = input("Input an adjective: ")
    adj2 = input("Input another adjective: ")
    noun = input("Input a noun: ")
    color = input("Input a color: ")
    bodypart = input("Input a body part(head/leg/belly): ")
    verb = input("Input a verb: ")
    num2 = input("Input another number: ")
    noun2 = input("Input another noun: ")
    noun3 = input("Input one more noun: ")
    bodypart2 = input("Input another body part(head/leg/belly): ")
    noun4 = input("Input the last noun)): ")
    adj3 = input("Input the last adjective: ")
    sillyword = input("Input a silly word: ")

    print("It was about " + number + " " + timemeasure + " ago when I arrived at the hospital in a "
                 + transportmode + ". The hospital is a/an " + adj + " place, there are a lot of " + adj2 + " "
                 + noun + " here. There are nurses here who have " + color + " " + bodypart
                 + ". If someone wants to come into my room I told them that they have to "
                 + verb + " first. I’ve decorated my room with " + num2 + " " + noun2
                 + ". Today I talked to a doctor and they were wearing a " + noun3 + " on their " + bodypart2
                 + ". I heard that all doctors " + verb + " " + noun4 + " every day for breakfast. The most "
                 + adj3 + " thing about being in the hospital is the " + sillyword + " " + noun + " !")


def camping():
    name = input("Input Person's name: ")
    noun = input("Input a proper noun: ")
    adj = input("Input a feeling describing adjective: ")
    verb = input("Input a verb: ")
    adj2 = input("Input another feeling describing adjective: ")
    animal = input("Input an animal: ")
    verb2 = input("Input another verb: ")
    color = input("Input a color: ")
    verbing = input("Input a vern ending with -ing: ")
    adverb = input("Input an adverb ending with -ly: ")
    number = input("Input a number: ")
    timemeasure = input("Input an measure of time(hour/min/sec): ")
    sillyword = input("Input a silly word: ")
    noun2 = input("Input another noun: ")

    print("This weekend I am going camping with " + name + ". I packed my lantern, sleeping bag, and " + noun
                 + ". I am so " + adj + " to " + verb + " in a tent. I am " + adj2 + " we might see a(n) " + animal
                 + ", I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and " + verb2
                 + ". I have heard that the " + color + " lake is great for " + verbing + ". Then we will " + adverb
                 + " hike through the forest for " + number + " " + timemeasure + ". If I see a " + color + " " + animal
                 + " while hiking, I am going to bring it home as a pet! At night we will tell " + number + " " + sillyword
                 + " stories and roast " + noun2 + " around the campfire!!!")


def castle():
    name = input("Input Person's name: ")
    adj = input("Input an adjective: ")
    color = input("Input a color: ")
    animal = input("Input an animal: ")
    place = input("Input a place: ")
    adj2 = input("Input another adjective: ")
    magicalcreature = input("Input a plural magical creature: ")
    adj3 = input("Input another adjective: ")
    magicalcreature2 = input("Input another plural magical creature: ")
    room = input("Input a room number: ")
    noun = input("Input a noun: ")
    noun2 = input("Input another noun: ")
    noun3 = input("Input a plural noun: ")
    adj4 = input("Input another adjective: ")
    noun4 = input("Input another plural noun: ")
    number = input("Input a number: ")
    timemeasure = input("Input an measure of time(hour/min/sec): ")
    verbing = input("Input a vern ending with -ing: ")
    adj5 = input("Input the last adjective: ")
    noun5 = input("Input the last noun: ")

    print("Dear " + name + ", I am writing to you from a " + adj
                 + " castle in an enchanted forest. I found myself here one day after going for a ride on a "
                 + color + " " + animal + " in " + place + ". There are " + adj2 + " " + magicalcreature
                 + " and " + adj3 + " " + magicalcreature2 + " here! In the " + room + " there is a pool full of "
                 + noun + ". I fall asleep each night on a " + noun2 + " of " + noun3 + " and dream of " + adj4 + " "
                 + noun4 + ". It feels as though I have lived here for " + number + " " + timemeasure
                 + ". I hope one day you can visit, although the only way to get here now is " + verbing + " on a "
                 + adj5 + " " + noun5 + "!!!")


topicNumber = input("Pick an option between (1,2,3) or any other number to get a random choice: ")


def isinteger(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


while not isinteger(topicNumber):
    topicNumber = input("INPUT AN INTEGER!:) ")

topicNumber = int(topicNumber)

templates = [1, 2, 3]
if topicNumber == 1:
    hospital()
elif topicNumber == 2:
    camping()
elif topicNumber == 3:
    castle()
else:
    topicNumber = random.choice(templates)
    if topicNumber == 1: hospital()
    elif topicNumber == 2: camping()
    elif topicNumber == 3: castle()