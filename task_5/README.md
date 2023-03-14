Завдання №5
(розробка модулів, яких бракує для запуску гри блукачка)

Розробка складається з двох частин: перша у main.py, де створюється фактично ігровий простір, та game.py, де розроблені класи для реалізації гри.

  1. main.py
У даному файлі ніяких імпортованих бібліотек не використовувала. Імпортовано лише файл game.

  2. game.py
У даному файлі імпортовані такі бібліотеки:

from typing import TypeVar
from typing import Dict

Реалізовано класи: Room, Enemy, Item.

  1. Клас Room містить такі методи: вбудовані (__init__), невбудовані (get_name, get_details, get_item, get_character, set_description, set_character, set_item, link_room, move)
Даний клас репрезентує кімнати гри, називаючи їх, надаючи опису тощо.

<img width="269" alt="Знімок екрана 2023-03-14 о 21 44 39" src="https://user-images.githubusercontent.com/116552566/225119261-e61da60c-5b0e-420a-bb16-68ea16a41b38.png">

  2. Клас Enemy містить методи: вбудовані(__init__) та невбудовані (get_defeated, set_conversation, set_weakness, describe, talk, fight)
Даний клас встановлює та описує ворожого персонажа, надаючи йому особливості, слабкості, на вміння комунікувати.

<img width="422" alt="Знімок екрана 2023-03-14 о 21 50 38" src="https://user-images.githubusercontent.com/116552566/225120553-5ec20f5c-0bdb-4d8b-9618-3e7ca65bc1e8.png">

  3. Клас Item містить методи: __init__, set_description, get_name, describе, де описується предмети для боротьби з ворогом.

<img width="573" alt="Знімок екрана 2023-03-14 о 21 52 16" src="https://user-images.githubusercontent.com/116552566/225120941-9ec089c4-9ed7-47cf-a2f0-2e44f5e79ecc.png">
