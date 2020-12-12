from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from lxml.html import parse
import os
import datetime

template_env = Environment(loader=FileSystemLoader(searchpath='./'))
template = template_env.get_template('layout.html')
articles = os.listdir('articles')

# Format articles
for article in articles:
    filename = os.path.splitext(article)[0]
    
    with open('articles/' + article) as markdown_file:
        formatted_article = markdown(
            markdown_file.read(),
            extras=['fenced-code-blocks', 'code-friendly', 'strike', 'tables', 'metadata'])
    
    dateblock = datetime.datetime.strptime(formatted_article.metadata['date'], '%m-%d-%Y').strftime('%Y%m%d')

    with open('posts/' + dateblock + filename + '.html', 'w') as output_file:
        output_file.write(
            template.render(
                title = formatted_article.metadata['title'],
                date = formatted_article.metadata['date'],
                article=formatted_article
            )
        )

# Format index
posts = os.listdir('posts')
posts.sort()

post1 = open('posts/' + posts[-1], 'r')
post1_parsed = parse(post1)
post1.close()
post1_link = 'posts/' + posts[-1]
post1_title = post1_parsed.find(".//title").text

post2 = open('posts/' + posts[-2], 'r')
post2_parsed = parse(post2)
post2.close()
post2_link = 'posts/' + posts[-2]
post2_title = post2_parsed.find(".//title").text

post3 = open('posts/' + posts[-3], 'r')
post3_parsed = parse(post3)
post3.close()
post3_link = 'posts/' + posts[-3]
post3_title = post3_parsed.find(".//title").text

index_template = template_env.get_template('index-layout.html')
with open('index.html', 'w') as index_output:
    index_output.write(
        index_template.render(
            post1_title = post1_title,
            post1_link = post1_link,
            post2_title = post2_title,
            post2_link = post2_link,
            post3_title = post3_title,
            post3_link = post3_link,
        )
    )

# Format blog page
posts.sort(reverse=True)
posts_html_array = []

for post in posts:
    post_file = open('posts/' + post)
    post_parsed = parse(post_file)
    post_file.close()
    post_link = 'posts/' + post
    post_title = post_parsed.find(".//title").text

    post_html_element = '<a href="' + post_link +'">' + post_title + '</a>'
    posts_html_array.append(post_html_element)

posts_html_combined = '<br>'.join(posts_html_array)
print(posts_html_combined)

blog_template = template_env.get_template('blog-layout.html')
with open('blog.html', 'w') as blog_output:
    blog_output.write(
        blog_template.render(
            posts = posts_html_combined,
        )
    )