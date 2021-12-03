
class Config(object):
    MERCHANT_ID='bghrebe563458'


class ProductionConfig(Config):
    MERCHANT_ID='&^GYG4dyyrw'
    DATABASE_URI=''
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USERNAME='aroyehunsegun20201@gmail.com'
    MAIL_PASSWORD='SHUTdown1991!'
    MAIL_USE_SSL=True

class DevelopmentConfig(Config):
    MERCHANT_ID='hjerebge'
    DATABASE_URI=''


class LiveConfig(Config):
    SECRET_KEY='Hz_Vjdkjdsdsd'
   
















