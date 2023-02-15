# The front end

The front end of a full stack application refers to the client-side code. This includes the user interface and any code that runs in the user's web browser.

## Front end languages

The front end is written in a mixture of `HTML`, `CSS`, and `JavaScript`.

`HTML` and `CSS` are both **declarative** languages, meaning that they just describe _something_. On the other hand, `JavaScript` is an **imperative** language, meaning that it describes a series of steps that lead to a final _result_.

| Name                                                                  | Description               | Kind of language     | Used for       |
| --------------------------------------------------------------------- | ------------------------- | -------------------- | -------------- |
| [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)             | HyperText Markup Language | Markup language      | Page structure |
| [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)               | Cascading Style Sheets    | Style language       | Styling        |
| [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) | Imperative                | Programming language | Behavior       |

## HTML tags

`HTML` is made up of **elements**. Elements have a _type_ called a **\<tag\>**. The tag is the name of the element, surrounded by angle brackets. For example, the `<p>` tag defines a paragraph element, the `<input>` tag defines some kind of user input, and the `<button>` tag defines a button element.

| Tag                | Description         | Example                                                                                                            |
| ------------------ | ------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `<!DOCTYPE html>`  | A doctype tag       | `<!DOCTYPE html>`                                                                                                  |
| `<html>`           | An html tag         | `<html><head><title>My page</title></head><body><h1>Hello world!</h1></body></html>`                               |
| `<head>`           | A head tag          | `<head><title>My page</title></head>`                                                                              |
| `<title>`          | A title tag         | `<head><title>My other page</title></head>`                                                                        |
| `<script>`         | A script tag        | `<head><script src="script.js"></script></head>`                                                                   |
| `<meta>`           | A meta tag          | `<head><meta charset="utf-8" /></head>`                                                                            |
| `<style>`          | A style tag         | `<head><style rel="stylesheet" href="style.css" /></head>`                                                         |
| `<body>`style      | A body tag          | `<body><h1>Hello world!</h1></body>`                                                                               |
| `<h1>`             | A heading tag       | `<h1>Hello world!</h1>`                                                                                            |
| `<p>`              | A paragraph         | `<p>This is a paragraph</p>`                                                                                       |
| `<input>`          | A text input        | `<input type="text" />`                                                                                            |
| `<button>`         | A button            | `<button>Click me!</button>`                                                                                       |
| `<div>`            | A division          | `<div>This is a division</div>`                                                                                    |
| `<hr>`             | A horizontal rule   | `<p>This is a paragraph</p><hr /><p>This is another paragraph</p>`                                                 |
| `<span>`           | A span              | `<p><span>This is a span</span></p>`                                                                               |
| `<ul>`             | An unordered list   | `<ul><li>Item 1</li><li>Item 2</li></ul>`                                                                          |
| `<ol>`             | An ordered list     | `<ol><li>Item 1</li><li>Item 2</li></ol>`                                                                          |
| `<table>`          | A table             | `<table><tr><td>Cell 1</td><td>Cell 2</td></tr></table>`                                                           |
| `<form>`           | A form              | `<form><input type="text" /><button>Submit</button></form>`                                                        |
| `<img>`            | An image            | `<img src="image.png" />`                                                                                          |
| `<a>`              | An anchor           | `<a href="https://google.com">Google</a>`                                                                          |
| `<link>`           | A link tag          | `<link rel="stylesheet" href="style.css" />`                                                                       |
| `<iframe>`         | An embedded website | `<iframe src="https://google.com"></iframe>`                                                                       |
| `<canvas>`         | A canvas            | `<canvas id="myCanvas"></canvas>`                                                                                  |
| `<svg>`            | An SVG              | `<svg width="100" height="100"><circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" /></svg>` |
| `<!-- comment -->` | A comment           | `<!-- This is a comment -->`                                                                                       |

These few can be used to achieve a lot, but you can find more [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element).

## CSS properties

`CSS` uses a collection of **properties** to define how an `element` should be rendered. Properties have a _name_ and a _value_. For example, the `color` property defines the colour of text, and the `background` property defines the background colour.

| CSS Property  | Description                                                   | Example                                  |
| ------------- | ------------------------------------------------------------- | ---------------------------------------- |
| `color`       | Text colour                                                   | `color: red;`                            |
| `background`  | Element background colour                                     | `background: blue;`                      |
| `font-size`   | Text size                                                     | `font-size: 20px;`                       |
| `font-family` | Text font                                                     | `font-family: "Times New Roman", serif;` |
| `width`       | Spatial width of an element                                   | `width: 100px;` or `width: 50%`          |
| `height`      | Spatial height of an element                                  | `height: 100px;` or `width: 50%`         |
| `margin`      | The space between an element's boundary and other elements    | `margin: 10px;`                          |
| `padding`     | The space between an element's boundary and it's own contents | `padding: 10px;`                         |
| `border`      | Boundary styling                                              | `border: 1px solid black;`               |
| `display`     | How an element is rendered.                                   | `display: none;` or `display: block;`    |
| `position`    | The positioning of an element                                 | `position: absolute;`                    |

This table shows some of the more common CSS properties, but there are more [here](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference).

## Selectors

When we wish to refer to a specific element or a group of elements, we use a **selector**. Selectors are used in `CSS` to define which elements a property should be applied to, and in `JavaScript` to select elements from within the page.

| Selector | Description                      | Example                     |
| -------- | -------------------------------- | --------------------------- |
| `*`      | All elements                     | `* { color: red; }`         |
| `p`      | All paragraph elements           | `p { color: red; }`         |
| `#id`    | An element with a specific id    | `#my-id { color: red; }`    |
| `.class` | An element with a specific class | `.my-class { color: red; }` |

You will use these few most of the time, but there are more [here](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors).

## Pseudo-classes

We can also use **pseudo-classes** to select elements based on their state. For example, we could select `<p>` elements that are being hovered over by the mouse.

| Pseudo-class | Description                      | Example                         |
| ------------ | -------------------------------- | ------------------------------- |
| `:hover`     | An element that is being hovered | `a:hover { color: red; }`       |
| `:active`    | An element that is being clicked | `button:active { color: red; }` |
| `:focus`     | An element that is being focused | `input:focus { color: red; }`   |

There are more pseudo-classes, see more [here](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes).

## Combinators

We can combine selectors to create more complex selectors. These are called **combinators**.

| Combinators | Description       | Example    |
| ----------- | ----------------- | ---------- |
| `a, b`      | Multiple elements | `h1, p`    |
| `a b`       | Descendant        | `div h1`   |
| `a > b`     | Direct child      | `div > h1` |
| `a + b`     | Adjacent sibling  | `h1 + p`   |
| `a ~ b`     | General sibling   | `h1 ~ p`   |

Personally, I don't use these very often - but I'm not very stylish! But see more [here](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors/Combinators).
