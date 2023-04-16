# PromptPal: An AI-powered command-line assistant

Welcome to the repository that showcases the use of [LlamaIndex](https://gpt-index.readthedocs.io/en/latest/index.html) and [OpenAI](https://platform.openai.com/docs/introduction) Chat Model to create an AI-powered CLI.

`LlamaIndex` is a powerful tool that allows you to connect your LLMs with external data through a central interface. With OpenAI's state-of-the-art chat model, you can create an intelligent conversational agent that can understand natural language and provide relevant responses.

This repository contains two files: `construct.py` and `run.py` & one folder `docs`:
- `construct.py` helps you to create embeddings for your training data stored in the docs directory.
- `run.py` runs your prompt through the same embeddings and generates responses from the OpenAI Chat Model.
- `docs` contains the documentation, training-data or knowledge-base. You should not change the directory name or location.
- In case you want to change the directory name or location, you should name fixes to the above two mentioned files as well.

The docs directory can contain various file types such as `.pdf`, `.docx`, `.pptx`, `.jpg`, `.png`, `.jpeg`, `.mp3`, `.mp4`, `.csv`, `.epub`, `.md`, and `.mbox`.

`OpenAI's text embeddings` are powerful tools that measure the relatedness of text strings. These embeddings can be used for a wide range of applications such as `search`, `clustering`, `recommendations`, `anomaly detection`, `diversity measurement`, and `classification`.

To get started with this repository, you need an `OpenAI API key`, `Python version >= 3.11.3`, and `Pip version >= 23.0.1 from Python (3.11)` then you can install the necessary dependencies by running the following command:

```bash
pip install -r requirements.txt
```

- `construct.py` constructs an index using the `GPTSimpleVectorIndex` from documents in a specified directory.
- The `LLMPredictor` generates embeddings for the documents, and a `PromptHelper` generates prompts for the LLMPredictor.
- The constructed index is saved as `index.json` to disk in JSON format.

## To use construct.py, run the following command:

```bash
export OPENAI_API_KEY="sk-xxx...xxx" python construct.py
```

Note that you need to set up the dependencies and provide the necessary API credentials before running the script. Once `construct.py` is successfully run, an `index.json` file containing embeddings will be created.

`run.py` implements a chatbot using the pre-constructed index. The chatbot takes input text as a command-line argument and generates a response by querying the index. The SentenceEmbeddingOptimizer is used to optimize the responses. The generated response is printed to the console with special markers indicating the start and end of the response.

## To use run.py, run the following command with your desired prompt:

```bash
export OPENAI_API_KEY="sk-xxx...xxx" python run.py "Hello, how are you?"
```

**Note** that you need to provide the path to the pre-constructed index in the `GPTSimpleVectorIndex.load_from_disk()` method in the `chatbot()` function. Incase you are planning to change the docs directory name or its path. Also, the chatbot may take some time to generate a response, depending on the complexity of the query and the size of the index.

I hope that this repository helps you to create powerful AI-powered CLI tools. Feel free to modify and extend the code as per your requirements.
