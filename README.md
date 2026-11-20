# Sort Decks by Column

An Anki add-on that lets you sort the decks on the main screen by clicking a column header. It works with **Deck**, **New**, **Learn** and **Review** in any interface language, because the column is identified by its position, not by its label.

## Installation

1. Download the `.ankiaddon` file from the [Releases](https://github.com/hd1fernando/anki-sort-by-due/releases) page.
2. Open the downloaded file (double-click) or use **Tools → Add-ons → Install from file...**.
3. Restart Anki.

## Usage

Click the header of the column you want to sort by:

- **First click:** ascending order (`▲`);
- **clicking the same column:** switches to descending order (`▼`);
- **clicking another column:** resets to ascending order.

Subdecks stay with their parent deck, so the hierarchy is preserved. The last column and direction are reapplied whenever the screen is refreshed (if `remember_last_sort` is enabled).

Sorting is visual only: it does not change the actual study order or any collection data.

## Compatibility

- Anki Desktop 2.1.50 or newer, including 25.x and 26.x.
- Tested on Anki 26.09.4.

## Configuration

Go to **Tools → Add-ons → Sort Decks by Column → Edit...**:

| Option | Default | Description |
| --- | --- | --- |
| `enabled` | `true` | Enables or disables the add-on. |
| `show_indicator` | `true` | Shows `▲`/`▼` on the active header. |
| `remember_last_sort` | `true` | Reapplies the last sort after every render. |

## Development

```bash
python3 scripts/build.py
```

This generates `dist/sort_by_due-1.0.0.ankiaddon` with the contents of the `addon/` folder at the root of the archive. To test locally, extract the contents of `addon/` into `addons21/sort_by_due/` and restart Anki.

## License

MIT — see [LICENSE](LICENSE).
