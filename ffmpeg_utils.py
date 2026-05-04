# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

import ffmpeg
import os

def add_metadata(input_file, output_file, title, author, artist, audio, subtitle, video):

    try:
        stream = ffmpeg.input(input_file)

        stream = ffmpeg.output(
            stream,
            output_file,
            codec="copy",  # 🔥 NO RE-ENCODE
            map_metadata="-1",

            metadata=f"title={title}",
            metadata:g=f"artist={artist}",
            metadata:g=f"author={author}",
            metadata:s:a=f"title={audio}",
            metadata:s:s=f"title={subtitle}",
            metadata:s:v=f"title={video}",

            movflags="faststart"  # 🔥 VERY IMPORTANT
        )

        ffmpeg.run(stream, overwrite_output=True, quiet=True)

        return output_file

    except Exception as e:
        print("Metadata Error:", e)
        return input_file
# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
