import transaction

from tictactoe.models import DBSession, Game

def get_winner(board):
    diagonal1 = [board[i][i] for i in range(3)]
    diagonal2 = [board[2-i][i] for i in range(3)]
    for brd in [board, zip(*board), [diagonal1, diagonal2]]:
        for row in brd:
            r = ''.join(row)
            if r == 'OOO':
                return 'O'
            elif r == 'XXX':
                return 'X'
    return None


def my_view(request):
    dbsession = DBSession()

    game_hash = None
    if "game_hash" not in request.params:
        game = Game()
        dbsession.add(game)
    else:
        game_hash = request.params.get('game_hash')
        game = dbsession.query(Game).filter_by(game_hash=game_hash).one()

    board = game.board
    winner = get_winner(board)

    if not winner and request.params.get('row') and request.params.get('col'):
        row = int(request.params.get('row')) - 1
        col = int(request.params.get('col')) - 1
        if not board[row][col]:
            board[row][col] = game.move
            if game.move == 'X':
                game.move = 'O'
            else:
                game.move = 'X'
            game.board = board

    winner = get_winner(board)

    return {'board': game.board,
            'winner': winner,
            'player': game.move,
            'game_hash': game.game_hash}

