import contextlib
import sqlite3

@contextlib.contextmanager
def connect():
    conn = sqlite3.connect('backend.db')
    cur = conn.cursor()
    try:
        yield cur
    finally:
        conn.commit()
        conn.close()

# Maps each hour 0-23 to its "12-hour style" Swedish name. Here I assume 23 is 11 (converting 24-hour to 12-hour system)
SWEDISH_HOUR = {
    0:  "tolv",  1:  "ett",  2:  "två",   3:  "tre",   4:  "fyra",  5:  "fem",
    6:  "sex",   7:  "sju",  8:  "åtta",  9:  "nio",   10: "tio",   11: "elva",
    12: "tolv", 13: "ett", 14: "två",   15: "tre",   16: "fyra",  17: "fem",
    18: "sex",  19: "sju", 20: "åtta", 21: "nio",   22: "tio",   23: "elva"
}

# Maps each hour 0-23 to its "12-hour style" English name
# This should be added if the Clock-Logic team intends to have the time translated
ENGLISH_HOUR = {
    0:  "twelve",  1:  "one",   2:  "two",   3:  "three", 4:  "four",  5:  "five",
    6:  "six",     7:  "seven", 8:  "eight", 9:  "nine",  10: "ten",   11: "eleven",
    12: "twelve", 13: "one",   14: "two",   15: "three", 16: "four",  17: "five",
    18: "six",    19: "seven", 20: "eight", 21: "nine",  22: "ten",   23: "eleven"
}

def swedish_time_string(hour: int, minute: int) -> str:
    """
    Returns a Swedish phrase for the given hour/minute, using 12-hour style (not a swedish expert lol)
      - :00 -> "klockan X"
      - :15 -> "kvart över X"
      - :30 -> "halv X+1"
      - :45 -> "kvart i X+1"
    """
    next_hour = (hour + 1) % 24
    if minute == 0:
        return f"klockan {SWEDISH_HOUR[hour]}"
    elif minute == 15:
        return f"kvart över {SWEDISH_HOUR[hour]}"
    elif minute == 30:
        return f"halv {SWEDISH_HOUR[next_hour]}"
    elif minute == 45:
        return f"kvart i {SWEDISH_HOUR[next_hour]}"
    else:
        return f"{hour:02}:{minute:02}"  # Fallback (shouldn't happen in this script)

def english_time_string(hour: int, minute: int) -> str:
    """
    Returns an English phrase for the given hour/minute, using 12-hour style:
      - :00 -> "X o'clock"
      - :15 -> "quarter past X"
      - :30 -> "half past X"
      - :45 -> "quarter to X+1"
    """
    next_hour = (hour + 1) % 24
    if minute == 0:
        return f"{ENGLISH_HOUR[hour]} o'clock"
    elif minute == 15:
        return f"quarter past {ENGLISH_HOUR[hour]}"
    elif minute == 30:
        return f"half past {ENGLISH_HOUR[hour]}"
    elif minute == 45:
        return f"quarter to {ENGLISH_HOUR[next_hour]}"
    else:
        return f"{hour:02}:{minute:02}"

def seed_times_24h():
    """
    Inserts every quarter-hour from 00:00 to 23:45 (24-hour format) into the 'times' table,
    with a Swedish expression, an English expression, and difficulty='easy'.
    """
    rows_to_insert = []
    quarter_minutes = [0, 15, 30, 45]

    for hour in range(24):
        for minute in quarter_minutes:
            # "time" column: 24-hour format HH:MM
            time_str = f"{hour:02}:{minute:02}"

            # Swedish expression (12-hour style phrases)
            swe_expr = swedish_time_string(hour, minute)

            # English expression (12-hour style phrases)
            eng_expr = english_time_string(hour, minute)

            # difficulty set to "easy" by default
            difficulty = "easy"

            # We'll store (time, swedish, english, difficulty) if your schema has all four columns
            # If your 'times' table only has (time, swedish, difficulty), remove eng_expr below
            rows_to_insert.append((time_str, swe_expr, eng_expr, difficulty))

    with connect() as cur:
        # If you want to clear existing data, uncomment the next line:
        # cur.execute("DELETE FROM times")

        # Adjust this INSERT to match your actual column names:
        # For example, if your table is: id | time | swedish | english | difficulty
        # then you can do:
        insert_sql = """
            INSERT INTO times (time, swedish, english, difficulty)
            VALUES (?, ?, ?, ?)
        """
        cur.executemany(insert_sql, rows_to_insert)

    print("Seeded the 'times' table with 24-hour quarter-hour data successfully!")

if __name__ == "__main__":
    seed_times_24h()

