# Website Logger

![Preview Image](https://github.com/Mubassim-Khan/Website-Status-Logger/blob/main/api/templates/assets/Preview.png)

<div align="center">
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" alt="python" />
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="html" />
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="css" />
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="flask" />
    <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="vercel" />
    <img src="https://img.shields.io/badge/Github%20Actions-282a2e?style=for-the-badge&logo=githubactions&logoColor=367cfe" alt="github-actions" />
</div>

## 📋 <a name="table">Table of Contents</a>

1. [Introduction](#introduction)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Getting Started](#quick-start)
5. [License](#license)
6. [Contributing](#contributing)
7. [Acknowledgements](#acknowledgements)
8. [Contact](#contact)

## <a name="introduction">Introduction</a>

This repository contains the code for a Website Status Logger, which monitors the uptime and availability of various websites, including personal projects and social media platforms. The application periodically checks website statuses, logs the results, and automatically commits updates to GitHub using GitHub Actions. The backend is built with Flask, while the frontend displays website statuses in an interactive UI. This project helps in tracking website availability efficiently, ensuring quick detection of downtime or errors.

## <a name="features">Features</a>
👉 **Automated Website Monitoring**: The app periodically checks the status of websites, including personal projects and social media platforms, ensuring real-time uptime tracking.  

👉 **Categorized Website Status**: Websites are categorized into "Personal Projects" and "Social Media," displaying their status separately for better clarity.  

👉 **Detailed Logging System**: Logs every status check with timestamps in a structured log file, making it easy to track historical uptime and failures.  

👉 **Automatic GitHub Commits**: Uses GitHub Actions to automatically commit and push updated website statuses to the repository without manual intervention.  

👉 **Flask-Powered Web Interface**: Displays real-time website statuses on a dynamic web page built with Flask, offering a user-friendly dashboard.  

👉 **Bootstrap-Powered UI**: Uses Bootstrap's accordion layout for a sleek and responsive design, allowing users to expand and view website details conveniently.  

👉 **Customizable URL Lists**: Users can define their own list of websites to monitor by modifying a simple configuration file.  

👉 **Error Detection & Handling**: Captures HTTP errors and exceptions, marking websites as "DOWN" when unreachable or returning unexpected responses.  

## <a name="tech-stack">Tech Stack 🛠️</a>

- [Python](https://www.python.org/) - Programming Language
- [GitHub Actions](https://github.com/features/actions) - CI/CD
- [Flask](https://flask.palletsprojects.com/) - Python Framework
- [Vercel](https://vercel.com/) - Web Hosting Service

## <a name="#quick-start">Getting Started</a>

To get started with this project, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/Mubassim-Khan/Website-Logger.git
```

2. Open the project in your preferred code editor.

3. Create a virtual environment of suitable python version using:

```bash
conda create -p venv python=3.x -y`
```

4. Activate environment using:

```bash
`source activate ./venv` or `conda activate ./venv`
```

5. Install the project dependencies using pip:

```bash
pip install -r requirements.txt
```

6. Run the project

```bash
`python flask_app.py`
```
## <a name="license">License</a>

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## <a name="contributing">Contributing</a>

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## <a name="acknowledgements">Acknowledgements</a>

- Copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

## <a name="contact">Contact</a>

If you have any questions, suggestions, or feedback, you can reach out to the project maintainer:

- LinkedIn : [Mubassim Ahmed Khan](https://www.linkedin.com/in/mubassim)
- Email: [mubassimkhan@gmail.com](mailto:mubassimkhan@gmail.com)

---

<!----->
