# Nebraska RARE

Official website for Nebraska RARE - empowering families affected by rare diseases through education, advocacy, and community inclusion.

🌐 **Live Site:** [nebraska-rare.org](https://nebraska-rare.org)

---

## About Nebraska RARE

Nebraska RARE is dedicated to empowering families impacted by rare diseases across Nebraska. We strive to elevate awareness and partner with healthcare providers and communities to ensure every child and adult with a rare condition is understood, supported, and valued.

**Mission:** Build a compassionate network where all families feel seen, heard, and never alone.

---

## Website Structure

This is a simple, static website built with HTML and CSS:

```
nebraska-rare/
├── index.html              # Homepage (rotating hero carousel)
├── who-we-are.html         # Board members page, links to bio pages
├── kelsey-bio.html         # Kelsey Lahaie bio
├── paige-bio.html          # Paige Rivard bio
├── susan-bio.html          # Susan Samuelson bio
├── events.html             # Events + policy victories
├── resources.html          # Resource library
├── contact.html            # Contact form (Formspree)
├── 404.html                # Custom 404 page
├── logo-square.png         # Social share image (og:image / twitter:image — absolute URL, keep in root)
├── favicon.ico, favicon-*.png, apple-touch-icon.png  # Site icons (root, browser/convention paths)
├── CNAME, robots.txt, sitemap.xml, security.txt      # Site/SEO config (must stay in root)
├── images/
│   ├── logo.png            # Nebraska RARE logo (site-wide nav/footer)
│   ├── people/              # Board headshots + homepage hero photos
│   └── partner-logos/        # Third-party org logos used on resources.html
├── scripts/update_sitemap.py        # Sitemap lastmod updater
├── .github/workflows/update-sitemap.yml  # Runs the script on every HTML push
└── README.md               # This file
```

---

## Local Development

### View Locally

1. Clone this repository
2. Open `index.html` in your web browser
3. Navigate between pages using the menu

No build process or dependencies required!

### Making Changes

1. Edit HTML files directly
2. Test changes by refreshing your browser
3. Commit and push to update live site

---

## Deployment

### GitHub Pages (Current)

This site is deployed via GitHub Pages, serving the custom domain:

1. Push changes to `main` branch
2. Site automatically redeploys at `https://nebraska-rare.org` (usually live within a minute or two)
3. `scripts/update_sitemap.py` runs automatically on every HTML push (see `.github/workflows/update-sitemap.yml`) to bump `<lastmod>` dates in `sitemap.xml`

### Custom Domain Setup (already configured)

The `CNAME` file in the repo root points GitHub Pages at `nebraska-rare.org`. DNS is managed at Porkbun with A records pointing to GitHub Pages:
```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

---

## Contact Form

The contact form uses [Formspree](https://formspree.io/) for form handling (already configured, form ID `xdaanbge`, with Formshield spam protection enabled instead of a CAPTCHA). No setup needed — if the endpoint ever needs to change, update `contact.html`:
```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
```

---

## Design

**Brand Colors:**
- Navy Blue: `#002743`
- Red: `#B21214`
- Gold: `#D4A556`

**Typography:**
- Headings: [Lora](https://fonts.google.com/specimen/Lora) (serif)
- Body: [Open Sans](https://fonts.google.com/specimen/Open+Sans) (sans-serif)

**Features:**
- Fully responsive design
- Mobile-friendly navigation
- Accessible color contrast
- Fast loading (no dependencies)

---

## Contributing

Nebraska RARE is a 501(c)(3) tax-exempt nonprofit organization (EIN 42-4109468). This website is maintained by the board of directors.

For suggestions or corrections, please contact us via the website contact form.

---

## License

© 2026 Nebraska RARE. All rights reserved.

---

## Contact

**Email:** info@nebraska-rare.org  
**Website:** [nebraska-rare.org](https://nebraska-rare.org)

---

## Acknowledgments

Built with care for the Nebraska rare disease community.