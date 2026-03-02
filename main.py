"""Speckle Automate function for digital tissue analysis.

Fetches the latest version of a model, calculates KPIs,
and sends results to a target model.
"""

import os
import sys

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from speckle_automate import (
    AutomateBase,
    AutomationContext,
    execute_automate_function,
)

from application.run_application import run_application


class FunctionInputs(AutomateBase):
    """Function inputs for digital tissue automate.
    
    Currently uses hardcoded configuration from config.py.
    """
    pass


def automate_function(
    automate_context: AutomationContext,
    function_inputs: FunctionInputs,
) -> None:
    """Execute the digital tissue automate function.
    
    Args:
        automate_context: Speckle Automate context with model data and client
        function_inputs: Function input parameters
    """
    try:
        # Call the business logic with the automate context
        run_application(automate_context, function_inputs, None)
        automate_context.mark_run_success("Digital tissue analysis completed successfully.")
    except Exception as e:
        automate_context.mark_run_exception(f"Error during analysis: {str(e)}")


if __name__ == "__main__":
    execute_automate_function(automate_function, FunctionInputs)