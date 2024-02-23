from __future__ import annotations

from ssdcoin.util.ints import uint32, uint64

# 1 SSDCoin coin = 1,000,000,000,000 = 1 trillion mojo.
MOJO_PER_SSD = 1000000000000
STAKE_FORK_HEIGHT = 800000
OLD_STAKE_FORK_HEIGHT = 1000000
_reward_per = [
    (150000, 8),
    (6000000, 2),
    (12000000, 1),
    (18000000, 0.5),
    (24000000, 0.25),
    (24000000, 0.125),
]


def calculate_reward(height: uint32, index: int = -1) -> int:
    _height, _reward = _reward_per[index]
    if height >= _height if index == -1 else height < _height:
        return _reward
    else:
        index += 1
        return calculate_reward(height, index)


def calculate_pool_reward(height: uint32) -> uint64:
    """
    Returns the pool reward at a certain block height. The pool earns 7/8 of the reward in each block. If the farmer
    is solo farming, they act as the pool, and therefore earn the entire block reward.
    These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """

    if height < STAKE_FORK_HEIGHT:
        return uint64(int((7 / 8) * calculate_reward(height) * MOJO_PER_SSD))
    return uint64(0)


def calculate_base_farmer_reward(height: uint32) -> uint64:
    """
    Returns the base farmer reward at a certain block height.
    The base fee reward is 1/8 of total block reward

    Returns the coinbase reward at a certain block height. These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """

    return uint64(int((1 / 8) * calculate_reward(height) * MOJO_PER_SSD))


def calculate_community_reward(height: uint32) -> uint64:
    if height < STAKE_FORK_HEIGHT:
        return uint64(int((3 / 100) * calculate_reward(height) * MOJO_PER_SSD))
    return uint64(100 * MOJO_PER_SSD)


def calculate_stake_farm_reward(height: uint32) -> uint64:
    if height < STAKE_FORK_HEIGHT:
        return uint64(0)
    return uint64(int((7 / 8) * calculate_reward(height) * MOJO_PER_SSD))
