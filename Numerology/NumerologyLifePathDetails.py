from Numerology import Numerology

class NumerologyLifePathDetails(Numerology):
    # Initialize with name and date of birth
    def __init__(self, sName, sDOB):
        # Call the parent class constructor using python's built in super() function. Less code, more readable
        super().__init__(sName, sDOB)

        # Dictionary of Life Path descriptions
        self.__LifePathDescriptions = {
            1: "The Independent: Wants to work/think for themselves",
            2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art and to perform or get attention",
            4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer: Likes to travel and meet others, often a extrovert",
            6: "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality",
            8: "The Executive: Gravitates to money and power",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way"
        }

    # Return Life Path description based on Life Path number
    def getLifePathDescription(self):
        # Get the Life Path number from the parent class
        iLifePath = self.getLifePath()
        return self.__LifePathDescriptions[iLifePath]

    # Override the __str__ method to include Life Path Description
    def __str__(self):
        # display all numerology including Life Path Description
        # Start with the parent class string representation
        parent_str = super().__str__()

        # Add the Life Path Description
        return f"{parent_str}\n    Life Path Description: {self.getLifePathDescription()}"