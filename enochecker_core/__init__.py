from dataclasses import dataclass
from enum import Enum
from typing import Optional, Callable, Any, Dict, List, Union, Type

class CheckerTaskResult(Enum):
    CHECKER_TASK_RESULT_OK = "OK"
    CHECKER_TASK_RESULT_MUMBLE = "MUMBLE"
    CHECKER_TASK_RESULT_DOWN = "OFFLINE"
    CHECKER_TASK_RESULT_INTERNAL_ERROR = "INTERNAL_ERROR"

    def __str__(self):
        return self.value

class CheckerTaskType(Enum):
    CHECKER_TASK_TYPE_PUTFLAG = "putflag"
    CHECKER_TASK_TYPE_GETFLAG = "getflag"
    CHECKER_TASK_TYPE_PUTNOISE = "putnoise"
    CHECKER_TASK_TYPE_GETNOISE = "getnoise"
    CHECKER_TASK_TYPE_HAVOC = "havoc"

    def __str__(self):
        return self.value

@dataclass
class CheckerInfoMessage:
    service_name: str
    flag_count: int
    havoc_count: int
    noise_count: int

@dataclass
class CheckerResultMessage:
    result: str

@dataclass
class EnoLogMessage:
    tool: str
    type: str
    severity: str
    severity_level: int
    timestamp: str
    module: Optional[str]
    function: Optional[str]
    flag: Optional[str]
    flag_index: Optional[int]
    run_id: Optional[int]
    round_id: Optional[int]
    related_round_id: Optional[int]
    message: str
    team_name: Optional[str]
    team_id: Optional[str]
    service_name: Optional[str]
    method: Optional[str]

@dataclass
class CheckerTaskMessage:
    run_id: int
    method: str
    address: str
    service_id: int
    service_name: str
    team_id: int
    team_name: str
    round_id: int
    related_round_id: int
    flag: Optional[str]
    flag_index: int

class BrokenServiceException(Exception):
    pass

class OfflineException(Exception):
    pass
