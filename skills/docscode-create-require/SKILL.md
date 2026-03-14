---
name: docscode-create-require
description: 基于现有项目和简要需求描述创建或更新 docs/requirements 下的详细需求文档与测试标准。Use when the user wants require.md and test.md drafted or refined, but does not want implementation changes.
---

# docscode-create-require

将简要需求整理成可执行的 `require.md` 与 `test.md`，建立需求、验收与测试之间的追踪关系。

这个 skill 只编写需求文档，不实现功能，不修改代码。

## Preconditions

开始前确认以下结构存在：

```text
docs/
  requirements/
    archive/
```

如果骨架缺失，先使用 `docscode-init-require` 初始化，再继续当前工作。

## Input Sources

优先使用以下信息构建需求：

- 用户当前提供的简要需求描述
- 已存在的 `docs/requirements/<folder>/require.md`
- 已存在的 `docs/requirements/<folder>/test.md`
- `docs/PRD.md`
- `docs/ARCHITETUCTURE.md`
- `docs/API.md`
- `docs/CURRENT.md`
- `AGENTS.md`

必须显式区分：

- 已观察到的事实
- 基于事实的推断
- 待用户确认的假设

## Target Resolution

- 如果用户给出 `docs/requirements/<folder>/`，直接使用该目录。
- 如果用户给出 `require.md` 或 `test.md` 路径，使用其父目录。
- 如果用户给出的是已有主题名，优先复用最匹配的现有目录。
- 如果没有匹配目录，则创建新的 kebab-case 目录名。
- 不要创建重复需求目录。

## Writing Rules

### require.md

至少覆盖这些章节：

- 背景与目标
- 用户与场景
- 范围
- 功能需求
- 非功能约束
- API 影响
- 架构影响
- 当前状态与差距
- 验收标准
- 风险与未决问题

编号规则：

- 功能需求使用 `REQ-001`、`REQ-002`
- 验收标准使用 `AC-001`、`AC-002`
- 除非结构显著变化，不重排既有编号

### test.md

至少覆盖这些章节：

- 测试目标与范围
- 环境与前置条件
- 追踪矩阵
- 关键场景测试
- 边界与失败测试
- 回归范围
- 未覆盖风险与未决问题

编号规则：

- 测试用例使用 `TC-001`、`TC-002`
- 每个关键 `REQ-*` 至少映射到一个 `TC-*`
- 每个关键 `AC-*` 也应被覆盖，或记录阻塞原因

## Ambiguity Handling

- 如果业务目标、范围边界、验收标准、权限或外部集成不清晰，先问一个最关键的问题。
- 如果不确定项不会阻断主结构，继续产出草案，并将其记录到“风险与未决问题”。
- 不要把未经确认的交互规则、匹配规则、默认值或权限规则写成正式 `REQ-*`、`AC-*` 或 `TC-*`。

## Guardrails

- 只允许修改 `docs/requirements/<folder>/` 内的 `require.md` 与 `test.md`。
- 不修改代码、脚本、配置、测试代码或 `docs/requirements` 之外的文件。
- 不把需求撰写和功能实现混在一起。
- 保持 `require.md` 与 `test.md` 同步更新。

## Output

完成后报告：

- 更新或创建了哪个 `docs/requirements/<folder>/`
- `require.md` 与 `test.md` 是否已同步更新
- 本次新增或调整了哪些关键 `REQ-*`
- 本次新增或调整了哪些关键 `AC-*`
- 当前测试覆盖了哪些关键 `REQ-*` 与 `AC-*`
- 仍有哪些待确认项
- 哪些上下文文件为空或缺失
- 明确说明未实现需求、未修改代码、未修改 `docs/requirements` 之外的文件
