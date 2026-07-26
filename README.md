A production-ready Retrieval-Augmented Generation (RAG) project built with LangChain, FAISS, HuggingFace Embeddings, Groq LLM, and RAGAS. This project implements and benchmarks multiple retrieval strategies to compare their impact on answer quality.
              

🚀 Features  
📄 Multi-PDF document ingestion  
✂️ Recursive text chunking  
🧠 HuggingFace sentence embeddings  
🗂️ FAISS vector database  
🤖 Groq LLM integration  
🔍 Multiple retrieval strategies:Similarity Search  
Max Marginal Relevance (MMR)  
BM25  
Hybrid Retrieval (BM25 + Dense)  
Multi-Query Retrieval  
📚 Source metadata support  
📊 Automated RAG evaluation using RAGAS  
📈 Retriever benchmarking and comparison  
⚡ Modular and extensible architecture  




Libraries Used

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | LangChain |
| API | FastAPI |
| Vector Database | FAISS |
| Embeddings | HuggingFace Sentence Transformers |
| LLM | Groq |
| Evaluation | RAGAS |
| Retrieval | BM25, Similarity, MMR, Hybrid, MultiQuery |


Retrievers
| Retriever | Description |
|------------|-------------|
| Similarity | Dense vector similarity search |
| BM25 | Sparse keyword search |
| MMR | Maximizes relevance while reducing redundancy |
| Hybrid | Combines BM25 and vector search |
| MultiQuery | Generates multiple query variations before retrieval |



| Version | Features |
|----------|----------|
| v0.0 | Basic RAG Pipeline |
| v0.1 | Advanced Retrieval Techniques |
| v0.2 | RAGAS Evaluation Framework |
| v0.3 | Source Citations *(planned)* |
| v0.4 | Parent Document Retriever *(planned)* |
| v1.0 | Production-ready RAG *(planned)* |
