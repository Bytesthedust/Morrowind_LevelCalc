# Morrowind_LevelCalc
Automatic notetaking regarding Morrowind character information and level calculator

Synopsis: The Elder Scrolls 3: Morrowind is an open-world action role-playing video game developed by Bethesda Game Studios that follows the Player Character (PC) as a recently released prisoner fated to save Morrowind from a great threat. Character creation in Morrowind is much more involved than later games of the series and while there is a lot more freedom in creating your character, the nuances of it and the levelling system can confuse new players. This programs aims to simplify the creation process and aid in effecient levelling.

Features: Character creation maker, leveling calculator, and provides a save of your characters stats

Character Creation 
Creating a character is the pivoting point between having an enjoyable and fun experience or a frustrating one. The breakdown of character creation below and the links provided will help in informing your decisions. Take as much time as needed to wrap your head around it.

Race and Gender (from: https://en.uesp.net/wiki/Morrowind:Races)

Character creation begins with choosing a race and gender. Each race has varying values of Attributes that are affected by race and gender,these attributes being Strength, Intelligence, Willpower, Agility, Speed, Endurance, Personality, and Luck. Each race also have bonuses for some of the 27 skills in the game. These skills and attributes will be explained later, but its important to note that each skill is associated with a Specialization and is governed by an attribute which is important for levelling.


Classes (from: https://en.uesp.net/wiki/Morrowind:Classes)

Next is choosing your class. Every humanoid NPC, including your character, has a class which represents their occupation or what they are good at. The three parts of a class is their Specialization, Major/Minor skills, and Favoured Attributes. There are three Specializations, Magic, Combat, and Stealth, and any skills associated with that Specialization gets a +5 bonus and is quicker to level up. With Major/Minor skills, your character's proficiencies will start at 30 in each Major Skill and 15 in each Minor Skill. Miscellaneous Skills start at 5. These are the values before any bonuses from race or Specialization. The experience points required to increase a Skill are only 75% of normal for Major Skills, but they are increased to 125% of normal for Miscellaneous Skills. Each class "favors" two of the eight primary Attributes. Your character will start with ten extra points in the favored Attributes of their class, added to the values determined by their race and gender.

Birthsigns (from: https://en.uesp.net/wiki/Morrowind:Birthsigns)

Lastly, you will choose a birthsign. Birthsigns provide bonuses such as abilities(including bonuses to attributes), powers(1/day special spells), and spells.


Levelling (from: https://en.uesp.net/wiki/Morrowind:Level)

Each class in the game has 5 Major skills, five Minor skills, and 17 Misc skills. Each time your character increases any combination of Major or Minor skills ten times, they become eligible to gain a level. When levelling up, you choose three of your attributes to increase and each attribute, except Luck, has a modifier that affects the attribute increase. The multiplier for each Attribute is determined by the total number of times that skills governed by that attribute have increased(includes Maj,Min,Misc) since the last level up:

    No skill increases = no multiplier (1 point)
    1–4 skill increases = 2×
    5–7 skill increases = 3×
    8–9 skill increases = 4×
    10 or more skill increases = 5×

It is important to note that while the counts for multipliers continue to accumulate for this level up, the count of Major/Minor skill increases to determine eligibility for level-up will not roll over to the next level. In other words, if you increase Major and Minor skills five times after you become eligible for a level up, your progress will show as "15/10" before the level up, and then "5/10" afterwards. Those extra five increases will not affect your multipliers for the next level, however, so if you instead had ten excess major/minor increases, upon leveling up you would be immediately eligible for another level up, with no attribute multipliers.

Objectives:
My objectives for what this program is able to do is;
  1. Provide a quick breakdown of your character's current level, skills, and attributes
  2. Provide a preview of attribute modifiers to inform the player if they need to level up some skills to get the desired modifier
  3. Save the current state of the character at their current and previous levels and skill values as files


Future Goals:

In the future, I hope to make the program more user-friendly with a better UI and hopefully a full app
