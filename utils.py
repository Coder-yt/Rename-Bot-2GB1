# ------------------------- #
# Don't Remove Credit
# Ask Doubt @AU_Bot_Discussion
# Owner @Mr_Mohammed_29
# ------------------------- #

import time
import os
import math
import gc
import psutil

# ---------- BYTE CONVERTER (FIXED) ----------
def humanbytes(size):
    if not size:
        return "0 B"

    power = 2**10
    n = 0

    Dic_powerN = {
        0: 'B',
        1: 'KB',
        2: 'MB',
        3: 'GB',
        4: 'TB'
    }

    # 🔥 FIX: >= and limit
    while size >= power and n < 4:
        size /= power
        n += 1

    return str(round(size, 2)) + " " + Dic_powerN[n]


# ---------- TIME FORMAT (IMPROVED) ----------
def time_formatter(seconds):
    seconds = int(seconds)

    if seconds <= 0:
        return "0s"

    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    tmp = ""

    if days > 0:
        tmp += f"{days}d "

    if hours > 0:
        tmp += f"{hours}h "

    if minutes > 0:
        tmp += f"{minutes}m "

    tmp += f"{seconds}s"

    return tmp.strip()


# ---------- SIMPLE PROGRESS BAR ----------
def progress_bar(current, total):
    if total == 0:
        return "[⬡⬡⬡⬡⬡⬡⬡⬡⬡⬡] 0%"

    percent = (current / total) * 100

    # 🔥 safer calculation
    filled = math.floor(percent / 10)

    # 🔥 avoid overflow
    if filled > 10:
        filled = 10

    bar = "⬢" * filled + "⬡" * (10 - filled)

    return f"[{bar}] {round(percent, 2)}%"


# ---------- FULL PROGRESS TEXT ----------
def format_progress(current, total, speed, eta):
    return (
        f"{progress_bar(current, total)}\n\n"
        f"📦 {humanbytes(current)} / {humanbytes(total)}\n"
        f"⚡ Speed: {humanbytes(speed)}/s\n"
        f"⏳ ETA: {time_formatter(eta)}"
    )


# ---------- RAM CHECK ----------
def get_ram():
    memory = psutil.virtual_memory()
    return memory.percent


# ---------- DISK CHECK ----------
def get_disk():
    disk = psutil.disk_usage('/')
    return disk.percent


# ---------- AUTO CLEANUP ----------
def cleanup(*paths):
    for path in paths:
        try:
            if path and os.path.exists(path):
                os.remove(path)
        except Exception:
            pass

    gc.collect()


# ---------- SAFE FILE LIMIT ----------
MAX_FILE_SIZE = 2.6 * 1024 * 1024 * 1024


# ---------- SAFE FILE CHECK ----------
def check_file_size(file_size):
    return file_size <= MAX_FILE_SIZE


# ---------- SAFE SERVER CHECK ----------
def server_busy():
    ram = get_ram()
    disk = get_disk()

    if ram > 90:
        return True

    if disk > 95:
        return True

    return False


# ------------------------- #
# Don't Remove Credit
# Ask Doubt @AU_Bot_Discussion
# Owner @Mr_Mohammed_29
# ------------------------- #
