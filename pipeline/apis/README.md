# 🌐 Data Collection - APIs — Holberton School

> *"Data is the new oil — and APIs are the pipelines that carry it."*

![Score](https://img.shields.io/badge/Score-100%25-brightgreen?style=flat-square)
![Language](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python)
![Style](https://img.shields.io/badge/Style-pycodestyle_2.11.1-orange?style=flat-square)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-purple?style=flat-square&logo=ubuntu)

---

## 📋 Table of Contents

- [Description](#-description)
- [Learning Objectives](#-learning-objectives)
- [Requirements](#-requirements)
- [APIs Used](#-apis-used)
- [Tasks](#-tasks)
- [Resources](#-resources)
- [Author](#-author)

---

## 📖 Description

Data is the foundation of every Machine Learning model. This project focuses on **data collection through REST APIs** — the first step in building a data pipeline. Using the Python `requests` package, we interact with real-world APIs (Star Wars, GitHub, SpaceX) to retrieve, paginate, handle rate limits, and transform JSON data into usable formats.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following **without the help of Google**:

- How to use the Python package **`requests`**
- How to make an HTTP **`GET` request**
- How to handle **rate limiting**
- How to handle **pagination**
- How to fetch and parse **JSON resources**
- How to **manipulate data** from an external service

---

## ⚙️ Requirements

- Interpreted on **Ubuntu 20.04 LTS** using **Python 3.9**
- First line of all files: `#!/usr/bin/env python3`
- Code must follow **pycodestyle** style (version 2.11.1)
- All modules, classes, and functions must be documented
- All files must be executable
- All files must end with a new line

---

## 🔌 APIs Used

| API | Base URL | Purpose |
|-----|----------|---------|
| **SWAPI** — Star Wars API | `https://swapi.dev/api/` | Starships & passenger data |
| **GitHub API** | `https://api.github.com/` | Repository & location data |
| **SpaceX API** | `https://api.spacexdata.com/v4/` | Rocket launches & payloads |

---

## ✅ Tasks

| # | Title | API | Description | Score |
|---|-------|-----|-------------|-------|
| 0 | **Can I join?** | SWAPI | Return list of ships that can hold a given number of passengers (with pagination) | 5/5 |
| 1 | **Where I am?** | GitHub | Return the location of a specific GitHub user | 4/4 |
| 2 | **Rate me if you can!** | GitHub | Fetch GitHub user data while handling rate limiting gracefully | 6/6 |
| 3 | **First launch** | SpaceX | Return the first SpaceX launch with its rocket name, date, and launchpad | 4/4 |
| 4 | **How many by rocket?** | SpaceX | Display the number of launches per rocket, sorted and formatted | 4/4 |

---

## 🔑 Key Concepts Demonstrated

### Pagination
```python
# SWAPI returns paginated results — loop through all pages
url = "https://swapi.dev/api/starships/"
while url:
    response = requests.get(url).json()
    # process response["results"]
    url = response["next"]  # None when last page is reached
```

### Rate Limiting
```python
# GitHub API returns rate limit info in headers
if response.status_code == 403:
    reset_time = response.headers.get("X-RateLimit-Reset")
    # Wait or inform the user
```

### JSON Parsing
```python
data = requests.get(url).json()
# Access nested fields directly
name = data["name"]
```

---

## 📚 Resources

- [Requests package documentation](https://docs.python-requests.org/en/latest/)
- [SWAPI — The Star Wars API](https://swapi.dev/)
- [GitHub REST API](https://docs.github.com/en/rest)
- [SpaceX API](https://github.com/r-spacex/SpaceX-API)

---

## 🗂️ Repository Structure

```
holbertonschool-machine_learning/
└── pipeline/
    └── apis/
        ├── README.md
        ├── 0-passengers.py     # SWAPI — ships by passenger count
        ├── 1-sentience.py      # GitHub — user location
        ├── 2-user_location.py  # GitHub — rate limit handling
        ├── 3-first_launch.py   # SpaceX — first launch details
        └── 4-rocket_frequency.py  # SpaceX — launches per rocket
```

---

## 👤 Author

**Alexa Orrico** — *Software Engineer at Holberton School*

---

*Holberton School — Machine Learning Track*