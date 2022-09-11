class Config:
    DEBUG = True

    # gives the connection string to the DB hosted as container on docker
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://smilecook:smilecook@192.168.178.10:5432/smilecook"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "TheSecret"
    JWT_ERROR_MESSAGE_KEY = "message"
