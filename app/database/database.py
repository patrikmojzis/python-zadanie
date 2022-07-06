from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import db_config

async def db_context(app):
    engine = create_engine(f'postgresql://{db_config.user}:{db_config.password}@{db_config.host}:{db_config.port}/{db_config.database}')
    session = sessionmaker(bind=engine)
    app['db'] = session()

    yield

    app['db'].close()

def setup_database(app):
    app.cleanup_ctx.append(db_context)