#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""公开仓库占位测试。"""

from __future__ import annotations

import sys
from pathlib import Path


def test_core_directory_does_not_contain_source_files() -> None:
    """core/ 应为 submodule 指针，不应包含 .py 源码。"""
    core_dir = Path(__file__).resolve().parent.parent / "core"
    if not core_dir.exists():
        return
    python_files = list(core_dir.rglob("*.py"))
    assert not python_files, f"公开仓库不应包含 core/ 下的 .py 文件: {python_files}"


def test_demo_script_runs() -> None:
    """示例脚本至少可以导入。"""
    examples_dir = Path(__file__).resolve().parent.parent / "examples"
    sys.path.insert(0, str(examples_dir))
    try:
        import demo_cad_prompt
    finally:
        sys.path.pop(0)
    assert callable(demo_cad_prompt.main)
