from piece.type import Type
from piece.piece import Piece
from piece.color import Color
from piece.move_direction import MoveDirection


class Pawn(Piece):
    """ Class for Pawn chess piece. """

    def __init__(self, color):
        """
        Create a Pawn object

        :param color: Color
            Color that this piece should have.
        :return:
        """
        super().__init__(Type.pawn, color)
        self._moves[MoveDirection.forward] = 2
        self._moves[MoveDirection.f_right_diag] = 1
        self._moves[MoveDirection.f_left_diag] = 1
        self._string_value = 'P' if color == Color.white else 'p'

    @property
    def has_moved(self):
        return super().has_moved

    @Piece.has_moved.setter
    def has_moved(self, moved):
        """
        Extends super class version. Changes the moves structure after piece has moved.

        :param moved: bool
            True if the piece has moved, False otherwise.
        :return:
        """
        Piece.has_moved.fset(self, moved)
        self._moves[MoveDirection.forward] = 1



