import datetime
class DateController():
    def __init__(self):
        self.date = datetime.datetime.now()
    def registerMoment(self) -> datetime.datetime:
        DateController()
        return self.date
    def formatedDate(self) -> str:
        moment = DateController()
        dia = moment.date.day
        mes = moment.date.month
        ano = moment.date.year
        hora = moment.date.time()
        return f'{dia}/{mes}/{ano} às {hora}'
