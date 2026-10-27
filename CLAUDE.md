# Magic Media website
- Single-file static site (`index.html`) for Hostinger. Keep it a full HTML document with the SEO head.
- Whenever the website is changed, commit and push to `origin` automatically (user has given standing permission). `main` = Ember design; branches: `daylight`, `dark`, `dark-full-graphics`.
- Contact: WhatsApp 7904526442, Instagram @_.magic_media._, Facebook profile id 61595099946331.
- **Build:** edit `src/index.html` (readable source), then run `python3 build.py` (needs esbuild; it writes the minified `index.html` that Hostinger serves). Commit both, then push.
- **Performance rules (Lighthouse):** never start hero/LCP text at `opacity:0` (it causes NO_LCP); keep animations to transform; no layout reads in scroll/resize handlers; start canvases after `load`; keep canvas work adaptive.
- `boss-logo.webp` is the Boss Computers client logo used in the testimonial.
