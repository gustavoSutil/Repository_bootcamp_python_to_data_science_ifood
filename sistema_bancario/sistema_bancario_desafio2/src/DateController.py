import datetime
class DateController:
    def now():
        moment = datetime.datetime.now()
        dia = moment.day
        mes = moment.month
        ano = moment.year
        hora = moment.time()
        return f'{dia}/{mes}/{ano} às {hora}'