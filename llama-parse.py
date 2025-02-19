import os
from llama_index.core import VectorStoreIndex
from llama_index.core import Settings
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from llama_parse import LlamaParse

# API access to llama-cloud
os.environ["LLAMA_CLOUD_API_KEY"] = "llx-KM7BHvTX1QhFKUE5iJ7hgD9kHt3URSizaQnfXLuu9EchPQ9B"

api_key = "78d406f975874c20ac2298c6d83e2f7d"
azure_endpoint = "https://nitoropenai.openai.azure.com/"
api_version = "2023-03-15-preview"

embed_model = AzureOpenAIEmbedding(
    model="text-embedding-ada-002",
    deployment_name="text-embedding-ada-002",
    api_key=api_key,
    azure_endpoint=azure_endpoint,
    api_version=api_version,
)

llm = AzureOpenAI(
    model="gpt-35-turbo-16k",
    deployment_name="gpt-35-turbo-16k",
    api_key=api_key,
    azure_endpoint=azure_endpoint,
    api_version=api_version,
)

Settings.llm = llm
Settings.embed_model = embed_model

documents = LlamaParse(result_type="markdown").load_data(
    "./docs/manual.pdf"
)

print(documents)

print("**"*30)
