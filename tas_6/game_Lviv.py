from typing import List, TypeVar

TStreet = TypeVar('TStreet', bound='Street')
TGood = TypeVar('TGood', bound='GoodCharacter')
TCharacter = TypeVar('TCharacter', bound='Character')
TBad = TypeVar('TBad', bound='BadCharacter')

class Character:
    def __init__(self, name: str, description: str) -> None:
        self.__name: str = name
        self.__description: str = description

    def describe(self) -> str:
        return (f'{self.__name} is here!\n{self.__description}')
        
    def get_name(self) -> str:
        return self.__name
    
    def set_description(self, description: str) -> None:
        self.__description: str = description

class GoodCharacter(Character):

    def __init__(self, name: str, description: str) -> None:
        super().__init__(name, description)
        self.__gift = None
        self.__wish: str = None

    def set_gift(self, gift) -> None:
        self.__gift = gift

    def set_wish(self, wish: str) -> None:
        self.__wish = wish

    def get_wish(self):
        return self.__wish
    
    def get_gift(self):
        return self.__gift

    def describe(self) -> str:
        print(f'{super().describe()} "I have {self.__gift}!\nBut I need {self.__wish}."')

class BadCharacter(Character):
    def __init__(self, name: str, description: str) -> None:
        super().__init__(name, description)
        self.__weakness = None

    def set_weakness(self, weakness) -> None:
        self.__weakness = weakness

    def get_weakness(self):
        return self.__weakness
    
    def describe(self) -> str:
        print(f'{super().describe()} "My weakness is - {self.__weakness}"')

    def fight(self, fight_with: str) -> bool:
        '''
        Method to fight with enemy
        '''
        if fight_with == self.__weakness:
            print(f'You fend {self.get_name()} off with the {self.__weakness}')
            return True
        print(f'{self.__name} crushes you, puny adventurer!')
        return False
    
class Item:
    def __init__(self, name: str, description: str) -> None:
        self.__name = name
        self.__description = description

    def get_name(self) -> str:
        return self.__name
    
    def set_description(self, description: str) -> None:
        self.__description: str = description

    def __str__(self) -> str:
        return f'{self.__name}: {self.__description}'

class Weapon(Item):
    def __init__(self, name: str, description: str) -> None:
        super().__init__(name, description)

    def give(self):
        pass


class Street:

    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__description: str|None = None
        self.__neighbours: List[TStreet] = []

    def get_name(self) -> str:
        return self.__name

    def set_description(self, description: str) -> None:
        self.__description: str = description

    def link_street(self, street: TStreet) -> None:
        self.__neighbours.append(street)

    def get_details(self) -> None:
        print(self.__name)
        print('-' * 20)
        print(self.__description)
        for  neibour in self.__neighbours:
            print(f'The {neibour.get_name()} is neignbour.')
        
    def set_character(self, character: TGood|None) -> None:
        self.__inhabitant = character
        
    def get_character(self) -> TCharacter|None:
        return self.__inhabitant
    
    def move(self) -> TStreet:
        for i, street in enumerate(self.__neighbours):
            print(f"Press {i} to move to {street.get_name()}")
        return self.__neighbours[int(input('> '))]
    
