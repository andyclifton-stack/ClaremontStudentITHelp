import html
import json
import re
import shutil
import stat
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SITE_TITLE = "Claremont Student IT Help"

CATEGORIES = [
    ("start-here", "Start Here", "The essentials to get unstuck quickly."),
    ("laptop-basics", "Laptop Basics", "Daily use, charging, updates and looking after your laptop."),
    ("accounts-sign-in", "Accounts & Sign-In", "Passwords, first sign-in and school account safety."),
    ("classlink-apps", "ClassLink & Apps", "Opening ClassLink, finding apps and installing approved software."),
    ("files-onedrive", "Files & OneDrive", "Where to save work and how to recover files."),
    ("troubleshooting", "Troubleshooting", "Quick fixes for sound, power, display and connection problems."),
    ("safety-security", "Safety & Security", "Phishing, passwords and keeping your laptop safe."),
    ("accessibility", "Accessibility", "Tools that make reading, writing and screen use easier."),
    ("exams", "Exams", "Using your laptop safely and sensibly around exam periods."),
]


def slugify(value):
    value = html.unescape(value).strip().lower().replace("&", "and")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-") or "page"


def article(title, category, summary, body):
    return {
        "title": title,
        "category": category,
        "summary": summary,
        "body": body.strip(),
        "slug": slugify(title),
    }


ARTICLES = [
    article(
        "Getting started with your school Windows 11 laptop",
        "Laptop Basics",
        "The first things to know when you start using your managed Windows 11 laptop at school.",
        """
        <p>Your school Windows 11 laptop is set up for learning. It uses your school account, connects to school services, and has settings that help keep school work safe and consistent.</p>
        <h2>Before you bring it to lessons</h2>
        <ul>
          <li>Charge it fully before school. Classroom charging points are limited.</li>
          <li>Bring your charger and stylus if your lessons need them.</li>
          <li>Restart it regularly so updates can finish properly.</li>
          <li>Save school work in OneDrive or another school-approved cloud location.</li>
        </ul>
        <h2>What is different about a managed laptop?</h2>
        <p>The school can apply security, safeguarding, filtering and learning settings. This also means some settings are restricted and students do not have administrator access.</p>
        <div class="callout blue"><p><strong>Good habit:</strong> if something odd happens, restart first, then check the relevant guide. A restart fixes more problems than it has any right to.</p></div>
        """,
    ),
    article(
        "Signing in for the first time",
        "Accounts & Sign-In",
        "How to sign in with your school account and what to check if the first sign-in does not work.",
        """
        <p>Use your school account to sign in. This is the same school identity used for ClassLink and Microsoft services.</p>
        <h2>First sign-in checklist</h2>
        <ol>
          <li>Connect to WiFi if the laptop asks for a network. In school, your laptop should normally use <strong>CLM-Secure</strong> automatically.</li>
          <li>Enter your school email address when asked.</li>
          <li>Enter your school password.</li>
          <li>Wait while Windows finishes preparing your account. The first sign-in can take longer than normal.</li>
          <li>Open ClassLink once you reach the desktop and check that your main school apps appear.</li>
        </ol>
        <h2>If it does not work</h2>
        <ul>
          <li>Check that your email address is typed correctly.</li>
          <li>Make sure Caps Lock is not on.</li>
          <li>Restart the laptop and try again.</li>
          <li>If you are still stuck, speak to your form tutor.</li>
        </ul>
        """,
    ),
    article(
        "What to do if you forgot your password",
        "Accounts & Sign-In",
        "What students should do when they cannot remember their school password.",
        """
        <p>If you cannot remember your school password, do not keep guessing for ages. You may lock yourself out temporarily.</p>
        <h2>What to do</h2>
        <ol>
          <li>Check that you are using your school account, not a personal Microsoft or Google account.</li>
          <li>Check Caps Lock and keyboard layout.</li>
          <li>Try signing in once more slowly.</li>
          <li>If it still does not work, speak to your form tutor and explain that you need a password reset.</li>
        </ol>
        <h2>What to include when asking for help</h2>
        <ul>
          <li>Your full name and form group.</li>
          <li>Whether the problem is with Windows, ClassLink, Google, Microsoft 365 or all of them.</li>
          <li>Any exact error message you can see.</li>
        </ul>
        <div class="callout"><p><strong>Never share your password</strong> with another student, even if they are trying to help.</p></div>
        """,
    ),
    article(
        "How to open ClassLink",
        "ClassLink & Apps",
        "How to get to ClassLink and sign in with the correct school account.",
        """
        <p>ClassLink is the launchpad for many school systems and learning apps.</p>
        <h2>Open ClassLink</h2>
        <ol>
          <li>Open your browser.</li>
          <li>Go to <a href="https://launchpad.classlink.com/ispschools">launchpad.classlink.com/ispschools</a>.</li>
          <li>Choose the Microsoft sign-in option if asked.</li>
          <li>Sign in with your school email address and password.</li>
        </ol>
        <h2>If you land on the wrong ClassLink page</h2>
        <p>If you see a generic page asking you to find your login page, search for <strong>ISP</strong>, choose <strong>Staff and Students</strong>, then sign in with Microsoft.</p>
        """,
    ),
    article(
        "ClassLink is using the wrong Microsoft account",
        "ClassLink & Apps",
        "How to fix ClassLink if the browser tries to use a personal Microsoft account.",
        """
        <p>If ClassLink keeps choosing a personal Microsoft account, your browser is probably already signed in to that account.</p>
        <h2>Fix the account selection</h2>
        <ol>
          <li>Go to <a href="https://myaccount.microsoft.com/">myaccount.microsoft.com</a>.</li>
          <li>Select your profile picture or initials in the top-right corner.</li>
          <li>Sign out of the personal account.</li>
          <li>Sign in with your school account.</li>
          <li>Return to ClassLink and try again.</li>
        </ol>
        <h2>If it still happens</h2>
        <p>Try a different browser, or ask your form tutor to request IT help with clearing the browser sign-in state.</p>
        """,
    ),
    article(
        "How to connect to school WiFi",
        "Laptop Basics",
        "How school WiFi should work on a managed laptop and what to do if it does not connect.",
        """
        <p>Your managed school laptop should connect to <strong>CLM-Secure</strong> automatically when you are on site. You should not need to enter a WiFi password.</p>
        <h2>If WiFi is not connected</h2>
        <ol>
          <li>Select the network icon near the clock.</li>
          <li>Check that WiFi is turned on.</li>
          <li>Look for <strong>CLM-Secure</strong> and try connecting to it.</li>
          <li>If CLM-Secure will not connect, use <strong>CLM Guest</strong>. It has no password.</li>
          <li>Restart the laptop if neither network connects.</li>
        </ol>
        <h2>At home</h2>
        <p>The laptop can connect to home WiFi in the usual way. School management applies to the laptop, not to your home router or other home devices.</p>
        <div class="callout blue"><p><strong>Still stuck?</strong> Tell your form tutor whether the problem is with CLM-Secure, CLM Guest, home WiFi, or all networks.</p></div>
        """,
    ),
    article(
        "How to find your school apps",
        "ClassLink & Apps",
        "Where to look for school apps on your laptop and in ClassLink.",
        """
        <p>Most school apps are available either from ClassLink, the Windows Start menu, or the browser.</p>
        <h2>Places to check</h2>
        <ul>
          <li><strong>ClassLink:</strong> open the launchpad and search for the app name.</li>
          <li><strong>Start menu:</strong> press the Windows key and type the app name.</li>
          <li><strong>Browser:</strong> some tools open as websites rather than installed apps.</li>
          <li><strong>Company Portal:</strong> approved apps may appear here on your managed laptop.</li>
        </ul>
        <h2>If an app is missing</h2>
        <p>Check the spelling, restart the laptop, then speak to your form tutor if the app is needed for schoolwork.</p>
        """,
    ),
    article(
        "How to use OneDrive on your laptop",
        "Files & OneDrive",
        "How OneDrive helps keep school work backed up and available across devices.",
        """
        <p>OneDrive is Microsoft cloud storage. It helps keep your school files backed up and available when you sign in on another school device.</p>
        <h2>Check OneDrive is working</h2>
        <ol>
          <li>Look for the cloud icon near the clock.</li>
          <li>A blue cloud usually means OneDrive is signed in.</li>
          <li>If you see a grey cloud, open it and sign in with your school account.</li>
          <li>Save school documents in your OneDrive folders.</li>
        </ol>
        <h2>Useful folders</h2>
        <p>Use clear folders for subjects, homework and projects. A tidy file system is boring until the exact moment it saves your work.</p>
        """,
    ),
    article(
        "Where should I save my work?",
        "Files & OneDrive",
        "Simple guidance on choosing the right place to save school work.",
        """
        <p>For school work, save files somewhere that is backed up and connected to your school account.</p>
        <h2>Recommended places</h2>
        <ul>
          <li><strong>OneDrive:</strong> best for Microsoft Office files and laptop work.</li>
          <li><strong>Google Drive:</strong> useful when a teacher asks for Google Docs, Sheets or Slides.</li>
          <li><strong>Classroom or subject platforms:</strong> use these when your teacher tells you to submit work there.</li>
        </ul>
        <h2>Avoid</h2>
        <ul>
          <li>Saving important work only in Downloads.</li>
          <li>Keeping the only copy on a USB stick.</li>
          <li>Using personal accounts for school work.</li>
        </ul>
        """,
    ),
    article(
        "How to recover a deleted OneDrive or Google Drive file",
        "Files & OneDrive",
        "Where to look if you deleted or changed a cloud file by mistake.",
        """
        <p>If a file was saved in OneDrive or Google Drive, there is often a way to recover it.</p>
        <h2>OneDrive</h2>
        <ol>
          <li>Open OneDrive in your browser or File Explorer.</li>
          <li>Check the Recycle Bin if the file was deleted.</li>
          <li>For a changed file, open version history if available.</li>
        </ol>
        <h2>Google Drive</h2>
        <ol>
          <li>Open Google Drive.</li>
          <li>Check Trash for deleted files.</li>
          <li>For Google Docs, Sheets or Slides, use version history to look for an earlier version.</li>
        </ol>
        <p>If you cannot find it, speak to your form tutor as soon as possible. File recovery is usually easier if you ask quickly.</p>
        """,
    ),
    article(
        "How to submit an IT help request",
        "Start Here",
        "What students should do before asking for IT help, and what information to include.",
        """
        <p>If something is not working, start with the guide that matches the problem. If you are still stuck, speak to your form tutor.</p>
        <h2>Before asking for help</h2>
        <ol>
          <li>Restart the laptop if it is safe to do so.</li>
          <li>Check the relevant guide on this site.</li>
          <li>Write down the exact error message if one appears.</li>
        </ol>
        <h2>Tell your form tutor</h2>
        <ul>
          <li>What you were trying to do.</li>
          <li>What happened instead.</li>
          <li>When the problem started.</li>
          <li>Whether it happens at school, at home or both.</li>
          <li>Your laptop name or asset label if there is one.</li>
        </ul>
        <div class="callout"><p><strong>Important:</strong> students should speak to their form tutor first rather than going directly to staff support systems.</p></div>
        """,
    ),
    article(
        "Laptop not charging or not turning on",
        "Troubleshooting",
        "Quick checks for power, charging and blank-screen problems.",
        """
        <p>If your laptop will not turn on or charge, try the simple checks first.</p>
        <h2>Power checks</h2>
        <ol>
          <li>Check the charger is plugged into the wall and the laptop.</li>
          <li>Try a different wall socket if one is available.</li>
          <li>Look for a charging light on the laptop or charger.</li>
          <li>Hold the power button for about 10 seconds, then press it once normally.</li>
          <li>Leave it charging for a few minutes before trying again.</li>
        </ol>
        <h2>Ask for help if</h2>
        <ul>
          <li>The charger or cable looks damaged.</li>
          <li>The laptop gets unusually hot.</li>
          <li>It still will not turn on after charging.</li>
        </ul>
        """,
    ),
    article(
        "No sound, microphone, or camera",
        "Troubleshooting",
        "Checks for speaker, microphone and camera problems before asking for help.",
        """
        <p>Sound, microphone and camera problems are often caused by the wrong device being selected or a privacy setting blocking access.</p>
        <h2>Sound</h2>
        <ul>
          <li>Check the volume near the clock.</li>
          <li>Make sure headphones are fully plugged in or Bluetooth headphones are connected.</li>
          <li>Check the app is not muted.</li>
        </ul>
        <h2>Microphone and camera</h2>
        <ul>
          <li>Check whether there is a physical camera cover or mute key.</li>
          <li>Close other apps that might already be using the camera or microphone.</li>
          <li>In Teams or Meet, check the selected camera and microphone before joining.</li>
        </ul>
        <p>If it still does not work after a restart, speak to your form tutor.</p>
        """,
    ),
    article(
        "Connecting to a classroom screen/projector",
        "Troubleshooting",
        "What to check when showing your laptop on a classroom display.",
        """
        <p>If a teacher asks you to connect to a classroom screen or projector, check the display mode and cable connection.</p>
        <h2>Windows display shortcut</h2>
        <ol>
          <li>Press <strong>Windows + P</strong>.</li>
          <li>Choose <strong>Duplicate</strong> if you want the same thing on both screens.</li>
          <li>Choose <strong>Extend</strong> only if you need a second desktop.</li>
        </ol>
        <h2>If nothing appears</h2>
        <ul>
          <li>Check the cable is fully connected.</li>
          <li>Check the classroom screen is on the correct input.</li>
          <li>Restart the app you are presenting from.</li>
        </ul>
        <p>Follow your teacher's instructions for classroom equipment.</p>
        """,
    ),
    article(
        "Updating and restarting your laptop",
        "Laptop Basics",
        "Why updates matter and how to restart without losing work.",
        """
        <p>Updates keep your laptop secure and reliable. A restart is often needed before updates fully apply.</p>
        <h2>Before restarting</h2>
        <ul>
          <li>Save your work.</li>
          <li>Close documents and browser tabs you no longer need.</li>
          <li>Make sure the laptop has enough battery or plug it in.</li>
        </ul>
        <h2>Restart properly</h2>
        <ol>
          <li>Select Start.</li>
          <li>Select the power icon.</li>
          <li>Choose Restart.</li>
        </ol>
        <p>Do not hold the power button to turn it off unless the laptop has completely frozen.</p>
        """,
    ),
    article(
        "How to install approved apps",
        "ClassLink & Apps",
        "How approved software can be installed on a managed student laptop.",
        """
        <p>Students do not have administrator rights on managed laptops. This means you cannot install any app you find online.</p>
        <h2>Use Company Portal</h2>
        <ol>
          <li>Open the Start menu.</li>
          <li>Search for <strong>Company Portal</strong>.</li>
          <li>Open it and look for the approved app you need.</li>
          <li>Select the app and choose Install.</li>
        </ol>
        <h2>If the app is not there</h2>
        <p>Speak to your form tutor and explain which app you need, which lesson or subject it is for, and why it is needed.</p>
        <div class="callout blue"><p><strong>Safety note:</strong> do not download installers from random websites. Managed laptops are restricted for security and safeguarding reasons.</p></div>
        """,
    ),
    article(
        "Keeping your laptop safe and charged",
        "Safety & Security",
        "Everyday habits for looking after your laptop, charger and stylus.",
        """
        <p>Your laptop is part of your school equipment. Look after it like you would a calculator, sports kit or exam materials.</p>
        <h2>Daily habits</h2>
        <ul>
          <li>Charge it overnight and bring it to school ready to use.</li>
          <li>Keep liquids away from the keyboard and charger.</li>
          <li>Use a protective case or laptop section in your bag.</li>
          <li>Do not leave it unattended in public areas.</li>
          <li>Keep your stylus with the laptop so it is available for lessons.</li>
        </ul>
        <h2>What not to do</h2>
        <ul>
          <li>Do not lend your laptop to another student.</li>
          <li>Do not use stickers that make it hard to identify.</li>
          <li>Do not wrap the charger cable tightly around the power brick.</li>
        </ul>
        """,
    ),
    article(
        "What to do if your laptop is lost or damaged",
        "Safety & Security",
        "What to do quickly if your laptop, charger or stylus is missing or damaged.",
        """
        <p>If your laptop is lost, stolen or damaged, tell an adult quickly. The sooner it is reported, the easier it is to help.</p>
        <h2>If it is lost</h2>
        <ol>
          <li>Retrace where you last used it.</li>
          <li>Check your classroom, locker, bag and form room.</li>
          <li>Tell your form tutor as soon as possible.</li>
        </ol>
        <h2>If it is damaged</h2>
        <ul>
          <li>Stop using it if there is broken glass, exposed wiring, liquid damage or overheating.</li>
          <li>Do not try to repair it yourself.</li>
          <li>Tell your form tutor what happened and when.</li>
        </ul>
        <p>Parents remain responsible for hardware damage, repair, loss, theft and replacement accessories unless the school has told you otherwise.</p>
        """,
    ),
    article(
        "Spotting phishing and suspicious messages",
        "Safety & Security",
        "How to recognise suspicious emails, chats and links.",
        """
        <p>Phishing messages try to trick you into giving away passwords, opening unsafe files or visiting fake websites.</p>
        <h2>Warning signs</h2>
        <ul>
          <li>The message creates panic or pressure.</li>
          <li>The sender address looks wrong or unfamiliar.</li>
          <li>It asks for your password, codes or personal information.</li>
          <li>The link does not match the organisation it claims to be from.</li>
          <li>There are unexpected attachments.</li>
        </ul>
        <h2>What to do</h2>
        <p>Do not click the link or reply. Take a screenshot if useful, then tell your form tutor or a trusted member of staff.</p>
        """,
    ),
    article(
        "Passwords and account safety",
        "Accounts & Sign-In",
        "Simple rules for protecting your school account.",
        """
        <p>Your school account gives access to your work, email and school systems. Treat it as private.</p>
        <h2>Keep your account safe</h2>
        <ul>
          <li>Use a password that other people cannot guess.</li>
          <li>Do not share your password with friends.</li>
          <li>Do not save your school password on someone else's device.</li>
          <li>Lock your laptop when you step away. Press <strong>Windows + L</strong>.</li>
          <li>Sign out of shared devices when you are finished.</li>
        </ul>
        <h2>If someone else knows your password</h2>
        <p>Tell your form tutor and ask for it to be changed. Do this even if nothing bad has happened yet.</p>
        """,
    ),
    article(
        "Using accessibility tools",
        "Accessibility",
        "Windows tools for text to speech, dictation, zoom and colour filters.",
        """
        <p>Windows includes tools that can make reading, writing and screen use easier. These are useful for lots of students, not only students with a formal access arrangement.</p>
        <h2>Useful shortcuts</h2>
        <ul>
          <li><strong>Text size and zoom:</strong> use Settings, Accessibility, Text size or press Ctrl + plus in many apps.</li>
          <li><strong>Magnifier:</strong> press Windows + Plus to zoom in, Windows + Esc to close Magnifier.</li>
          <li><strong>Dictation:</strong> press Windows + H in a text box.</li>
          <li><strong>Narrator:</strong> press Ctrl + Windows + Enter to turn Narrator on or off.</li>
          <li><strong>Colour filters:</strong> open Settings, Accessibility, Colour filters.</li>
        </ul>
        <h2>Ask if you need a setting changed</h2>
        <p>Some accessibility settings may be restricted on a managed laptop. If a setting would help you learn, speak to your form tutor or learning support staff.</p>
        """,
    ),
    article(
        "Exams: using your laptop safely and correctly",
        "Exams",
        "General exam-period guidance for using a managed laptop responsibly.",
        """
        <p>Follow the instructions given by your teachers and exam staff. Exam rules always come before general laptop guidance.</p>
        <h2>Before an exam period</h2>
        <ul>
          <li>Make sure your laptop charges properly.</li>
          <li>Restart it regularly so updates do not pile up.</li>
          <li>Tell your form tutor early if the keyboard, screen, charger or battery is unreliable.</li>
          <li>Bring your charger if you are told to.</li>
        </ul>
        <h2>During exams or controlled work</h2>
        <ul>
          <li>Only open the software or files you are told to use.</li>
          <li>Do not use messaging, email or websites unless allowed.</li>
          <li>Do not try to change settings or work around restrictions.</li>
        </ul>
        <div class="callout"><p><strong>If in doubt:</strong> ask the supervising member of staff before doing anything on the laptop.</p></div>
        """,
    ),
]

COMMON_TASKS = [
    "How to submit an IT help request",
    "Signing in for the first time",
    "What to do if you forgot your password",
    "How to open ClassLink",
    "How to connect to school WiFi",
    "Where should I save my work?",
    "Laptop not charging or not turning on",
    "No sound, microphone, or camera",
]

def strip_tags(value):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", value)).strip()


def excerpt(value, limit=150):
    text = strip_tags(value)
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].rstrip(" ,.;:") + "..."


def article_url(item):
    return f"articles/{item['slug']}/index.html"


def category_url(slug):
    return f"categories/{slug}/index.html"


def root_prefix(output_path):
    depth = len(Path(output_path).parts) - 1
    return "../" * depth


def nav_html(prefix, current=""):
    links = [("index.html", "Home", "home")]
    links.extend((category_url(slug), label, slug) for slug, label, _ in CATEGORIES)
    rendered = []
    for href, label, key in links:
        active = ' aria-current="page" class="active"' if key == current else ""
        rendered.append(f'<a href="{prefix}{href}"{active}>{html.escape(label)}</a>')
    return "".join(rendered)


def page_shell(title, description, body, output_path, current=""):
    prefix = root_prefix(output_path)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} | {SITE_TITLE}</title>
  <meta name="description" content="{html.escape(description[:155])}">
  <link rel="stylesheet" href="{prefix}assets/css/styles.css">
  <link rel="icon" href="{prefix}favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="{prefix}assets/img/favicon-32.png">
  <link rel="apple-touch-icon" sizes="180x180" href="{prefix}assets/img/favicon-180.png">
</head>
<body data-root="{prefix}">
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
      <span></span><span></span><span></span>
      <span class="sr-only">Menu</span>
    </button>
    <nav id="site-nav" class="site-nav" aria-label="Primary navigation">{nav_html(prefix, current)}</nav>
  </header>
  <main id="main">
{body}
  </main>
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-brand">
        <img src="{prefix}assets/img/claremont-logo.png" alt="Claremont School">
        <span>{SITE_TITLE}</span>
      </div>
      <p>Student-facing help for school laptops, accounts, apps and safe digital learning.</p>
      <p><strong>Need help?</strong> Speak to your form tutor first.</p>
    </div>
  </footer>
  <script src="{prefix}assets/data/search-index.js"></script>
  <script src="{prefix}assets/js/site.js"></script>
</body>
</html>
"""


def home_page():
    by_title = {item["title"]: item for item in ARTICLES}
    common_cards = []
    for title in COMMON_TASKS:
        item = by_title[title]
        common_cards.append(
            f"""<a class="quick-link" href="{article_url(item)}">
              <strong>{html.escape(item['title'])}</strong>
              <span>{html.escape(item['summary'])}</span>
            </a>"""
        )
    category_cards = []
    for index, (slug, label, description) in enumerate(CATEGORIES):
        count = len([item for item in ARTICLES if item["category"] == label])
        accent = ["navy", "blue", "sky", "orange"][index % 4]
        category_cards.append(
            f"""<a class="category-card" href="{category_url(slug)}">
              <span class="category-icon {accent}" aria-hidden="true">{icon_svg(index)}</span>
              <span class="category-count">{count} {'guide' if count == 1 else 'guides'}</span>
              <strong>{html.escape(label)}</strong>
              <small>{html.escape(description)}</small>
            </a>"""
        )
    body = f"""
    <section class="home-hero">
      <div class="container home-hero-inner">
        <div class="home-intro">
          <img class="hero-logo" src="assets/img/claremont-logo-white.png" alt="Claremont School">
          <h1>{SITE_TITLE}</h1>
          <p>Practical help for school laptops, ClassLink, OneDrive, apps, safety and common fixes.</p>
        </div>
        <div class="search-panel" role="search">
          <label for="site-search">Search student IT help</label>
          <input id="site-search" type="search" placeholder="Try password, WiFi, OneDrive, sound or ClassLink">
          <div id="search-results" class="search-results" aria-live="polite"></div>
        </div>
      </div>
    </section>
    <section class="support-strip">
      <div class="container">
        <div class="support-message">
          <strong>Stuck?</strong>
          <span>Try the matching guide first. If you still need help, speak to your form tutor.</span>
          <a class="button" href="{article_url(by_title['How to submit an IT help request'])}">How to ask for help</a>
        </div>
      </div>
    </section>
    <section class="section home-section">
      <div class="container">
        <div class="section-heading">
          <h2>Common Tasks</h2>
          <p>{len(ARTICLES)} student guides across {len(CATEGORIES)} help areas.</p>
        </div>
        <div class="quick-link-grid">{''.join(common_cards)}</div>
      </div>
    </section>
    <section class="section soft home-section">
      <div class="container">
        <div class="section-heading">
          <h2>Browse by Category</h2>
          <p>Choose the area that matches what you are trying to do.</p>
        </div>
        <div class="category-grid">{''.join(category_cards)}</div>
      </div>
    </section>
    <section class="section home-section">
      <div class="container two-col">
        <div>
          <h2>Designed for students</h2>
          <p>This site is separate from staff IT support. It focuses on what students need day to day: signing in, saving work, keeping devices charged, using school apps and fixing common laptop issues.</p>
        </div>
        <aside class="callout blue">
          <p><strong>Managed laptop note:</strong> some settings and app installs are restricted because school laptops are managed for learning, security and safeguarding.</p>
        </aside>
      </div>
    </section>"""
    return page_shell("Home", "Student-facing IT help for Claremont School.", body, "index.html", "home")


def icon_svg(index):
    paths = [
        "M4 5.5h16M4 12h10M4 18.5h16",
        "M4 5h16v10H4V5ZM8 19h8M10 15v4M14 15v4",
        "M12 3l7 3v5c0 4.5-3 7.5-7 10-4-2.5-7-5.5-7-10V6l7-3Z",
        "M7 8h10M7 12h10M7 16h6M5 4h14v16H5V4Z",
        "M6 3h8l4 4v14H6V3ZM13 3v5h5M9 13h6M9 17h4",
        "M8 4h8v4H8V4ZM5 10h14v10H5V10ZM9 14h6",
        "M9.5 12l1.7 1.7 3.8-4M12 3l7 3v5c0 4.5-3 7.5-7 10-4-2.5-7-5.5-7-10V6l7-3Z",
        "M12 4v16M6 8h12M7 16h10M4 20h16",
        "M7 8V4h10v4M7 17H5a2 2 0 0 1-2-2v-4a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2h-2M7 14h10v6H7v-6Z",
    ]
    return f'<svg viewBox="0 0 24 24" focusable="false"><path d="{paths[index % len(paths)]}"></path></svg>'


def category_page(slug, label, description):
    items = [item for item in ARTICLES if item["category"] == label]
    cards = "".join(
        f"""<article class="list-card">
          <h2><a href="../../{article_url(item)}">{html.escape(item['title'])}</a></h2>
          <p>{html.escape(item['summary'])}</p>
        </article>"""
        for item in items
    )
    body = f"""
    <section class="page-hero compact">
      <div class="container">
        <h1>{html.escape(label)}</h1>
        <p class="page-meta">{html.escape(description)} {len(items)} {'guide' if len(items) == 1 else 'guides'} in this section.</p>
      </div>
    </section>
    <section class="section">
      <div class="container list-layout">
        {cards}
      </div>
    </section>"""
    return page_shell(label, description, body, category_url(slug), slug)


def article_page(item):
    related = [other for other in ARTICLES if other["category"] == item["category"] and other["title"] != item["title"]][:3]
    related_links = "".join(
        f'<li><a href="../../{article_url(other)}">{html.escape(other["title"])}</a></li>' for other in related
    )
    body = f"""
    <section class="page-hero compact">
      <div class="container">
        <h1>{html.escape(item['title'])}</h1>
        <p class="page-meta">{html.escape(item['category'])}</p>
      </div>
    </section>
    <section class="section">
      <div class="container article-layout">
        <article class="article-content">
          {item['body']}
        </article>
        <aside class="article-aside">
          <h2>Need more help?</h2>
          <p>If this guide does not solve it, speak to your form tutor and explain what happened.</p>
          <a class="button" href="../../articles/how-to-submit-an-it-help-request/index.html">How to ask for help</a>
          {f'<h3>Related guides</h3><ul>{related_links}</ul>' if related_links else ''}
        </aside>
      </div>
    </section>"""
    return page_shell(item["title"], item["summary"], body, article_url(item), slugify(item["category"]))


def write(path, content):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def main():
    def clear_readonly(func, path, _exc):
        Path(path).chmod(stat.S_IWRITE)
        func(path)

    for folder in ["articles", "categories"]:
        target = ROOT / folder
        if target.exists():
            shutil.rmtree(target, onexc=clear_readonly)

    write("index.html", home_page())
    for slug, label, description in CATEGORIES:
        write(category_url(slug), category_page(slug, label, description))
    for item in ARTICLES:
        write(article_url(item), article_page(item))

    search_index = [
        {
            "title": item["title"],
            "category": item["category"],
            "url": article_url(item),
            "summary": item["summary"],
            "text": strip_tags(item["body"])[:1600],
        }
        for item in ARTICLES
    ]
    write("assets/data/search-index.js", "window.STUDENT_HELP_SEARCH_INDEX = " + json.dumps(search_index, indent=2) + ";\n")
    print(f"Generated {len(ARTICLES)} articles and {len(CATEGORIES)} category pages.")


if __name__ == "__main__":
    main()
