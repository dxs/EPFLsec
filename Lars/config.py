import ConfigParser
import json
import datetime  

class Config:
    file_name = r'./config.ini'
    mail_server_name = ''
    mail_name = ''

    server_list = []
    date_string = ''

    def __init__(self):
        self.read_config()
        self.set_date()

    def set_date(self):
        myDate = datetime.date.today() 
        t = datetime.datetime(myDate.year, myDate.month, myDate.day, 0, 0)
        self.date_string = t.strftime('%Y%m%d')

    def read_config(self):
        parser = ConfigParser.SafeConfigParser()
        parser.readfp(open(self.file_name, 'U'))
        self.mail_server_name = parser.get('EMAIL','SERVER')
        self.mail_name = parser.get('EMAIL','NAME')

        self.server_list = json.loads(parser.get("SERVER","LIST"))
        print(self.server_list[1])