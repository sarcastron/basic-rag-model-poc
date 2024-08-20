# Ariel LLM

This is a prototype of an AI Assistant using retrieval-augmented generation. The app has two main parts. The first part is a web scraper that indexes a website, generates embeddings and stores the embeddings in a database. The second part interfaces with an LLM that uses the indexed embeddings to answer questions. The interface takes the question asked, generated an embedding, performs a search in the vector database and generates a prompt to submit to a generative LLM to generate the response.

Much of the work and concepts are based on [this video tutorial](https://www.youtube.com/watch?v=2TJxpyO3ei4) and the [corresponding repo](https://github.com/pixegami/rag-tutorial-v2)

##  Requirements
- Python >=3.11
- [poetry](https://python-poetry.org/docs/)
- [Ollama](https://ollama.com/)

## Getting started

### 1. 💾  Install Ollama and pull models
After installing [ollama](https://ollama.com/download), you will need to pull some models. For this proof of concept I am using `mxbai-embed-large` for embeddings and `llama3:instruct` for the chat model. You can pull them by running:

```sh
# Pull the models. Make sure you have ollama running as specified for your platform
ollama pull mxbai-embed-large
ollama pull llama3:instruct

```

### 2. 🏗️  Install deps with poetry

```sh
poetry install
```

### 3. 🏃🏼‍♂️‍➡️  Run it

```sh
# enter the virtual environment with poetry
poetry shell

# Populate the database with the embeddings. In this case we are using the amtrav.com knowledge base
python cli.py fetch sitemap https://www.amtrav.com/sitemap.xml --filter-urls https://www.amtrav.com/sitemap.xml/knowledgebase

# Test everything is working by asking a query
python cli.py query -q "How can I create a new travel policy?"

# Enter interactive mode which is basically a chat loop
python cli.py query
```

## Next steps

- [ ] Implement model testing framework.
- [X] Implement improved site indexing using the `sitemap.xml`. Look at using (ScrapeGraph)[https://github.com/ScrapeGraphAI/Scrapegraph-ai].
- [ ] Implement a web interface.
- [ ] Implement a vector datastore that can be distributed instead of using a local SQLite database.
- [ ] Consider using an agent chain approach to improve the quality of the responses.
- [ ] Implement agent chain using multiple models.
