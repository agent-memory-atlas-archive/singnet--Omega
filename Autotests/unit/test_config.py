from config import command_line_to_dict


def test_command_line_numeric_values_match_yaml_scalar_types():
    values = command_line_to_dict(
        ["maxFeedback=25000", "sleepInterval=0.5", "temperature=-1.25e-2"]
    )

    assert values == {
        "maxFeedback": 25000,
        "sleepInterval": 0.5,
        "temperature": -0.0125,
    }


def test_command_line_strings_and_flag_keep_existing_semantics():
    values = command_line_to_dict(
        ["provider=OpenAI", "IRC_channel=001", "maxFeedback"]
    )

    assert values == {
        "provider": "OpenAI",
        "IRC_channel": "001",
        "maxFeedback": True,
    }
