function siteUrl(path) {
  const root = document.body.dataset.root || "";
  return `${root}${path.replace(/^\//, "")}`;
}

function wireNavigation() {
  const button = document.querySelector(".nav-toggle");
  const nav = document.querySelector(".site-nav");
  if (!button || !nav) return;

  button.addEventListener("click", () => {
    const expanded = button.getAttribute("aria-expanded") === "true";
    button.setAttribute("aria-expanded", String(!expanded));
    nav.classList.toggle("open", !expanded);
  });
}

function wireSearch() {
  const input = document.getElementById("site-search");
  const results = document.getElementById("search-results");
  const index = window.STUDENT_HELP_SEARCH_INDEX || [];
  if (!input || !results || !index.length) return;

  function render(matches) {
    if (!input.value.trim()) {
      results.innerHTML = "";
      results.classList.remove("active");
      return;
    }

    results.classList.add("active");
    if (!matches.length) {
      results.innerHTML = "<p>No matching guides found.</p>";
      return;
    }

    results.innerHTML = matches
      .slice(0, 8)
      .map(
        (item) => `<a href="${siteUrl(item.url)}">
          <strong>${item.title}</strong>
          <span>${item.category} - ${item.summary || "Open guide"}</span>
        </a>`
      )
      .join("");
  }

  input.addEventListener("input", () => {
    const terms = input.value.toLowerCase().split(/\s+/).filter(Boolean);
    if (!terms.length) {
      render([]);
      return;
    }

    const matches = index
      .map((item) => {
        const haystack = `${item.title} ${item.category} ${item.summary} ${item.text}`.toLowerCase();
        const score = terms.reduce((total, term) => total + (haystack.includes(term) ? 1 : 0), 0);
        return { ...item, score };
      })
      .filter((item) => item.score > 0)
      .sort((a, b) => b.score - a.score || a.title.localeCompare(b.title));

    render(matches);
  });

  document.addEventListener("click", (event) => {
    if (!event.target.closest(".search-panel")) {
      results.classList.remove("active");
    }
  });

  input.addEventListener("focus", () => {
    if (input.value.trim() && results.innerHTML.trim()) {
      results.classList.add("active");
    }
  });
}

wireNavigation();
wireSearch();
