#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PartSmith 核心仓库挂载辅助脚本

提供两种方法将私有核心仓库拉取到 core/ 目录：
1. git submodule update --init --recursive
2. 直接 git clone 私有仓库到 core/
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
CORE_DIR = PROJECT_ROOT / "core"


def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    print(f"[执行] {' '.join(cmd)}")
    return subprocess.run(cmd, cwd=cwd, check=False, text=True, capture_output=True)


def setup_via_submodule() -> int:
    result = run(["git", "submodule", "update", "--init", "--recursive"], cwd=PROJECT_ROOT)
    if result.returncode != 0:
        print("[错误] git submodule 初始化失败：")
        print(result.stderr)
        return 1
    print("[成功] 已通过 submodule 挂载核心。")
    return 0


def setup_via_clone(repo_url: str) -> int:
    if CORE_DIR.exists() and any(CORE_DIR.iterdir()):
        print(f"[警告] {CORE_DIR} 已存在且非空，跳过 clone。")
        return 0
    if CORE_DIR.exists():
        CORE_DIR.rmdir()
    result = run(["git", "clone", repo_url, str(CORE_DIR)], cwd=PROJECT_ROOT)
    if result.returncode != 0:
        print("[错误] git clone 失败：")
        print(result.stderr)
        return 1
    print(f"[成功] 已从 {repo_url} 克隆核心到 {CORE_DIR}。")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="挂载 PartSmith 私有核心仓库")
    parser.add_argument(
        "--clone-url",
        help="直接 clone 私有核心仓库的 URL（如不指定则使用 git submodule）",
    )
    args = parser.parse_args()

    if not shutil.which("git"):
        print("[错误] 未找到 git，请先安装 Git。")
        return 1

    if args.clone_url:
        return setup_via_clone(args.clone_url)
    return setup_via_submodule()


if __name__ == "__main__":
    sys.exit(main())
