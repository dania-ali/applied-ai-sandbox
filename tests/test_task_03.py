"""Acceptance tests for TASK 03 — starred filter."""


def _seed(app, n=2):
    app.notes.clear()
    for i in range(n):
        app.notes.append({"title": f"Note {i}", "body": f"Body {i}", "starred": False})


def test_new_note_default_unstarred(client, app):
    app.notes.clear()
    client.post("/notes/new", data={"title": "T", "body": "B"})
    assert app.notes[0]["starred"] is False


def test_star_toggles_to_true(client, app):
    _seed(app, 1)
    r = client.post("/notes/0/star")
    assert r.status_code in (302, 303)
    assert app.notes[0]["starred"] is True


def test_star_toggles_back_to_false(client, app):
    _seed(app, 1)
    app.notes[0]["starred"] = True
    client.post("/notes/0/star")
    assert app.notes[0]["starred"] is False


def test_starred_filter_shows_only_starred(client, app):
    _seed(app, 2)
    app.notes[1]["starred"] = True
    r = client.get("/?starred=1")
    body = r.data.decode()
    assert "Note 1" in body
    assert "Note 0" not in body


def test_starred_filter_empty_state(client, app):
    _seed(app, 1)
    r = client.get("/?starred=1")
    assert b"No starred notes yet" in r.data


def test_star_nonexistent_returns_404(client, app):
    _seed(app, 1)
    r = client.post("/notes/99/star")
    assert r.status_code == 404
