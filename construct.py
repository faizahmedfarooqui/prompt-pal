"""
File Name: construct.py
Author: Faiz A. Farooqui (github.com/faizahmedfarooqui)
"""

from llama_index import LLMPredictor, GPTSimpleVectorIndex, PromptHelper, ServiceContext, SimpleDirectoryReader
from langchain.chat_models import ChatOpenAI

def construct_index(directory_path):
	max_input_size = 4096
	num_outputs = 2047
	max_chunk_overlap = 10
	chunk_size_limit = 600

	prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

	llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.4, model_name="gpt-4"))

	service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)

	documents = SimpleDirectoryReader(directory_path).load_data()

	index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)

	index.save_to_disk('openai/index.json')

	return index

if __name__ == '__main__':
	index = construct_index("docs")
