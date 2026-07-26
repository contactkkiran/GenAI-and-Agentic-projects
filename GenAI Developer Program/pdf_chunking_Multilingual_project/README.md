# PDF Chunking Project

This project is a learning scaffold for building a PDF processing pipeline for RAG applications.

The goal is to load PDF files, extract text and table content, split the extracted content into useful chunks, and prepare those chunks for later embedding, retrieval, or LLM workflows.

## Current Status

This project is currently in progress. The folder structure exists, but the core Python implementation is not complete yet.

| Item | Path | Purpose | Status |
| --- | --- | --- | --- |
| Sample PDF | `data/sample.pdf` | Example PDF file for testing extraction and chunking. | Available |
| Driver script | `src/main.py` | Main entry point that should run the PDF loading and chunking workflow. | Placeholder only |
| PDF loader | `src/loaders/loaders.py` | Should contain PDF loading and extraction logic. | Placeholder only |
| Chunking strategies | `src/chunkers/chunkers.py` | Should contain text/table chunking strategies. | Placeholder only |
| Utilities | `src/utils/utils.py` | Should contain helper functions used across the project. | Placeholder only |

## Planned Workflow

1. Read PDF files from the `data/` folder.
2. Extract normal paragraph text from each PDF page.
3. Extract table content when a PDF contains tables.
4. Convert extracted tables into a clean text or Markdown-table format.
5. Split text into chunks using a chunking strategy.
6. Keep metadata such as file name, page number, chunk number, and content type.
7. Prepare the chunks for embedding or storage in a vector database.

## PDF With Table Handling

PDFs with tables need special handling because simple text extraction can lose row and column structure.

Planned table-aware behavior:

| Content Type | Example | Chunking Approach |
| --- | --- | --- |
| Paragraph text | Policy terms, explanations, descriptions | Split by paragraphs, sentences, or token/character limits. |
| Small table | A few rows of pricing, policy limits, or feature comparison | Keep the full table together in one chunk when possible. |
| Large table | Many rows across one or more pages | Split by row groups while repeating the header row in each chunk. |
| Mixed content | Text before or after a table | Keep nearby explanation text close to the related table chunk. |

Recommended table output format:

```markdown
| Column 1 | Column 2 | Column 3 |
| --- | --- | --- |
| Value A | Value B | Value C |
```

This format is useful because it preserves table structure and works well in RAG prompts.

## Suggested Project Structure

```text
pdf_chunking_project/
├── data/
│   └── sample.pdf
├── src/
│   ├── main.py
│   ├── loaders/
│   │   └── loaders.py
│   ├── chunkers/
│   │   └── chunkers.py
│   └── utils/
│       └── utils.py
└── README.md
```

## Suggested Implementation Plan

| Step | Task | Suggested Library | Status |
| --- | --- | --- | --- |
| 1 | Load PDF files from `data/` | `pathlib` | Not started |
| 2 | Extract page text | `pymupdf` or `pdfplumber` | Not started |
| 3 | Extract tables | `pdfplumber` | Not started |
| 4 | Normalize table rows and headers | Python lists/dicts | Not started |
| 5 | Convert tables to Markdown | Custom utility function | Not started |
| 6 | Chunk extracted text | LangChain text splitters or custom logic | Not started |
| 7 | Attach metadata to each chunk | Python dict/dataclass | Not started |
| 8 | Print or save chunks for review | JSON, CSV, or console output | Not started |

## Example Chunk Format

```python
{
    "source": "sample.pdf",
    "page": 1,
    "chunk_id": "sample-page-1-table-1",
    "content_type": "table",
    "content": "| Plan | Coverage | Premium |\\n| --- | --- | --- |\\n| Basic | 5L | 5000 |"
}
```

## Running the Project

There is no runnable pipeline yet. After implementation, the expected command should be:

```bash
python src/main.py
```

## Notes

- This project is intended for learning PDF preprocessing for RAG.
- Table-aware chunking is important for documents such as policies, invoices, reports, and financial PDFs.
- For production RAG, preserve metadata carefully so answers can cite the original file and page.
