import subprocess
from pathlib import Path

SOURCE_DIR = Path(__file__).parent / "source"
OUTPUT_DIR = Path(__file__).parent / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

mov_files = list(SOURCE_DIR.glob("*.mov")) + list(SOURCE_DIR.glob("*.MOV"))

if not mov_files:
    print("No .mov files found in source/")
else:
    for mov in mov_files:
        mp3 = OUTPUT_DIR / (mov.stem + ".mp3")
        print(f"Converting: {mov.name} -> {mp3.name}")
        result = subprocess.run(
            ["ffmpeg", "-i", str(mov), "-vn", "-acodec", "libmp3lame", "-q:a", "2", str(mp3)],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print(f"  Done: {mp3.name}")
        else:
            print(f"  Failed: {mov.name}")
            print(result.stderr[-500:])

    print(f"\nFinished. Output in: {OUTPUT_DIR}")
