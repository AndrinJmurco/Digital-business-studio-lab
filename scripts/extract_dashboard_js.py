from pathlib import Path
import re
html=Path(__file__).resolve().parents[1].joinpath('assets/business-studio-offline.html').read_text(encoding='utf-8')
parts=re.findall(r'<script[^>]*>(.*?)</script>', html, re.S|re.I)
if not parts: raise SystemExit('No inline JS found')
print('\n'.join(parts))
