# ReDirected: Simple URL Redirect Service

### A simple URL redirect tool designed to let you manage your links easily.

## Table of Contents:

- [What is this?](#what-is-this)
- [Why this exist?](#why-this-exist)
- [Features](#features)
- [How It Works](#how-it-works)
- [How to Set Up](#how-to-set-up)
- [How to Use](#how-to-use)
- [Contributing](#contributing)


## What is this?

This project allows you to set up a minimal URL redirect service. You provide short keywords for your URLs, and the app will automatically redirect users to the original link based on the keyword. Great for organizing your project, social media links, or personal URLs!


## Why this exist?

This project exists to solve a common issue I faced while managing links across multiple platforms like GitHub, my portfolio, and social media profiles. Each time a link changed, I had to update it manually on every platform.

To simplify this process, I created this project as a central hub where all my links can be updated in one place. By sharing a single, consistent link, such as `yoursite.com/yourproject`, I can ensure that it always redirects to the correct destination. And only have to change/update link in just one place.


## Features:
- Simple keyword-based redirection
- Easy-to-modify database for your own links
- Lightweight and efficient
- Great for self-hosting on platforms like Vercel or Heroku


## How It Works:
To see how this works, go to `redirected.vercel.app/github`. You will be redirected to my GitHub profile. 

So, to make it work, 
1. You have to define a set of keywords and URLs in the `database` dictionary in `app.py`.
2. When someone visits your site using a specific keyword, they will be redirected to the corresponding URL.

For example, if the keyword is `github`, visiting `yourdomain.com/github` will send the user to your GitHub profile.

## How to Set Up:

1. **Fork the repo**: [Fork this repository](https://github.com/your-repo-link)
2. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

3. **Customize the links**: Open `app.py` and update the `database` dictionary with your own URLs and keywords. Database dictonary format: `{"keyword" : "original url"}`
    ```python
    database = {
        "github": "https://github.com/yourusername",
        "portfolio": "https://yourportfolio.com",
    }
    ```
    Visiting `yourdomain.com/portfolio` will send the user to your actual prrtfolio (`https://yourportfolio.com`).

4. **Running Locally**: To test this project on your local machine before deploying, follow these steps:

    1. **Clone the repository**: If you already done this, then navigate to the folder. 

    2. **Set up a virtual environment**: If you don't already have `venv` installed, you can install it using `pip`:
        ```bash
        pip install virtualenv
        ```
        Then create and activate a virtual environment:
        ```bash
        python -m venv venv

        # On Windows,
        venv\Scripts\activate
        ```

    3. **Install dependencies**: Only `flask` is needed. 
        ```bash
        pip install -r requirements.txt
        ```

    4. **Run the application**: Start the Flask app using:
        ```bash
        python app.py
        ```

    5. **Access the app**: Once the app is running, open your browser and navigate to:
        ```
        http://127.0.0.1:5000/
        ```

    This will allow us to test the redirect functionality locally.

5. **Deploy**: You can deploy it to platforms like Vercel, Heroku, or any other service:
    - For Vercel: Follow [this guide](https://vercel.com/docs/cli).
    - For Heroku: Follow [this guide](https://devcenter.heroku.com/articles/getting-started-with-python).

## How to Use:

Once deployed, simply use your keywords as URLs. For example:
- To link GitHub, use `yourdomain.com/github`.
- To link a Project, use `yourdomain.com/projectName` 

## Contributing

If you have any suggestions, feel free to submit pull requests with your ideas.

**PEACE ✌️**
