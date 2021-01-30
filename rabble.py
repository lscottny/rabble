from random import randint

POINTS_BY_LETTER = {'': 0,'a': 1,'b': 3,'c': 3,'d': 2,'e': 1,'f': 4,'h': 4,'i': 1,'j':8,'k':5,'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,'v':4,'w':4,'x':8,'y':4,'z':10}
LETTER_MULTIPLIERS = [
    [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
    [1, 1, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1],
    [2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1],
    [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
    [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
    [1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2],
    [1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 1, 1],
    [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
]
WORD_MULTIPLIERS = [
    [3, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 3],
    [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 3],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
    [3, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 3],
]

LETTER_DISTRIBUTION = ['k','j','x','q','z','b','b','c','c','m','m','p','p','f','f','h','h','v','v','w','w','y','y','g','g','g','l','l','l','l','s','s','s','s','u','u','u','u','d','d','d','d','n','n','n','n','n','n','r','r','r','r','r','r','t','t','t','t','t','t','o','o','o','o','o','o','o','o','a','a','a','a','a','a','a','a','a','i','i','i','i','i','i','i','i','i','e','e','e','e','e','e','e','e','e','e','e','e','','']


class Game:
    def __init__(self,players):
        self.letter_bag = LETTER_DISTRIBUTION
        self.board = 15 * [15 * [None]]

        self.players = players
        self.player_scores = []
        self.current_player = randint(0, len(self.players) - 1)

        self.player_letters = []
     

        self.distributeLetters()
        
        

    def distributeLetters(self):
        for i in range(len(self.players)):
            
            current_letters = []
            for j in range(7):
                index = randint(0,len(self.letter_bag)-1)
                letter = self.letter_bag[index]
                current_letters += [letter]
                self.letter_bag.remove(letter)
            self.player_letters += [current_letters]

    def validate_move(self):
        #INPUT: word, position, orientation, blanks
        # TODO(Scott): Implement this properly. 1) will it fit on the board
        # 2) will it cover other letters?
        # 3) is it using letters the user has?
        # 4) Is it a valid scrabble word?
        # 5) If it adds additional words are they valid scr words?
        return True


    def score_move(self, word, position, is_horizontal, blank_indices):
        # TODO(Scott): Implement this to score a player's move
        # first validate & score original move
        # then validate & score extra words

        # use position adn orientation and length!!
        cells = []
        if is_horizontal:
            for i in range(len(word)):
                cells += [[position[0] + i, position[1]]]
        else:
            for i in range(len(word)):
                cells += [[position[0], position[1] + i]]
        word_mults = []
        score = 0
        for cell_index in range(len(cells)):
            cell = cells[cell_index]
            letter_mult = LETTER_MULTIPLIERS[cell[0]][cell[1]]
            word_mult = WORD_MULTIPLIERS[cell[0]][cell[1]]
            letter_points = POINTS_BY_LETTER[word[cell_index]]
            word_mults += [word_mult]
            score += letter_points * letter_mult
        print(word_mults)
        for multiplier in word_mults:
            score *= multiplier
        # list of cells the word covers
        # get point value for each letter
        # 
     
        return score

        
    def update_board(self):
        # TODO(Scott): Implement this to update the model of the board with the new move
        return True

    def update_players_letters(self):
        # TODO(Scott): Implement this properly. Remove used letters. Randomly assign new letters.
        # blank space
        return True


  

class ScrabblePlayer:
    def __init__(self):
        self.letters = []
        self.score = 0
        self.turnorder = 0
        self.df


scrab = Game(['Scott','Nick','Nathan','Milo'])


scrab.player_letters = [[]]

def test_scoring():
    new_game = Game(['Sam', 'Susan', 'Sharon'])

    new_game.player_letters = [
        ['a', 'e', 'i', 'p', 't', 'k', 's'],
        ['m', 'n', 'e', 'i', 'k', 't', 'w'],
        ['l', 'r', 'h', 'f', 'a', 'u', 'o'],
    ]
    new_game.current_player = 0

    word = 'spit'
    position = (7, 7)
    is_horizontal = False
    blank_indices = []

    score = new_game.score_move('skit', (7, 7), is_horizontal=True, blank_indices=[])
    assert score == 16

    score = new_game.score_move('spit', (7, 7), is_horizontal=False, blank_indices=[])
    assert score == 12
