import csv #handling of csv files

class Character:
    def __init__(self, name, race, gender):
        self.name = name
        self.race = race
        self.gender = gender


    def createNewCharacter(self, name, race, gender):
        """Creates a default character stat board"""
        characterDict = {
            "Name": name,
            "Race": race,
            "Gender": gender}

        attributes = self.readAttributes() #dict of attributes
        skills = self.readSkills() #dict of skills
        for i in range(19):
            r = list(attributes[i].values())#return each line of the file as a list
            
            r_race = r[0].split("_")#split the first element of list to get race and gender
            if(r_race[0] == self.getRace() and r_race[1] == self.getGender()): #checks if race and gender are in the list then updates character dictionary with appropriate attributes
                characterDict.update({"Stats":{"Strength": int(r[1]), "Intelligence": int(r[2]), "Willpower": int(r[3]), "Agility": int(r[4]), "Speed": int(r[5]), "Endurance": int(r[6]), "Personality": int(r[7]), "Luck": int(r[8])}})

        #load default skills into stat board
        for i in range(27):
            s = list(skills[i].values()) #return each line of the file as a list
            characterDict.update({s[0]: int(s[1])}) #updates character dict with each skill and their default value

        #dictionary of racial skill bonuses
        racial_bonus = {
        "Argonian": {"Alchemy": 5, "Athletics": 15, "Illusion": 5, "Medium Armor": 5, "Mysticism": 5, "Spear": 5, "Unarmored": 5},
        "Breton": {"Alchemy": 5, "Alteration": 5, "Conjuration": 10, "Illusion": 5, "Mysticism": 10, "Restoration": 10},
        "Dunmer": {"Destruction": 10, "Athletics": 5, "Long Blade": 5, "Light Armor": 5, "Mysticism": 5, "Marksman": 5, "Short Blade": 10},
        "Altmer": {"Alchemy": 10, "Alteration": 5, "Conjuration": 5, "Destruction": 10, "Enchant": 10, "Illusion": 5},
        "Imperial": {"Blunt Weapon": 5, "Hand-to-hand": 5, "Long Blade": 10, "Light Armor": 5, "Mercantile": 10, "Speechcraft": 10},
        "Khajiit": {"Acrobatics": 15, "Athletics": 5, "Hand-to-hand": 5, "Light Armor": 5, "Security": 5, "Sneak": 5, "Short Blade": 5},
        "Nord": {"Axe": 10, "Blunt": 10, "Long Blade": 5, "Heavy Armor": 5, "Medium Armor": 10, "Spear": 5},
        "Orc": {"Armorer": 10, "Axe": 5, "Block": 10, "Medium Armor": 10, "Heavy Armor": 10},
        "Redguard": {"Axe": 5, "Athletics": 5, "Blunt Weapon": 5, "Medium Armor": 5, "Long Blade": 15, "Heavy Armor": 5, "Short Blade": 5},
        "Bosmer": {"Acrobatics": 5, "Alchemy": 5, "Light Armor": 10, "Marksman": 15, "Sneak": 10}}

        bonus_stats = racial_bonus.get(race) #returns dictionary of given race
        
        #for each relevant skill in the dictionary, increment the skill value and update the character dict
        for i in bonus_stats:

            stat = characterDict.get(i)
            stat += bonus_stats.get(i)
            characterDict.update({i: stat})

        return characterDict

    
    def readAttributes(self):
        '''Returns a dictionary of racial/gender attributes'''

        with open('Morrowind_Python\Morrowind_Races.csv', 'r') as racefile:
            reader = csv.DictReader(racefile)
            
            attriDict = list(reader)
        return attriDict
    
    def readSkills(self):
        '''Returns a dictionary of skills'''
        
        with open('Morrowind_Python\Morrowind_Skills.csv', 'r') as skillfile:
            reader = csv.DictReader(skillfile)
            skillDict = list(reader)

        return skillDict

    def getRace(self):
        return self.race
    
    def getGender(self):
        return self.gender

    def calculateModifier(self):
        """Returns potential modifiers for attributes upon levelling up"""

    def updateStats(self):
        """Updates values of stats"""
    
    def saveStats(self):
        """Updates character file with new stats"""

    #if user chooses a pre-defined class
    class Class:
        def __init__(self, choice):
            self.choice = choice

        def readClass(self):
            """Reads class file and returns a list-dictionary with values"""
            with open('Morrowind_Python\Morrowind_Classes.csv', 'r') as classfile:
                reader = csv.DictReader(classfile)
            
                attriDict = list(reader)
            return attriDict

        def chooseClass(self, choice):
            """Returns updated stats based on chosen class"""
            classes = self.readClass()


        
    #if use creates a custom class
    class Custom:
        def __init__(self, attributes, major, minor, special):
            self.attributes = attributes
            self.major = major
            self.minor = minor
            self.special = special
            #all but 'special' takes a list

        def createCustomClass(self, favAttributes, Major, Minor, special):
            """Returns updated stats based on choices made in custom class"""
        
    



def main():
    entity = Character("Unknown", "Dunmer", "M")
    entityDict = entity.createNewCharacter("Unknown", "Dunmer", "M")

    skills = entity.readSkills()
    race = entity.readAttributes() #max index: 19


    print(entityDict)
    # for i in range(19):
    #     r = list(skills[i].values())
    #     print(r)
    
    # for i in entityDict:
    #     print(i)

    #print(skills)
    #s = list(skills[0].values())
    #print(s)

main()