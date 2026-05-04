# 📊 NLP Metrics — BLEU Score Implementation

> **Holberton School** | Supervised Learning | Natural Language Processing  
> `#advanced`

---

## 📚 Description

This project implements the **BLEU (Bilingual Evaluation Understudy)** score from scratch — one of the most widely used metrics for evaluating the quality of machine-generated text (e.g., machine translation, text summarization).

BLEU measures how similar a machine-generated sentence is to one or more human reference translations, based on **n-gram precision** with a **brevity penalty** to avoid rewarding overly short outputs.

---

## 🗂️ Project Structure

```
supervised_learning/nlp_metrics/
├── 0-uni_bleu.py         # Unigram BLEU score
├── 1-ngram_bleu.py       # N-gram BLEU score
├── 2-cumulative_bleu.py  # Cumulative N-gram BLEU score
└── README.md
```

---

## ⚙️ Requirements

- Python 3.6+
- NumPy

```bash
pip install numpy
```

---

## 📐 BLEU Score — Core Concepts

### ✂️ Clipped Precision
For each n-gram in the hypothesis sentence, its count is **clipped** to the maximum count found in any reference:

```
Clipped Count = min(count_in_sentence, max_count_in_any_reference)
Precision = Clipped Count / Total N-grams in Sentence
```

### ⚖️ Brevity Penalty (BP)
Prevents the score from rewarding very short sentences:

```
BP = 1                          if c >= r
BP = exp(1 - r/c)               if c < r
```
Where `c` = sentence length, `r` = closest reference length.

### 🧮 Final BLEU Score
```
BLEU = BP × precision
```

---

## 📝 Tasks

### Task 0 — Unigram BLEU Score (`0-uni_bleu.py`)

**Function:** `uni_bleu(references, sentence)`

Calculates the **unigram (1-gram)** BLEU score by comparing individual words between the hypothesis and references.

| Parameter | Type | Description |
|-----------|------|-------------|
| `references` | `list of list` | List of reference translations (each a list of words) |
| `sentence` | `list` | The proposed sentence as a list of words |
| **Returns** | `float` | The unigram BLEU score |

**Example:**

```python
references = [
    ["the", "cat", "is", "on", "the", "mat"],
    ["there", "is", "a", "cat", "on", "the", "mat"]
]
sentence = ["there", "is", "a", "cat", "here"]

print(uni_bleu(references, sentence))
# → 0.6549846024623855
```

---

### Task 1 — N-gram BLEU Score (`1-ngram_bleu.py`)

**Function:** `ngram_bleu(references, sentence, n)`

Generalizes the BLEU score to any **n-gram order**. Instead of single words, it compares sequences of `n` consecutive words.

| Parameter | Type | Description |
|-----------|------|-------------|
| `references` | `list of list` | List of reference translations |
| `sentence` | `list` | The proposed sentence as a list of words |
| `n` | `int` | The n-gram size (e.g., 2 for bigrams) |
| **Returns** | `float` | The n-gram BLEU score |

**Example:**

```python
print(ngram_bleu(references, sentence, 2))
# → 0.6140480648084865
```

**How n-grams work:**

```
sentence = ["there", "is", "a", "cat", "here"]

bigrams (n=2):
  ("there", "is"), ("is", "a"), ("a", "cat"), ("cat", "here")

trigrams (n=3):
  ("there", "is", "a"), ("is", "a", "cat"), ("a", "cat", "here")
```

---

### Task 2 — Cumulative N-gram BLEU Score (`2-cumulative_bleu.py`)

**Function:** `cumulative_bleu(references, sentence, n)`

Calculates the **cumulative BLEU-n** score — the standard BLEU formula used in practice. It computes a **weighted geometric mean** of all n-gram precisions from 1 up to `n`, with equal weights.

| Parameter | Type | Description |
|-----------|------|-------------|
| `references` | `list of list` | List of reference translations |
| `sentence` | `list` | The proposed sentence as a list of words |
| `n` | `int` | The largest n-gram order to include |
| **Returns** | `float` | The cumulative BLEU-n score |

**Formula:**

```
BLEU-n = BP × exp( (1/n) × Σ log(p_k) )   for k = 1..n
```

Where each `p_k` is the clipped precision for k-grams, and all weights are `1/n`.

**Example:**

```python
print(cumulative_bleu(references, sentence, 4))
# → 0.5475182535069453
```

**Score comparison across tasks:**

| Metric | Score |
|--------|-------|
| Unigram BLEU (n=1) | 0.6550 |
| Bigram BLEU (n=2) | 0.6140 |
| Cumulative BLEU-4 | 0.5475 |

> Higher n-gram orders are harder to match, so cumulative scores tend to be lower.

---

## 🚀 Usage

```bash
# Task 0 — Unigram BLEU
./0-main.py

# Task 1 — Bigram BLEU
./1-main.py

# Task 2 — Cumulative BLEU-4
./2-main.py
```

---

## 🔍 Why BLEU Matters

BLEU is the industry-standard metric for:

- **Machine Translation** (e.g., Google Translate evaluation)
- **Text Summarization** quality measurement
- **Image Captioning** evaluation
- **Dialogue Systems** and chatbot response quality

| BLEU Score | Interpretation |
|------------|----------------|
| < 0.10 | Almost useless |
| 0.10 – 0.19 | Hard to understand |
| 0.20 – 0.29 | Some fragments correct |
| 0.30 – 0.40 | Understandable, but flawed |
| 0.40 – 0.50 | High quality translation |
| > 0.50 | Expert-level quality |

---

## 👤 Author

**Holberton School** — Machine Learning Track  
`supervised_learning/nlp_metrics`

---

## 📄 License

This project is part of the Holberton School curriculum.
