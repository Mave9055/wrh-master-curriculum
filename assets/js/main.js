/* WRH Master Curriculum — shared interactions */

(function () {
  "use strict";

  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => Array.from(root.querySelectorAll(selector));

  document.addEventListener("DOMContentLoaded", () => {
    initMobileMenu();
    initSmoothAnchors();
    initProgressTracking();
    initSessionExplorer();
  });

  function initMobileMenu() {
    const toggle = $(".menu-toggle");
    const menu = $("nav ul");
    if (!toggle || !menu) return;

    toggle.addEventListener("click", () => {
      const open = menu.classList.toggle("active");
      toggle.setAttribute("aria-expanded", String(open));
      toggle.setAttribute("aria-label", open ? "Close navigation menu" : "Open navigation menu");
    });

    $$("a", menu).forEach((link) => link.addEventListener("click", () => {
      menu.classList.remove("active");
      toggle.setAttribute("aria-expanded", "false");
    }));
  }

  function initSmoothAnchors() {
    $$('a[href^="#"]').forEach((anchor) => {
      anchor.addEventListener("click", (event) => {
        const target = document.querySelector(anchor.getAttribute("href"));
        if (!target) return;
        event.preventDefault();
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });
  }

  function initProgressTracking() {
    const bar = $(".progress-bar");
    if (!bar) return;
    const update = () => {
      const total = document.documentElement.scrollHeight - window.innerHeight;
      const percent = total > 0 ? Math.min(100, Math.max(0, (window.scrollY / total) * 100)) : 0;
      bar.style.width = `${percent}%`;
    };
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    update();
  }

  async function initSessionExplorer() {
    const shell = $("#session-explorer");
    if (!shell) return;

    const status = $("#catalog-status");
    const list = $("#session-list");
    const content = $("#session-content");
    const search = $("#session-search");
    const results = $("#search-results");
    const previous = $("#previous-session");
    const next = $("#next-session");
    const position = $("#session-position");
    let sessions = [];
    let currentIndex = -1;

    try {
      const response = await fetch("../assets/data/sessions.json");
      if (!response.ok) throw new Error(`Catalog request failed (${response.status})`);
      const catalog = await response.json();
      sessions = catalog.sessions || [];
      if (!sessions.length) throw new Error("The catalog is empty.");
      shell.hidden = false;
      status.textContent = `${sessions.length} source sessions ready. Select one to begin reading.`;
      renderSidebar(sessions);
      selectSession(sessionFromLocation() || sessions[0].id, false);
    } catch (error) {
      status.className = "alert alert-danger";
      status.textContent = "The session catalog could not be loaded. Please refresh the page or browse the Part I–IV overview pages instead.";
      console.error(error);
      return;
    }

    function renderSidebar(items) {
      const groups = new Map();
      items.forEach((session) => {
        if (!groups.has(session.part)) groups.set(session.part, { label: session.partLabel, theme: session.theme, items: [] });
        groups.get(session.part).items.push(session);
      });
      list.innerHTML = Array.from(groups.values()).map((group) => `
        <div class="session-group">
          <div class="session-group-title"><span>${group.label}</span><span>${group.items.length}</span></div>
          <ul class="session-list">
            ${group.items.map((session) => `<li><a href="#${session.id}" data-session-id="${session.id}"><strong>${String(session.number).padStart(2, "0")}</strong> ${escapeHtml(session.title)}</a></li>`).join("")}
          </ul>
        </div>
      `).join("");

      $$('[data-session-id]', list).forEach((link) => link.addEventListener("click", (event) => {
        event.preventDefault();
        selectSession(link.dataset.sessionId, true);
      }));
    }

    function selectSession(id, updateUrl = true) {
      const nextIndex = sessions.findIndex((session) => session.id === id);
      if (nextIndex < 0) return;
      currentIndex = nextIndex;
      const session = sessions[currentIndex];
      content.innerHTML = `
        <div class="session-meta"><span class="meta-pill">${session.partLabel}</span><span class="meta-pill">Session ${String(session.number).padStart(2, "0")}</span><span class="meta-pill">Source: ${escapeHtml(session.filename)}</span></div>
        <h1>${escapeHtml(session.title)}</h1>
        <p style="color:var(--ink-muted); max-width: 760px;">${escapeHtml(session.summary)}</p>
        <hr style="border:0; border-top:1px solid var(--line); margin:1.6rem 0;">
        <div class="markdown-body">${session.html}</div>
        <div class="session-toolbar" style="margin-top:2rem; margin-bottom:0;"><span style="color:var(--ink-muted); font-size:.8rem;">You are reading ${currentIndex + 1} of ${sessions.length}</span><a class="btn btn-outline" href="../${session.sourcePath}" target="_blank" rel="noopener">Open source file ↗</a></div>
      `;
      position.textContent = `${session.partLabel} · Session ${String(session.number).padStart(2, "0")} · ${session.title}`;
      previous.disabled = currentIndex === 0;
      next.disabled = currentIndex === sessions.length - 1;
      $$("[data-session-id]", list).forEach((link) => link.classList.toggle("active", link.dataset.sessionId === session.id));
      if (updateUrl) history.replaceState(null, "", `#${session.id}`);
      localStorage.setItem("wrh-last-session", session.id);
      content.focus({ preventScroll: true });
    }

    function sessionFromLocation() {
      const hash = window.location.hash.replace(/^#/, "");
      const stored = localStorage.getItem("wrh-last-session");
      const candidate = hash || stored;
      return sessions.some((session) => session.id === candidate) ? candidate : null;
    }

    function runSearch(query) {
      const term = query.trim().toLowerCase();
      if (!term) {
        results.hidden = true;
        results.innerHTML = "";
        list.hidden = false;
        return;
      }
      const matches = sessions.filter((session) => `${session.title} ${session.partLabel} ${session.text}`.includes(term)).slice(0, 18);
      list.hidden = true;
      results.hidden = false;
      results.innerHTML = matches.length ? matches.map((session) => `<a class="search-result" href="#${session.id}" data-search-id="${session.id}"><strong>Session ${String(session.number).padStart(2, "0")}: ${escapeHtml(session.title)}</strong><small>${session.partLabel} · ${escapeHtml(session.summary.slice(0, 130))}</small></a>`).join("") : '<div class="empty-state" style="padding:1.5rem .5rem;"><p>No sessions match that search.</p></div>';
      $$('[data-search-id]', results).forEach((link) => link.addEventListener("click", (event) => {
        event.preventDefault();
        selectSession(link.dataset.searchId, true);
        search.value = "";
        results.hidden = true;
        list.hidden = false;
      }));
    }

    search.addEventListener("input", () => runSearch(search.value));
    previous.addEventListener("click", () => { if (currentIndex > 0) selectSession(sessions[currentIndex - 1].id, true); });
    next.addEventListener("click", () => { if (currentIndex < sessions.length - 1) selectSession(sessions[currentIndex + 1].id, true); });
    window.addEventListener("hashchange", () => selectSession(sessionFromLocation(), false));
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>'"]/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" }[char]));
  }

  window.WRH = {
    formatDate: (date) => new Date(date).toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric" }),
    validateForm: (formId) => {
      const form = document.getElementById(formId);
      if (!form) return false;
      let valid = true;
      $$('[required]', form).forEach((field) => {
        field.classList.toggle("error", !field.value.trim());
        valid = valid && Boolean(field.value.trim());
      });
      return valid;
    }
  };
})();
