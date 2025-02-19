# cpg-flow-pipeline-template
A template repository to use as a base for CPG workflows using the cpg-flow pipeline framework

## Purpose

When migrating workflows from production-pipelines, this template respository structure can be used to start with a
sensible directory structure, and some suggested conventions for naming and placement of files.

```commandline
src
├── workflow_name
│   ├── __init__.py
│   ├── config_template.toml
│   ├── jobs
│   │   └── LogicForAStage.py
│   ├── main.py
│   ├── stages.py
│   └── utils.py
```
