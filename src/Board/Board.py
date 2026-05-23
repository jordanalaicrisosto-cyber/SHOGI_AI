from Pieces import Piece, Pawn, Bishop, GoldGeneral, King, Knight, Lance, Pawn, Rook, SilverGeneral

"""Class that represent the board of the shogi game"""
class Board :
    def init(self) :
        self.board = [[] for i in range(9)]

        for i in range(9) :
            self.board[2][i] = Pawn()
            self.board[6][i] = Pawn()

        self.board[1][1] = Bishop()
        self.board[7][7] = Bishop()

        self.board[1][7] = Rook()
        self.board[7][1] = Rook()

        self.board[0][0] = Lance()
        self.board[0][1] = Knight()
        self.board[0][2] = SilverGeneral()
        self.board[0][3] = GoldGeneral()
        self.board[0][4] = King()
        self.board[0][5] = GoldGeneral()
        self.board[0][6] = SilverGeneral()
        self.board[0][7] = Knight()
        self.board[0][8] = Lance()

        self.board[8][0] = Lance()
        self.board[8][1] = Knight()
        self.board[8][2] = SilverGeneral()
        self.board[8][3] = GoldGeneral()
        self.board[8][4] = King()
        self.board[8][5] = GoldGeneral()
        self.board[8][6] = SilverGeneral()
        self.board[8][7] = Knight()
        self.board[8][8] = Lance()
