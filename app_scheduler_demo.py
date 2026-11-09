# Author: Gracious Cunningham
# NOT TESTED JUST A DEMO -- DONT TOUCH

import sqlite3
import tkinter as tk
from datetime import datetime, date, timedelta
from tkinter import ttk, messagebox, simpledialog

DB_FILE = "therapist_flow.db"
SESSION_TYPES = ["Individual", "Couples", "Family", "Group", "Intake", "Crisis", "Supervision"]
STATUSES = ["Scheduled", "Completed", "Cancelled", "No-show"]
COUNTS_TOWARD_LOAD = ("Scheduled", "Completed")  # cancelled / no-show don't add load
DEFAULT_SETTINGS = {"max_weekly_hours": "25", "max_daily_hours": "6"}
RISK_COLORS = {"Low": "#2e7d32", "Moderate": "#ef8f00", "High": "#c62828"}


# --------------------------------------------------------------------------
# Database stuff that needs to be changed
# --------------------------------------------------------------------------
'''
class Database:
    def __init__(self, path=DB_FILE):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute(
            """CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client TEXT NOT NULL,
                session_date TEXT NOT NULL,
                start_time TEXT NOT NULL,
                duration_min INTEGER NOT NULL,
                type TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'Scheduled',
                notes TEXT DEFAULT '',
                override_reason TEXT DEFAULT ''
            )"""
        )
        self.conn.execute("CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT)")
        for k, v in DEFAULT_SETTINGS.items():
            self.conn.execute("INSERT OR IGNORE INTO settings VALUES (?, ?)", (k, v))
        self.conn.commit()

    # settings
    def get_setting(self, key):
        row = self.conn.execute("SELECT value FROM settings WHERE key=?", (key,)).fetchone()
        return float(row["value"]) if row else float(DEFAULT_SETTINGS[key])

    def set_setting(self, key, value):
        self.conn.execute("INSERT OR REPLACE INTO settings VALUES (?, ?)", (key, str(value)))
        self.conn.commit()

    # sessions
    def add(self, d):
        cur = self.conn.execute(
            """INSERT INTO sessions (client, session_date, start_time, duration_min, type,
               status, notes, override_reason) VALUES (?,?,?,?,?,?,?,?)""",
            (d["client"], d["date"], d["time"], d["duration"], d["type"],
             d["status"], d["notes"], d.get("override_reason", "")),
        )
        self.conn.commit()
        return cur.lastrowid

    def update(self, sid, d):
        self.conn.execute(
            """UPDATE sessions SET client=?, session_date=?, start_time=?, duration_min=?,
               type=?, status=?, notes=?, override_reason=? WHERE id=?""",
            (d["client"], d["date"], d["time"], d["duration"], d["type"],
             d["status"], d["notes"], d.get("override_reason", ""), sid),
        )
        self.conn.commit()

    def set_status(self, sid, status):
        self.conn.execute("UPDATE sessions SET status=? WHERE id=?", (status, sid))
        self.conn.commit()

    def delete(self, sid):
        self.conn.execute("DELETE FROM sessions WHERE id=?", (sid,))
        self.conn.commit()

    def get(self, sid):
        return self.conn.execute("SELECT * FROM sessions WHERE id=?", (sid,)).fetchone()

    def in_range(self, start=None, end=None):
        q, args = "SELECT * FROM sessions", []
        if start and end:
            q += " WHERE session_date BETWEEN ? AND ?"
            args = [start.isoformat(), end.isoformat()]
        q += " ORDER BY session_date, start_time"
        return self.conn.execute(q, args).fetchall()
'''


# --------------------------------------------------------------------------
# Workload logic (kept separate from the UI so it is easy to extend later)
# --------------------------------------------------------------------------
def week_start(d):
    return d - timedelta(days=d.weekday())


def to_minutes(hhmm):
    h, m = hhmm.split(":")
    return int(h) * 60 + int(m)


class Workload:
    def __init__(self, db):
        self.db = db

    def totals(self, monday, exclude_id=None, extra=None):
        """Return (week_minutes, {date_iso: minutes}) for the week starting `monday`.
        `extra` = (date_iso, minutes) to include a hypothetical session."""
        per_day = {}
        for r in self.db.in_range(monday, monday + timedelta(days=6)):
            if r["id"] == exclude_id or r["status"] not in COUNTS_TOWARD_LOAD:
                continue
            per_day[r["session_date"]] = per_day.get(r["session_date"], 0) + r["duration_min"]
        if extra:
            per_day[extra[0]] = per_day.get(extra[0], 0) + extra[1]
        return sum(per_day.values()), per_day

    def limits(self):
        return (self.db.get_setting("max_weekly_hours") * 60,
                self.db.get_setting("max_daily_hours") * 60)

    def risk(self, week_minutes, per_day):
        max_week, max_day = self.limits()
        ratio = max(week_minutes / max_week if max_week else 0,
                    max(per_day.values(), default=0) / max_day if max_day else 0)
        if ratio >= 1:
            return "High"
        return "Moderate" if ratio >= 0.75 else "Low"


# --------------------------------------------------------------------------
# Add / edit dialog
# --------------------------------------------------------------------------
class SessionDialog(tk.Toplevel):
    def __init__(self, parent, on_save, session=None, default_date=None):
        super().__init__(parent)
        self.on_save = on_save
        self.session = session
        self.title("Edit Session" if session else "New Session")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()

        f = ttk.Frame(self, padding=14)
        f.grid()
        s = session
        self.client = tk.StringVar(value=s["client"] if s else "")
        self.date = tk.StringVar(value=s["session_date"] if s else (default_date or date.today()).isoformat())
        self.time = tk.StringVar(value=s["start_time"] if s else "09:00")
        self.duration = tk.StringVar(value=str(s["duration_min"]) if s else "50")
        self.type = tk.StringVar(value=s["type"] if s else SESSION_TYPES[0])
        self.status = tk.StringVar(value=s["status"] if s else "Scheduled")

        rows = [
            ("Client (initials / ID)", ttk.Entry(f, textvariable=self.client, width=28)),
            ("Date (YYYY-MM-DD)", ttk.Entry(f, textvariable=self.date, width=28)),
            ("Start time (HH:MM, 24h)", ttk.Entry(f, textvariable=self.time, width=28)),
            ("Duration (minutes)", ttk.Combobox(f, textvariable=self.duration, width=26,
                                                values=["30", "45", "50", "60", "90"])),
            ("Session type", ttk.Combobox(f, textvariable=self.type, width=26,
                                          values=SESSION_TYPES, state="readonly")),
            ("Status", ttk.Combobox(f, textvariable=self.status, width=26,
                                    values=STATUSES, state="readonly")),
        ]
        for i, (label, widget) in enumerate(rows):
            ttk.Label(f, text=label).grid(row=i, column=0, sticky="w", pady=4, padx=(0, 10))
            widget.grid(row=i, column=1, pady=4)
        ttk.Label(f, text="Notes").grid(row=len(rows), column=0, sticky="nw", pady=4)
        self.notes = tk.Text(f, width=29, height=4, wrap="word")
        self.notes.grid(row=len(rows), column=1, pady=4)
        if s:
            self.notes.insert("1.0", s["notes"] or "")

        btns = ttk.Frame(f)
        btns.grid(row=len(rows) + 1, column=0, columnspan=2, pady=(10, 0), sticky="e")
        ttk.Button(btns, text="Cancel", command=self.destroy).pack(side="right", padx=(6, 0))
        ttk.Button(btns, text="Save", command=self.save).pack(side="right")

    def save(self):
        client = self.client.get().strip()
        if not client:
            return messagebox.showerror("Missing client", "Please enter a client initials/ID.", parent=self)
        try:
            d = datetime.strptime(self.date.get().strip(), "%Y-%m-%d").date()
        except ValueError:
            return messagebox.showerror("Invalid date", "Use the format YYYY-MM-DD.", parent=self)
        try:
            t = datetime.strptime(self.time.get().strip(), "%H:%M").strftime("%H:%M")
        except ValueError:
            return messagebox.showerror("Invalid time", "Use 24-hour HH:MM, e.g. 14:30.", parent=self)
        try:
            dur = int(self.duration.get())
            assert 5 <= dur <= 480
        except (ValueError, AssertionError):
            return messagebox.showerror("Invalid duration", "Duration must be 5-480 minutes.", parent=self)

        data = {
            "client": client, "date": d.isoformat(), "time": t, "duration": dur,
            "type": self.type.get(), "status": self.status.get(),
            "notes": self.notes.get("1.0", "end").strip(),
        }
        if self.on_save(data, self.session["id"] if self.session else None, self):
            self.destroy()


# --------------------------------------------------------------------------
# Main application
# --------------------------------------------------------------------------
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Therapist Flow - Scheduler")
        self.geometry("1020x580")
        self.minsize(900, 500)
        self.db = Database()
        self.load = Workload(self.db)
        self.anchor = date.today()
        self.view_mode = tk.StringVar(value="Week")
        self.build_ui()
        self.refresh()

    # ---- layout ----
    def build_ui(self):
        style = ttk.Style(self)
        style.configure("Treeview", rowheight=26)
        style.configure("Title.TLabel", font=("TkDefaultFont", 14, "bold"))
        style.configure("Big.TLabel", font=("TkDefaultFont", 20, "bold"))

        top = ttk.Frame(self, padding=(12, 10))
        top.pack(fill="x")
        ttk.Button(top, text="◀", width=3, command=lambda: self.shift(-7)).pack(side="left")
        ttk.Button(top, text="Today", command=self.go_today).pack(side="left", padx=4)
        ttk.Button(top, text="▶", width=3, command=lambda: self.shift(7)).pack(side="left")
        self.range_label = ttk.Label(top, style="Title.TLabel")
        self.range_label.pack(side="left", padx=14)
        ttk.Button(top, text="Settings", command=self.open_settings).pack(side="right")
        view = ttk.Combobox(top, textvariable=self.view_mode, values=["Week", "All sessions"],
                            state="readonly", width=12)
        view.pack(side="right", padx=8)
        view.bind("<<ComboboxSelected>>", lambda e: self.refresh())
        ttk.Label(top, text="View:").pack(side="right")

        body = ttk.Frame(self, padding=(12, 0, 12, 12))
        body.pack(fill="both", expand=True)

        # session list
        left = ttk.Frame(body)
        left.pack(side="left", fill="both", expand=True)
        cols = ("date", "time", "client", "type", "dur", "status")
        self.tree = ttk.Treeview(left, columns=cols, show="headings", selectmode="browse")
        for c, label, w in [("date", "Date", 120), ("time", "Time", 70), ("client", "Client", 130),
                            ("type", "Type", 110), ("dur", "Min", 50), ("status", "Status", 100)]:
            self.tree.heading(c, text=label)
            self.tree.column(c, width=w, anchor="w")
        sb = ttk.Scrollbar(left, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        self.tree.pack(side="top", fill="both", expand=True)
        sb.place(relx=1.0, rely=0, relheight=0.88, anchor="ne")
        self.tree.tag_configure("inactive", foreground="#9e9e9e")
        self.tree.tag_configure("override", background="#fff3e0")
        self.tree.bind("<Double-1>", lambda e: self.edit_session())
        self.tree.bind("<Delete>", lambda e: self.delete_session())

        actions = ttk.Frame(left, padding=(0, 8, 0, 0))
        actions.pack(fill="x")
        ttk.Button(actions, text="+ New session", command=self.new_session).pack(side="left")
        ttk.Button(actions, text="Edit", command=self.edit_session).pack(side="left", padx=6)
        mb = ttk.Menubutton(actions, text="Set status ▾")
        menu = tk.Menu(mb, tearoff=0)
        for s in STATUSES:
            menu.add_command(label=s, command=lambda s=s: self.change_status(s))
        mb["menu"] = menu
        mb.pack(side="left")
        ttk.Button(actions, text="Delete", command=self.delete_session).pack(side="left", padx=6)
        self.empty_hint = ttk.Label(actions, text="", foreground="#757575")
        self.empty_hint.pack(side="right")

        # workload panel
        right = ttk.LabelFrame(body, text="This week's workload", padding=12)
        right.pack(side="right", fill="y", padx=(12, 0))
        right.configure(width=260)
        self.risk_label = ttk.Label(right, style="Big.TLabel")
        self.risk_label.pack(anchor="w")
        ttk.Label(right, text="burnout risk level", foreground="#757575").pack(anchor="w", pady=(0, 10))
        self.week_text = ttk.Label(right)
        self.week_text.pack(anchor="w")
        self.week_bar = ttk.Progressbar(right, length=230, maximum=100)
        self.week_bar.pack(anchor="w", pady=(2, 10))
        self.day_text = ttk.Label(right, justify="left")
        self.day_text.pack(anchor="w")
        self.alert = tk.Label(right, text="", wraplength=230, justify="left", fg="#c62828",
                              font=("TkDefaultFont", 10, "bold"))
        self.alert.pack(anchor="w", pady=(12, 0))

    # ---- navigation ----
    def shift(self, days):
        self.anchor += timedelta(days=days)
        self.refresh()

    def go_today(self):
        self.anchor = date.today()
        self.refresh()

    # ---- rendering ----
    def refresh(self):
        monday = week_start(self.anchor)
        sunday = monday + timedelta(days=6)
        week_mode = self.view_mode.get() == "Week"
        self.range_label.config(
            text=f"{monday:%b %d} – {sunday:%b %d, %Y}" if week_mode else "All sessions")

        self.tree.delete(*self.tree.get_children())
        rows = self.db.in_range(monday, sunday) if week_mode else self.db.in_range()
        for r in rows:
            d = datetime.strptime(r["session_date"], "%Y-%m-%d")
            tags = []
            if r["status"] not in COUNTS_TOWARD_LOAD:
                tags.append("inactive")
            if r["override_reason"]:
                tags.append("override")
            self.tree.insert("", "end", iid=str(r["id"]), tags=tags, values=(
                f"{d:%a %b %d}", r["start_time"], r["client"], r["type"],
                r["duration_min"], r["status"]))
        self.empty_hint.config(text="" if rows else "No sessions yet. Click “+ New session”.")
        self.update_workload(monday)

    def update_workload(self, monday):
        week_min, per_day = self.load.totals(monday)
        max_week, max_day = self.load.limits()
        risk = self.load.risk(week_min, per_day)
        self.risk_label.config(text=risk, foreground=RISK_COLORS[risk])
        self.week_text.config(text=f"{week_min / 60:.1f} of {max_week / 60:.0f} hours scheduled")
        self.week_bar["value"] = min(100, week_min / max_week * 100) if max_week else 0
        busiest = max(per_day.items(), key=lambda kv: kv[1], default=None)
        n = sum(1 for r in self.db.in_range(monday, monday + timedelta(days=6))
                if r["status"] in COUNTS_TOWARD_LOAD)
        lines = [f"Sessions: {n}"]
        if busiest:
            bd = datetime.strptime(busiest[0], "%Y-%m-%d")
            lines.append(f"Busiest day: {bd:%a} ({busiest[1] / 60:.1f} h)")
        self.day_text.config(text="\n".join(lines))
        msgs = []
        if week_min > max_week:
            msgs.append("⚠ Weekly workload is over your limit.")
        over = [datetime.strptime(k, "%Y-%m-%d").strftime("%a") for k, v in per_day.items() if v > max_day]
        if over:
            msgs.append("⚠ Daily limit exceeded: " + ", ".join(over))
        if not msgs and risk == "Moderate":
            msgs.append("Approaching your limit. Consider spacing out sessions.")
        self.alert.config(text="\n".join(msgs))

    # ---- CRUD ----
    def selected_id(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Select a session", "Please select a session in the list first.")
            return None
        return int(sel[0])

    def new_session(self):
        SessionDialog(self, self.save_session, default_date=self.anchor)

    def edit_session(self):
        sid = self.selected_id()
        if sid:
            SessionDialog(self, self.save_session, session=self.db.get(sid))

    def change_status(self, status):
        sid = self.selected_id()
        if sid:
            self.db.set_status(sid, status)
            self.refresh()

    def delete_session(self):
        sid = self.selected_id()
        if sid and messagebox.askyesno("Delete session", "Delete this session permanently?\n"
                                       "(Tip: use “Set status → Cancelled” to keep a record.)"):
            self.db.delete(sid)
            self.refresh()

    def save_session(self, data, sid, dialog):
        """Validate, check conflicts / workload, then persist. Returns True if saved."""
        day = datetime.strptime(data["date"], "%Y-%m-%d").date()
        counts = data["status"] in COUNTS_TOWARD_LOAD

        if counts:  # overlap check
            start = to_minutes(data["time"])
            end = start + data["duration"]
            for r in self.db.in_range(day, day):
                if r["id"] == sid or r["status"] not in COUNTS_TOWARD_LOAD:
                    continue
                s2 = to_minutes(r["start_time"])
                if start < s2 + r["duration_min"] and s2 < end:
                    messagebox.showerror(
                        "Time conflict",
                        f"This overlaps with {r['client']} at {r['start_time']} "
                        f"({r['duration_min']} min).", parent=dialog)
                    return False

            # workload check (warn + override)
            monday = week_start(day)
            max_week, max_day = self.load.limits()
            cur_week, cur_days = self.load.totals(monday)
            new_week, new_days = self.load.totals(monday, exclude_id=sid,
                                                  extra=(data["date"], data["duration"]))
            problems = []
            if new_week > max_week and new_week > cur_week:
                problems.append(f"weekly total would be {new_week / 60:.1f} h (limit {max_week / 60:.0f} h)")
            if new_days[data["date"]] > max_day and new_days[data["date"]] > cur_days.get(data["date"], 0):
                problems.append(f"{day:%A} would be {new_days[data['date']] / 60:.1f} h "
                                f"(limit {max_day / 60:.0f} h)")
            if problems:
                reason = simpledialog.askstring(
                    "Workload limit reached",
                    "Adding this session would overload your schedule:\n  • "
                    + "\n  • ".join(problems)
                    + "\n\nTo override, enter a reason. Cancel to go back.",
                    parent=dialog)
                if not reason or not reason.strip():
                    return False
                data["override_reason"] = reason.strip()

        if sid:
            old = self.db.get(sid)
            data.setdefault("override_reason", old["override_reason"])
            self.db.update(sid, data)
        else:
            self.db.add(data)
        self.anchor = day
        self.refresh()
        return True

    # ---- settings ----
    def open_settings(self):
        win = tk.Toplevel(self)
        win.title("Workload limits")
        win.transient(self)
        win.grab_set()
        f = ttk.Frame(win, padding=14)
        f.pack()
        wk = tk.StringVar(value=f"{self.db.get_setting('max_weekly_hours'):g}")
        dy = tk.StringVar(value=f"{self.db.get_setting('max_daily_hours'):g}")
        ttk.Label(f, text="Max session hours per week").grid(row=0, column=0, sticky="w", pady=4)
        ttk.Entry(f, textvariable=wk, width=8).grid(row=0, column=1, padx=8)
        ttk.Label(f, text="Max session hours per day").grid(row=1, column=0, sticky="w", pady=4)
        ttk.Entry(f, textvariable=dy, width=8).grid(row=1, column=1, padx=8)

        def save():
            try:
                w, d = float(wk.get()), float(dy.get())
                assert w > 0 and d > 0
            except (ValueError, AssertionError):
                return messagebox.showerror("Invalid", "Enter positive numbers.", parent=win)
            self.db.set_setting("max_weekly_hours", w)
            self.db.set_setting("max_daily_hours", d)
            win.destroy()
            self.refresh()

        ttk.Button(f, text="Save", command=save).grid(row=2, column=1, sticky="e", pady=(10, 0))


if __name__ == "__main__":
    App().mainloop()
