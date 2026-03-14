---
name: docscode-archive-require
description: 归档 docs/requirements/ 下已完成、废弃或不再维护的需求文件夹。Use when the user asks to archive a requirement, move a requirement folder to archive, or close a docs requirement without editing code.
---

# docscode-archive-require

归档单个 `docs/requirements/<folder>/` 需求文件夹，并保留目录内原始内容。

## Workflow

1. 解析目标目录。
2. 确认目标位于 `docs/requirements/` 下，且不在 `docs/requirements/archive/` 下。
3. 检查 `require.md` 与 `test.md` 是否存在，并记录缺失或明显未完成风险。
4. 仅在目标归档路径不存在时，将整个目录移动到 `docs/requirements/archive/<folder>/`。
5. 输出归档结果、警告和未执行原因。

## Target Resolution

- 优先使用用户明确给出的 `docs/requirements/<folder>/` 路径。
- 如果用户给出的是 `require.md` 或 `test.md`，使用其父目录作为目标。
- 如果用户只给出主题名，在 `docs/requirements/` 下查找最匹配且不在 `archive/` 下的目录。
- 如果存在多个候选，不要猜测，只提出一个最小必要问题。
- 如果目标已经在 `archive/` 下，说明其已归档，不重复移动。

## Guardrails

- 只修改 `docs/requirements/` 内的内容。
- 不要归档多个需求目录，除非用户明确逐个指定。
- 不要覆盖、合并或删除已有归档目录。
- 不要在归档前补写、重写或清理 `require.md`、`test.md`。
- 如果发现明显风险，先记录事实，再在总结中说明推断。

## Warnings To Surface

- 缺少 `require.md` 或 `test.md`
- 文档为空或明显仍在执行中
- 目录可能仍被引用或仍在维护中
- 归档目标已存在，导致无法移动

## Output

完成后报告：

- 原始路径
- 归档路径
- `require.md` 与 `test.md` 是否存在
- 是否发现归档前警告
- 是否因为冲突、目标不存在或已归档而未执行移动
- 明确说明未修改 `docs/requirements` 之外的文件
