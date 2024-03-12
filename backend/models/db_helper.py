from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from backend.settings import db_url


class DatabaseHelper:
    def __init__(self) -> None:
        self.engine = create_async_engine(
            url=db_url,
            echo=True,
        )
        self.session_maker = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            autoflush=False,
            expire_on_commit=False,
        )
    
    async def get_session(self) -> AsyncSession:
        async with self.session_maker() as session:
            yield session



db_helper = DatabaseHelper()