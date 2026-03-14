# Docscode Skills

公开维护的 `docscode` 系列 Codex skills。

这个仓库采用当前较常见的 skill 分发方式：

- GitHub 仓库作为源码与版本来源
- `skills/<skill-name>/` 作为单个 skill 的发布单元
- 用户按 `repo + path` 或 GitHub URL 安装指定 skill
- 用 PR、Issue、Release、CI 做持续维护

## Included Skills

- `docscode-archive-require`
- `docscode-init-require`
- `docscode-create-require`

## Repository Layout

```text
skills/
  docscode-archive-require/
  docscode-init-require/
  docscode-create-require/
scripts/
  validate_skills.py
.github/workflows/
  validate-skills.yml
```

## Install

推荐按仓库路径安装单个 skill，而不是手工复制目录。

示例：

```bash
python install-skill-from-github.py \
  --repo <owner>/<repo> \
  --path skills/docscode-init-require \
  --ref v0.1.0
```

也可以使用 GitHub URL：

```bash
python install-skill-from-github.py \
  --url https://github.com/<owner>/<repo>/tree/v0.1.0/skills/docscode-init-require
```

说明：

- `--ref` 推荐使用 tag 或 release，而不是长期追踪 `main`
- 一次可以安装多个 `--path`
- 安装后通常需要重启 Codex 以加载新 skill

## Maintenance Workflow

建议维护方式：

1. 在 `main` 上开发，所有修改通过 PR 合并
2. 每次改动都运行 `python scripts/validate_skills.py`
3. 重要变更通过 GitHub Issue 讨论触发词、边界与输出格式
4. 对外分发时打 tag，例如 `v0.1.0`
5. 在 Release 中记录新增 skill、触发词调整、兼容性变化

## Local Validation

```bash
python scripts/validate_skills.py
```

校验项：

- `skills/` 下每个 skill 都存在 `SKILL.md`
- `SKILL.md` frontmatter 只包含 `name` 和 `description`
- `name` 为 hyphen-case，且与目录名一致
- 每个 skill 都包含 `agents/openai.yaml`

## Publishing Steps

1. 在 GitHub 新建仓库
2. 将当前目录内容推送到远端
3. 创建首个 tag，例如 `v0.1.0`
4. 在 README 中把 `<owner>/<repo>` 替换成真实仓库名

## Notes

- skill 目录内部只保留 agent 运行所需内容，不放 README、CHANGELOG 等仓库文档
- 版本说明、License、CI 与安装文档统一放在仓库根目录
- 这三个 skill 当前以中文工作流为主，适合中文需求文档场景
