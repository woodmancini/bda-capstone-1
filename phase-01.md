# Phase 01: Preparation (10 minutes)

## Goal

Set up a clean Python development workspace for the capstone activity.

## Steps

1. Make sure Python is installed on your computer and your GitHub account is ready in your browser.
2. Fork the class repository to your own GitHub account. 
   * Click `Fork`.
   * Select your username as the owner.
   * Click `Create fork`.
3. On your computer, open a new, fresh VS Code window.
4. Clone your fork to your computer.

```bash
git clone https://github.com/YOUR-USERNAME/bda-capstone-1.git
cd bda-capstone-1
```

5. Open the cloned folder in VS Code.

6. Create and activate a virtual environment.

7. Install the dependencies in the `requirements.txt`.

>  [!TIP]
>
> You should work in your own fork because you will not have permission to push changes directly to the instructor repository.

## Create a virtual environment

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Checkpoint

Before moving to Phase 02, confirm that:

- **You cloned your own fork, not the instructor repository.**

  Check your Git remote (you should see your own GitHub username in the remote URL).

  ```bash
  git remote -v
  ```

- The project folder is open in VS Code.
- You are in the correct folder (`bda-capstone-1`)
- Your virtual environment is activated.
- The dependencies were installed without errors.
