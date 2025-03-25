from datetime import datetime, timezone, timedelta

tmzone = 0
current_time = datetime.now(timezone(timedelta(seconds=tmzone)))

print(current_time)