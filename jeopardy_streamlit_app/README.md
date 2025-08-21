# Wedding Jeopardy — Streamlit

A web version of your Jeopardy-style game. No Apple developer certificates needed. Share via Streamlit or run locally.

## Local Run

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

The app opens at http://localhost:8501

## Deploy to Streamlit Community Cloud (free)

1. Create a GitHub repo (e.g., `wedding-jeopardy-streamlit`) and push these files.
2. Go to https://share.streamlit.io
3. Choose your repo and set **Main file path** to `streamlit_app.py`.
4. Deploy. Share the URL with your players.

## Files

- `main.py` — your original content (categories/answers and Final Jeopardy).  
- `streamlit_app.py` — Streamlit UI wrapper (reads data embedded in this file that was extracted from your original to keep it self-contained for hosting).  
- `requirements.txt` — Python dependencies (just Streamlit).  
- `.gitignore` — convenience.

## Notes

- The "Bridesmaids" category displays and scores as $200 to match your original app.
- Final Jeopardy has a dedicated flow with scoring buttons.
- If you later edit the categories/answers in `main.py`, you can re-run the wrapper generator to refresh `streamlit_app.py`, or directly edit `streamlit_app.py` where the data dicts live.
