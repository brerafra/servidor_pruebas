from dotenv import load_dotenv
import dotenv
import os

#Cargamos el archvio con las variables de ambiente, verificando que exista
dotenv_file_path=os.path.join(os.path.dirname(__file__),'.env')

if os.path.exists(dotenv_file_path):
    load_dotenv(dotenv_file_path)

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV ="development"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:demosprosa#1@localhost:3306/dog"

class ProductionConfig(Config):
    pass

