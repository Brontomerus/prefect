import pytest
import os
from pathlib import Path
import subprocess
import prefect

examples_dir = Path(__file__).parents[1] / "examples"


def test_examples_exist():
    assert examples_dir.exists()
    assert len(os.listdir(examples_dir)) > 0


@pytest.mark.parametrize("f", os.listdir(examples_dir))
def test_all_examples_run_without_error(f):
    subprocess.check_call(["python", str(examples_dir / f)])
