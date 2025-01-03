from datetime import datetime, timedelta

def add_week_to_dates(dates: list[str]) -> list[str]:
    output_dates = []
    for date in dates:
        date_obj = datetime.strptime(date, '%Y.%m.%d')
        new_date_obj = date_obj + timedelta(days=7)
        output_dates.append(new_date_obj.strftime('%B %#d, %Y'))
    return output_dates
