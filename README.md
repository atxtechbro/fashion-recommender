# Snazzy Closet

Snazzy Closet is a fashion recommender app that helps users manage their wardrobe and receive personalized outfit recommendations. The project leverages FastAPI for the backend, MongoDB for data storage, React for the frontend, and machine learning for analyzing user data to improve recommendations.

## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Backend](#backend)
  - [API](#api)
  - [Database](#database)
  - [Machine Learning](#machine-learning)
- [Frontend](#frontend)
- [Testing](#testing)
- [Collaboration](#collaboration)
- [License](#license)

## Project Overview

Snazzy Closet aims to provide a seamless and personalized fashion recommendation experience. Users can upload information about their wardrobe, and the system will suggest outfits based on their preferences, previous selections, and other criteria. The core of this functionality is powered by machine learning models that classify clothing items and detect colors, enhancing the personalization of recommendations.

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

The machine learning components are the heart of Snazzy Closet, providing intelligent recommendations based on image classification and color detection.

- **`model.py`**: Defines the structure of the machine learning model.
- **`preprocess.py`**: Handles data preprocessing, including image resizing, normalization, and feature extraction.
- **`train.py`**: Manages the training process for the model, including loading and preprocessing images, training the model, and saving the trained model to disk.

### Model Versioning and Storage

When saving the trained model with `model.save('final_model.h5')`, ensure that a versioning strategy is in place to avoid overwriting models, especially in a CI/CD pipeline or production environment.

## Frontend

The frontend is built using React and includes all the user interface components.

- **`App.js`**: Main entry point for the React application.
- **`index.js`**: Renders the React application to the DOM.
- **`App.css`** and **`index.css`**: Styles for the application.

## Testing

We use `pytest` for backend testing, with tests located in the `tests` directory.

- **`test_api.py`**: Contains unit tests for the API routes, covering user creation, retrieval, updating, and deletion.

To run the tests:

```bash
export PYTHONPATH=$(pwd)
pytest snazzy-closet/backend/tests
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
