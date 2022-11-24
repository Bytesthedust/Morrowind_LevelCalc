import csv #handling of csv files

class Character:
    def __init__(self, name, race, gender):
        self.name = name
        self.race = race
        self.gender = gender
        self.definedClass = self.characterClass("x")


    def createNewCharacter(self):
        """Creates a default character stat board"""
        characterDict = {
            "Name": self.name,
            "Race": self.race,
            "Gender": self.gender,
            "Class": ""}

        attributes = self.readAttributes() #dict of attributes
        skills = self.readSkills() #dict of skills

        for i in range(19):
            r = list(attributes[i].values())#return each line of the file as a list
            
            r_race = r[0].split("_")#split the first element of list to get race and gender
            if(r_race[0] == self.race and r_race[1] == self.gender): #checks if race and gender are in the list then updates character dictionary with appropriate attributes
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
        "Nord": {"Axe": 10, "Blunt Weapon": 10, "Long Blade": 5, "Heavy Armor": 5, "Medium Armor": 10, "Spear": 5},
        "Orc": {"Armorer": 10, "Axe": 5, "Block": 10, "Medium Armor": 10, "Heavy Armor": 10},
        "Redguard": {"Axe": 5, "Athletics": 5, "Blunt Weapon": 5, "Medium Armor": 5, "Long Blade": 15, "Heavy Armor": 5, "Short Blade": 5},
        "Bosmer": {"Acrobatics": 5, "Alchemy": 5, "Light Armor": 10, "Marksman": 15, "Sneak": 10}}

        bonus_stats = racial_bonus.get(self.race) #returns dictionary of given race
        
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


    def calculateModifier(self):
        """Returns potential modifiers for attributes upon levelling up"""

    def updateStats(self):
        """Updates values of stats"""
    
    def saveStats(self):
        """Updates character file with new stats"""

    #if user chooses a pre-defined class
    class characterClass:

        def __init__(self, choice):
            self.choice = choice

        def readClass(self):
            """Reads class file and returns a list-dictionary with values"""
            with open('Morrowind_Python\Morrowind_Classes.csv', 'r') as classfile:
                reader = csv.DictReader(classfile)
            
                attriDict = list(reader)
            return attriDict

        def chooseClass(self):
            """Returns a list of stats based on chosen class"""
            classes = self.readClass()
            
            for i in range(len(classes)):
                l = list(classes[i].values())
                if(l[0] == self.choice):
                    return l
                

        def addClass(self, characterDict):
            """Update character stats based on chosen class"""
            characterClass = self.chooseClass()
            characterDict["Class"] = self.choice
            attributes = characterClass[1].split("/")
            major = characterClass[2].split("/")
            minor = characterClass[3].split("/")
            special = characterClass[4]

            stats = characterDict.get("Stats") #returns the nested dictionary with attributes

            #updates attributes
            for i in attributes:
                #print(i)
                x = stats.get(i)+10
                stats.update({i: x})
            
            #updates major skills
            for i in major:
                mjSkill = characterDict.get(i)
                x = mjSkill + 25
                characterDict.update({i: x})
            
            #updates minor skills
            for i in minor:
                miSkill = characterDict.get(i)
                x = miSkill + 10
                characterDict.update({i: x})

            
            #All 27 skills and the specialization they fall under
            stealthSpecial = ["Acrobatics", "Light Armor", "Marksman", "Short Blade", "Sneak", "Speechcraft", "Mercantile", "Security", "Hand-to-hand"]
            combatSpecial = ["Heavy Armor", "Medium Armor", "Spear", "Armorer", "Axe", "Blunt Weapon", "Long Blade", "Block", "Athletics"]
            magicSpecial = ["Unarmored", "Illusion", "Alchemy", "Conjuration", "Enchant", "Restoration", "Mysticism", "Destruction", "Alteration"]

            #updating skills based on chose specialization
            for i in range(9):
                if(special == "Stealth"):
                    x = characterDict.get(stealthSpecial[i]) + 5
                    characterDict.update({stealthSpecial[i]: x})

                elif(special == "Combat"):
                    x = characterDict.get(combatSpecial[i]) + 5
                    characterDict.update({combatSpecial[i]: x})
                else:
                    x = characterDict.get(magicSpecial[i]) + 5
                    characterDict.update({magicSpecial[i]: x})


        
    #if use creates a custom class
    class Custom:
        def __init__(self, className, attributes, major, minor, special):
            self.className = className
            self.attributes = attributes
            self.major = major
            self.minor = minor
            self.special = special
            #all but 'special' and 'className' takes a list

        def createCustomClass(self, characterDict):
            """Returns updated stats based on choices made in custom class"""
            
            characterDict["Class"] = self.className
            
            stats = characterDict.get("Stats") #returns the nested dictionary with attributes

            for i in self.attributes:
                x = stats.get(i)+10
                stats.update({i: x})
            
            #updates major skills
            for i in self.major:
                mjSkill = characterDict.get(i)
                x = mjSkill + 25
                characterDict.update({i: x})
            
            #updates minor skills
            for i in self.minor:
                miSkill = characterDict.get(i)
                x = miSkill + 10
                characterDict.update({i: x})

            
            #All 27 skills and the specialization they fall under
            stealthSpecial = ["Acrobatics", "Light Armor", "Marksman", "Short Blade", "Sneak", "Speechcraft", "Mercantile", "Security", "Hand-to-hand"]
            combatSpecial = ["Heavy Armor", "Medium Armor", "Spear", "Armorer", "Axe", "Blunt Weapon", "Long Blade", "Block", "Athletics"]
            magicSpecial = ["Unarmored", "Illusion", "Alchemy", "Conjuration", "Enchant", "Restoration", "Mysticism", "Destruction", "Alteration"]

            #updating skills based on chosen specialization
            for i in range(9):
                if(self.special == "Stealth"):
                    x = characterDict.get(stealthSpecial[i]) + 5
                    characterDict.update({stealthSpecial[i]: x})

                elif(self.special == "Combat"):
                    x = characterDict.get(combatSpecial[i]) + 5
                    characterDict.update({combatSpecial[i]: x})
                else:
                    x = characterDict.get(magicSpecial[i]) + 5
                    characterDict.update({magicSpecial[i]: x})
        


           

            
    

#driver code for testing

def main():
    entity = Character("Artemis Fayden", "Argonian", "M")
    entityDict = entity.createNewCharacter()

    #entityClass = entity.characterClass("Agent")
    #entityClass.addClass(entityDict)
    entityClass = entity.Custom("Berserker", ["Strength", "Endurance"],["Light Armor", "Athletics", "Axe", "Security", "Alchemy"], ["Blunt Weapon", "Block", "Armorer", "Marksman", "Mysticism"], "Combat")
    entityClass.createCustomClass(entityDict)

    print(entityDict)

    
main()
