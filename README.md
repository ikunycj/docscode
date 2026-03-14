<div align="center">

# Docscode —— 面向文档编程

# **Markdown 是AI时代的源代码**

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](./LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/ikunycj/docscode?style=social)](https://github.com/ikunycj/docscode)
[![Last Commit](https://img.shields.io/github/last-commit/ikunycj/docscode)](https://github.com/ikunycj/docscode/commits/master)

面向文档驱动编程工作模式的开源 Skills 仓库。  
规范化个人新项目需求编写流程，把“不清晰的需求”编程“明确记录的需求+测试方案”。

</div>

---

## Overview

`Docscode` 不是一组零散提示词，而是一套围绕需求文档生命周期设计的 Skills：

- `docscode-init-require`: 初始化文档工作区
- `docscode-create-require`: 把模糊需求整理成 `require.md` / `test.md`
- `docscode-archive-require`: 将已完成或废弃的 requirement 目录安全归档

它适合这类场景：

- 新项目，需求模糊，只有大致的蓝图
- 想要快速利用AI生成MVP产品，但是很难控制AI生成质量

## AI Coding Best Practices

1. **Docscode Skills**：负责把需求文档生命周期标准化，尤其是 `docs/requirements/` 这层文档工作
2. **OpenSpec**：把具体需求拆成设计草图 `proposal`、`specs`、`design`、`tasks`


相关项目：

- [OpenSpec](https://github.com/Fission-AI/OpenSpec)

### Documentation-Oriented Programming

这套工作流的核心核心是：Markdown 是AI时代的源代码。

- `README.md` 解释项目定位
- `AGENTS.md` 告诉 AI 工具项目规则和边界
- `docs/PRD.md`、`docs/CURRENT.md`、`docs/ARCHITETUCTURE.md`、`docs/API.md` 提供长期上下文
- `docs/requirements/<requirement>/require.md` 和 `test.md` 则描述某次具体需求

推荐目录结构：

```text
README.md                     # 项目介绍
AGENTS.md                     # 给 AI 编程工具阅读的项目概览和约束
.codex/
  rules/                      # AI 规则、电子围栏、宏命令
docs/
  requirements/
    archive/                  # 已完成需求归档
    requirename-date/         # 某次具体需求
      require.md              # 需求描述
      test.md                 # 测试用例与验证说明
  PRD.md                      # 产品宏观描述，最终形态
  CURRENT.md                  # 当前产品状态
  ARCHITETUCTURE.md           # 系统架构
  API.md                      # 项目 API 文档
```

`Docscode` 的三个 Skills，本质上就是在帮助你维护这套文档结构，而不是绕过它。

### Test-Oriented Development

除了“面向文档”，另一条关键原则是“面向测试”。

推荐把 `test.md` 当成需求交付的一部分，而不是最后补的附件。  
在实现阶段，可以自然衔接到 TDD 的经典循环：

1. `Red`：先写一个会失败的测试
2. `Green`：写最少量代码让测试通过
3. `Refactor`：在测试保护下优化结构，不改变行为

这也是为什么 `docscode-create-require` 会强调 `require.md` 和 `test.md` 一起维护，而不是只写一份看起来完整的需求文档。

## Skill Catalog

| Skill | What it does | Typical use case |
| --- | --- | --- |
| `docscode-init-require` | 初始化 `docs/`、`docs/requirements/`、`archive/` 和 Markdown 骨架 | 仓库还没有 requirements 文档工作区 |
| `docscode-create-require` | 生成或更新 `require.md` 与 `test.md`，建立 `REQ / AC / TC` 追踪关系 | 只有简要需求，需要落成结构化文档 |
| `docscode-archive-require` | 将完成、废弃或不再维护的 requirement 目录移入 `archive/` | 功能已结束维护，需要关闭对应需求目录 |

t.md`
3. 需求完成或废弃后，用 `docscode-archive-require` 做归档

## Recommended End-to-End Workflow

如果你采用 `OpenSpec + CLI Agent + Docscode Skills` 这套组合，可以按下面的顺序工作：

1. 基于 `PRD`、`CURRENT`、`ARCHITETUCTURE`、`API`、`AGENTS` 生成某次需求的 `requirename-date/`
2. 使用 `docscode-create-require` 补齐并细化 `require.md` 与 `test.md`
3. 执行 OpenSpec 的 `opsx-propose`，生成 `proposal`、`spec`、`design`、`tasks`
4. 再执行 `opsx-apply` 落地代码，并依据 `test.md` 进行验证
5. 需求完成后，使用 `opsx-archive`和`docscode-archive-require` 归档对应目录

对应关系可以理解为：

- `Docscode`：管理需求文档输入与归档
- `OpenSpec`：管理变更设计与任务拆分
- `Agent`：管理实际实现与验证过程

## Download And Install

这些 Skills 以普通目录的形式发布，不依赖 Codex 专用安装脚本。  
你可以用任何支持本地 Skill 目录、Agent Recipe、Prompt Pack 或工作流模板导入的工具来使用它们。

### Option 1: Download ZIP

1. 打开仓库首页：`https://github.com/ikunycj/docscode`
2. 点击 `Code -> Download ZIP`
3. 解压后进入 `skills/`
4. 选择你需要的 Skill 目录，例如：
   - `skills/docscode-init-require`
   - `skills/docscode-create-require`
   - `skills/docscode-archive-require`
5. 将该目录导入你的本地 AI 工具或工作流系统

### Option 2: Clone The Repository

```bash
git clone https://github.com/ikunycj/docscode.git
```

然后从仓库里的 `skills/` 目录选择需要的 Skill。

### Option 3: Sparse Checkout A Single Skill

```bash
git clone --filter=blob:none --no-checkout https://github.com/ikunycj/docscode.git
cd docscode
git sparse-checkout init --cone
git sparse-checkout set skills/docscode-create-require
git checkout master
```

如果你只想拿一个 Skill，这种方式比完整 clone 更轻。

### Option 4: Copy The Skill Folder Into Your Tool

以 `docscode-create-require` 为例，你真正需要的只是这个目录：

```text
skills/docscode-create-require/
```

把它复制到你的工具约定的本地 Skills 目录，或在你的平台里按“导入本地目录”的方式接入即可。

如果你的工具不支持 Skills 目录，也可以直接把 `SKILL.md` 作为工作流规范文件使用。

### What To Import

每个 Skill 最少包含：

```text
<skill-name>/
  SKILL.md
```
通常情况下：
- `SKILL.md` 是核心说明文件
- 真正的发布单元就是 `skills/<skill-name>/`


## Example Prompts

`docscode-init-require`

```text
Use $docscode-init-require to scaffold docs/requirements for this repository.
```

`docscode-create-require`

```text
Use $docscode-create-require to draft require.md and test.md for a new export feature under docs/requirements.
```

`docscode-archive-require`

```text
Use $docscode-archive-require to archive docs/requirements/user-export after the feature is retired.
```

## Where Docscode Fits

如果把整个 AI Coding 流程拆开看，`Docscode` 主要负责最前面的“需求输入质量”与最后面的“需求生命周期收尾”：

- 在编码前，把模糊想法沉淀成结构化需求
- 在实现中，为 OpenSpec 和代码实现提供稳定输入
- 在完成后，把历史需求有边界地归档，不污染进行中的工作区

它不替代 OpenSpec，也不替代代码实现型 Agent。  
它更像是整个流程里负责需求文档层的那一层基础设施。

## Design Principles

这些 Skills 不是为了“多写文档”，而是为了“少写错文档”。

核心原则：

- **只在允许的路径内工作**
- **区分事实、推断和待确认项**
- **require.md 与 test.md 必须一起维护**
- **归档是归档，不混入撰写或实现**
- **初始化是初始化，不顺手补全业务内容**

## Compatibility Notes

这个仓库使用“目录即分发单元”的方式组织 Skills，因此不绑定单一平台。

你可以这样理解它的兼容性：

- 适合支持本地 Skill / Agent / Prompt 目录导入的工具
- 适合作为团队内部 AI 工作流模板仓库直接引用
- 也适合手工复制 `SKILL.md` 到你自己的规则系统中

如果某个工具只认自己的专用格式，你也可以把本仓库作为上游来源，再做一层适配转换。


## FAQ

### 这是提示词仓库，还是 Skill 仓库？

这是 Skill 仓库。核心交付物是 `skills/<skill-name>/SKILL.md`，而不是一段单次使用的 prompt。

### 适合什么项目？

适合希望在仓库内维护结构化需求文档的项目，尤其适合已经采用 `docs/requirements/` 目录约定的团队。

### 为什么强调 `require.md` 和 `test.md` 一起维护？

因为这个仓库的目标不是只写“看起来完整”的文档，而是维持需求、验收和测试之间的追踪关系。

## License

本项目使用 [MIT License](./LICENSE)。
