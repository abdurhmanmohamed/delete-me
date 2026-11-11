"""Vercel Python entrypoint.

Vercel looks for a Flask instance named ``app`` in an ``api/`` module and turns it
into a single serverless function. The real application still lives in the
repository root (``server.py``), so add it to ``sys.path`` and re-export it.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server import app  # noqa: E402  (Vercel imports this as the WSGI handler)

__all__ = ["app"]
