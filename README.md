# SSD Labs

Lab activities for the Software Systems Development course at IIIT Hyderabad (Monsoon 2021): shell scripting, HTML/CSS, DOM manipulation, SQL, Node.js, Python, Flask REST APIs and socket programming.

![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)

## Overview

Each folder holds one timed lab activity: the problem statement (PDF or DOCX) and my solution. The labs follow the course syllabus, from Unix tooling to web development and backend services.

## Labs

| Lab | Topic | What the solution does |
|---|---|---|
| [Lab 2](./Lab%202/) | Bash: `awk`, `grep`, `head`, `tail`, arguments | `q1.sh` computes `a + b - c` (decimals allowed) with argument validation; `q2.sh` prints lines containing the whole word "is", the middle 10 lines, and the 3rd and 5th words of each line; `q3.sh` lists files in the current directory that the group can execute. |
| [Lab 3](./Lab%203/) | HTML and CSS | A two-page static site with a shared nav bar, headings, lists, divs, background image, favicon and external CSS. |
| [Lab 4](./Lab%204/) | DOM manipulation | A to-do list in vanilla JS: live preview of the typed text, add item with a timestamp, remove the last item, highlight on hover, and toggle the list font. |
| [Lab 6](./Lab%206/) | SQL | Five nested and aggregate queries on the classic `COMPANY` schema (employees, departments, projects, dependents), one per file. `schema.png` shows the schema. |
| [Lab 8](./Lab%208/) | Node.js (no Express) | A plain `http` server on port 8080 that reads `data.json` and, depending on `?query=`, returns the student with the highest total or all marks for subject `index` sorted in ascending order. |
| [Lab 9](./Lab%209/) | Python basics | `q1` splits a CamelCase string into lowercase words with regex; `q2` checks whether a binary number's decimal value is a palindrome; `q3` sorts a space-separated list of numbers with a lambda key; `q4` demonstrates inheritance. |
| [Lab 10](./Lab%2010/) | Flask, Flask-RESTful, SQLAlchemy | A CRUD REST API for students (`/create`, `/read`, `/update`, `/delete/<id>`) backed by SQLite, plus a menu-driven `requests` client. |
| [Lab 11](./Lab%2011/) | Socket programming | A threaded TCP server that greets each client and echoes every message back reversed, and a client that sends messages until `bye`. |

## Tech stack

Bash, GNU coreutils (`awk`, `grep`, `bc`), HTML5, CSS3, vanilla JavaScript, Node.js `http`, MySQL, Python 3, Flask, Flask-RESTful, Flask-SQLAlchemy, Flask-Login, `requests`, `socket` and `threading`.

## Project structure

```
SSD-Labs/
├── Lab 2/    q1.sh, q2.sh, q3.sh
├── Lab 3/    home.html, second.html, home.css, image/
├── Lab 4/    index.html, scripts/main.js
├── Lab 6/    1.sql ... 5.sql, lab6_ans.sql, schema.png
├── Lab 8/    server/server.js, server/service.js, server/data.json
├── Lab 9/    q1.py ... q4.py
├── Lab 10/   app.py, client.py
└── Lab 11/   server.py, client.py
```

Every lab folder also contains its problem statement. Labs 3, 4, 8 and 9 have their own short `README.md` with notes.

## Running the labs

Prerequisites, depending on the lab: a Unix-like shell with `bc` (Git Bash or WSL on Windows), a web browser, MySQL with the `COMPANY` sample database, Node.js, and Python 3.

```bash
# Lab 2: shell scripts
cd "Lab 2"
bash q1.sh 1.5 2 3
bash q2.sh hamlet.txt        # any text file
bash q3.sh

# Lab 3 / Lab 4: open in a browser
#   Lab 3/home.html   and   Lab 4/index.html

# Lab 6: run against a MySQL server that has the COMPANY database
mysql -u <user> -p < "Lab 6/1.sql"

# Lab 8: run from inside server/ (data.json is read relative to the working directory)
cd "Lab 8/server"
node server.js
# http://localhost:8080/?query=1
# http://localhost:8080/?query=2&index=1

# Lab 9
python "Lab 9/q1.py" BruceWayneIsBatman
python "Lab 9/q2.py" 1001
python "Lab 9/q3.py" "34 45 65 11 34"
python "Lab 9/q4.py"

# Lab 10: start the API on port 8000, then run the client in a second terminal
pip install flask flask-restful flask-sqlalchemy flask-login requests
cd "Lab 10"
python app.py
python client.py

# Lab 11: start the server, then one or more clients with the same port
cd "Lab 11"
python server.py 5000
python client.py 5000
```

## Context

Built as part of the Software Systems Development course in the M.Tech programme at IIIT Hyderabad (Monsoon 2021).

---

Made by [Mukul Kumar](https://mkk96.github.io) · [GitHub](https://github.com/mkk96) · [LinkedIn](https://www.linkedin.com/in/mukul-kumar-60322616b/)
