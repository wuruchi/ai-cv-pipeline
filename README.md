# Chat CV Solution

We have the projects:

- `cv_generation`: Allows you to generate CVs with fake data.
- `cv_chat_api`: Builds an API that allows you to ask questions about he CVs you generated.
- `cv_chat_ui`: Implements a UI that allows you to query an LLM about the CVs you generated. Answers general questions about the candidates.

## Demo

[Video Demo](https://www.loom.com/share/6cc67a40df474449be7f186b1ca8c56c)

## How to Run it

First, make sure there are `PDF` CVs available in `data/cvs`, the `API` needs them to run. Follow the instructions in the `cv_generation` projec to generate some fake CVs.

Then, run:

```bash
docker compose up --build --watch
```

Or

```bash
make run
```

And that's it. Open the `UI` from the link in your terminal. Wait for the `API` to finish starting up before making requests.

