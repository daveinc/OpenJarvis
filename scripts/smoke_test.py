"""Phase 1 smoke test — verify Jarvis SDK talks to Ollama."""
from openjarvis import Jarvis

print("=== Jarvis SDK Smoke Test ===")
print(f"Version: ", end="")

with Jarvis(engine_key="ollama", model="llama3.2:3b") as j:
    print(j.version)

    print("\n[1] ask()...")
    response = j.ask("Say exactly: HOD Jarvis is alive")
    print("Response:", response)

    print("\n[2] list_models()...")
    models = j.list_models()
    print("Models:", models)

    print("\n[3] list_engines()...")
    engines = j.list_engines()
    print("Engines:", engines)

print("\nSmoke test complete.")
