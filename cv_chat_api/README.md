# CV Chat API

The `API` relies on CVs existing in the `data` folder. When running it using `docker-compose` from the solution root, you can expect that this folder is populated with CVs from the root's `data/cvs` folder. If running it standalone, make sure to copy CVs in this folder first.

## Install

Make sure that you have installed `uv` by following the [official documentation](https://docs.astral.sh/uv/getting-started/installation/) 

Install:

```bash
uv sync
```

## Star the API

```bash
uv run python main.py
```

Or better yet, run `docker compose` from the parent folder.
