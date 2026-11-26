"""
check that the workflow entry point can call cpg-flow
"""

import inspect
import sys

from workflow_name import run_workflow as entry_point

from cpg_flow import workflow


def test_cli_main_passes_what_run_workflow_requires(monkeypatch):
    """
    cli_main should call cpg-flow's run_workflow with arguments that method accepts
    """
    calls = []

    def fake_run_workflow(*args, **kwargs):
        # raises a TypeError if a required argument is missing
        inspect.signature(workflow.run_workflow).bind(*args, **kwargs)
        calls.append(kwargs)

    monkeypatch.setattr(entry_point, 'run_workflow', fake_run_workflow)
    monkeypatch.setattr(sys, 'argv', ['run_workflow'])

    entry_point.cli_main()

    assert len(calls) == 1
