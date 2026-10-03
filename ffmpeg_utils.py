# ------------------------- #
# Don't Remove Credit
# Ask Doubt @AU_Bot_Discussion
# Owner @Mr_Mohammed_29
# ------------------------- #

import os
import subprocess


def add_metadata(
    input_file,
    output_file,
    title="",
    author="",
    artist="",
    video="",
    audio="",
    subtitle=""
):
    """
    Add MKV metadata without re-encoding audio/video/subtitle streams.

    Streams are copied with -c copy.
    Old container metadata is removed first.
    """

    try:
        # -------------------------------------------------
        # BUILD FFMPEG COMMAND
        # -------------------------------------------------

        command = [
            "ffmpeg",
            "-y",
            "-i", input_file,

            # Keep ALL streams
            "-map", "0",

            # Remove old global/container metadata
            "-map_metadata", "-1",

            # Do NOT re-encode
            "-c", "copy",
        ]

        # -------------------------------------------------
        # GLOBAL METADATA
        # -------------------------------------------------

        if title:
            command.extend([
                "-metadata",
                f"title={title}"
            ])

        if author:
            command.extend([
                "-metadata",
                f"author={author}"
            ])

        if artist:
            command.extend([
                "-metadata",
                f"artist={artist}"
            ])

        # -------------------------------------------------
        # VIDEO STREAM METADATA
        # -------------------------------------------------

        if video:
            command.extend([
                "-metadata:s:v:0",
                f"title={video}"
            ])

        # -------------------------------------------------
        # AUDIO STREAM METADATA
        # -------------------------------------------------

        if audio:
            command.extend([
                "-metadata:s:a:0",
                f"title={audio}"
            ])

        # -------------------------------------------------
        # SUBTITLE STREAM METADATA
        # -------------------------------------------------

        if subtitle:
            command.extend([
                "-metadata:s:s:0",
                f"title={subtitle}"
            ])

        # -------------------------------------------------
        # OUTPUT
        # -------------------------------------------------

        command.append(output_file)

        print("========================================")
        print("METADATA FFMPEG COMMAND:")
        print(" ".join(command))
        print("========================================")

        # -------------------------------------------------
        # RUN FFMPEG
        # -------------------------------------------------

        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # -------------------------------------------------
        # CHECK FFMPEG ERROR
        # -------------------------------------------------

        if result.returncode != 0:

            print("========================================")
            print("METADATA FFMPEG ERROR:")
            print(result.stderr)
            print("========================================")

            if os.path.exists(output_file):
                try:
                    os.remove(output_file)
                except OSError:
                    pass

            raise RuntimeError(
                "FFmpeg metadata processing failed"
            )

        # -------------------------------------------------
        # VALIDATE OUTPUT
        # -------------------------------------------------

        if not os.path.exists(output_file):
            raise RuntimeError(
                "FFmpeg finished but output file was not created"
            )

        size = os.path.getsize(output_file)

        if size < 100000:
            try:
                os.remove(output_file)
            except OSError:
                pass

            raise RuntimeError(
                "Generated output file is too small"
            )

        print(
            f"✅ Metadata processing successful: "
            f"{output_file} ({size} bytes)"
        )

        return output_file

    except Exception as e:

        print("========================================")
        print("❌ METADATA ERROR:")
        print(repr(e))
        print("========================================")

        if os.path.exists(output_file):
            try:
                os.remove(output_file)
            except OSError:
                pass

        # Do NOT return the original file.
        # The caller must know metadata processing failed.
        raise


# ------------------------- #
# Don't Remove Credit
# Ask Doubt @AU_Bot_Discussion
# Owner @Mr_Mohammed_29
# ------------------------- #