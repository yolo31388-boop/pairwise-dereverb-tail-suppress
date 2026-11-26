import pytest
import av.dereverb as mod

CASES = [
    ("rt60_time_varying", (1,)),
    ("early_reflection_preserve", (1,)),
    ("inference_delay_adapt", (1,)),
    ("channel_order_calib", (1,)),
    ("monitor_latency_comp", (1,)),
    ("tail_state_migrate", (1,)),
    ("load_reverb_audio", (1,)),
    ("estimate_reverb", (1,)),
    ("suppress_tail", (1,)),
    ("present_dereverb", (1,)),
    ("validate_dereverb", (1,)),
    ("metrics_dereverb", (1,)),
    ("audit_dereverb", (1,)),
    ("fallback_dereverb", (1,)),
    ("determinism_dereverb", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
