import sys
import json
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from application.run_application import run_application

def main():
    run_application()

if __name__ == "__main__":
    main()

def automate_entrypoint():
    """
    Contract entrypoint for Speckle Automate compatibility.
    Usage: python src/main.py <automation_context_json> <function_inputs_json> <token>
    """
    if len(sys.argv) == 4:
        automation_context = json.loads(sys.argv[1])
        function_inputs = json.loads(sys.argv[2])
        token = sys.argv[3]
        # Pass these to your business logic as needed
        run_application(automation_context, function_inputs, token)
    else:
        # Fallback to legacy main
        run_application()

if __name__ == "__main__":
    automate_entrypoint()