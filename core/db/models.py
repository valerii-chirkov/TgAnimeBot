from sqlalchemy import Column, Integer, String, DateTime, func

from core.db.database import Base


class UserData(Base):
    __tablename__ = "user_data"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    date_joined = Column(DateTime(timezone=True), server_default=func.now())
