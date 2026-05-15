#-------------------------#

#Don't Remove Credit

#Ask Doubt @AU_Bot_Discussion

#Owner @Mr_Mohammed_29

#-------------------------#

import time
import os

#---------- BYTE CONVERTER (FIXED) ----------#

def humanbytes(size):
if not size:
return "0 B"
power = 2**10
n = 0
Dic_powerN = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}

# 🔥 FIX: >= and limit  
while size >= power and n < 4:  
    size /= power  
    n += 1  

return str(round(size, 2)) + " " + Dic_powerN[n]

#---------- TIME FORMAT (IMPROVED) ----------#

def time_formatter(seconds):
seconds = int(seconds)

if seconds <= 0:  
    return "0s"  

m, s = divmod(seconds, 60)  
h, m = divmod(m, 60)  

# 🔥 CLEAN FORMAT  
if h > 0:  
    return f"{h}h {m}m {s}s"  
elif m > 0:  
    return f"{m}m {s}s"  
else:  
    return f"{s}s"

#---------- SIMPLE PROGRESS BAR ----------#

def progress_bar(current, total):
if total == 0:
return "[⬡⬡⬡⬡⬡⬡⬡⬡⬡⬡] 0%"

percent = (current / total) * 100   # 🔥 more accurate  
filled = int(percent // 10)  

bar = "⬢" * filled + "⬡" * (10 - filled)  

return f"[{bar}] {round(percent, 2)}%"

#---------- ADD THIS (FULL PROGRESS TEXT) ----------#

def format_progress(current, total, speed, eta):
return (
f"{progress_bar(current, total)}\n\n"
f"📦 {humanbytes(current)} / {humanbytes(total)}\n"
f"⚡ Speed: {humanbytes(speed)}/s\n"
f"⏳ ETA: {time_formatter(eta)}"
)

#-------------------------#

#Don't Remove Credit

#Ask Doubt @AU_Bot_Discussion

#Owner @Mr_Mohammed_29

-------------------------
