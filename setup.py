from __future__ import annotations

import os
import sys

from setuptools import find_packages, setup

dependencies = [
    "aiofiles==23.2.1",  # Async IO for files
    "anyio==4.0.0",
    "boto3==1.29.4",  # AWS S3 for DL s3 plugin
    "chiavdf==1.1.0",  # timelord and vdf verification
    "chiabip158==1.3",  # bip158-style wallet filters
    "chiapos==2.0.3",  # proof of space
    "clvm==0.9.8",
    "clvm_tools==0.4.7",  # Currying, Program.to, other conveniences
    "chia_rs==0.2.15",
    "clvm-tools-rs==0.1.39",  # Rust implementation of clvm_tools' compiler
    "aiohttp==3.9.1",  # HTTP server for full node rpc
    "aiosqlite==0.19.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==4.1.2",  # Binary data management library
    "colorama==0.4.6",  # Colorizes terminal output
    "colorlog==6.7.0",  # Adds color to logs
    "concurrent-log-handler==0.9.24",  # Concurrently log and rotate logs
    "cryptography==41.0.5",  # Python cryptography library for TLS - keyring conflict
    "filelock==3.13.1",  # For reading and writing config multiprocess and multithread safely  (non-reentrant locks)
    "keyring==24.3.0",  # Store keys in MacOS Keychain, Windows Credential Locker
    "PyYAML==6.0.1",  # Used for config file format
    "setproctitle==1.3.3",  # Gives the ssdcoin processes readable names
    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
    "click==8.1.3",  # For the CLI
    "dnspython==2.4.2",  # Query DNS seeds
    "watchdog==2.2.0",  # Filesystem event watching - watches keyring.yaml
    "dnslib==0.9.23",  # dns lib
    "typing-extensions==4.8.0",  # typing backports like Protocol and TypedDict
    "zstd==1.5.5.1",
    "packaging==23.2",
    "psutil==5.9.4",
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "build==1.0.3",
    "coverage==7.3.2",
    "diff-cover==8.0.1",
    "pre-commit==3.5.0",
    "py3createtorrent==1.1.0",
    "pylint==3.0.2",
    "pytest==7.4.3",
    "pytest-cov==4.1.0",
    "pytest-mock==3.12.0",
    "pytest-xdist==3.5.0",
    "pyupgrade==3.15.0",
    "twine==4.0.2",
    "isort==5.12.0",
    "flake8==6.1.0",
    "mypy==1.7.0",
    "black==23.11.0",
    "lxml==4.9.3",
    "aiohttp_cors==0.7.0",  # For blackd
    "pyinstaller==5.13.0",
    "types-aiofiles==23.2.0.0",
    "types-cryptography==3.3.23.2",
    "types-pyyaml==6.0.12.12",
    "types-setuptools==68.2.0.1",
]

legacy_keyring_dependencies = [
    "keyrings.cryptfile==1.3.9",
]

kwargs = dict(
    name="ssdcoin-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@ssdcoin.top",
    description="SSDCoin blockchain full node, farmer, timelord, and wallet.",
    url="https://ssdcoin.top/",
    license="Apache License",
    python_requires=">=3.8.1, <4",
    keywords="ssdcoin blockchain node",
    install_requires=dependencies,
    extras_require=dict(
        dev=dev_dependencies,
        upnp=upnp_dependencies,
        legacy_keyring=legacy_keyring_dependencies,
    ),
    packages=find_packages(include=["build_scripts", "ssdcoin", "ssdcoin.*", "mozilla-ca"]),
    entry_points={
        "console_scripts": [
            "ssd = ssdcoin.cmds.ssdcoin:main",
            "ssdcoin_daemon = ssdcoin.daemon.server:main",
            "ssdcoin_wallet = ssdcoin.server.start_wallet:main",
            "ssdcoin_full_node = ssdcoin.server.start_full_node:main",
            "ssdcoin_harvester = ssdcoin.server.start_harvester:main",
            "ssdcoin_farmer = ssdcoin.server.start_farmer:main",
            "ssdcoin_introducer = ssdcoin.server.start_introducer:main",
            "ssdcoin_crawler = ssdcoin.seeder.start_crawler:main",
            "ssdcoin_seeder = ssdcoin.seeder.dns_server:main",
            "ssdcoin_timelord = ssdcoin.server.start_timelord:main",
            "ssdcoin_timelord_launcher = ssdcoin.timelord.timelord_launcher:main",
            "ssdcoin_full_node_simulator = ssdcoin.simulator.start_simulator:main",
            "ssdcoin_data_layer = ssdcoin.server.start_data_layer:main",
            "ssdcoin_data_layer_http = ssdcoin.data_layer.data_layer_server:main",
            "ssdcoin_data_layer_s3_plugin = ssdcoin.data_layer.s3_plugin_service:run_server",
        ]
    },
    package_data={
        "": ["*.clsp", "*.clsp.hex", "*.clvm", "*.clib", "py.typed"],
        "ssdcoin.util": ["initial-*.yaml", "english.txt"],
        "ssdcoin.ssl": ["ssdcoin_ca.crt", "ssdcoin_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    long_description=open("README.md", encoding="UTF-8").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    project_urls={
        "Source": "https://github.com/ball-network/ssdcoin-blockchain/",
        "Changelog": "https://github.com/Chia-Network/chia-blockchain/blob/main/CHANGELOG.md",
    },
)

if "setup_file" in sys.modules:
    # include dev deps in regular deps when run in snyk
    dependencies.extend(dev_dependencies)

if len(os.environ.get("SSDCOIN_SKIP_SETUP", "")) < 1:
    setup(**kwargs)  # type: ignore
