registry = dict(version=0)
def bind():
    from cPickle import loads as _loads
    _lookup_attr = _loads('cchameleon.core.codegen\nlookup_attr\np1\n.')
    _init_scope = _loads('cchameleon.core.utils\necontext\np1\n.')
    _re_amp = _loads("cre\n_compile\np1\n(S'&(?!([A-Za-z]+|#[0-9]+);)'\np2\nI0\ntRp3\n.")
    _attrs_167426764 = _loads('(dp1\n.')
    _attrs_167426316 = _loads('(dp1\n.')
    _attrs_167427788 = _loads('(dp1\nVhref\np2\nV/\ns.')
    _attrs_167424524 = _loads('(dp1\n.')
    _attrs_167427052 = _loads('(dp1\n.')
    _attrs_167425836 = _loads('(dp1\n.')
    _init_stream = _loads('cchameleon.core.generation\ninitialize_stream\np1\n.')
    _attrs_167426508 = _loads('(dp1\nVid\np2\nVboard\np3\ns.')
    _attrs_167424300 = _loads('(dp1\n.')
    _init_default = _loads('cchameleon.core.generation\ninitialize_default\np1\n.')
    _attrs_167425068 = _loads('(dp1\n.')
    _attrs_167426956 = _loads('(dp1\n.')
    _attrs_167424812 = _loads('(dp1\n.')
    _attrs_167425260 = _loads('(dp1\n.')
    _init_tal = _loads('cchameleon.core.generation\ninitialize_tal\np1\n.')
    _attrs_167427372 = _loads('(dp1\nVhref\np2\nV?row=${repeat.row.number}&col=${repeat.cell.number}\np3\ns.')
    def render(econtext, rcontext=None):
        macros = econtext.get('macros')
        _translate = econtext.get('_translate')
        _slots = econtext.get('_slots')
        target_language = econtext.get('target_language')
        u'_init_stream()'
        (_out, _write, ) = _init_stream()
        u'_init_tal()'
        (_attributes, repeat, ) = _init_tal()
        u'_init_default()'
        _default = _init_default()
        u'None'
        default = None
        u'None'
        _domain = None
        _write('<!DOCTYPE html>\n')
        attrs = _attrs_167424300
        _write(u'<html>\n  ')
        attrs = _attrs_167424524
        _write(u'<head>\n    ')
        attrs = _attrs_167424812
        _write(u'<title>Tic! Tac!  And even Toe!</title>\n    ')
        attrs = _attrs_167425068
        _write(u'<style>\n      #board {\n        border-collapse: collapse;\n      }\n      #board td {\n        width: 10em;\n        height: 10em;\n        border: 1px solid black;\n        text-align: center;\n      }\n      #board td a:hover {\n        background-color: #668800;\n      }\n      #board td a {\n        width: 2em;\n        height: 2em;\n        display: block;\n        font-size: 5em;\n        text-decoration: none;\n        line-height: 2em;\n      }\n    </style>\n  </head>\n  ')
        attrs = _attrs_167425260
        u'winner'
        _write(u'<body>\n    ')
        _tmp1 = econtext['winner']
        if _tmp1:
            pass
            _write(u'')
            attrs = _attrs_167425836
            u'winner'
            _write(u'<p>')
            _tmp1 = econtext['winner']
            _tmp = _tmp1
            if (_tmp.__class__ not in (str, unicode, int, float, )):
                try:
                    _tmp = _tmp.__html__
                except:
                    _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
                else:
                    _tmp = _tmp()
                    _write(_tmp)
                    _tmp = None
            if (_tmp is not None):
                if not isinstance(_tmp, unicode):
                    _tmp = str(_tmp)
                if ('&' in _tmp):
                    if (';' in _tmp):
                        _tmp = _re_amp.sub('&amp;', _tmp)
                    else:
                        _tmp = _tmp.replace('&', '&amp;')
                if ('<' in _tmp):
                    _tmp = _tmp.replace('<', '&lt;')
                if ('>' in _tmp):
                    _tmp = _tmp.replace('>', '&gt;')
                _write(_tmp)
            _write(u' wins.</p>\n    ')
        u'not winner'
        _write(u'\n    ')
        _tmp1 = not econtext['winner']
        if _tmp1:
            pass
            _write(u'\n      ')
            attrs = _attrs_167426316
            u'player'
            _write(u'<p>Your move ')
            _tmp1 = econtext['player']
            _tmp = _tmp1
            if (_tmp.__class__ not in (str, unicode, int, float, )):
                try:
                    _tmp = _tmp.__html__
                except:
                    _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
                else:
                    _tmp = _tmp()
                    _write(_tmp)
                    _tmp = None
            if (_tmp is not None):
                if not isinstance(_tmp, unicode):
                    _tmp = str(_tmp)
                if ('&' in _tmp):
                    if (';' in _tmp):
                        _tmp = _re_amp.sub('&amp;', _tmp)
                    else:
                        _tmp = _tmp.replace('&', '&amp;')
                if ('<' in _tmp):
                    _tmp = _tmp.replace('<', '&lt;')
                if ('>' in _tmp):
                    _tmp = _tmp.replace('>', '&gt;')
                _write(_tmp)
            _write(u'.</p>\n    ')
        _write(u'\n    ')
        attrs = _attrs_167426508
        u'board'
        _write(u'<table id="board">\n      ')
        _tmp1 = econtext['board']
        row = None
        (_tmp1, _tmp2, ) = repeat.insert('row', _tmp1)
        for row in _tmp1:
            _tmp2 = (_tmp2 - 1)
            attrs = _attrs_167426764
            u'row'
            _write(u'<tr>\n        ')
            _tmp3 = row
            cell = None
            (_tmp3, _tmp4, ) = repeat.insert('cell', _tmp3)
            for cell in _tmp3:
                _tmp4 = (_tmp4 - 1)
                attrs = _attrs_167427052
                _write(u'<td>')
                attrs = _attrs_167427372
                "join(u'?row=', value('repeat.row.number'), u'&col=', value('repeat.cell.number'))"
                _write(u'<a')
                _tmp5 = ('%s%s%s%s' % (u'?row=', _lookup_attr(repeat.row, 'number'), u'&col=', _lookup_attr(repeat.cell, 'number'), ))
                if (_tmp5 is _default):
                    _tmp5 = u'?row=${repeat.row.number}&col=${repeat.cell.number}'
                if ((_tmp5 is not None) and (_tmp5 is not False)):
                    if (_tmp5.__class__ not in (str, unicode, int, float, )):
                        _tmp5 = unicode(_translate(_tmp5, domain=_domain, mapping=None, target_language=target_language, default=None))
                    else:
                        if not isinstance(_tmp5, unicode):
                            _tmp5 = str(_tmp5)
                    if ('&' in _tmp5):
                        if (';' in _tmp5):
                            _tmp5 = _re_amp.sub('&amp;', _tmp5)
                        else:
                            _tmp5 = _tmp5.replace('&', '&amp;')
                    if ('<' in _tmp5):
                        _tmp5 = _tmp5.replace('<', '&lt;')
                    if ('>' in _tmp5):
                        _tmp5 = _tmp5.replace('>', '&gt;')
                    if ('"' in _tmp5):
                        _tmp5 = _tmp5.replace('"', '&quot;')
                    _write(((' href="' + _tmp5) + '"'))
                u'cell'
                _write('>')
                _tmp5 = cell
                _tmp = _tmp5
                if (_tmp.__class__ not in (str, unicode, int, float, )):
                    try:
                        _tmp = _tmp.__html__
                    except:
                        _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
                    else:
                        _tmp = _tmp()
                        _write(_tmp)
                        _tmp = None
                if (_tmp is not None):
                    if not isinstance(_tmp, unicode):
                        _tmp = str(_tmp)
                    if ('&' in _tmp):
                        if (';' in _tmp):
                            _tmp = _re_amp.sub('&amp;', _tmp)
                        else:
                            _tmp = _tmp.replace('&', '&amp;')
                    if ('<' in _tmp):
                        _tmp = _tmp.replace('<', '&lt;')
                    if ('>' in _tmp):
                        _tmp = _tmp.replace('>', '&gt;')
                    _write(_tmp)
                _write(u'</a></td>')
                if (_tmp4 == 0):
                    break
                _write(' ')
            _write(u'\n      </tr>')
            if (_tmp2 == 0):
                break
            _write(' ')
        _write(u'\n    </table>\n    ')
        attrs = _attrs_167426956
        _write(u'<p>')
        attrs = _attrs_167427788
        _write(u'<a href="/">New game</a></p>\n  </body>\n</html>')
        return _out.getvalue()
    return render

__filename__ = '/home/ignas/src/dojo/tictactoe/tictactoe/tictactoe/templates/mytemplate.pt'
registry[(None, True, '1488bdb950901f8f258549439ef6661a49aae984')] = bind()
