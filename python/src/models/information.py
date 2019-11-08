import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, DateTime
from settings import Base, DATABASE_ENGINE

class Information(Base):
    """
    Information model
    """
    __tablename__ = 'informations'
    id = Column('id', 
                Integer, 
                primary_key=True, 
                autoincrement=True, 
                nullable=False
        )
    x = Column('x',
               Float,
               nullable=False
        )
    y = Column('y',
               Float,
               nullable=False
        )
    image_url = Column('image_url',
                       String(200),
                       nullable=False
                )
    info = Column('info',
                  String(200),
                  nullable=False
    )

def main(args):
    Base.metadata.create_all(bind=DATABASE_ENGINE)

if __name__ == '__main__':
    main(sys.argv)
