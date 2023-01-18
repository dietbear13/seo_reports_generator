import calendar
import datetime
import pymorphy2

### СТАВИМ ПРОГНОЗ ТРАФИКА НА МЕСЯЦ
trafic_forecast = '220230'
trafic_forecast_2 = '67907'
trafic_forecast_3 = '72797'


### СТАВИМ ФАКТИЧЕСКИЙ ТРАФИК ЗА ЭТОТ МЕСЯЦ БЕЗ СЕГОДНЯШНЕГО ДНЯ
trafic_fact = '96499'  # для первого отчёта
trafic_fact_2 = '25490'  # для второго отчёта
trafic_fact_3 = '17747'  # для третьего отчёта


### ВВОДНЫЕ ДАННЫЕ И РАСЧЁТЫ
dateTodayNumber = int(datetime.date.today().strftime("%d"))
last_month_number = dateTodayNumber - 1
percentOfExpectation = float(f"{(int(trafic_fact) / int(trafic_forecast) * 100)}")
percentOfExpectation2 = float(f"{(int(trafic_fact_2) / int(trafic_forecast_2) * 100)}")
percentOfExpectation3 = float(f"{(int(trafic_fact_3) / int(trafic_forecast_3) * 100)}")
now = datetime.datetime.now()
dayWithoutToday = calendar.monthrange(now.year, now.month)[1]
expectation = int(trafic_fact) * int(dayWithoutToday) / (dateTodayNumber - 1)
expectation2 = int(trafic_fact_2) * int(dayWithoutToday) / (dateTodayNumber - 1)
expectation3 = int(trafic_fact_3) * int(dayWithoutToday) / (dateTodayNumber - 1)
mouthNumber = str(datetime.date.today().strftime("%m"))

monthTable = {
    '01': 'январь',
    '02': 'февраль',
    '03': 'март',
    '04': 'апрель',
    '05': 'май',
    '06': 'июнь',
    '07': 'юиль',
    '08': 'август',
    '09': 'сентябрь',
    '10': 'октябрь',
    '11': 'ноябрь',
    '12': 'декабрь',
}

### ПРОВЕРЯЕМ ЕСТЬ ЛИ ТЕКУЩИЙ МЕСЯЦ В СЛОВАРЕ
checkKey = mouthNumber in monthTable
if mouthNumber in monthTable:
    month = monthTable[mouthNumber]

check_last_month = last_month_number in monthTable
if mouthNumber in monthTable:
    month = monthTable[mouthNumber]

### СТАВИМ МЕСЯЦ В 3 ПАДЕЖА
morph = pymorphy2.MorphAnalyzer()
p = morph.parse(month)[0]
monthNomn = p.inflect({"nomn"}).word
monthGent = p.inflect({"gent"}).word
monthLoc2 = p.inflect({"loc2"}).word


### ОФОРМЛЯЕМ СТИЛИ ФОРМАТИРОВАНИЯ ТЕКСТА — при копировании не переносятся!
class Style:
    BOLD = '\033[1m'
    END = '\033[0m'


def print_report():
    report_petel = '''
непересчитанный прогноз естественного трафика на {monthNomn} — {traficForecast}. 
{bold}выполнено на {date} {monthGent} — {traficFact} ({percent}%{end} от непересчитанного реалистичного). 
В {monthLoc2} 2019 — 79 809, {monthLoc2} 2020 — 147 677, 
{monthLoc2} 2021 — 279 823, 
{bold}ожидание на {monthNomn} — {total} ({toatalPercent}%{end} от непересчитанного естественного прогноза).
'''.format(
        traficForecast=trafic_forecast,
        date=dateTodayNumber,
        traficFact=trafic_fact,
        percent=round(percentOfExpectation, 1),
        total=round(expectation),
        toatalPercent=round(int(round(expectation)) / int(trafic_forecast) * 100, 1),
        bold=Style.BOLD,
        end=Style.END,
        monthNomn=monthNomn,
        monthGent=monthGent,
        monthLoc2=monthLoc2
    )

    report_pava = '''
непересчитанный прогноз естественного трафика на {monthNomn} — {traficForecast}. 
{bold}выполнено на {date} {monthGent} — {traficFact} ({percent}%{end} от непересчитанного реалистичного). 
В {monthLoc2} 2019 — 115, {monthLoc2} 2020 — 2 522, 
{monthLoc2} 2021 — 8 685, 
{bold}ожидание на {monthNomn} — {total} ({toatalPercent}%{end} от непересчитанного естественного прогноза).
'''.format(
        traficForecast=trafic_forecast_2,
        date=dateTodayNumber,
        traficFact=trafic_fact_2,
        percent=round(percentOfExpectation2, 1),
        total=round(expectation2),
        toatalPercent=round(int(round(expectation2)) / int(trafic_forecast_2) * 100, 1),
        bold=Style.BOLD,
        end=Style.END,
        monthNomn=monthNomn,
        monthGent=monthGent,
        monthLoc2=monthLoc2
    )

    report_altaibroiler = '''
непересчитанный прогноз естественного трафика на {monthNomn} — {traficForecast}. 
{bold}выполнено на {date} {monthGent} — {traficFact} ({percent}%{end} от непересчитанного реалистичного). 
В {monthLoc2} 2019 — 382, {monthLoc2} 2020 — 1 485, 
{monthLoc2} 2021 — 36 416, 
{bold}ожидание на {monthNomn} — {total} ({toatalPercent}%{end} от непересчитанного естественного прогноза).
'''.format(
        traficForecast=trafic_forecast_3,
        date=dateTodayNumber,
        traficFact=trafic_fact_3,
        percent=round(percentOfExpectation3, 1),
        total=round(expectation3),
        toatalPercent=round(int(round(expectation3)) / int(trafic_forecast_3) * 100, 1),
        bold=Style.BOLD,
        end=Style.END,
        monthNomn=monthNomn,
        monthGent=monthGent,
        monthLoc2=monthLoc2
    )

    print(report_petel, report_pava, report_altaibroiler)


if __name__ == "__main__":
    print_report()
