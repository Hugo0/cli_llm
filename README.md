little CLI tool for accessing LLMs quickly


add this to .bashrc:

```

llm() {
    source ~/Dropbox/Programs/Settings\ &\ Commands/cli_llm/venv/bin/activate
    python ~/Dropbox/Programs/Settings\ &\ Commands/cli_llm/cli_llm.py "$@"
    deactivate
}
```