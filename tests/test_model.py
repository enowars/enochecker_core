from enochecker_core import (
    CheckerMethod,
    CheckerResultMessage,
    CheckerTaskMessage,
    CheckerInfoMessage,
    CheckerTaskResult,
)
import json


def test_serialize_result_message():
    msg = CheckerResultMessage(
        result=CheckerTaskResult.INTERNAL_ERROR,
        message="Internal error occured",
        attack_info=None,
        flag=None,
    )
    msg_ = {
        "result": "INTERNAL_ERROR",
        "message": "Internal error occured",
        "attack_info": None,
        "flag": None,
    }
    assert msg == CheckerResultMessage.model_validate_json(json.dumps(msg_))
    assert json.loads(msg.model_dump_json()) == msg_


def test_serialize_task_message():
    msg = CheckerTaskMessage(
        task_id=123,
        method=CheckerMethod.EXPLOIT,
        address="10.32.1.2",
        team_id=42,
        team_name="Team",
        current_round_id=1337,
        related_round_id=1336,
        flag="TESTFLAG",
        variant_id=2,
        timeout=15,
        round_length=60,
        task_chain_id="chain_id",
        flag_regex=None,
        flag_hash=None,
        attack_info=None,
    )
    msg_ = {
        "task_id": 123,
        "method": "exploit",
        "address": "10.32.1.2",
        "team_id": 42,
        "team_name": "Team",
        "current_round_id": 1337,
        "related_round_id": 1336,
        "flag": "TESTFLAG",
        "variant_id": 2,
        "timeout": 15,
        "round_length": 60,
        "task_chain_id": "chain_id",
        "flag_regex": None,
        "flag_hash": None,
        "attack_info": None,
    }
    assert msg == CheckerTaskMessage.model_validate_json(json.dumps(msg_))
    assert json.loads(msg.model_dump_json()) == msg_


def test_serialize_info_message():
    msg = CheckerInfoMessage(
        service_name="Dummy Service",
        flag_variants=3,
        noise_variants=2,
        havoc_variants=2,
        exploit_variants=0,
        test_variants=3,
    )
    msg_ = {
        "service_name": "Dummy Service",
        "flag_variants": 3,
        "noise_variants": 2,
        "havoc_variants": 2,
        "exploit_variants": 0,
        "test_variants": 3,
    }
    assert msg == CheckerInfoMessage.model_validate_json(json.dumps(msg_))
    assert json.loads(msg.model_dump_json()) == msg_
