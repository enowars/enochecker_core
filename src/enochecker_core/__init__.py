__all__ = [
    "CheckerTaskResult",
    "CheckerMethod",
    "CheckerInfoMessage",
    "CheckerResultMessage",
    "EnoLogMessage",
    "CheckerTaskMessage",
    "CheckerTaskMessageModel",
]

from enum import StrEnum
from pydantic.alias_generators import to_camel
from pydantic import AliasGenerator, BaseModel as PydanticBaseModel, ConfigDict


class CheckerTaskResult(StrEnum):
    OK = "OK"
    MUMBLE = "MUMBLE"
    OFFLINE = "OFFLINE"
    INTERNAL_ERROR = "INTERNAL_ERROR"


class CheckerMethod(StrEnum):
    PUTFLAG = "putflag"
    GETFLAG = "getflag"
    PUTNOISE = "putnoise"
    GETNOISE = "getnoise"
    HAVOC = "havoc"
    EXPLOIT = "exploit"


class BaseModel(PydanticBaseModel):
    model_config = ConfigDict(
        use_enum_values=True,
        alias_generator=AliasGenerator(alias=to_camel),
        validate_by_name=True,
    )


class CheckerInfoMessage:
    service_name: str
    flag_variants: int
    noise_variants: int
    havoc_variants: int
    exploit_variants: int


class CheckerInfoMessageModel(CheckerInfoMessage, BaseModel):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    pass


class CheckerResultMessage:
    result: CheckerTaskResult
    message: str | None = None
    attack_info: str | None = None
    flag: str | None = None


class CheckerResultMessageModel(CheckerResultMessage, BaseModel):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)


class CheckerTaskMessage:
    task_id: int
    method: CheckerMethod
    address: str
    team_id: int
    team_name: str
    current_round_id: int
    related_round_id: int
    flag: str | None
    variant_id: int
    timeout: int
    round_length: int
    task_chain_id: str
    flag_regex: str | None = None
    flag_hash: str | None = None
    attack_info: str | None = None


class CheckerTaskMessageModel(CheckerTaskMessage, BaseModel):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)


class EnoLogMessage:
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


class EnoLogMessageModel(EnoLogMessage, BaseModel):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
