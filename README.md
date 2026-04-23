# 📓 video-journal

Turn personal screen recordings into a living journal — Bengali subtitles, word-for-word transcripts, and a richly written Word doc that captures what you were doing, thinking, and feeling.

---

## What it does

```
MOV recordings
    │
    ├─ 🎙  Whisper (chunked, 5-min pieces with 10s overlaps)
    │       ├─ subtitles/   ← .srt files (Bengali Unicode)
    │       └─ transcriptions/  ← plain .txt files
    │
    ├─ 🤖  Anthropic Claude + OpenAI GPT-4o (per chunk, dual-system)
    │       └─ Anthropic synthesises the best of both
    │
    └─ 📄  journal/video_journal.docx
            ├─ Overview & vibe
            ├─ What I Was Doing  (with inline transcript excerpts)
            ├─ 🪞 Reflections & Introspections
            ├─ 📸 Key Moments  (screenshots, only when visually interesting)
            ├─ ✅ TODO  (action items you mentioned)
            └─ 🧵 Loose Threads  (unfinished thoughts to return to)
```

**Chunking strategy** — audio is split into 5-minute segments with 10-second overlaps. Each chunk is transcribed independently (better Whisper accuracy on shorter audio) then stitched at overlap midpoints to handle mid-sentence boundaries. The same chunks are sent to both AIs separately, so neither model has to handle a 30-minute context in one shot.

---

## Requirements

- Python 3.10+
- [ffmpeg](https://ffmpeg.org/) installed via Homebrew: `brew install ffmpeg`
- API keys for **Anthropic** and **OpenAI** (Gemini optional)

---

## Setup

```bash
git clone git@github.com:rajdeep-biswas/video-journal.git
cd video-journal

pip3 install -r requirements.txt

cp keys_template.json keys.json
# → fill in your API keys in keys.json (it's gitignored)
```

---

## Usage

Drop your `.mov` files into the `source/` folder, then run:

```bash
python3 journal_pipeline.py
```

You'll see live progress — per-chunk transcription, AI analysis timings, screenshot extraction — and a total runtime at the end.

**Outputs:**

| Folder | Contents |
|---|---|
| `subtitles/` | `.srt` subtitle files (Bengali Unicode) |
| `transcriptions/` | Full plain-text transcripts |
| `screenshots/` | Extracted frames at visually interesting moments |
| `journal/` | `video_journal.docx` — the main output |

---

## Config

All tuneable constants are at the top of `journal_pipeline.py`:

| Constant | Default | Description |
|---|---|---|
| `WHISPER_MODEL` | `"small"` | Whisper model size (`tiny` → `large`) |
| `WHISPER_LANGUAGE` | `"bn"` | ISO 639-1 language code; `None` = auto-detect |
| `CHUNK_DURATION` | `300` | Seconds per chunk (5 min) |
| `CHUNK_OVERLAP` | `10` | Overlap between chunks for seam stitching |
| `MAX_TOKENS` | `8192` | Token budget for all LLM calls |

---

## Also included

**`convert.py`** — quick batch converter if you just want MP3s:

```bash
python3 convert.py
# reads from source/, writes to output/
```

---

## Folder structure

```
video-journal/
├── journal_pipeline.py   # main pipeline
├── convert.py            # MOV → MP3 utility
├── requirements.txt
├── keys_template.json    # copy to keys.json and fill in
├── keys.json             # gitignored — your actual keys
├── source/               # drop .mov files here
├── subtitles/            # generated .srt files
├── transcriptions/       # generated .txt transcripts
├── screenshots/          # extracted video frames
├── journal/              # final Word doc output
└── output/               # MP3s from convert.py
```
