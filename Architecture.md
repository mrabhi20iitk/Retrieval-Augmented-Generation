                                    ┌────────────────────┐
                                    │   Multiple PDFs    │
                                    │  (Knowledge Base)  │
                                    └─────────┬──────────┘
                                              │
                                              ▼
                                   ┌─────────────────────┐
                                   │   Document Loader   │
                                   │    (PyPDFLoader)    │
                                   └─────────┬───────────┘
                                             │
                                             ▼
                               ┌──────────────────────────┐
                               │ Text Chunking            │
                               │ RecursiveCharacterSplitter│
                               └─────────┬────────────────┘
                                         │
                                         ▼
                               ┌──────────────────────────┐
                               │ HuggingFace Embeddings   │
                               │ all-MiniLM-L6-v2         │
                               └─────────┬────────────────┘
                                         │
                                         ▼
                               ┌──────────────────────────┐
                               │ FAISS Vector Store       │
                               │ + Metadata               │
                               └─────────┬────────────────┘
                                         │
                  ┌──────────────────────┼──────────────────────┐
                  │                      │                      │
                  ▼                      ▼                      ▼
        ┌────────────────┐    ┌────────────────┐    ┌─────────────────┐
        │ Similarity     │    │ BM25           │    │ MMR             │
        │ Retriever      │    │ Retriever      │    │ Retriever       │
        └────────────────┘    └────────────────┘    └─────────────────┘
                  │                      │                      │
                  └──────────────┬───────┴──────────────┬───────┘
                                 │                      │
                                 ▼                      ▼
                         ┌────────────────┐     ┌──────────────────┐
                         │ Hybrid         │     │ MultiQuery       │
                         │ Retriever      │     │ Retriever        │
                         └────────┬───────┘     └─────────┬────────┘
                                  └──────────────┬────────┘
                                                 │
                                                 ▼
                                  ┌─────────────────────────┐
                                  │ Retrieved Contexts      │
                                  └───────────┬─────────────┘
                                              │
                                              ▼
                                  ┌─────────────────────────┐
                                  │ Groq LLM               │
                                  │ Answer Generation      │
                                  └───────────┬─────────────┘
                                              │
                                              ▼
                                  ┌─────────────────────────┐
                                  │ REST API (FastAPI)      │
                                  └───────────┬─────────────┘
                                              │
                                              ▼
                                  ┌─────────────────────────┐
                                  │ User Response           │
                                  │ + Sources               │
                                  └─────────────────────────┘

────────────────────────────────────────────────────────────────────────────

                    Evaluation & Benchmarking Pipeline

      Questions + Ground Truth
                  │
                  ▼
       Retrieve Contexts (Each Retriever)
                  │
                  ▼
           Generate Answers (Groq)
                  │
                  ▼
        RAGAS Evaluation Metrics
                  │
      ┌───────────┼────────────┬──────────────┬──────────────┐
      ▼           ▼            ▼              ▼              ▼
 Faithfulness  Answer      Context        Context      Answer
               Relevancy   Precision      Recall       Correctness
      └───────────┬────────────┴──────────────┬──────────────┘
                  ▼
        Retriever Benchmark Report
