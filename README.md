# Docscode

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](./LICENSE)
[![Validate Skills](https://github.com/ikunycj/docscode/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/ikunycj/docscode/actions/workflows/validate-skills.yml)
[![Codex Skills](https://img.shields.io/badge/Codex-Skills-1f6feb)](./skills)

`Docscode` 是一个面向中文需求文档工作流的开源 Skills 仓库，专门为 Codex / agent 场景提供可复用的 requirements 文档能力。

它聚焦一件事：把 `docs/requirements/` 这套文档工作流做成可以安装、组合、维护和迭代的 Skills，而不是零散提示词。

## Why Docscode

- 面向真实仓库：围绕 `docs/requirements/`、`require.md`、`test.md` 组织工作流
- 强约束输出：强调范围边界、追踪关系、归档规则和最小副作用
- 适合团队协作：用 GitHub 仓库、PR、Issue、Release、CI 维护 Skills
- 可按需安装：每个 Skill 都可以单独分发和安装

## Included Skills

| Skill | Purpose |
| --- | --- |
| `docscode-init-require` | 初始化 `docs/`、`docs/requirements/` 和基础 Markdown 骨架 |
| `docscode-create-require` | 基于简要需求创建或更新 `require.md` 与 `test.md` |
| `docscode-archive-require` | 归档已完成、废弃或不再维护的 requirement 目录 |

## Quick Start

推荐通过 GitHub 仓库路径安装单个 Skill。

安装 `docscode-init-require`：

```bash
python install-skill-from-github.py \
  --repo ikunycj/docscode \
  --path skills/docscode-init-require \
  --ref master
```

安装 `docscode-create-require`：

```bash
python install-skill-from-github.py \
  --repo ikunycj/docscode \
  --path skills/docscode-create-require \
  --ref master
```

安装 `docscode-archive-require`：

```bash
python install-skill-from-github.py \
  --repo ikunycj/docscode \
  --path skills/docscode-archive-require \
  --ref master
```

也可以直接使用 GitHub URL：

```bash
python install-skill-from-github.py \
  --url https://github.com/ikunycj/docscode/tree/master/skills/docscode-create-require
```

建议：

- 日常试用可以跟 `master`
- 面向团队或生产环境时，优先使用 release tag
- 安装后重启 Codex，以确保新 Skill 被正确加载

## Repository Layout

```text
skills/
  docscode-archive-require/
  docscode-create-require/
  docscode-init-require/
scripts/
  validate_skills.py
.github/workflows/
  validate-skills.yml
```

说明：

- `skills/<skill-name>/` 是实际发布单元
- `agents/openai.yaml` 提供 UI 展示所需元数据
- `scripts/validate_skills.py` 用于仓库级结构校验

## Quality Checks

本仓库使用 GitHub Actions 对 Skill 结构做基础校验。

本地执行：

```bash
python scripts/validate_skills.py
```

当前会检查：

- 每个 Skill 是否存在 `SKILL.md`
- `SKILL.md` frontmatter 是否只包含 `name` 与 `description`
- Skill 名称是否为 hyphen-case，且与目录名一致
- 每个 Skill 是否存在 `agents/openai.yaml`

## Versioning And Releases

推荐维护方式：

1. 通过 PR 合并 Skill 变更
2. 使用 Issue 讨论新增 Skill、触发词和边界约束
3. 用 tag / Release 发布稳定版本，例如 `v0.1.0`
4. 在 Release Notes 中记录新增 Skill、行为变化和兼容性影响

如果你是使用方，建议优先安装 release tag，而不是长期跟随分支头部。

## Contributing

欢迎提交：

- 新的 requirements 工作流 Skill
- 已有 Skill 的触发词和 guardrails 改进
- 更清晰的 `SKILL.md` 结构与示例
- 校验脚本和分发流程优化

提交前建议：

```bash
python scripts/validate_skills.py
```

并确保：

- Skill 目录结构完整
- `SKILL.md` 触发描述准确
- 不把仓库级文档塞进单个 Skill 目录

## License

本项目使用 [MIT License](./LICENSE)。
