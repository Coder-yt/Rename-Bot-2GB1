# ------------------------- #
# Don't Remove Credit
# Ask Doubt @AU_Bot_Discussion
# Owner @Mr_Mohammed_29
# ------------------------- #

import ffmpeg
import os
import gc
import psutil
import asyncio


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
def check_file_size(file_path):
    try:
        size = os.path.getsize(file_path)
        return size <= MAX_FILE_SIZE
    except:
        return False


# ---------- SERVER CHECK ----------
def server_busy():
    ram = get_ram()
    disk = get_disk()

    if ram > 90:
        return True

    if disk > 95:
        return True

    return False


# ---------- MAIN METADATA FUNCTION ----------
def add_metadata(input_file, output_file, title, author, artist, audio, subtitle, video):

    try:

        # ---------- FILE CHECK ----------
        if not os.path.exists(input_file):
            raise Exception("Input file missing")

        if not check_file_size(input_file):
            raise Exception("File exceeds 2.6GB limit")

        if server_busy():
            raise Exception("Server overloaded")

        # -------- STEP 1: FAST COPY -------- #
        stream = ffmpeg.input(input_file)

        stream = ffmpeg.output(
            stream,
            output_file,

            codec="copy",
            map_metadata="-1",

            **{
                "metadata": f"title={title}",
                "metadata:g": f"artist={artist}",
                "metadata:g:1": f"author={author}",
                "metadata:s:a:0": f"title={audio}",
                "metadata:s:s:0": f"title={subtitle}",
                "metadata:s:v:0": f"title={video}",
            },

            movflags="+faststart",
            fflags="+genpts",
            avoid_negative_ts="make_zero"
        )

        ffmpeg.run(
            stream,
            overwrite_output=True,
            quiet=True
        )

        # -------- STEP 2: VALIDATE OUTPUT -------- #
        if not os.path.exists(output_file):
            raise Exception("Output not created")

        size = os.path.getsize(output_file)

        if size < 100000:
            raise Exception("Broken file")

        # ---------- CLEAN MEMORY ----------
        gc.collect()

        return output_file

    except Exception as e:

        print("⚠️ Cᴏᴘʏ Fᴀɪʟᴇᴅ, Sᴡɪᴛᴄʜɪɴɢ Tᴏ Rᴇ-Eɴᴄᴏᴅᴇ:", e)

        # -------- STEP 3: FALLBACK RE-ENCODE -------- #
        try:

            if server_busy():
                raise Exception("Server overloaded during encode")

            stream = ffmpeg.input(input_file)

            stream = ffmpeg.output(
                stream,
                output_file,

                vcodec="libx264",
                acodec="aac",

                # 🔥 FASTEST FOR RENDER
                preset="ultrafast",

                # 🔥 LOWER CPU USAGE
                threads=2,

                # 🔥 SAFE METADATA
                **{
                    "metadata": f"title={title}",
                    "metadata:g": f"artist={artist}",
                    "metadata:g:1": f"author={author}",
                },

                movflags="+faststart"
            )

            ffmpeg.run(
                stream,
                overwrite_output=True,
                quiet=True
            )

            # ---------- VALIDATE AGAIN ----------
            if not os.path.exists(output_file):
                raise Exception("Re-encode failed")

            # ---------- CLEAN MEMORY ----------
            gc.collect()

            return output_file

        except Exception as e2:

            print("❌ Rᴇ-Eɴᴄᴏᴅᴇ Aʟsᴏ Fᴀɪʟᴇᴅ:", e2)

            # ---------- CLEAN BROKEN OUTPUT ----------
            cleanup(output_file)

            return input_file


# ------------------------- #
# Don't Remove Credit
# Ask Doubt @AU_Bot_Discussion
# Owner @Mr_Mohammed_29
# ------------------------- #
