from app.controllers.voice import parse_voice_command


def test_parse_current_command():
    parsed = parse_voice_command("Bruce, set current to 800")
    assert parsed["intent"] == "update_parameters"
    assert parsed["current_a"] == 800.0


def test_parse_distance_mm_command():
    parsed = parse_voice_command("distance to 10 mm")
    assert parsed["distance_m"] == 0.01


def test_parse_layer_intent():
    parsed = parse_voice_command("show me the scientist layer")
    assert parsed["intent"] == "show_scientific"
