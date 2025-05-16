from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///db/lernario.db", echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()