# Nebraska RARE

Official website for Nebraska RARE - empowering families affected by rare diseases through education, advocacy, and community inclusion.

🌐 **Live Site:** [nebraska-rare.org](https://nebraska-rare.org) *(coming soon)*

---

## About Nebraska RARE

Nebraska RARE is dedicated to empowering families impacted by rare diseases across Nebraska. We strive to elevate awareness and partner with healthcare providers and communities to ensure every child and adult with a rare condition is understood, supported, and valued.

**Mission:** Build a compassionate network where all families feel seen, heard, and never alone.

---

## Website Structure

This is a simple, static website built with HTML and CSS:

```
nebraska-rare/
├── index.html          # Mission statement homepage
├── who-we-are.html     # Board members page
├── contact.html        # Contact form
├── logo.png            # Nebraska RARE logo
└── README.md           # This file
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

This site is deployed via GitHub Pages:

1. Push changes to `main` branch
2. Site automatically updates at `https://YOUR-USERNAME.github.io/nebraska-rare/`
3. Custom domain configured via DNS settings

### Custom Domain Setup

DNS A Records pointing to GitHub Pages:
```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

CNAME: `www` → `YOUR-USERNAME.github.io`

---

## Contact Form

The contact form uses [Formspree](https://formspree.io/) for form handling.

**To activate:**
1. Sign up at formspree.io (free)
2. Create a new form
3. Update `contact.html` with your Formspree endpoint:
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

Nebraska RARE is working toward 501(c)(3) nonprofit status. This website is maintained by the board of directors.

For suggestions or corrections, please contact us via the website contact form.

---

## License

© 2026 Nebraska RARE. All rights reserved.

---

## Contact

**Email:** contact@nebraska-rare.org  
**Website:** [nebraska-rare.org](https://nebraska-rare.org)

---

## Acknowledgments

Built with care for the Nebraska rare disease community.