<!-- Save to: storybook_primordial_soup/.gitignore.md -->

# 🧹 .gitignore – Primordial Soup

This file describes which files and folders should be ignored by version control.

It corresponds to a standard `.gitignore` but is written in Markdown for documentation or review purposes.  
Use it alongside the actual `.gitignore` file in the project root.

---

## 📂 Ignored Folders

- `.venv/` – Local virtual environment (not portable across machines)
- `__pycache__/` – Python cache directories
- `.mypy_cache/` – Static analysis cache
- `.pytest_cache/` – Test framework cache
- `.vscode/` – Editor-specific settings (optional, but often excluded)

---

## 📄 Ignored Files

- `*.pyc` – Compiled Python files
- `*.pyo`
- `*.log` – Logs from scripts or play sessions
- `*.tmp` – Temporary files
- `*.DS_Store` – macOS directory metadata
- `Thumbs.db` – Windows Explorer cache file

---

## 📄 Not Ignored (Important)

- `requirements.txt`
- `README.md`
- `documentation_model.md`
- All `.md` game design and gameplay files
- All `.py` code used in automation or game infrastructure

---

## ✨ Reminder

This `.gitignore.md` is for **documentation** only.  
To activate ignoring behavior, ensure the real `.gitignore` file exists with matching rules.
