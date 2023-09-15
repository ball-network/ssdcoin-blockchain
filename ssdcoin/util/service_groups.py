from __future__ import annotations

from typing import Generator, KeysView

SERVICES_FOR_GROUP = {
    "all": [
        "ssdcoin_harvester",
        "ssdcoin_timelord_launcher",
        "ssdcoin_timelord",
        "ssdcoin_farmer",
        "ssdcoin_full_node",
        "ssdcoin_wallet",
        "ssdcoin_data_layer",
        "ssdcoin_data_layer_http",
    ],
    # TODO: should this be `data_layer`?
    "data": ["ssdcoin_wallet", "ssdcoin_data_layer"],
    "data_layer_http": ["ssdcoin_data_layer_http"],
    "node": ["ssdcoin_full_node"],
    "harvester": ["ssdcoin_harvester"],
    "farmer": ["ssdcoin_harvester", "ssdcoin_farmer", "ssdcoin_full_node", "ssdcoin_wallet"],
    "farmer-no-wallet": ["ssdcoin_harvester", "ssdcoin_farmer", "ssdcoin_full_node"],
    "farmer-only": ["ssdcoin_farmer"],
    "timelord": ["ssdcoin_timelord_launcher", "ssdcoin_timelord", "ssdcoin_full_node"],
    "timelord-only": ["ssdcoin_timelord"],
    "timelord-launcher-only": ["ssdcoin_timelord_launcher"],
    "wallet": ["ssdcoin_wallet"],
    "introducer": ["ssdcoin_introducer"],
    "simulator": ["ssdcoin_full_node_simulator"],
    "crawler": ["ssdcoin_crawler"],
    "seeder": ["ssdcoin_crawler", "ssdcoin_seeder"],
    "seeder-only": ["ssdcoin_seeder"],
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
