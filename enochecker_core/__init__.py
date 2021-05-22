from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Type, Union


class CheckerTaskResult(Enum):
    value: str
    OK = "OK"
    MUMBLE = "MUMBLE"
    OFFLINE = "OFFLINE"
    INTERNAL_ERROR = "INTERNAL_ERROR"

    def __str__(self) -> str:
        return self.value


class CheckerMethod(Enum):
    value: str
    PUTFLAG = "putflag"
    GETFLAG = "getflag"
    PUTNOISE = "putnoise"
    GETNOISE = "getnoise"
    HAVOC = "havoc"
    EXPLOIT = "exploit"

    def __str__(self) -> str:
        return self.value


@dataclass
class CheckerInfoMessage:
    service_name: str
    flag_variants: int
    noise_variants: int
    havoc_variants: int
    exploit_variants: int


@dataclass
class CheckerResultMessage:
    result: CheckerTaskResult
    message: Optional[str]
    attack_info: Optional[str] = None
    flag: Optional[str] = None


@dataclass
class EnoLogMessage:
    tool: str
    type: str
    severity: str
    severity_level: int
    timestamp: str
    message: str
    module: Optional[str]
    function: Optional[str]
    service_name: Optional[str]
    task_id: Optional[int]
    method: Optional[str]
    team_id: Optional[int]
    team_name: Optional[str]
    current_round_id: Optional[int]
    related_round_id: Optional[int]
    flag: Optional[str]
    variant_id: Optional[int]
    task_chain_id: Optional[str]
    flag_regex: Optional[str]
    flag_hash: Optional[str]
    attack_info: Optional[str]


@dataclass
class CheckerTaskMessage:
    task_id: int
    method: CheckerMethod
    address: str
    team_id: int
    team_name: str
    current_round_id: int
    related_round_id: int
    flag: Optional[str]
    variant_id: int
    timeout: int
    round_length: int
    task_chain_id: str
    flag_regex: Optional[str] = None
    flag_hash: Optional[str] = None
    attack_info: Optional[str] = None


class BrokenServiceException(Exception):
    pass


class OfflineException(Exception):
    pass
