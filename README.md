Supplemental [`pre-commit`](https://pre-commit.com) hook to run `cargo clippy --fix`,
silencing its stderr unless an error prevents Clippy from exiting correctly.
Intended to be used together with regular `cargo clippy` call that would list
warnings as usual.
Since there seems to be no way to make `--fix` explain what and why it fixes.

# How to use

Add the hook to your `.pre-commit-config.yaml` __*after*__ your regular Clippy hook.
Order is important as `pre-commit` runs hooks one by one in the way they were listed
in the config file.
```yaml
repos:
  - repo: https://github.com/doublify/pre-commit-rust
    rev: v1.0
    hooks:
      - id: clippy
  - repo: https://github.com/Artalus/pre-commit-clippy-fix
    rev: v0.1
    hooks:
      - id: clippy-fix
```
- If Clippy has nothing to fix, it will exit with code 0 and the hook will succeed.
- If there were any changes applied, Clippy still will exit with 0, but the hook
will fail detecting a change in workdir:
```
clippy fix...............................................................Failed
- hook id: clippy-fix
- duration: 2.12s
- files were modified by this hook
```
- If Clippy actually fails with non-zero exit code, the hook will dump the stderr:
```
clippy fix...............................................................Failed
- hook id: clippy-fix
- duration: 0.25s
- exit code: 101

cargo clippy --fix --allow-staged exited with 101; STDERR was:

error: invalid table header
expected `.`, `]`
 --> Cargo.toml:1:11
  |
1 | [workspace
  |           ^
```

As with any other `pre-commit` hook, you can use `args` to pass additional
arguments to Clippy:
```yaml
      - id: clippy-fix
        args: [--all-targets, --no-deps, --, -D, warnings]
```
