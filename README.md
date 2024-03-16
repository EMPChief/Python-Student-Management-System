# Python Student Management System

Welcome to the Python Student Management System! This project is a simple GUI application for managing student records. It uses PyQt6 as the GUI framework, and connects to a MySQL database to store student information.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

Python Student Management System is a simple application that allows users to manage student records in a GUI. It uses PyQt6 for the GUI framework and connects to a MySQL database to store student information.

## Features

- Create, read, update, and delete student records.
- Search for students by name, grade, or ID.
- Display student records in a table view.
- Add, edit, and remove courses for each student.
- Save and load student records from a sqlite or mysql.

## Requirements

To run this project, you'll need the following:

- Python 3.8 or higher
- MySQL 8.0 or higher
- PyQt6 library
- MySQL Connector library
- python-dotenv library
- pymysql library

## Installation

1. Clone this repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the project dependencies by running `pip install -r requirements.txt`.

## Usage

1. Create a `.env` file in the root of the project directory and populate it with the following variables:
MYSQL_HOST=host
MYSQL_USER=name
MYSQL_PASSWORD=password
MYSQL_DATABASE=school

## Getting Started

To get started with this project, you'll need to have Python 3.8 or higher installed on your system. You'll also need to have MySQL installed and running, and create a database named `pms` (Python Student Management System).
1. (install gudie for mysql)

2. Clone this repository to your local machine.

3. populete .env with these:
MYSQL_HOST=host
MYSQL_USER=name
MYSQL_PASSWORD=password
MYSQL_DATABASE=school


4. Create a virtual environment for the project. This can be done by running the following command in the project directory:
- `python -m venv venv`
Linux:
- `source venv/bin/activate`
Windows:
- `venv\Scripts\activate`

- `pip install -r requirements.txt`

- `deactivate`


5. Run the project by running the following command:
- `python main.py`
