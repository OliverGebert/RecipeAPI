class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://smilecook:smilecook@192.168.178.10:5432/smilecook"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
