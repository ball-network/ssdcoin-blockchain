from __future__ import annotations

from enum import IntEnum


class TransactionType(IntEnum):
    INCOMING_TX = 0
    OUTGOING_TX = 1
    COINBASE_REWARD = 2
    FEE_REWARD = 3
    INCOMING_TRADE = 4
    OUTGOING_TRADE = 5
    INCOMING_CLAWBACK_RECEIVE = 6
    INCOMING_CLAWBACK_SEND = 7
    OUTGOING_CLAWBACK = 8
    INCOMING_CRCAT_PENDING = 9

    STAKE_FARM_REWARD = 60

    OUTGOING_STAKE_FARM = 70
    INCOMING_STAKE_FARM_RECEIVE = 72
    STAKE_FARM_WITHDRAW = 74


CLAWBACK_INCOMING_TRANSACTION_TYPES = {
    TransactionType.INCOMING_CLAWBACK_SEND.value,
    TransactionType.INCOMING_CLAWBACK_RECEIVE.value,
    TransactionType.INCOMING_CRCAT_PENDING.value,

    TransactionType.INCOMING_STAKE_FARM_RECEIVE.value,
}
