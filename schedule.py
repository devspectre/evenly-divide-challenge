from datetime import datetime
from typing import List

from constants import (
    MINUTE_INTERVAL,
    HOUR_INTERVAL,
)


def get_account_ids_to_run_every_x_minutes(
    account_ids_list: List[int]
) -> List[int]:
    """
    Return account ids that should run at current minute
    """
    if len(account_ids_list) == 0:
        return []
    now = datetime.now()
    current_minute = now.minute
    bucket_number = current_minute % MINUTE_INTERVAL

    return [
        account_id
        for account_id in account_ids_list
        if (account_id % MINUTE_INTERVAL) == bucket_number
    ]


def get_account_ids_to_run_every_x_hours(
    account_ids_list: List[int]
) -> List[int]:
    """
    Return account ids that should run at current minute
    with additional hour interval
    """
    if len(account_ids_list) == 0:
        return []
    now = datetime.now()
    current_minute, current_hour = now.minute, now.hour
    bucket_number = (current_hour * 60 + current_minute) % (HOUR_INTERVAL * 60)

    return [
        account_id
        for account_id in account_ids_list
        if (account_id % (HOUR_INTERVAL * 60)) == bucket_number
    ]


if __name__ == '__main__':
    input = [account_id for account_id in range(100, 500)]
    print(
        f"Jobs to run every {MINUTE_INTERVAL} minutes:",
        get_account_ids_to_run_every_x_minutes(input)
    )
    print(
        f"Jobs to run every {HOUR_INTERVAL} hours:",
        get_account_ids_to_run_every_x_hours(input)
    )
