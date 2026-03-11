# Bruce Electrical Laboratory Design Brief

## Objective
Deliver a serious engineering laboratory simulation environment with immersive interaction and layered electrical reasoning.

## Fidelity principle
Models should be educationally realistic, assumption-explicit, and safe-by-design. Full multiphysics fidelity is out of scope for baseline and should be identified where needed.

## Baseline architecture
- Streamlit host UI
- Browser-embedded 3D lab scene (Three.js)
- Modular experiment controllers wired to physics functions
- Voice/text command parser with safety gate
- Layered explanation renderer for every experiment result

## Next extensions
- Rich 3D equipment models and click interactions per instrument
- Browser-native microphone capture bridge and TTS output channel
- Enhanced field overlays and waveform instrumentation
- Scenario presets for fault/transient studies in safe simulation form
