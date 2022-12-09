import os.path
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(f"sqlite:///{os.getenv('project_dir')}/assets/data/bot.db", echo=True)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

Base = declarative_base()
from sqlalchemy import Sequence, ForeignKey, Column, Integer, String, DateTime, Boolean


class Anime(Base):
    __tablename__ = "anime"
    id = Column(Integer, Sequence("anime_id_seq"), primary_key=True)
    url = Column(String)
    title = Column(String)
    series_cnt = Column(Integer)
    films_cnt = Column(Integer)
    changed_at = Column(DateTime)

    def __repr__(self):
        return "<Anime(id='%s', url='%s', title='%s', series_cnt='%s', films_cnt='%s', changed_at= '%s')>" % (
            self.id,
            self.url,
            self.title,
            self.series_cnt,
            self.films_cnt,
            self.changed_at
        )


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(513))
    nickname = Column(String(32))
    muted_to = Column(DateTime)
    is_stopped = Column(Boolean)

    def __repr__(self):
        return "<User(id='%s', name='%s', nickname='%s', muted_to='%s', is_stopped='%s')>" % (
            self.id,
            self.name,
            self.nickname,
            self.muted_to,
            self.is_stopped
        )

class UserAnime(Base):
    __tablename__ = "user_anime"
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    anime_id = Column(Integer, ForeignKey("anime.id"), primary_key=True)
    reported_series_cnt = Column(Integer)

    def __repr__(self):
        return "<UserAnime(id='%s', name='%s', reported_series_cnt='%s')>" % (
            self.id,
            self.name,
            self.reported_series_cnt
        )

if __name__== "__main__":
    Base.metadata.create_all(engine)

# ed_user = User(name="ed", fullname="Ed Jones", nickname="edsnickname")
# ed_user.name
# 'ed'
# ed_user.nickname
# 'edsnickname'
# str(ed_user.id)
# 'None'