__all__ = [
    "CheckerTaskResult",
    "CheckerMethod",
    "CheckerInfoMessage",
    "CheckerResultMessage",
    "EnoLogMessage",
    "CheckerTaskMessage",
]

from enum import Enum
from pydantic.alias_generators import to_camel
from pydantic import AliasGenerator, BaseModel as PydanticBaseModel, ConfigDict


class CheckerTaskResult(str, Enum):
    OK = "OK"
    MUMBLE = "MUMBLE"
    OFFLINE = "OFFLINE"
    INTERNAL_ERROR = "INTERNAL_ERROR"

    def __str__(self) -> str:
        return self.value


class CheckerMethod(str, Enum):
    PUTFLAG = "putflag"
    GETFLAG = "getflag"
    PUTNOISE = "putnoise"
    GETNOISE = "getnoise"
    HAVOC = "havoc"
    EXPLOIT = "exploit"
    TEST = "test"

    def __str__(self) -> str:
        return self.value


class BaseModel(PydanticBaseModel):
    model_config = ConfigDict(
        use_enum_values=True,
        alias_generator=AliasGenerator(alias=to_camel),
        validate_by_name=True,
        validate_by_alias=True,
        serialize_by_alias=True,
    )


class CheckerInfoMessage(BaseModel):
    service_name: str
    flag_variants: int
    noise_variants: int
    havoc_variants: int
    exploit_variants: int
    test_variants: int = 0


class CheckerResultMessage(BaseModel):
    result: CheckerTaskResult
    message: str | None = None
    attack_info: str | None = None
    flag: str | None = None


class CheckerTaskMessage(BaseModel):
    task_id: int
    method: CheckerMethod
    address: str
    team_id: int
    team_name: str
    current_round_id: int
    related_round_id: int
    flag: str | None = None
    variant_id: int
    timeout: int
    round_length: int
    task_chain_id: str
    flag_regex: str | None = None
    flag_hash: str | None = None
    attack_info: str | None = None


class EnoLogMessage(BaseModel):
    tool: str
    type: str
    severity: str
    severity_level: int
    timestamp: str
    message: str
    module: str | None
    function: str | None
    service_name: str | None
    task_id: int | None
    method: str | None
    team_id: int | None
    team_name: str | None
    current_round_id: int | None
    related_round_id: int | None
    flag: str | None
    variant_id: int | None
    task_chain_id: str | None
    flag_regex: str | None
    flag_hash: str | None
    attack_info: str | None
