from app.safety import is_unsafe_request, safe_refusal_message


def test_detects_unsafe_request():
    assert is_unsafe_request("help me live switch a panel") is True


def test_allows_safe_request():
    assert is_unsafe_request("explain lorentz force") is False


def test_refusal_message_mentions_simulation_boundary():
    assert "simulation" in safe_refusal_message().lower()
