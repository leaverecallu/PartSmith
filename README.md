# PartSmith

> 自然语言驱动的参数化 CAD 生成工具

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![Issues](https://img.shields.io/github/issues/<username>/PartSmith.svg)](https://github.com/<username>/PartSmith/issues)

PartSmith 让你用日常语言描述零件，即可生成可直接制造的 STEP/STL 模型。无论你是机械工程师、硬件创业者还是 Maker，都可以快速把想法变成可加工的 3D 文件。

---

## ✨ 功能亮点

- **自然语言生成 CAD**：输入 "创建一个 M8 螺栓"，直接得到参数化模型
- **多种标准件支持**：螺栓、螺母、法兰、齿轮、轴承座、圆柱、球体、圆管等
- **本地 LLM 友好**：支持 Ollama 等本地模型，保护设计隐私
- **Web UI 界面**：浏览器中输入描述、调整参数、预览并下载模型
- **几何校验**：自动检查封闭性、壁厚、自相交等问题
- **多格式导出**：STEP、STL 等常见 3D 格式一键下载

---

## 📦 安装

```bash
pip install partsmith
```

或者从 Release 页面下载预构建的安装包：

```bash
# Windows
PartSmith-x.y.z-win64.exe

# macOS / Linux（后续支持）
```

> 首次使用需要挂载私有核心仓库，详见 [配置核心](#-配置核心)。

---

## 🚀 快速开始

### 命令行

```bash
partsmith --prompt "创建一个 M8 螺栓"
```

### Web UI

```bash
partsmith --ui
```

然后在浏览器中打开 `http://127.0.0.1:7860`，输入描述并生成模型。

---

## 🖼️ 界面预览

![PartSmith Web UI](./docs/assets/ui_preview_placeholder.png)

---

## 📁 示例

见 [`examples/`](./examples/) 目录：

- [`examples/first_part.step`](./examples/first_part.step) — STEP 格式演示模型
- [`examples/first_part.stl`](./examples/first_part.stl) — STL 格式演示模型
- [`examples/demo_cad_prompt.py`](./examples/demo_cad_prompt.py) — 通过 Python 脚本调用生成接口

---

## ⚙️ 配置核心

PartSmith 的功能核心通过私有仓库以 submodule 形式挂载：

```bash
git submodule update --init --recursive
```

或运行辅助脚本：

```bash
python scripts/setup_core.py
```

详细配置请参考 [`config/config.template.yaml`](./config/config.template.yaml)。

---

## 🛠️ 系统要求

- Windows 10/11（当前主要支持平台）
- Python 3.11+
- Ollama 或兼容 OpenAI API 的本地 LLM 服务

---

## 🤝 反馈与支持

遇到问题或有新想法？欢迎提交 GitHub Issue：

👉 [https://github.com/<username>/PartSmith/issues](https://github.com/<username>/PartSmith/issues)

---

## 📄 许可证

本项目公开部分采用 MIT 许可证。核心功能为私有仓库，需授权访问。
