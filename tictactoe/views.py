
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

    if (not request.session.has_key('game')
        or not request.params):
        request.session['move'] = 'X'
        request.session['game'] = [['', '', ''],
                                   ['', '', ''],
                                   ['', '', '']]

    board = request.session['game']
    if request.params.get('row') and request.params.get('col'):
        row = int(request.params.get('row')) - 1
        col = int(request.params.get('col')) - 1
        if not board[row][col]:
            board[row][col] = request.session['move']
            if request.session['move'] == 'X':
                request.session['move'] = 'O'
            else:
                request.session['move'] = 'X'

    winner = get_winner(board)

    return {'board': request.session['game'],
            'winner': winner,
            'player': request.session['move']}

