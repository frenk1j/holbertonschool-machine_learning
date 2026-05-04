# 🤖 QA Bot — Question Answering with BERT & Semantic Search

> **Holberton School** | Supervised Learning | Natural Language Processing

---

## 📚 Description

This project implements an intelligent **Question Answering chatbot** using state-of-the-art NLP models. It combines **BERT** for extractive question answering and the **Universal Sentence Encoder** for semantic document retrieval, allowing the bot to find accurate answers from a corpus of reference documents.

---

## 🗂️ Project Structure

```
supervised_learning/qa_bot/
├── 0-qa.py                  # BERT-based question answering function
├── 1-loop.py                # Interactive Q&A input loop
├── 2-qa.py                  # Answer questions from a single reference
├── 3-semantic_search.py     # Semantic search over a document corpus
├── 4-qa.py                  # Multi-reference question answering bot
├── ZendeskArticles/         # Corpus of reference documents (.md files)
└── README.md
```

---

## ⚙️ Requirements

- Python 3.6+
- TensorFlow 2.x
- TensorFlow Hub
- Transformers (HuggingFace)
- NumPy

Install dependencies:

```bash
pip install tensorflow tensorflow-hub transformers numpy
```

---

## 📝 Tasks

### Task 0 — Question Answering (`0-qa.py`)

**Function:** `question_answer(question, reference)`

Uses the `bert-uncased-tf2-qa` model from TensorFlow Hub together with `BertTokenizer` (`bert-large-uncased-whole-word-masking-finetuned-squad`) to extract an answer snippet from a reference document.

| Parameter | Type | Description |
|-----------|------|-------------|
| `question` | `str` | The question to answer |
| `reference` | `str` | The reference document text |
| **Returns** | `str` or `None` | The answer snippet, or `None` if not found |

**Example:**

```bash
$ ./0-main.py
on - site days from 9 : 00 am to 3 : 00 pm
```

---

### Task 1 — Create the Loop (`1-loop.py`)

An interactive script that continuously prompts the user with `Q:` and responds with `A:`. Recognizes exit keywords and terminates gracefully.

**Exit keywords** *(case-insensitive)*: `exit`, `quit`, `goodbye`, `bye`

**Example:**

```
Q: Hello
A:
Q: How are you?
A:
Q: BYE
A: Goodbye
```

---

### Task 2 — Answer Questions (`2-qa.py`)

**Function:** `answer_loop(reference)`

Extends the loop from Task 1 by integrating the BERT QA model. If no answer is found in the reference text, the bot responds with a fallback message.

| Parameter | Type | Description |
|-----------|------|-------------|
| `reference` | `str` | The reference text to search |

**Example:**

```
Q: When are PLDs?
A: from 9 : 00 am to 3 : 00 pm
Q: What are Mock Interviews?
A: Sorry, I do not understand your question.
Q: What does PLD stand for?
A: peer learning days
Q: EXIT
A: Goodbye
```

---

### Task 3 — Semantic Search (`3-semantic_search.py`)

**Function:** `semantic_search(corpus_path, sentence)`

Uses the **Universal Sentence Encoder (USE-large)** from TensorFlow Hub to embed all documents in a corpus and the query sentence, then returns the most semantically similar document using cosine similarity.

| Parameter | Type | Description |
|-----------|------|-------------|
| `corpus_path` | `str` | Path to the folder of `.md` reference files |
| `sentence` | `str` | The query sentence |
| **Returns** | `str` | The full text of the most relevant document |

**Example:**

```bash
$ ./3-main.py
PLD Overview
Peer Learning Days (PLDs) are a time for you and your peers...
```

---

### Task 4 — Multi-reference Question Answering (`4-qa.py`)

**Function:** `question_answer(corpus_path)`

The complete bot. Combines semantic search (Task 3) and BERT QA (Task 0) into a full pipeline:

1. Receives a question from the user
2. Finds the most relevant document using semantic similarity
3. Extracts the answer using BERT
4. Falls back gracefully if no answer is found

| Parameter | Type | Description |
|-----------|------|-------------|
| `corpus_path` | `str` | Path to the corpus of reference documents |

**Example:**

```
Q: When are PLDs?
A: on - site days from 9 : 00 am to 3 : 00 pm
Q: What are Mock Interviews?
A: help you train for technical interviews
Q: What does PLD stand for?
A: peer learning days
Q: goodbye
A: Goodbye
```

---

## 🧠 Models Used

| Model | Source | Purpose |
|-------|--------|---------|
| `bert-uncased-tf2-qa` | TensorFlow Hub | Extractive QA — finds answer spans |
| `bert-large-uncased-whole-word-masking-finetuned-squad` | HuggingFace Transformers | Tokenizer for BERT QA |
| `universal-sentence-encoder-large/5` | TensorFlow Hub | Semantic similarity between sentences |

---

## 🚀 Usage

```bash
# Task 0 — Single question on a reference file
./0-main.py

# Task 1 — Interactive loop (no answers yet)
./1-loop.py

# Task 2 — Loop with single-document answers
./2-main.py

# Task 3 — Semantic search on corpus
./3-main.py

# Task 4 — Full multi-document QA bot
./4-main.py
```

---

## 👤 Author

**Holberton School** — Machine Learning Track  
`supervised_learning/qa_bot`

---

## 📄 License

This project is part of the Holberton School curriculum.
