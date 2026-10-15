# 📄 ATS Resume Analyzer

Upload a resume (PDF, DOCX or TXT), optionally paste a job description, and get:

- an **overall ATS score (0-100)** with a category breakdown
- found vs. **missing keywords**
- **prioritised improvements** and **bullet-point rewrites**
- a downloadable Markdown report

Built with [Streamlit](https://streamlit.io) and Google **Gemini Flash**.

> The overall score is calculated in code from five category scores
> (keywords 30%, formatting 20%, content 20%, impact 15%, structure 15%).
> It is an estimate, not the output of any real employer's ATS.
> Formatting is judged from the extracted text only, not the visual layout.

## Files

| File | Purpose |
|------|---------|
| `app.py` | The Streamlit app |
| `requirements.txt` | Python dependencies |
| `README.md` | This file |

## Run locally

1. Get a free API key: https://aistudio.google.com/apikey
2. Install and run:

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

export GEMINI_API_KEY="your-key"   # Windows PowerShell: $env:GEMINI_API_KEY="your-key"
streamlit run app.py
```

Alternatively, create `.streamlit/secrets.toml` (never commit it):

```toml
GEMINI_API_KEY = "your-key"
```

## Choosing the Gemini model

The default is `gemini-3.6-flash`. Google retires models regularly, so if you see a
"model not found" error, change it in the sidebar, or set the `GEMINI_MODEL` env var / secret
(for example `gemini-2.5-flash`). Current names: https://ai.google.dev/gemini-api/docs/models

## Push to GitHub

```bash
cd your-project-folder
git init
printf "venv/\n__pycache__/\n.env\n.streamlit/secrets.toml\n" > .gitignore
git add .
git commit -m "Initial commit: ATS resume analyzer"
git branch -M main
```

Create an empty repository on https://github.com/new (do not add a README there), then:

```bash
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

If GitHub asks for a password, use a Personal Access Token
(GitHub -> Settings -> Developer settings -> Tokens) or sign in with GitHub CLI (`gh auth login`).

## Deploy on Streamlit Community Cloud (free)

1. Go to https://share.streamlit.io and sign in with GitHub.
2. Click **Create app** -> **Deploy a public app from GitHub**.
3. Pick your repository, branch `main`, and main file path `app.py`.
4. Open **Advanced settings** and paste into **Secrets**:
   ```toml
   GEMINI_API_KEY = "your-key"
   ```
5. Click **Deploy**. After a minute or two you get a public `https://<name>.streamlit.app` URL.

Every `git push` to `main` redeploys the app automatically.

### Important notes

- Never commit your API key. Use secrets only.
- A public app that uses **your** key spends **your** quota. Anyone with the link can use it.
  To avoid this, remove the key from secrets and let each visitor paste their own in the sidebar,
  or make the app private in the Streamlit settings.
- Resumes are sent to Google's Gemini API. Tell users so (the app already says it in the sidebar).
- Scanned/image-only PDFs have no extractable text; the app will tell the user to upload a text-based file.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `404 model not found` | Change the model name in the sidebar (see above) |
| `API key not valid` | Create a new key at aistudio.google.com/apikey |
| `429 / quota exceeded` | Wait a minute or use a billing-enabled key |
| "Almost no text could be extracted" | Upload a text-based PDF or a DOCX |
| `ModuleNotFoundError` on deploy | Make sure `requirements.txt` is in the repo root |
