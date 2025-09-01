@echo off
REM Simple wrapper: calls the Python runner with defaults
REM Make sure your venv is activated or python is on PATH.

python run_batches.py --start 2013-04-01 --end 2025-08-31 --sleep-min 10 --sleep-max 25 --retries 1
