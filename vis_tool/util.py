import html
from htbuilder import H, HtmlElement, styles
from htbuilder.units import unit

span = H.span
rem = unit.rem
em = unit.em

PALETTE = [
    "#ff4b4b",
    "#21c354",
    "#00d4b1",
    "#00c0f2",
    "#1c83e1",
    "#803df5",
    "#808495",
    "#fa7cd2",
    "#964a7e"
]

#"#ffa421","#ffe312",

OPACITIES = [
    "33", "66",
]

def annotation(body, label="", background=None, color=None, **style):
    
    color_style = {}

    if color:
        color_style['color'] = color

    if not background:
        label_sum = sum(ord(c) for c in label)
        background_color = PALETTE[label_sum % len(PALETTE)]
        background_opacity = OPACITIES[label_sum % len(OPACITIES)]
        background = background_color + background_opacity

    return (
        span(
            style=styles(
                background=background,
                border_radius=rem(0.33),
                padding=(rem(0.125), rem(0.5)),
                overflow="hidden",
                **color_style,
                **style,
            ))(

            html.escape(body),

            span(
                style=styles(
                    padding_left=rem(0.5),
                    text_transform="uppercase",
                ))(
                span(
                    style=styles(
                        font_size=em(0.67),
                        opacity=0.5,
                    ))(
                    html.escape(label),
                ),
            ),
        )
    )
