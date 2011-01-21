from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from sqlalchemy import engine_from_config

from tictactoe.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    my_session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    config = Configurator(settings=settings, session_factory=my_session_factory)
    config.add_static_view('static', 'tictactoe:static')
    config.add_route('home', '/', view='tictactoe.views.my_view',
                     view_renderer='templates/mytemplate.pt')
    return config.make_wsgi_app()


