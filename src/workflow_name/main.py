#!/usr/bin/env python3

"""
This is the main entry point for the workflow.
"""

from argparse import ArgumentParser

from cpg_flow.workflow import run_workflow

from workflow_name.stages import DoSomethingGenericWithBash, PrintPreviousJobOutputInAPythonJob


def cli_main():
    """
    CLI entrypoint
    """
    parser = ArgumentParser()
    parser.add_argument('--dry_run', action='store_true', help='Dry run')
    args = parser.parse_args()

    stages = [DoSomethingGenericWithBash, PrintPreviousJobOutputInAPythonJob]

    run_workflow(stages=stages, dry_run=args.dry_run)


if __name__ == '__main__':
    cli_main()
