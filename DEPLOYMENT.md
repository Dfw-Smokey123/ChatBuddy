# ChatBuddy Deployment Guide

## Local Development

1. Create a `.env` file in the root directory:
```
GROQ_API_KEY=your-groq-api-key-here
DEBUG_MODE=false
STREAMLIT_THEME=dark
```

2. Run locally:
```bash
streamlit run streamlit_app.py
```

## Streamlit Cloud Deployment

### Prerequisites
- GitHub account with this repository
- Streamlit Cloud account (free tier available)
- Groq API key

### Step 1: Add Secrets to Streamlit Cloud

1. Go to [Streamlit Cloud Dashboard](https://share.streamlit.io/)
2. Select your app from the list
3. Click the **"⋮"** menu → **Settings**
4. Go to the **Secrets** section
5. Add your secrets in TOML format:

```toml
GROQ_API_KEY = "your-actual-groq-api-key"
```

**Important**: Never commit `.env` or `.streamlit/secrets.toml` files to GitHub. They're in `.gitignore` for security.

### Step 2: Deploy

1. Ensure all changes are pushed to GitHub (`master` branch)
2. Go to [Streamlit Cloud](https://share.streamlit.io/)
3. Click **"New app"**
4. Select your repository, branch (`master`), and main file (`streamlit_app.py`)
5. Click **Deploy**

The app will automatically:
- Install dependencies from `requirements.txt`
- Load secrets from Streamlit Cloud
- Run your application

### Step 3: Monitor

- Check logs in the Streamlit Cloud dashboard
- The app will restart automatically on code changes
- Use the ⬆️ **Redeploy** button if needed

## Environment Variables

| Variable | Local | Cloud | Required |
|----------|-------|-------|----------|
| GROQ_API_KEY | `.env` | Secrets | Yes |
| DEBUG_MODE | `.env` | Secrets | No |
| STREAMLIT_THEME | `.env` | Secrets | No |

## Troubleshooting

### "GROQ_API_KEY not found"
- **Local**: Check `.env` file exists and has the correct key
- **Cloud**: Go to app Settings → Secrets and verify GROQ_API_KEY is set

### Dependencies Won't Install
- Clear cache: Settings → Cache → Clear cache
- Check `requirements.txt` for version conflicts
- Use `pip install -r requirements.txt` locally first to verify

### API Calls Fail
- Verify Groq API key is valid at [console.groq.com](https://console.groq.com)
- Check remaining API quota
- Review Groq API documentation for rate limits

## API Key Security Best Practices

1. ✅ **DO**: Store API keys in Streamlit Secrets (cloud) or `.env` (local)
2. ✅ **DO**: Add `.env` and `.streamlit/secrets.toml` to `.gitignore`  
3. ❌ **DON'T**: Hardcode API keys in Python files
4. ❌ **DON'T**: Commit `.env` files to GitHub
5. ❌ **DON'T**: Share API keys in public channels

