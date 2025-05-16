# AWS Region Finder

This is a FastAPI-based web app that detects AWS regions available for a given country.

## Features

- Input a country name via a web form
- Returns AWS region info (name + code)
- Validates country using RESTCountries API
- Uses FastAPI with Jinja2 templates

## Run Locally

```bash
uvicorn app.main:app --reload
