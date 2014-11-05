import ConfigParser


config = ConfigParser.ConfigParser()
config.readfp(open('../conf/db.ini'))
print config.get("global", "host")