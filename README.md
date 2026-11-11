# delete-me

Flask storefront (products, cart, orders, admin dashboard) deployed as a single
Vercel Function.

- Production: https://delete-me-peach.vercel.app
- Health check: https://delete-me-peach.vercel.app/healthz

## How the deployment works

| File | Purpose |
| --- | --- |
| `server.py` | The Flask app (`app`), models and all routes |
| `api/index.py` | Vercel entrypoint — re-exports `server.app` |
| `vercel.json` | Flask preset + bundles `static/`, `templates/`, seed DB into the function |
| `pyproject.toml` | Pins Python 3.12 and lists the dependencies Vercel installs |

Vercel builds `api/index.py` into one Python function and routes every request
there, so Flask keeps serving `/static/*` and `/templates/*` itself.

## Configuration

Everything is read from the environment, with working defaults:

| Variable | Default | Notes |
| --- | --- | --- |
| `DATABASE_URL` | seeded SQLite copy in `/tmp` | Set this to a Postgres URL (e.g. Supabase) for durable data |
| `SECRET_KEY` | `abdomohamed` | Set a real value in production |
| `SUPABASE_URL` | empty | Used for product image uploads from the admin dashboard |
| `SUPABASE_KEY` | empty | Supabase anon/publishable key |
| `SUPABASE_BUCKET` | `data` | Storage bucket for uploads |

On serverless, the app copies `instance/mariam.db` to `/tmp` on cold start so the
catalogue renders. Writes made through the site are stored in that SQLite file
and are **not** durable on Vercel — set `DATABASE_URL` to Postgres for that.

## Local development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python server.py          # http://127.0.0.1:5000
```
