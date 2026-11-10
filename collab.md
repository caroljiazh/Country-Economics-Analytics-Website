# Collaboration

**Final Deliverable**
- https://www.w3schools.com/howto/howto_js_navbar_sticky.asp
    - After suggestions, we sticked the navbar so it always shows up even scrolling.

- https://www.w3schools.com/howto/howto_js_autocomplete.asp
    - We were having trouble making autocomplete for our html page so we used Geeks for Geeks code
    - Some of the autocomplete code is directly copied from https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_autocomplete (javascript functions and autoscript initiation)
 
- https://gemini.google.com/app
    - We used Gemini to help figure out how to test flask pages.
    - The prompt was the code for one of our old flask test routes (test valid country route) with the phrase "How do I make this test function when the output should be a flask html page"
    - It responded saying we should include a line `html_content = response.get_data(as_text=True)` before using `html_content` as our response data.

**Front End**
- https://claude.ai
    - We used Claude for the style.css. The prompt was 'create a light and gentle CSS theme for this html' with our homepage html attached. The style.css is commented to show that we understand what it is doing and how it works. It is surprisingly difficult to find colors that work well together!
    - Here's the claude response back:
Now I have a clear picture of all the HTML templates. Let me analyze what's missing/needed and write an updated `style.css`.

Now I have everything I need. The existing CSS is missing styles for: `<h1>` on result/about pages (bare, outside `.hero`), `<dl>`, `<dt>`, `<dd>` on the about page, `<progress>` + `<output>` on the results pages, `<canvas>` for the chart, and the result `<section>` wrappers. Let me write the updated CSS.

Here's what was added to your original CSS (all colors, tokens, and formatting style kept intact):

New sections covering your HTML templates:

- **Bare `<h1>` on result/about pages** — the heading that appears directly in `<body>` or `<main>` (outside `.hero`) now gets the same warm brown styling, with a bottom border separator and proper margin.
- **Definition lists (`<dl>`, `<dt>`, `<dd>`) in `about_page.html`** — styled with a two-column grid layout so the label (Data Source, Citation, etc.) sits neatly beside its value, using your existing brown and text-light colors.
- **`<progress>` bars** — fully custom-styled across Chrome, Firefox, and Safari to match your brown palette (`--brown` fill on a `--border`-colored track), with rounded caps.
- **`<output>` element** — the bold percentage readout next to the progress bar is now styled to match your UI font and brown-dark color.
- **`main section` (result pages)** — the result card sections get the same card treatment (white background, border-top accent, shadow, radius) as your home page cards.
- **`canvas#schoolingChart`** — the Chart.js canvas gets padding, border, shadow, and centered layout. The alt-text `<h2>` below it is styled as a small, muted caption.
- **Responsive additions** — the result section cards collapse gracefully on mobile too.

- https://gemini.google.com/app
    - `results_literacy.html` mentions Gemini was used because I (Gray) used it in my individual frontend, and we decided to copy-paste our individual front end htmls into the templates. Gemini was not used on this deliverable.


**Command Line Interface**
- https://gemini.google.com/app - I needed help reversing a list that is returned
    - I originally had a second list that I resorted in reverse, but I thought that was too inefficient so I hit the refactoring code into gemini and asked if there was a more effective way of inverting the list
- https://www.calculatorsoup.com/calculators/algebra/percentage-increase-calculator.php (last updated November 21, 2025) - I had to double check how to calculate percent increase.
- https://docs.python.org/3/tutorial/datastructures.html (last updated May 18, 2026) - Used because I am still new to python and did not know as much as I needed to about list and dicts
- https://docs.python.org/3/howto/sorting.html (last updated May 18, 2026) - Used because I am still new to python and needed help with writing `sort` calls for lists.


**Flask**
- Used Gemini specifically to figure out how to return a multi-line statement. It is the statement in the 404 error app route. Gemini told me to add `<br>`
- We used the moodle flask lab to figure out how to do 404 responses and connect

**Database**
- https://flask.palletsprojects.com/en/stable/api/#flask.Flask.run (updated February 19, 2026) - Used because I wasn't sure how to run the flask and call port so I used the flask page the flask.run() section
- https://docs.python.org/3/library/sys.html (last updated May 18, 2026) - Used to consult sys arguments
- https://www.postgresql.org/docs/current/sql-copy.html (updated May 14, 2026) SQL website used to learn copy command and avoid csv heading.



