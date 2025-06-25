# Health and Fitness Tracker

A web application for tracking workouts, nutrition, and progress, built with Flask and deployed serverlessly on Vercel.

## Features
- Personalized weekly workout plan
- Nutrition suggestions
- Interactive daily workout checklist
- Dynamic progress and activity chart

## Project Structure
```
Health and Fitness Tracker/
  api/
    index.py           # Flask app entry point (for Vercel serverless)
  static/              # Static files (images, CSS, JS)
  templates/           # Jinja2 HTML templates
  requirements.txt     # Python dependencies
  vercel.json          # Vercel deployment config
```

## Local Development
1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
2. **Run Flask app locally:**
   ```sh
   export FLASK_APP=api/index.py
   flask run
   ```
   Or, if using Windows:
   ```sh
   set FLASK_APP=api/index.py
   flask run
   ```
3. **Visit:** [http://localhost:5000](http://localhost:5000)

## Deploying to Vercel
1. **Install Vercel CLI:**
   ```sh
   npm install -g vercel
   ```
2. **Login to Vercel:**
   ```sh
   vercel login
   ```
3. **Deploy:**
   ```sh
   vercel --prod
   ```
   Follow the prompts. Vercel will build and deploy your app.

## Notes
- **Static and template folders** must be in the project root (not inside `api/`).
- **No `app.run()` needed** in `api/index.py` (Vercel handles the server).
- **Persistence:** For persistent data, use a cloud database (not local files), as Vercel serverless functions are stateless.

## License
MIT 