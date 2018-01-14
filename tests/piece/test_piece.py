import unittest
from piece.King import King
from piece.Pawn import Pawn
from piece.Queen import Queen
from piece.Bishop import Bishop
from piece.Knight import Knight
from piece.Rook import Rook
from piece.MoveDirection import MoveDirection
from piece.Color import Color
from piece.Type import Type


class PieceTest(unittest.TestCase):
    """
    Test piece attributes
    """

    def setUp(self):
        self.types = {
            Type.pawn: Pawn,
            Type.bishop: Bishop,
            Type.king: King,
            Type.knight: Knight,
            Type.queen: Queen,
            Type.rook: Rook
        }

    def test_create(self):
        """
        Test the creation of pieces and the states
        :return:
        """
        for t, piece_class in self.types.items():
            with self.subTest(t):
                piece = piece_class(Color.white)
                self.assertEqual(Color.white, piece.color, 'Color was not set correctly')
                self.assertEqual(t, piece.type, 'Piece type does not match')

    def test_capture(self):
        """
        Test capture property
        :return:
        """
        for t, piece_class in self.types.items():
            with self.subTest(t):
                piece = piece_class(Color.white)
                self.assertFalse(piece.capture, 'Piece should not be captured')

                piece.capture = True
                self.assertTrue(piece.capture, 'Piece should not be captured')

    def test_has_moved(self):
        """
        Test has_moved property
        :return:
        """
        for t, piece_class in self.types.items():
            with self.subTest(t):
                piece = piece_class(Color.white)
                self.assertFalse(piece.has_moved, 'Piece has not moved')

                piece.has_moved = True
                self.assertTrue(piece.has_moved, 'Piece has moved')

    def test_move_directions(self):
        """
        Test move directions per piece
        :return:
        """
        piece_directions = {
            Type.pawn: {MoveDirection.forward: 2,
                        MoveDirection.f_right_diag: 1,
                        MoveDirection.f_left_diag: 1},
            Type.bishop: {MoveDirection.f_left_diag: -1,
                          MoveDirection.f_right_diag: -1,
                          MoveDirection.b_right_diag: -1,
                          MoveDirection.b_left_diag: -1},
            Type.king: {MoveDirection.forward: 1,
                        MoveDirection.f_right_diag: 1,
                        MoveDirection.right: 2,
                        MoveDirection.b_right_diag: 1,
                        MoveDirection.backward: 1,
                        MoveDirection.b_left_diag: 1,
                        MoveDirection.left: 2,
                        MoveDirection.f_left_diag: 1},
            Type.knight: {MoveDirection.l_shape: True},
            Type.queen: {MoveDirection.forward: -1,
                         MoveDirection.f_right_diag: -1,
                         MoveDirection.right: -1,
                         MoveDirection.b_right_diag: -1,
                         MoveDirection.backward: -1,
                         MoveDirection.b_left_diag: -1,
                         MoveDirection.left: -1,
                         MoveDirection.f_left_diag: -1},
            Type.rook: {MoveDirection.forward: -1,
                        MoveDirection.right: -1,
                        MoveDirection.backward: -1,
                        MoveDirection.left: -1}
        }
        for t, piece_class in self.types.items():
            with self.subTest(t):
                piece = piece_class(Color.white)
                directions = piece.move_directions
                self.assertDictEqual(piece_directions[t], directions, 'Directions dont match expected')

    def test_pawn_movement_adjusted_after_moving(self):
        """
        Test a pawn cannot move forward two squares once it has moved.
        :return:
        """
        expected_directions = {
            MoveDirection.forward: 1,
            MoveDirection.f_right_diag: 1,
            MoveDirection.f_left_diag: 1
        }
        for color in [Color.black, Color.white]:
            pawn = Pawn(color)
            pawn.has_moved = True

            self.assertDictEqual(expected_directions, pawn.move_directions, 'Directions do not match expected')

    def test_king_movement_adjusted_after_moving(self):
        """
        Test a king cannot move left or right two squares once it has moved.
        :return:
        """
        expected_directions = {
            MoveDirection.forward: 1,
            MoveDirection.f_right_diag: 1,
            MoveDirection.right: 1,
            MoveDirection.b_right_diag: 1,
            MoveDirection.backward: 1,
            MoveDirection.b_left_diag: 1,
            MoveDirection.left: 1,
            MoveDirection.f_left_diag: 1
        }
        for color in [Color.black, Color.white]:
            king = King(color)
            king.has_moved = True

            self.assertDictEqual(expected_directions, king.move_directions, 'Directions do not match expected')


if __name__ == '__main__':
    unittest.main()