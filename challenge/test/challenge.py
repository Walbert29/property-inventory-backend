from typing import List
import unittest

def blocks_numbers(list_number: List[int]):
    """
    Sorts the numbers into individual blocks and returns a text string representing the blocks.

    Args:
        list_number (List[int]): List of numbers containing blocks separated by zeros.

    Returns:
        str: A text string representing individually ordered blocks of numbers.
    """
    block_numbers = []
    numbers_temp = []
    for key, value in enumerate(list_number):
        if value != 0:
            numbers_temp.append(value)

        # Check if a zero has been found and if there are temporary numbers in the list
        # This indicates the end of a block
        if (value == 0 and numbers_temp) or ((key+1) == len(list_number) and value != 0):
            numbers_temp.sort()

            #Create a string representation of sorted numbers by removing unwanted characters
            number_text = str(numbers_temp).replace('[','').replace(']','').replace(',','').replace(' ','')
            block_numbers.append(number_text)
            numbers_temp = []

        # This indicates an empty block
        elif value == 0 and not numbers_temp:
            block_numbers.append("X")
        if ((key+1) == len(list_number) and value == 0):
            block_numbers.append("X")
        
    return " ".join(block_numbers)


class TestBlockNumbers(unittest.TestCase):
    
    def test_return_type_str(self):
        # Validte return tytpe
        list_numbers = [1,3,2,0,7,8,1,3,0,6,7,1]
        result = blocks_numbers(list_numbers)
        self.assertEqual(type(result), str)
    
    def test_order_split_list_number(self):
        # Split the list every time it finds a 0
        list_numbers = [1,3,2,0,7,8,1,3,0,6,7,1]
        result = blocks_numbers(list_numbers)
        self.assertEqual(result, '123 1378 167')

    def test_empty_block(self):
        # Split the list when locked in half
        list_numbers = [2,1,0,0,3,4]
        result = blocks_numbers(list_numbers)
        self.assertEqual(result, '12 X 34')
    
    def test_split_init_empty_block(self):
        # Split the list when there is an empty block at the start of the list
        list_numbers = [0,2,1,0,0,3,4]
        result = blocks_numbers(list_numbers)
        self.assertEqual(result, 'X 12 X 34')