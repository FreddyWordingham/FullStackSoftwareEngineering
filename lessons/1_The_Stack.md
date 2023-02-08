# The Stack

-   [The Stack](#the-stack)
    -   [Tables](#tables)
    -   [Introduction](#introduction)
    -   [The Stack](#the-stack-1)
        -   [Front-end](#front-end)
            -   [HTML](#html)
            -   [CSS](#css)
            -   [JavaScript](#javascript)
    -   [What is a full-stack engineer?](#what-is-a-full-stack-engineer)
        -   [What is a software engineer?](#what-is-a-software-engineer)
        -   [What is a full-stack engineer?](#what-is-a-full-stack-engineer-1)

## Tables

| Name                                                                  | Description               |
| --------------------------------------------------------------------- | ------------------------- |
| [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)             | HyperText Markup Language |
| [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)               | Cascading Style Sheets    |
| [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) | A programming language    |
| [Python](https://www.python.org/)                                     | A programming language    |
| [C++](https://isocpp.org/)                                            | A programming language    |
| [Rust](https://www.rust-lang.org/)                                    | A programming language    |

| Tag        | Description       | Example                                                     |
| ---------- | ----------------- | ----------------------------------------------------------- |
| `<p>`      | A paragraph       | `<p>This is a paragraph</p>`                                |
| `<input>`  | A text input      | `<input type="text" />`                                     |
| `<button>` | A button          | `<button>Click me!</button>`                                |
| `<style>`  | A style tag       | `<style>body { background-color: red; }</style>`            |
| `<div>`    | A division        | `<div>This is a division</div>`                             |
| `<span>`   | A span            | `<span>This is a span</span>`                               |
| `<ul>`     | An unordered list | `<ul><li>Item 1</li><li>Item 2</li></ul>`                   |
| `<ol>`     | An ordered list   | `<ol><li>Item 1</li><li>Item 2</li></ol>`                   |
| `<table>`  | A table           | `<table><tr><td>Cell 1</td><td>Cell 2</td></tr></table>`    |
| `<form>`   | A form            | `<form><input type="text" /><button>Submit</button></form>` |

| CSS Property  | Description               | Example                                  |
| ------------- | ------------------------- | ---------------------------------------- |
| `color`       | The color of text         | `color: red;`                            |
| `background`  | The background color      | `background: blue;`                      |
| `font-size`   | The size of the font      | `font-size: 20px;`                       |
| `font-family` | The font family           | `font-family: "Times New Roman", serif;` |
| `width`       | The width of an element   | `width: 100px;`                          |
| `height`      | The height of an element  | `height: 100px;`                         |
| `margin`      | The margin of an element  | `margin: 10px;`                          |
| `padding`     | The padding of an element | `padding: 10px;`                         |
| `border`      | The border of an element  | `border: 1px solid black;`               |

| CSS Selector      | Description                       | Example                     |
| ----------------- | --------------------------------- | --------------------------- |
| `*`               | All elements                      | `* { color: red; }`         |
| `p`               | All paragraph elements            | `p { color: red; }`         |
| `#id`             | An element with a specific id     | `#my-id { color: red; }`    |
| `.class`          | An element with a specific class  | `.my-class { color: red; }` |
| `element element` | An element inside another element | `div p { color: red; }`     |

## Introduction

In this lesson we will learn about the different parts of the stack and how they work together.

## The Stack

The stack is a collection of technologies that are used to build web applications. Often, the stack is thought as being made of three parts: the front-end, the back-end, and the database.

### Front-end

The front-end is what the user sees and interacts with. For web applications it is written in a mixture of HTML, CSS, and JavaScript.

#### HTML

HTML stands for **H**yper**T**ext **M**arkup **L**anguage. It is used to define the structure of a web page. It looks like this:

```html
<html>
    <p>Type some text in this box:</p>
    <input type="text" />
    <button>Submit</button>
</html>
```

If we save this as `index.html` and open it in a browser, we will see it render something like this:

<html>
    <p>Type some text in this box:</p>
    <input type="text" />
    <button>Submit</button>
</html>

HTML is made up of **elements**. Elements are defined by a **tag**. The tag is the name of the element, surrounded by angle brackets. For example, the `<p>` tag defines a paragraph element, `<input>` tag defines some kind of user input, and the `<button>` tag defines a button element.

Elements can also have **attributes**, additional data encapsulated within the tag. Attributes are defined by a **name** and a **value**, separated by an equals sign. For example, the `type` attribute of the `<input>` element above tells us that it should receive and hold text. If the `type` attribute was changed to `number`, the input would expect numbers:

```html
<html>
    <p>Type some text in this box:</p>
    <input type="number" />
    <button>Submit</button>
</html>
```

<html>
    <p>Type some text in this box:</p>
    <input type="number" />
    <button>Submit</button>
</html>

All web pages have a 'root' `<html>` tag at the start of the document. It contains all of the other elements. A tag which surrounds other elements is called the **parent** element, and the contained elements are it's **children**.

Elements can also have **content**. For example, the `<p>` element above has the text "Type some text in this box:" as it's content.

#### CSS

CSS stands for **C**ascading **S**tyle **S**heets. It is used to define the style of a web page and save us from that 1990's chic.

We can add CSS directly to an element by adding a `style` attribute to the element's tag. This is called inline CSS. Let's make the text red and the button green:

```html
<html>
    <body>
        <p style="color: red">Type some text in this box:</p>
        <input type="text" />
        <button style="background-color: green">Submit</button>
    </body>
</html>
```

<html>
    <p style="color: red">Type some text in this box:</p>
    <input type="text" />
    <button style="background-color: green">Submit</button>
</html>

Sometimes we want to apply the same style to multiple elements. We can do this by giving the element an **class** attribute, and then using the `.` symbol to select the element by it's id. Let's use classes instead, and move the CSS to the `<style>` tag:

```html
<html>
    <body>
        <p class="red_text" Type some text in this box:</p>
        <input type="text" />
        <button class="green_button">Submit</button>
        <style>
            .red_text {
                color: red;
            }
            .green_button {
                background-color: green;
            }
        </style>
    </body>
</html>
```

<html>
    <p class="red_text" Type some text in this box:</p>
    <input type="text" />
    <button class="green_button">Submit</button>
    <style>
        .red_text {
            color: red;
        }
        .green_button {
            background-color: green;
        }
    </style>
</html>

CSS can also be written in a separate file, which is then linked to the HTML file. This is called external CSS. Let's move the CSS we wrote inline into a separate file called `style.css`:

```css
.red_text {
    color: red;
}

.green_button {
    background-color: green;
}
```

This file can then be linked to the HTML file using the `<link>` tag:

```html
<html>
    <head>
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>
        <p class="red_text">Type some text in this box:</p>
        <input type="text" />
        <button class="green_button">Submit</button>
    </body>
</html>
```

We denote a class by using the `.` symbol. We can also select a specific named element by its **id**. We denote an id by using the `#` symbol. For example we can select give the button element id called `submit_button`:

```html
<html>
    <head>
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>
        <p class="red_text">Type some text in this box:</p>
        <input type="text" />
        <button id="submit_button" class="green_button">Submit</button>
    </body>
</html>
```

Important: The id of an element must be unique on that page. In contrast, a class can be used on multiple elements. Finally we can refer to a type of tag by using the tag name. For example, to apply bold text to all `<p>` elements:

```css
p {
    font-weight: bold;
}
```

#### JavaScript

JS allows us to add interactivity to the page. Let's add an alert that pops up when the button is clicked:

```html
<html>
    <head>
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>
        <p>Type some text in this box:</p>
        <input type="text" />
        <button onclick="show_alert()">Submit</button>
    </body>
    <script>
        function show_alert() {
            window.alert(message);
        }
    </script>
</html>
```

<html>
    <head>
        <link rel="stylesheet" href="style.css" />
    </head>
    <p>Type some text in this box:</p>
    <input type="text" />
    <button onclick="show_alert()">Submit</button>
    <script>
        function show_alert() {
            window.alert(message);
        }
    </script>
</html>

## What is a full-stack engineer?

### What is a software engineer?

A software engineer is someone who **designs** and builds software. In contrast a

software **developers** who primarily focus on building it. ### Software developer vs software engineer Generally, software engineers look after the bigger
picture, while software developers focus on one specific area Engineers can act as developers, too, or simply oversee developers who create functional programs.

### What is a full-stack engineer?

Modern web applications are made up of many different parts: a back-end server, a front-end client, a database, etc. A

full-stack engineer will work across all of these parts, rather than focusing on just one.
