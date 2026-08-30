# Current lesson: 3.2 Testing edge cases

**Out of scope:** Databases, web servers, and packaging for distribution. That comes later on the track.

## Section 1: Writing and running scripts
**Start point:** Can use a terminal.
**End goal:** Writes and runs a multi-function script that reads command-line arguments.

### 1.1 Running scripts and functions
**Start point:** Can use a terminal.
**End goal:** Writes a script with two functions where one calls the other, and runs it.

### 1.2 Reading command-line arguments
**Start point:** Can write a multi-function script.
**End goal:** Reads a `--name` argument with `argparse` and uses it in the output.

## Section 2: Project structure and modules
**Start point:** Can write a multi-function script that takes arguments.
**End goal:** Splits code into modules and runs it as a package with `python -m`.

### 2.1 Splitting code into modules
**Start point:** Has a single-file script.
**End goal:** Moves the greeting logic into `greetings/core.py` and imports it from `greetings/__main__.py`.

### 2.2 Running it as a package
**Start point:** Has a `greetings/` package.
**End goal:** Runs the tool with `python -m greetings --name ...` and it behaves the same as before.

## Section 3: Tests with pytest
**Start point:** Has a runnable `greetings` package.
**End goal:** Writes passing pytest tests for the package's core function, including an edge case.

### 3.1 Your first pytest test
**Start point:** Has a `greetings` package.
**End goal:** Writes `tests/test_core.py` with one passing test for `greet(name)` and runs it with `pytest`.

### 3.2 Testing edge cases
**Start point:** Has one passing test.
**End goal:** Adds a second test covering an edge case (empty name) and both tests pass with `pytest`.
