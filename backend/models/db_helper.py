from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from backend.settings import db_url

class DatabaseHelper:
    def __init__(self) -> None:
        self.engine = create_async_engine(
            url=db_url,
            echo=True,
        )
        self.session_maker = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
        )

db_helper = DatabaseHelper()