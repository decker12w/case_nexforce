from datetime import datetime, timedelta, time

def calculate_end_datetime(start_date: datetime | str, duration: time | str) -> datetime:
    """
    Calcula a data/hora final adicionando a duração à data/hora de início.

    Args:
        start_date (datetime | str): Data/hora de início. Se for uma string, deve estar no formato "%Y-%m-%d %H:%M:%S".
        duration (time | str): Duração a ser adicionada. Se for uma string, deve estar no formato "%H:%M:%S".

    Return:
        datetime: Data/hora final resultante da soma da duração com a data/hora de início.
    """
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
    elif isinstance(start_date, datetime):
        start_date = start_date

    if isinstance(duration, str):
        duration_time = datetime.strptime(duration, "%H:%M:%S").time()
    elif isinstance(duration, time):
        duration_time = duration

    duration_delta = timedelta(
        hours=duration_time.hour if duration_time else 0,
        minutes=duration_time.minute if duration_time else 0,
        seconds=duration_time.second if duration_time else 0
    )

    return start_date + duration_delta if start_date else None
