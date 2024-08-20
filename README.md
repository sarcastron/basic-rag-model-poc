# Ariel LLM

This is a prototype of an AI Assistant powered by a Retrieval augmented generation. The model will be prompted with embeddings from [Prospero's learn site](https://learn.prospero.ai) and from [prospero.ai](https://prospero.ai) to generate the responses.

Much of the work and concepts are based on [this video tutorial](https://www.youtube.com/watch?v=2TJxpyO3ei4) and the [corresponding repo](https://github.com/pixegami/rag-tutorial-v2)

##  Requirements
- Python >=3.11
- [poetry](https://python-poetry.org/docs/)
- [Ollama](https://ollama.com/)

## Getting started

### 1. Install Ollama
After installing ollama, you will need to pull some models. For this proof of concept I am using `mxbai-embed-large` for embeddings and `llama3` for the chat model. You can pull them by running:

```sh
# Pull the models. Make sure you have ollama running as specified for your platform
ollama pull mxbai-embed-large
ollama pull llama3:instruct

```

### 2. Install deps with poetry

```sh
poetry install
```

### 3. Run the app

```sh
# enter the virtual environment with poetry
poetry shell

# Populate the database with the embeddings
python cli.py fetch

# Test everything is working by asking a query
python cli.py ask "Is a Net Options sentiment of 35 considered good?"
```

## Next steps

- [ ] Implement model testing framework.
- [X] Implement improved site indexing using the `sitemap.xml`. Look at using (ScrapeGraph)[https://github.com/ScrapeGraphAI/Scrapegraph-ai].
- [ ] Implement a web interface.
- [ ] Implement a vector datastore that can be distributed instead of using a local SQLite database.
- [ ] Consider using an agent chain approach to improve the quality of the responses.
- [ ] Implement agent chain using multiple models.
