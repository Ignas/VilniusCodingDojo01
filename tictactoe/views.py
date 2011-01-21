
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

    return {'board': request.session['game'],}

