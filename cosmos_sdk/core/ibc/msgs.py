"""IBC module message types."""

from __future__ import annotations

import attr
from cosmos_proto.ibc.applications.transfer.v1 import MsgTransfer as MsgTransfer_pb

from cosmos_sdk.core import AccAddress, Coin
from cosmos_sdk.core.msg import Msg

from .data import Height

__all__ = ["MsgTransfer"]


@attr.s
class MsgTransfer(Msg):
    """
    MsgTransfer defines a msg to transfer fungible tokens (i.e Coins) between ICS20 enabled chains.

    Args:
        source_port (str): the port on which the packet will be sent
        source_channel (str): the channel by which the packet will be sent
        token (Union[Coin, str, dict]): the tokens to be transferred
        sender (AccAddress): the sender address
        receiver (str): the recipient address on the destination chain
        timeout_height (Height): Timeout height relative to the current block height.
            The timeout is disabled when set to 0.
        timeout_timestamp (int): Timeout timestamp (in nanoseconds) relative to the current block timestamp.
            The timeout is disabled when set to 0.
    """

    type_amino = "cosmos-sdk/MsgTransfer"
    """"""
    type_url = "/ibc.applications.transfer.v1.MsgTransfer"
    """"""
    proto_msg = MsgTransfer_pb
    """"""
    source_port = "transfer"
    """"""

    source_channel: str = attr.ib()
    token: Coin = attr.ib(converter=Coin.parse)
    sender: AccAddress = attr.ib()
    receiver: str = attr.ib()  # stay str-typed because it may not be our address
    timeout_height: Height = attr.ib(default=Height())
    timeout_timestamp: int = attr.ib(default=0, converter=int)

    def to_amino(self) -> dict:
        return {
            "type": self.type_amino,
            "value": {
                "source_port": self.source_port,
                "source_channel": self.source_channel,
                "token": self.token.to_amino(),
                "sender": self.sender,
                "receiver": self.receiver,
                "timeout_height": self.timeout_height.to_amino(),
                "timeout_timestamp": self.timeout_timestamp,
            },
        }

    @classmethod
    def from_data(cls, data: dict) -> MsgTransfer:
        return cls(
            source_channel=data["source_channel"],
            token=Coin.from_data(data["token"]),
            sender=data["sender"],
            receiver=data["receiver"],
            timeout_height=Height.from_data(data["timeout_height"]),
            timeout_timestamp=data["timeout_timestamp"],
        )

    @classmethod
    def from_proto(cls, proto: MsgTransfer_pb) -> MsgTransfer:
        return cls(
            source_channel=proto.source_channel,
            token=Coin.from_proto(proto.token),
            sender=AccAddress(proto.sender),
            receiver=proto.receiver,
            timeout_height=Height.from_proto(proto.timeout_height),
            timeout_timestamp=proto.timeout_timestamp,
        )

    def to_proto(self) -> MsgTransfer_pb:
        return MsgTransfer_pb(
            source_port=self.source_port,
            source_channel=self.source_channel,
            token=self.token.to_proto(),
            sender=self.sender,
            receiver=self.receiver,
            timeout_height=self.timeout_height.to_proto(),
            timeout_timestamp=self.timeout_timestamp,
        )
