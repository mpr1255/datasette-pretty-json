from datasette_pretty_json import render_cell
import jinja2
import json
import pytest


@pytest.mark.parametrize(
    "input,expected",
    (
        # Ignore not-JSON-values
        ("blah", None),
        ("1.34", None),
        # JSON values should be pretty-printed
        (
            '{"foo": {"bar": 1}}',
            """<pre>{
    &#34;foo&#34;: {
        &#34;bar&#34;: 1
    }
}</pre>""",
        ),
        (
            '[{"foo": {"bar": 1}}]',
            """<pre>[
    {
        &#34;foo&#34;: {
            &#34;bar&#34;: 1
        }
    }
]</pre>""",
        ),
    ),
)
def test_render_cell(input, expected):
    actual = render_cell(input)
    assert expected == actual
    assert actual is None or isinstance(actual, jinja2.Markup)
