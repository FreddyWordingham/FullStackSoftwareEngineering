# The Stack

Different languages are really good at different things. For example, `C` is really good at low-level tasks, like accessing the memory of the computer. `Python` is really good at interoperating with other languages, like `C`, `C++`, `Rust` and `FORTRAN`, gluing them together in a very readable way. `JavaScript` is good at manipulating the DOM, the document object model, which is the structure of a `HTML` document.

And they're less good at other things. For example, whilst `C` can be used to render a GUI on the screen, it takes a lot of code to do it. It might be really fast, but it's not very convenient.

**rule[0] The best code is no code at all.**

And a `C` program that renders a GUI on the screen is a lot of code. It's a lot of code that needs to be maintained. A lot of code which **will** need to be debugged.

If we can find a way to achieve the same goal without writing any code at all, then that is simply the best code.

**rule[1] The second best code is _neat_ code.**

Code that is easy to read, easy to understand, easy to maintain, easy to debug. And (as I always say) in general the smaller it is the better.

**rule[2] The third best is _fast_ code**

Code that is fast to run. Code that is fast to compile. Code that is fast to load. Code that is fast to execute. But it very rarely better than writing neat code.

Overall, we want to use the right tool for the job. We want to use the most convenient tech that achieves the goal. So instead of writing everything in a single language, we use a collection of languages.

The stack is a collection of technologies that are used to build web applications. The front end is the part of the application that runs on the client's local device. The backend is the part of the application that runs on the server.

The computer running the back end severer is typically much more powerful than the client's local device, and therefore can handle more complex tasks, like computing simulations and accessing large amounts of data. It is common for a backend to serve multiple front ends, but it is not common for a front end to be served by multiple backends.
