
class Numerology():
    # Initialize with name and date of birth, format data, and set up letter values
    def __init__(self, sName, sDOB):
        self.__sName = sName.strip().upper()
        self.__startDOB = sDOB
        self.__dob = sDOB.replace('-', '').replace('/', '')

        self.__Alphabet = { ('A', 'J', 'S'):1,
                                ('B', 'K', 'T'):2,
                                ('C', 'L', 'U'):3,
                                ('D', 'M', 'V'):4,
                                ('E', 'N', 'W'):5,
                                ('F', 'O', 'X'):6,
                                ('G', 'P', 'Y'):7,
                                ('H', 'Q', 'Z'):8,
                                ('I', 'R')     :9
                            }
    # reduce numerology number back down to a single digit
    def _reduceNum(func):
        def wrapper(self):
            iNum = func(self)
            while iNum > 9:
                iNum = sum(int(iNum) for iNum in str(iNum))
            return iNum
        return wrapper

    # getName returns subjects name
    def getName(self):
        return self.__sName

    # getBirthDate returns date of birth
    def getBirthDate(self):
        return self.__dob

    # gets original start of date of birth
    def getstartDOB(self):
        return self.__startDOB

    # summing up month and day using decorator
    @_reduceNum
    def getAttitude(self):
        sAttitude = self.getBirthDate()[:4]
        iSum = 0
        for sNumber in sAttitude:
            iSum += int(sNumber)
        return iSum

    # getting sum of birthday using its index positions
    @_reduceNum
    def getBirthDay(self):
        return int(self.getBirthDate()[2:4])

    # Calculates life path number by summing all digits in birth date
    @_reduceNum
    def getLifePath(self):
        iSum = 0
        for sNumber in self.getBirthDate():  # This iterates through the entire birth date string
            iSum += int(sNumber)
        return iSum

    # Calculates personality number from consonants in name
    @_reduceNum
    def getPersonality(self):
        iSum = 0
        for char in self.getName():
            if char not in 'AEIOU':
                for key, value in self.__Alphabet.items():
                    if char in key:
                        iSum += value
                        break
        return iSum

    # soul number from vowels in name
    @_reduceNum
    def getSoul(self):
        iSum = 0
        for char in self.getName():
            if char in 'AEIOU':
                for key, value in self.__Alphabet.items():
                    if char in key:
                        iSum += value
                        break
        return iSum

    # Calculates power name by combining soul and personality numbers
    @_reduceNum
    def getPowerName(self):
        return self.getSoul() + self.getPersonality()

    # displaying all numerology calculations
    def __str__(self):
        """String representation displaying all numerology calculations"""
        return f"""Name: {self.getName()}
    DOB: {self.getstartDOB()}
    Life Path: {self.getLifePath()}
    Attitude: {self.getAttitude()}
    Birthday: {self.getBirthDay()}
    Personality: {self.getPersonality()}
    Power Name: {self.getPowerName()}
    Soul: {self.getSoul()}"""