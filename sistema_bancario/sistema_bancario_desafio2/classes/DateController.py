import datetime
class DateController():
    def registerMoment() -> datetime.datetime:
        return datetime.datetime.now()
    def formatedDate(moment = registerMoment()) -> str:
        dia = moment.day
        mes = moment.month
        ano = moment.year
        hora = moment.time()
        return f'{dia}/{mes}/{ano} às {hora}'
