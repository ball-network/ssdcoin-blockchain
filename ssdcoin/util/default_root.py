from __future__ import annotations

import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("SSDCOIN_ROOT", "~/.ssd/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("SSDCOIN_KEYS_ROOT", "~/.ssd_keys"))).resolve()

SIMULATOR_ROOT_PATH = Path(os.path.expanduser(os.getenv("SSDCOIN_SIMULATOR_ROOT", "~/.ssd/simulator"))).resolve()
