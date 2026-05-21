# Claremont Student IT Help

Standalone student-facing IT help site for school laptops, accounts, ClassLink, OneDrive, apps, safety and common troubleshooting.

This project is separate from the staff support site and the laptop onboarding site. It does not include a `CNAME` yet, so it is safe to publish initially on a default GitHub Pages project URL.

## Local preview

```powershell
python -m http.server 8080
```

Then open `http://localhost:8080`.

## Rebuild generated pages

```powershell
python scripts\build_site.py
```

The generator rebuilds article pages, category pages, the homepage and the search index from the article definitions in `scripts/build_site.py`.
