import json

from aqt import gui_hooks, mw


JS_CODE = r"""
(function () {
    const CONFIG = __CONFIG__;
    if (!CONFIG.enabled) return;

    const STORAGE_KEY = "sort_by_due:last_sort";
    const INDICATOR_CLASS = "sort-by-column-indicator";

    function sortableHeaders() {
        const headerRow = document.querySelector("table tr");
        if (!headerRow) return [];
        const headers = Array.from(headerRow.querySelectorAll("th, td"));
        return headers.slice(0, -1);
    }

    function deckRows() {
        return Array.from(document.querySelectorAll("table tr.deck"));
    }

    function levelOf(row) {
        const cell = row.querySelector("td.decktd");
        const text = cell ? cell.textContent : "";
        const match = text.match(/^\u00a0*/);
        return Math.floor((match ? match[0].length : 0) / 6);
    }

    function valueOf(row, index) {
        if (index === 0) {
            const link = row.querySelector("a.deck");
            return (link ? link.textContent : "").trim();
        }
        const cell = row.cells[index];
        const raw = cell ? cell.textContent : "0";
        const parsed = parseInt(raw.replace(/[^\d]/g, ""), 10);
        return Number.isNaN(parsed) ? 0 : parsed;
    }

    function compare(a, b, index) {
        if (index === 0) {
            return a.localeCompare(b, undefined, { numeric: true, sensitivity: "base" });
        }
        return a - b;
    }

    function readLastSort() {
        try {
            const value = JSON.parse(localStorage.getItem(STORAGE_KEY) || "null");
            return value && typeof value.column === "number" ? value : null;
        } catch (error) {
            return null;
        }
    }

    function writeLastSort(column, descending) {
        try {
            localStorage.setItem(
                STORAGE_KEY,
                JSON.stringify({ column: column, descending: descending })
            );
        } catch (error) {
            return;
        }
    }

    function clearIndicators() {
        const indicators = document.querySelectorAll("." + INDICATOR_CLASS);
        indicators.forEach((element) => element.remove());
    }

    function showIndicator(header, descending) {
        if (!CONFIG.show_indicator) return;
        const span = document.createElement("span");
        span.className = INDICATOR_CLASS;
        span.textContent = descending ? " \u25bc" : " \u25b2";
        header.appendChild(span);
    }

    function applySort(column, descending) {
        const table = document.querySelector("table");
        const rows = deckRows();
        if (!table || rows.length === 0) return;

        const tbody = table.tBodies[0] || table;
        const groups = [];
        let current = null;

        rows.forEach((row) => {
            if (levelOf(row) === 0 || current === null) {
                current = { root: row, rows: [] };
                groups.push(current);
            }
            current.rows.push(row);
        });

        groups.sort((a, b) => {
            const result = compare(
                valueOf(a.root, column),
                valueOf(b.root, column),
                column
            );
            return descending ? -result : result;
        });

        groups.forEach((group) => {
            group.rows.forEach((row) => tbody.appendChild(row));
        });

        clearIndicators();
        const header = sortableHeaders()[column];
        if (header) showIndicator(header, descending);

        if (CONFIG.remember_last_sort) writeLastSort(column, descending);
    }

    function onClick(column) {
        const last = CONFIG.remember_last_sort ? readLastSort() : null;
        const descending = last && last.column === column ? !last.descending : false;
        applySort(column, descending);
    }

    sortableHeaders().forEach((header, column) => {
        header.style.cursor = "pointer";
        header.addEventListener("click", () => onClick(column));
    });

    const last = CONFIG.remember_last_sort ? readLastSort() : null;
    if (last) {
        const limit = sortableHeaders().length - 1;
        const column = Math.min(Math.max(last.column, 0), limit);
        if (column >= 0) applySort(column, last.descending);
    }
})();
"""


def on_deck_browser_did_render(deck_browser) -> None:
    config = mw.addonManager.getConfig(__name__) or {}
    deck_browser.web.eval(JS_CODE.replace("__CONFIG__", json.dumps(config)))


gui_hooks.deck_browser_did_render.append(on_deck_browser_did_render)
