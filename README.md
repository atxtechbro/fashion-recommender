# Snazzy Closet

Snazzy Closet is a fashion recommender app that helps users manage their wardrobe and receive personalized outfit recommendations. The project leverages FastAPI for the backend, MongoDB for data storage, and React for the frontend. It also includes machine learning components for analyzing user data to improve recommendations.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Backend](#backend)
  - [API](#api)
  - [Database](#database)
  - [Machine Learning](#machine-learning)
  - [Utilities](#utilities)
- [Frontend](#frontend)
- [Testing](#testing)
- [Getting Started](#getting-started)
- [Collaboration](#collaboration)
- [License](#license)

## Project Overview

Snazzy Closet aims to provide a seamless and personalized fashion recommendation experience. Users can upload information about their wardrobe, and the system will suggest outfits based on their preferences, previous selections, and other criteria.
## Project Structure
```
```
.
├── snazzy-closet
│   ├── public
│   │   ├── logo512.png
│   │   ├── index.html
│   │   ├── logo192.png
│   │   ├── favicon.ico
│   │   ├── robots.txt
│   │   └── manifest.json
│   ├── package-lock.json
│   ├── backend
│   │   ├── tests
│   │   │   ├── test_user_crud.py
│   │   │   ├── conftest.py
│   │   │   └── test_clothing_item_crud.py
│   │   ├── api
│   │   │   ├── user_routes.py
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   │   │   └── clothing_item_routes.py
│   │   ├── utils
│   │   │   ├── helpers.py
│   │   │   ├── __init__.py
│   │   │   ├── logger.py
│   │   │   └── config.py
│   │   ├── ml
│   │   │   ├── train.py
│   │   │   ├── model.py
│   │   │   ├── __init__.py
│   │   │   └── preprocess.py
│   │   └── db
│   │   │   ├── db_config.py
│   │   │   ├── models.py
│   │   │   └── __init__.py
│   ├── README.md
│   ├── src
│   │   ├── App.css
│   │   ├── index.js
│   │   ├── logo.svg
│   │   ├── index.css
│   │   ├── setupTests.js
│   │   ├── reportWebVitals.js
│   │   ├── App.js
│   │   ├── App.test.js
│   │   └── SplashPage.js
│   └── package.json
├── README.md
├── scripts
│   └── update_readme.py
├── .gitignore
├── .github
│   ├── labels.yaml
│   ├── workflows
│   │   ├── manage-labels.yml
│   │   └── update-readme.yml
│   └── ISSUE_TEMPLATE
│   │   ├── docs_delight.yml
│   │   ├── feature_fever.yaml
│   │   ├── product_polish.yml
│   │   ├── issue_template.md
│   │   ├── bug_squash.yml
│   │   └── easy_win.yml
└── project_structure.txt
```
```
## Backend

The backend is responsible for handling API requests, interacting with the database, and running machine learning models.

### API

- **`main.py`**: The entry point for the FastAPI application.
- **`user_routes.py`**: Manages user-related API endpoints (create, read, update, delete).
- **`clothing_item_routes.py`**: Handles CRUD operations for clothing items.

### Database

- **`db_config.py`**: Configures the MongoDB connection.
- **`models.py`**: Defines the data schemas for users and clothing items.

### Machine Learning

- **`model.py`**: Defines the structure of the machine learning model.
- **`preprocess.py`**: Handles data preprocessing.
- **`train.py`**: Manages the training process for the model.

### Utilities

- **`config.py`**: Stores configuration settings.
- **`helpers.py`**: Provides utility functions used throughout the backend.
- **`logger.py`**: Configures the application’s logging.

## Frontend

The frontend is built using React and includes all the user interface components.

- **`App.js`**: Main entry point for the React application.
- **`index.js`**: Renders the React application to the DOM.
- **`App.css`** and **`index.css`**: Styles for the application.
- **`App.test.js`** and **`setupTests.js`**: Files for testing React components.

## Testing

We use `pytest` for backend testing, with tests located in the `tests` directory.

- **`test_api.py`**: Contains unit tests for the API routes, covering user creation, retrieval, updating, and deletion.

To run the tests:

```bash
export PYTHONPATH=$(pwd)
pytest snazzy-closet/backend/tests
```

## Getting Started

### Prerequisites

- **Python 3.10+**
- **MongoDB**
- **Node.js and npm/yarn**

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/snazzy-closet.git
cd snazzy-closet
```

2. Install backend dependencies:

```bash
pip install -r requirements.txt
```

3. Install frontend dependencies:

```bash
cd snazzy-closet
npm install
```

4. Run the backend:

```bash
uvicorn backend.api.main:app --reload
```

5. Run the frontend:

```bash
npm start
```

## Collaboration

All changes should be made through pull requests. Follow branch naming conventions tied to issues for clarity (e.g., `issue-1-add-tests`).

### Creating a Pull Request

1. Create a new branch:

```bash
git checkout -b issue-1-add-tests
```

2. Push your branch to GitHub:

```bash
git push origin issue-1-add-tests
```

3. Create a PR:

You can use the GitHub website or the CLI:

```bash
gh pr create --title "Add update and delete test coverage" --body "This PR adds tests for updating and deleting users via the API. Closes #1."
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
