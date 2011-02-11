import random
from string import letters

import transaction
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy import String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from zope.sqlalchemy import ZopeTransactionExtension


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    board_state = Column(Unicode(255))
    move = Column(Integer)
    game_hash = Column(String(10), unique = True)

    @property
    def board(self):
        return [x.split('-') for x in self.board_state.split('|')]

    @board.setter
    def board(self, board):
        self.board_state = "|".join("-".join(row) for row in board)

    def __init__(self, game_hash=None, move="X", board=None):
        if not game_hash:
            game_hash = ''.join([random.choice(letters) for x in range(10)])
        if board is None:
            board = [['', '', ''],
                     ['', '', ''],
                     ['', '', '']]
        self.move = move
        self.board = board
        self.game_hash = game_hash


def populate():
    session = DBSession()

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    try:
        populate()
    except IntegrityError:
        DBSession.rollback()
