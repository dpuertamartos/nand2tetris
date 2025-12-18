Personal Implementation of nand2tetris following the book `The Elements of Computing Systems`

# Python usage

## Local Development Setup

### Prerequisites

-   Python 3.11+
-   `uv` installed ([`pipx install uv`](https://astral.sh/uv#installation) or `pip install uv`)

### Instructions

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd uvtest
    ```

2.  **Create a virtual environment:**
    ```bash
    uv venv -p 3.11
    ```

3.  **Activate the virtual environment:**
    -   macOS / Linux: `source .venv/bin/activate`
    -   Windows: `.venv\Scripts\activate`

4.  **Install dependencies:**
    This project uses lock files for reproducible builds. We'll install development dependencies, which include everything needed for production.
    ```bash
    # First, compile the dev lock file to ensure it's up-to-date
    uv pip compile pyproject.toml --extra dev -o requirements-dev.lock

    # Then, sync the environment with the lock file and install the project
    uv pip sync requirements-dev.lock
    uv pip install -e .
    ```

---

## Commands

1. Format code with Ruff `ruff format .`
2. Lint with Ruff `ruff check .`
3. Run Mypy for static type checking `mypy src`
4. test `pytest`