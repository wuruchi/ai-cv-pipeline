# How to run

Make sure that you have installed `uv` by following the [official documentation](https://docs.astral.sh/uv/getting-started/installation/) 

Make sure you have installed `weasyprint` in your system. Follow the [Official documentation](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#)

Install:

```bash
uv sync
```

# How to use

Run

```bash
uv run python main.py
```

And follow the instructions. In summary:

`Option 1` allows you to generate `json` CV contents using a LLM model of your choice. You need to provided the credentials following the `.env.template`.

`Option 2` allows you to generate `pdf` CVs from the `json` contents you have previously generated.

`Option 3` moves all the generated `pdf` files from this project's data folder into the root `data/cvs` folder. It is important 
to move these files once you have finished generating them because they are passed to the `API` project by the
`docker compose` configuration.
