# Use the xample of 'Chi' name to test
# Santise the input - convert to lowercase, check for non-existant characters

# Define a method that breaks the word up into a list of characters

# Define a method that iterates through the word list and counts the moves for each letter in order

# x Define a method that calculates the number of moves from position a to b

# TODO:
# x Define the data model as a two-dimensional array (using a dictionary and lists)

# x Define a class, set instance variables including a cursor from 0,0 (x,y) and the word

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

        # add one for hitting 'OK' on the remote
        print('adding 1 to hit that OK button...')
        total_moves += 1 

        return total_moves

    def calculate_moves(self, startchar, targetcharacter):

        print("looking for {} to {}".format(startchar, targetcharacter))
        start_pos = self.calculate_char_pos(startchar)
        target_pos = self.calculate_char_pos(targetcharacter)

        xmoves = abs(start_pos[0]-target_pos[0])
        ymoves = abs(start_pos[1]-target_pos[1])

        moves = xmoves + ymoves
        # add the lateral and longitudinal moves

        result = {
            'moves' : moves,
            'endpos' : target_pos
        }

        print(moves)

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

remote_map = [
    ['a', 'b', 'c', 'd', 'e', '1', '2', '3'],
    ['f', 'g', 'h', 'i', 'j', '4', '5', '6'],
    ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],
    ['p', 'q', 'r', 's', 't', '.', '@', '0'],
    ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']
]

word = 'jamie'

service = WordFinder()
count = service.calculate(remote_map, word)

print("Total number of moves taken is: {}".format(count))