'''
Module of classes for the game
'''
from typing import TypeVar, Dict

TRoom = TypeVar('TRoom', bound='Room')
TEnemy = TypeVar('TEnemy', bound='Enemy')
TItem = TypeVar('TItem', bound='Item')

class Room:
    '''
    Class represents the rooms
    '''
    def __init__(self, name: str) -> None:
        '''
        Needed atributes for class
        '''
        self.__name: str = name
        self.__description: str|None = None
        self.__neighbours: Dict[str, TRoom] = {}
        self.__inhabitant: TEnemy|None = None
        self.__item: TItem|None = None

    def get_name(self) -> str:
        '''
        Gets name
        '''
        return self.__name

    def set_description(self, description: str) -> None:
        '''
        Sets the description
        '''
        self.__description: str = description

    def link_room(self, room: TRoom, side: str) -> None:
        '''
        Links neighbours to the current room
        '''
        self.__neighbours[side] = room

    def get_details(self) -> None:
        '''
        Gets detail information
        '''
        print(self.__name)
        print('-'*20)
        print(self.__description)
        for side, neibour in self.__neighbours.items():
            print(f'The {neibour.get_name()} is {side}')
        
    def set_character(self, character: TEnemy|None) -> None:
        '''
        Sets the character
        '''
        self.__inhabitant = character

    def get_item(self) -> TItem|None:
        '''
        Gets item's name
        '''
        return self.__item
    
    def set_item(self, item: TItem|None) -> None:
        '''
        Sets item
        '''
        self.__item = item
        
    def get_character(self) -> TEnemy|None:
        '''
        Gets character
        '''
        return self.__inhabitant
    
    def move(self, side: str) -> TRoom:
        '''
        Method for moving to the neignbour room
        '''
        return self.__neighbours[side]


class Enemy:
    '''
    Class for Emeny in the game
    '''
    defeated = 0

    def __init__(self, name: str, description: str) -> None:
        '''
        Needed atributes for class
        '''
        self.__name = name
        self.__description = description
        self.__conversation: str|None = None
        self.__weakness: str|None = None

    def set_conversation(self, conversation: str) -> None:
        '''
        Sets the propriate dialog
        '''
        self.__conversation: str = conversation
    
    def set_weakness(self, weakness: str) -> None:
        '''
        Sets the weakness of the enemy
        '''
        self.__weakness: str = weakness

    def describe(self) -> str:
        '''
        Method for describing
        '''
        print(f'{self.__name} is here!\n{self.__description}')

    def talk(self) -> None:
        '''
        Method to talk to enemy
        '''
        print(f'[{self.__name} says]: {self.__conversation}')
    
    def fight(self, fight_with: str) -> bool:
        '''
        Method to fight with enemy
        '''
        if fight_with == self.__weakness:
            print(f'You fend {self.__name} off with the {self.__weakness}')
            Enemy.defeated += 1
            return True
        print(f'{self.__name} crushes you, puny adventurer!')
        return False
    
    def get_defeated(self) -> int:
        '''
        Gets the defeated enemy
        '''
        return Enemy.defeated


class Item:
    '''
    Class to describe the items
    '''
    def __init__(self, name: str) -> None:
        '''
        Needed atributes for class
        '''
        self.__name = name
        self.__description: str|None = None
    
    def set_description(self, description: str) -> None:
        '''
        Sets description for the items
        '''
        self.__description: str = description
    
    def get_name(self) -> str:
        '''
        Gets name of the item
        '''
        return self.__name
    
    
    def describe(self) -> str:
       '''
       Method to descibe the item in string
       '''
       print(f'The [{self.__name}] is here - {self.__description}')
