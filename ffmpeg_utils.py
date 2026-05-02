# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

import ffmpeg
import os

def add_metadata(input_path, output_path, title="", author="", description=""):
    try:
        (
            ffmpeg
            .input(input_path)
            .output(
                output_path,
                codec="copy",
                metadata=f"title={title}",
                metadata=f"artist={author}",
                metadata=f"comment={description}"
            )
            .run(overwrite_output=True)
        )

        return output_path

    except Exception as e:
        print("FFmpeg Error:", e)
        return input_path

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
