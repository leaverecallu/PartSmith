#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PartSmith 调用示例

本脚本演示如何检查私有核心是否已挂载，并模拟调用生成接口。
实际接口由 core/ 子模块提供。
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def ensure_core() -> Path:
    """确认 core/ 私有核心已挂载。"""
    core_dir = Path(__file__).resolve().parent.parent / "core"
    if not core_dir.exists() or not any(core_dir.iterdir()):
        print("[错误] 未找到私有核心 core/ 目录。")
        print("请执行以下命令初始化子模块：")
        print("    git submodule update --init --recursive")
        print("或直接运行：")
        print("    python scripts/setup_core.py")
        sys.exit(1)
    return core_dir


def generate_cad(prompt: str) -> dict[str, object]:
    """模拟调用 PartSmith 生成接口。"""
    # 实际项目中，这里会导入 core/src/partsmith 并调用 Agent
    print(f"[模拟调用] prompt={prompt!r}")
    return {
        "success": True,
        "prompt": prompt,
        "output_file": "outputs/demo_part.step",
        "message": "生成完成（演示模式，未实际执行 LLM）",
    }


def main() -> int:
    core_dir = ensure_core()
    print(f"[信息] 私有核心已挂载: {core_dir}")

    prompt = "创建一个 M8 螺栓"
    result = generate_cad(prompt)
    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
