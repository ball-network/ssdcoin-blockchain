#!/usr/bin/env bash
# Post install script for the UI .rpm to place symlinks in places to allow the CLI to work similarly in both versions

set -e

ln -s /opt/ssdcoin/resources/app.asar.unpacked/daemon/ssd /usr/bin/ssd || true
ln -s /opt/ssdcoin/ssdcoin-blockchain /usr/bin/ssdcoin-blockchain || true
