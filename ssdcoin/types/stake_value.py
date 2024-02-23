from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ssdcoin.consensus.block_rewards import MOJO_PER_SSD
from ssdcoin.util.ints import uint16, uint64
from ssdcoin.util.streamable import Streamable, streamable

STAKE_PER_COEFFICIENT = 10 ** 17

STAKE_FARM_COUNT = 100
STAKE_FARM_MIN = 100 * MOJO_PER_SSD
STAKE_FARM_PREFIX = "dpos:ssd:"


@streamable
@dataclass(frozen=True)
class StakeValue(Streamable):
    time_lock: uint64
    coefficient: str
    reward_coefficient: Optional[str]

    def stake_amount(self, amount: uint64) -> int:
        return int(int(amount) * float(self.coefficient) * MOJO_PER_SSD)

    def least_reward_amount(self, amount: uint64) -> float:
        if self.reward_coefficient is None:
            return 0
        return int(amount) * MOJO_PER_SSD * float(self.coefficient) * float(self.reward_coefficient)


STAKE_FARM_LIST: List[StakeValue] = [
    StakeValue(86400 * 3, "1.0", None),
    StakeValue(86400 * 10, "1.1", None),
    StakeValue(86400 * 30, "1.25", None),
    StakeValue(86400 * 90, "1.5", None),
    StakeValue(86400 * 180, "1.75", None),
    StakeValue(86400 * 365, "2.0", None),
    StakeValue(86400 * 730, "2.25", None),
    StakeValue(86400 * 1095, "2.5", None),
    StakeValue(86400 * 1825, "2.75", None),
    StakeValue(86400 * 3650, "3.0", None),
]


def get_stake_value(stake_type: uint16) -> StakeValue:
    if 0 <= stake_type < 10:
        return STAKE_FARM_LIST[stake_type]
    return StakeValue(0, "0", None)
