import re,subprocess,sys
ES='/opt/npm-tools/node_modules/.bin/esbuild'
src=open('src/index.html').read()
def esb(code,loader):
    r=subprocess.run([ES,'--minify','--loader='+loader,'--target=es2018,chrome80,safari13'],input=code,capture_output=True,text=True)
    if r.returncode: raise SystemExit('esbuild fail '+loader+r.stderr[:300])
    return r.stdout.strip()
def sty(m): return m.group(1)+esb(m.group(2),'css')+m.group(3)
def scr(m):
    if 'ld+json' in m.group(1): return m.group(0)
    return m.group(1)+esb(m.group(2),'js')+m.group(3)
out=re.sub(r'(<style[^>]*>)(.*?)(</style>)',sty,src,flags=re.S)
out=re.sub(r'(<script(?![^>]*src)[^>]*>)(.*?)(</script>)',scr,out,flags=re.S)
out=re.sub(r'<!--(?!\[).*?-->','',out,flags=re.S)
# collapse whitespace outside script/style/pre/textarea
parts=re.split(r'(<script.*?</script>|<style.*?</style>|<pre.*?</pre>)',out,flags=re.S)
for i in range(0,len(parts),2): parts[i]=re.sub(r'\s{2,}',' ',parts[i])
out=''.join(parts)
# ld+json compact
def ld(m):
    import json
    try: return m.group(1)+json.dumps(json.loads(m.group(2)),ensure_ascii=False,separators=(',',':'))+m.group(3)
    except Exception: return m.group(0)
out=re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)',ld,out,flags=re.S)
open('index.html','w').write(out)
print(len(src),'->',len(out))
