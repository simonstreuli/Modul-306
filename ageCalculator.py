from datetime import datetime
from dateutil.relativedelta import relativedelta
import sys


def validate_date(date_text):
    try:
        return datetime.strptime(date_text, '%d.%m.%Y')
    except ValueError:
        print("Fehler: Falsches Datumformat. Bitte in der Form dd.mm.yyyy eingeben.")
        sys.exit(1)


def calculate_age(birth_date):
    today = datetime.today()
    age_difference = relativedelta(today, birth_date)

    years = age_difference.years
    months = age_difference.months
    days = age_difference.days

    total_days = (today - birth_date).days

    return years, months, days, total_days


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Fehler: Bitte das Geburtsdatum in der Form dd.mm.yyyy eingeben.")
        sys.exit(1)

    # Geburtsdatum validieren und umwandeln
    birth_date = validate_date(sys.argv[1])

    # Alter berechnen
    years, months, days, total_days = calculate_age(birth_date)

    # Ausgabe
    print(
        f"Das Alter ist {years} Jahre {months} Monate und {days} Tage, das sind {total_days} Tage")
