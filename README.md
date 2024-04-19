# AI Copyeditor
A web app that sends text to GPT-3.5-Turbo for copy editing. Built on the Django pure-Python full-stack web application framework.

This web app will handle almost any length behind the scenes, breaking down large documents into chunks of about one thousand words, submitting them in successive API calls, then returning the results in one file. Be mindful that this app breaks documents down by paragraph, so if your document has huge paragraphs (specifically, two successive paragraphs totaling more than about 1500 words), then it may resort in an error. 

## Local setup with Docker

Build a Docker image from the remote repository:

```bash
docker build -t ai-copyeditor . https://github.com/chriscarrollsmith/ai-copyeditor.git
```

Run the Docker container, replacing `$OPENAI_API_KEY` with your [OpenAI API key](https://platform.openai.com/account/api-keys/):

```bash
docker run -e OPENAI_API_KEY=$OPENAI_API_KEY -p 8000:8000 ai-copyeditor
```

## Local setup without Docker

Make sure you have Python 3.12 and poetry installed. Clone the repository and run the following commands:

```bash
poetry install
```

This will install the dependencies. `diff-match-patch` and `python-docx` are used to manage text comparison and creating a downloadable Word file. The `openai` Python library is used to interact with the GPT-3.5-Turbo API. The `python-dotenv` library is used to manage environment variables.

Next, copy the `.env.example` file to `.env` and fill in your [OpenAI API key](https://platform.openai.com/account/api-keys/).

```bash
cp .env.example .env
```

Finally, run the following command to set up the database:

```bash
python manage.py migrate
```

This will create a SQLite database in the root directory of the project.

To run the server, use the following command:

```bash
poetry run python manage.py runserver
```

## Usage

The server will be running at `http://localhost:8000/`. Navigate to this URL in your web browser.

On the uploader page, you may submit a text file, Word document, or paste your text directly into the web page. Click submit and let ChatGPT do the work! Longer pieces will require about 20 seconds per thousand words, so if you are editing a long piece, please have patience!

All of your submissions are stored in the workshop. Click on an article to review ChatGPT's edits against your submission. If reviewing an article after you have already saved changes, you will only see the remaining edits that were not saved. Removed text appears in red, while inserted text appears in green.

## Deployment

This application is deployed with gunicorn. To deploy the application, run the following command:

```bash
poetry run gunicorn editcraft.wsgi:application --bind 0.0.0.0:8000 --workers 4
```
