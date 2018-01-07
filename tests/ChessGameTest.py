import unittest
from game.ChessGame import ChessGame

class ChessGameTest(unittest.TestCase):

    def test_current_player(self):
        """
        Move a piece as one player.
        Expected result is opposite colored player is the current player.
        :return:
        """
        pass

    def test_is_game_over(self):
        """
        Test if game is over.
        Expected result is game is over when there is a winner or draw
        :return:
        """
        pass

    def test_get_game_results(self):
        """
        Test game reports correct results.
        Game should inform who the game state and winner if there is one
        :return:
        """
        pass
        # Game state should be Constant from Game Class?
        # Win, draw, In progress
        # if there is a win condition, check for winner. Should be player object?

    def test_move_piece_to_invalid_position(self):
        """
        Test moving a piece to an invalid position.
        Expected result is an exception is thrown
        :return:
        """
        pass
        # Game should not allow pieces to be moved to invalid locations

    def test_move_piece_to_valid_position(self):
        """
        Move a piece to a valid position on board.
        Expected result is piece was moved and object returned indicating what happened on board
        :return:
        """
        pass

    def test_invalid_algebraic_positions(self):
        """
        Test providing invalid algebraic notation for every method that expects it
        Expected result is exception is thrown
        :return:
        """
        pass