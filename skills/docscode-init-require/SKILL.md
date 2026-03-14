---
name: docscode-init-require
description: 初始化 docscode 需求文档工作区。Use when a repo is missing docs, docs/requirements, archive, or requirement markdown skeletons, and only scaffolding should be created without drafting requirement content.
---

# docscode-init-require

初始化 `docscode` 的需求文档目录与空白 Markdown 骨架。

这个 skill 只负责搭建结构，不负责撰写需求内容或实现功能。

## Workflow

1. 检查 `docs/`、`docs/requirements/`、`docs/requirements/archive/` 是否存在。
2. 仅创建缺失目录。
3. 检查公共文档是否存在：`docs/PRD.md`、`docs/ARCHITETUCTURE.md`、`docs/API.md`、`docs/CURRENT.md`。
4. 仅在文件缺失时创建空白骨架。
5. 如果用户明确指定需求目录，再补齐 `docs/requirements/<folder>/require.md` 与 `test.md`。
6. 输出本次新建内容与跳过项。

## Scope Selection

- 如果用户只说“初始化环境”或“初始化目录”，只创建公共工作区，不新建业务需求目录。
- 如果用户给出 `docs/requirements/<folder>/`，只补齐该目录中的缺失骨架。
- 如果用户给出 `require.md` 或 `test.md`，以其父目录为目标。
- 如果用户要求为某个主题初始化需求目录，生成简短 kebab-case 目录名。
- 如果已存在匹配目录，只补齐缺失文件，不重复创建。
- 不要在 `docs/requirements/archive/` 下创建进行中的需求目录。

## Skeleton Content

新建文件必须是空白骨架，不预写具体业务内容。

推荐占位内容：

- `docs/PRD.md`: `# PRD`
- `docs/ARCHITETUCTURE.md`: `# ARCHITETUCTURE`
- `docs/API.md`: `# API`
- `docs/CURRENT.md`: `# CURRENT`
- `require.md`: 最小需求章节骨架
- `test.md`: 最小测试章节骨架

## Guardrails

- 只创建缺失目录和缺失文件。
- 不覆盖、不追加、不重排已存在文件。
- 不推断业务逻辑，不扫描代码来补写需求。
- 不实现功能，不修改代码，不改动 `docs/` 之外的路径。
- 初始化完成后立即停止，不继续写需求内容。

## Output

完成后报告：

- 本次创建了哪些目录
- 本次创建了哪些文件
- 哪些目标已存在并被跳过
- 是否存在路径冲突或输入缺失
- 明确说明未改写任何已存在文件
- 如需撰写需求内容，下一步应使用 `docscode-create-require`
