# AI in CLI

## Built using Llama & OpenAI using OpenAI Chat Model

## What does this repository contains?

- This repository contains two files ie. `construct.py` & `run.py` and these files helps in constructing your data into OpenAI and getting results for your prompt from OpenAI Chat Model
- `construct.py` helps to create the embedding from your files available in `docs` directory
- `run.py` runs your prompt through the same embedding
- `docs` directory contains your training-data or knowledge-base. You can keep below mentioned file types in your `docs` directory -
  - ".pdf"
  - ".docx"
  - ".pptx"
  - ".jpg"
  - ".png"
  - ".jpeg"
  - ".mp3"
  - ".mp4"
  - ".csv"
  - ".epub"
  - ".md"
  - ".mbox"

## What are OpenAI Embedding?

OpenAI’s text embeddings measure the relatedness of text strings. Embeddings are commonly used for:

- **Search** (where results are ranked by relevance to a query string)
- **Clustering** (where text strings are grouped by similarity)
- **Recommendations** (where items with related text strings are recommended)
- **Anomaly detection** (where outliers with little relatedness are identified)
- **Diversity measurement** (where similarity distributions are analyzed)
- **Classification** (where text strings are classified by their most similar label)

An embedding is a vector (list) of floating point numbers. The distance between two vectors measures their relatedness. Small distances suggest high relatedness and large distances suggest low relatedness.

## What are the Prerequisites?

- OpenAI API Key
- Python version >= 3.11.3
- Pip version >= 23.0.1 from python (3.11)

If you have the correct version of Python & Pip installed, you can use the following command to install the dependencies -
```bash
pip install -r requirements.txt
```

## Construct.py:

- This script constructs an index using the GPTSimpleVectorIndex from documents in a specified directory.
- The LLMPredictor is used to generate embeddings for the documents, and a PromptHelper is used to generate prompts for the LLMPredictor. The constructed index is saved to disk in JSON format.

### Usage:

Run the script and keep the docs at the level same as this script.

```bash
export OPENAI_API_KEY="sk-xxx...xxx" python construct.py
```

Note:
1. Make sure to set up the dependencies and provide the necessary API credentials before running the script.
2. Once your `construct.py` is successfully run, then you should see an index.json file containing embeddings.

## Run.py:

1. This script implements a chatbot using the GPTSimpleVectorIndex from a pre-constructed index.
2. The chatbot takes input text as a command line argument and generates a response by querying
the index.
3. The SentenceEmbeddingOptimizer is used to optimize the responses. The generated response is
printed to the console with special markers indicating the start and end of the response.

### Usage:

Run the script with the input text as the command line argument. For example:

```bash
export OPENAI_API_KEY="sk-xxx...xxx" python run.py "Hello, how are you?"
```

Note:
Make sure to provide the path to the pre-constructed index in the `GPTSimpleVectorIndex.load_from_disk()` method in the chatbot() function. Also, the chatbot may take some time to generate a response, depending on the complexity of the query and the size of the index.
