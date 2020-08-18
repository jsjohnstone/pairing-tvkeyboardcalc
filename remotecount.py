## Implementation notes:
# A small tool that calculates the number of moves necessary to enter a given word using
# a remote control and an on-screen keyboard (able to move up, down, left, right)
# and adds one to count clicking 'OK' for each character.
#
# Use the example of 'chi' name to test
# Define a method that can find the position of a character in a multi-dimensional list
# Define a method that calculates the number of moves from character a to b based on above position
# Define a method that breaks the word up into a list of characters
# Define a method that iterates through the word list and counts the moves for each letter
# Return the total count of moves
#
## TODO:
# Santise the input - convert to lowercase, check for non-existant characters
# Handle other edge cases (e.g. a map that has the same character twice)
# Allow word to be provided by commandline argument

class WordFinder:

    def calculate(self, map, word):
        word_characters = list(word)
        self.map = map

        startpos = 'a'
        total_moves = 0

        for char in word_characters:
            char_moves = self.calculate_moves(startpos, char)
            total_moves += char_moves['moves']
            startpos = char

        return total_moves

    def calculate_moves(self, startchar, targetcharacter):

        print("looking for {} to {}".format(startchar, targetcharacter))
        start_pos = self.calculate_char_pos(startchar)
        target_pos = self.calculate_char_pos(targetcharacter)

        xmoves = abs(start_pos[0]-target_pos[0])
        ymoves = abs(start_pos[1]-target_pos[1])

        moves = xmoves + ymoves + 1
        # add the lateral and longitudinal moves, plus 1 for 'OK'

        result = {
            'moves' : moves,
            'endpos' : target_pos
        }

        print("{} moves required...".format(moves))

        return result

    # Define a method that looks up the position of a specific character to return and x and y value
    def calculate_char_pos(self, char):
 
        map = self.map

        for xpos, xcharset in enumerate(map):
            for ypos, ychar in enumerate(xcharset):
                if char == ychar:
                    xcoord = xpos
                    ycoord = ypos
                    break

        pos = [xcoord, ycoord]

        # To do - add error handling if can't find the character

        return pos


### MAIN PROGRAM

# Given a remote map that looks like this...
remote_map = [
    ['a', 'b', 'c', 'd', 'e', '1', '2', '3'],
    ['f', 'g', 'h', 'i', 'j', '4', '5', '6'],
    ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],
    ['p', 'q', 'r', 's', 't', '.', '@', '0'],
    ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']
]

# ...how many moves are required to spell out the following?
word = 'chi'

# Make a class and submit the word and map
service = WordFinder()
count = service.calculate(remote_map, word)

# Print out the returned move count!
print("Total number of moves taken is: {}".format(count))