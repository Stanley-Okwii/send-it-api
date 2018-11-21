
class Config:
    """
    Base configuration
    """
    DEBUG = False

class DevelopmentConfig(Config):
    """
    Development configuration
    """
    DEBUG = True
    DATABASE_URL="postgresql://stanley:abracadabra@localhost/sendit"



class TestingConfig(Config):
    """
    Testing configuration
    """
    DEBUG = True
    DATABASE_URL="postgresql://stanley:abracadabra@localhost/sendit_test"


class ProductionConfig(Config):
    """
    Production configuration
    """
    DEBUG = True
    DATABASE_URL="postgres://hfwrtyjqlsqsvr:6646ac58269bd3319912b99108680df5fc979ee71c87752442d396de9f057ffc@ec2-54-163-230-178.compute-1.amazonaws.com:5432/dacuphvi0nn8fa"
