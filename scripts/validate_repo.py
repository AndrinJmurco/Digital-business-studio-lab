from pathlib import Path
import json,re,sys
root=Path(__file__).resolve().parents[1]
errors=[]
skills=sorted((root/'skills').glob('*/SKILL.md'))
if len(skills)!=26: errors.append(f'Expected 26 skills, found {len(skills)}')
for p in skills:
 s=p.read_text(encoding='utf-8')
 if not re.match(r'(?s)\A---\nname: [^\n]+\ndescription: [^\n]+\n---\n',s): errors.append(f'Invalid frontmatter: {p}')
for p in ['plugin.json','.codex-plugin/plugin.json']:
 try:
  x=json.loads((root/p).read_text(encoding='utf-8'))
  if x.get('name')!='digital-business-studio' or x.get('version')!='2.0.0': errors.append(f'Invalid manifest: {p}')
  if '@' in str(x): errors.append(f'Email-like metadata in {p}')
 except Exception as exc: errors.append(f'{p}: {exc}')
agents=(root/'assets/AGENT_LIBRARY.md').read_text(encoding='utf-8')
ids=re.findall(r'^\| (G\d{2}) \|',agents,re.M)
if ids!=[f'G{i:02d}' for i in range(1,55)]: errors.append('Expected G01-G54 agent IDs')
for p in ['assets/business-studio-offline.html','docs/BACKLOG.md','docs/PROJECT_PLAN.md','.github/workflows/validate.yml']:
 if not (root/p).exists(): errors.append(f'Missing {p}')
if errors:
 for err in errors:print('ERROR',err,file=sys.stderr)
 sys.exit(1)
print('PASS: 26 skills, 54 agent recipes, public manifests, dashboard and docs')
