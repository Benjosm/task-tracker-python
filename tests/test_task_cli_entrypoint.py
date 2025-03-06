# tests/test_task_cli_entrypoint.py

import subprocess
import sys
import pytest

def test_console_script_entry_point():
    # Verify the console script is not available when not installed
    with pytest.raises(FileNotFoundError):
        subprocess.run(
            ['taskman', '--help'],  # Execute 'taskman' directly
            capture_output=True,
            text=True,
            check=True
        )
