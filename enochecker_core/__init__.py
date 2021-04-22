from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Type, Union


class CheckerTaskResult(Enum):
    value: str
    CHECKER_TASK_RESULT_OK = "OK"
    CHECKER_TASK_RESULT_MUMBLE = "MUMBLE"
    CHECKER_TASK_RESULT_OFFLINE = "OFFLINE"
    CHECKER_TASK_RESULT_INTERNAL_ERROR = "INTERNAL_ERROR"

    def __str__(self) -> str:
        return self.value


class CheckerMethod(Enum):
    value: str
    CHECKER_METHOD_PUTFLAG = "putflag"
    CHECKER_METHOD_GETFLAG = "getflag"
    CHECKER_METHOD_PUTNOISE = "putnoise"
    CHECKER_METHOD_GETNOISE = "getnoise"
    CHECKER_METHOD_HAVOC = "havoc"

    def __str__(self) -> str:
        return self.value


@dataclass
class CheckerInfoMessage:
    service_name: str
    flag_variants: int
    noise_variants: int
    havoc_variants: int


@dataclass
class CheckerResultMessage:
    result: CheckerTaskResult
    message: Optional[str]


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
    team_id: Optional[int]
    team_name: Optional[str]
    current_round_id: Optional[int]
    related_round_id: Optional[int]
    flag: Optional[str]
    variant_id: Optional[int]
    task_chain_id: Optional[str]


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


class BrokenServiceException(Exception):
    pass


class OfflineException(Exception):
    pass
