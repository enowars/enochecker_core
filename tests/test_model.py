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
        attack_info="abc",
        flag="TESTFLAG",
    )
    msg_ = {
        "result": "INTERNAL_ERROR",
        "message": "Internal error occured",
        "attackInfo": "abc",
        "flag": "TESTFLAG",
    }
    assert msg == CheckerResultMessage.model_validate_json(
        json.dumps(msg_), strict=True
    )
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
        "taskId": 123,
        "method": "exploit",
        "address": "10.32.1.2",
        "teamId": 42,
        "teamName": "Team",
        "currentRoundId": 1337,
        "relatedRoundId": 1336,
        "flag": "TESTFLAG",
        "variantId": 2,
        "timeout": 15,
        "roundLength": 60,
        "taskChainId": "chain_id",
        "flagRegex": None,
        "flagHash": None,
        "attackInfo": None,
    }
    assert msg == CheckerTaskMessage.model_validate_json(json.dumps(msg_), strict=True)
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
        "serviceName": "Dummy Service",
        "flagVariants": 3,
        "noiseVariants": 2,
        "havocVariants": 2,
        "exploitVariants": 0,
        "testVariants": 3,
    }
    assert msg == CheckerInfoMessage.model_validate_json(json.dumps(msg_), strict=True)
    assert json.loads(msg.model_dump_json()) == msg_
