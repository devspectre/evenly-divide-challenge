from datetime import datetime
from typing import List

from constants import (
    MINUTE_INTERVAL,
)


def get_account_ids_to_run(account_ids_list: List[int]) -> List[int]:
    """
    Return account ids that should run at current minute
    """
    account_ids_to_return = []
    if len(account_ids_list) == 0:
        return account_ids_to_return
    now = datetime.now()
    current_minute = now.minute
    bucket_number = current_minute % MINUTE_INTERVAL

    return [
        account_id
        for account_id in account_ids_list
        if (account_id % MINUTE_INTERVAL) == bucket_number
    ]


if __name__ == '__main__':
    input = [account_id for account_id in range(100, 200)]
    print(get_account_ids_to_run(input))
