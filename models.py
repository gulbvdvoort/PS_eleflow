from db import Base
from sqlalchemy import Column, Float, Integer, DateTime

class DadoClP(Base):
    """
    Modelo dos dados do CLP
    """
    __tablename__ = 'dadoCLP'
    id =  Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime)
    temperatura_ar = Column(Float) 
    velocidade_ar = Column(Float)
    vazao_ar = Column(Float)
    rotacao_motor = Column(Float)
    temperatura_s1 = Column(Float)
    temperatura_s2 = Column(Float)
    pressao_s1 = Column(Float)
    pressao_s2 = Column(Float)
    pressao_s3 = Column(Float)
    frequencia_scroll = Column(Float)
