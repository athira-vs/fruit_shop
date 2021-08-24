#fruit_dict = {}
cart = {}

fruit_obj_lst = []
class Fruits:
    def __init__(self, f_id, name, rate, import_from, import_date, buy_price):
        self.f_id = f_id
        self.name = name
        self.rate = rate
        self.import_from = import_from
        self.import_date = import_date
        self.buy_price = buy_price

    def set_f_id(self,f_id):
    	self.f_id = f_id

    def set_name(self, name):
    	self.name = name

    def set_rate(self, rate):
    	self.rate = rate

    def set_import_from(self, import_from):
    	self.import_from = import_from

    def set_import_date(self, import_date):
    	self.import_date = import_date

    def set_buy_price(self, buy_price):
    	self.buy_price = buy_price



