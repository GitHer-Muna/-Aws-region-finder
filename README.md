# AWS Region Finder

A simple FastAPI web application that allows users to input a country name and returns corresponding AWS data center regions for that country.

---

## What This Project Does

This project validates the user-provided country name by querying the [RESTCountries API](https://restcountries.com/). Upon successful validation, it displays AWS data center regions mapped statically in the application for the given country. It includes:

- Country name validation via external API call.
- AWS region lookup from a predefined dictionary.
- A user-friendly HTML form interface.
- Containerized with Docker.
- Demonstrates 12-Factor app principles like environment config, dependency management, and CI readiness.

---

## How to Run Locally

### Prerequisites

- Python 3.10 or higher
- (Optional) Virtual environment

### Steps

1. Clone the repository and navigate into it:

    ```bash
    git clone <your-github-repo-url>
    cd aws-region-finder
    ```

2. Create and activate a virtual environment (recommended):

    ```bash
    python -m venv venv
    venv\Scripts\activate        # Windows
    # or
    source venv/bin/activate     # macOS/Linux
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the FastAPI app:

    ```bash
    uvicorn app.main:app --reload
    ```

5. Open your browser at:

    ```
    http://localhost:8000
    ```

---

## How to Run Using Docker

1. Build the Docker image:

    ```bash
    docker build -t aws-region-finder .
    ```

2. Run the container:

    ```bash
    docker run -p 8000:8000 aws-region-finder
    ```

3. Access the app in your browser:

    ```
    http://localhost:8000
    ```

---


