"""Download configuration constants."""

from pathlib import Path

NUM_THREADS = 4
BUFFER_SIZE = 8192
PROGRESS_BAR_LEN = 40
CHUNK_TIMEOUT = 30        # seconds per read (not total)
MAX_RETRIES = 3           # retry attempts per chunk
RETRY_BACKOFF = 2         # seconds base between retries
DOWNLOAD_DIR = Path.home() / "Videos"
