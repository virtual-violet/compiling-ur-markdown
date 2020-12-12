## What does Compiling Ur Markdown do?
Compiling Ur Markdown does just that: compiles your markdown. It's a very basic static site generator for adding a simple blog to a site. It creates pages for each post, a `blog.html` page that lists each of them, and adds the 3 most recent to the homepage of your site

## What are the dependencies?
Compiling Ur Markdown requires [markdown2](https://pypi.org/project/markdown2/), [Jinja2](https://pypi.org/project/Jinja2/), and [lxml](https://pypi.org/project/lxml/).

## How do I set it up?
Place the Python script in the directory of your site. Create three directories: `articles`, `posts`, and `layouts`. `articles` will contain all your markdown files. `posts` is where the site will place all of the completed markdown files. `layouts` will three layout files, one for your main page, one for your posts, and one for your blog (the page that will list all of your posts).

Your templates should be set up as such:

`index-layout.html` should be written as your site's actual homepage, but contain 3 links like this (which will be turned into the 3 most recent posts):

```html
<a href="{{ post1_link }}">{{ post1_title }}</a>
<a href="{{ post2_link }}">{{ post2_title }}</a>
<a href="{{ post3_link }}">{{ post3_title }}</a>
```
`posts-layout.html` must contain an `{{ article }}` anchor. `{{ title }}` and `{{ date }}` are optional.

`blog-layout.html` must contain a `{{ posts }}` anchor

You can set up the rest of your templates as standard HTML files. 

## How do I use it?
After doing the setup, just place your markdown files in the `articles` directory, run Compiling Ur Markdown, and it will handle the rest. Make sure all of your markdown files contain the following metadata at the top of the file:

```
---
title: My Cool Blog Post
date: 01-11-2020
---
```

## What's with the name?
Compiling Ur Markdown is an apt description of what this piece of software does, that is all.