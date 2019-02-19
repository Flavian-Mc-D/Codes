***Markdown Codes***

# Heading 
HTML
<h1>Heading level 1</h1>	

## Heading 
HTML
<h2>Heading level 2</h2>	

### Heading 
HTML
<h3>Heading level 3</h3>	

#### Heading 
HTML
<h4>Heading level 4</h4>	

##### Heading 
HTML
<h5>Heading level 5</h5>	

###### Heading 
HTML
<h6>Heading level 6</6>	

Heading level 1
=============== 
Heading level 2
---------------
*Lo anterior sube el encabezado*

***Paragraphs***

To create paragraphs, use a blank line to separate one or more lines of text. <br> You should not indent paragraphs with spaces or tabs.
Igual que en HTML el párrafo se crea con el comando 
<p> "p" </p>

***Line Breaks***

To create a line break (<br>), end a line with two or more spaces, and then type return.

***Emphasis***
You can add emphasis by making text bold or italic.

***Bold***
To bold text, add two asterisks or underscores before and after a word or phrase. <br> To bold the middle of a word for emphasis, <br> add two asterisks without spaces around the letters.
(son 3 asteriscos y/o un underscore, tanto para abrir como para cerrar )

I just love **bold text**.	
I just love __bold text__.	
Love**is**bold

***Italic***
To italicize text, add one asterisk or underscore before and after a word or phrase. To italicize the middle of a word for emphasis, add one asterisk without spaces around the letters.

"
Italicized text is the *cat's meow*.	
Italicized text is the _cat's meow_.	
A*cat*meow	
"
**Bold and Italic**
To emphasize text with bold and italics at the same time, add three asterisks or underscores before and after a word or phrase.

This text is __*really important*__.
This text is **_really important_**.

**Blockquotes**
To create a blockquote, add a > in front of a paragraph.
> this will be a blockquotes

**Nested Blockquotes**
Blockquotes can be nested. Add a >> in front of the paragraph you want to nest.
>  This is a blockquote
>
>> Nested Blockquotes

**Blockquotes with Other Elements**

Blockquotes can contain other Markdown formatted elements. Not all elements can be used — you’ll need to experiment to see which ones work.

> #### The quarterly results look great!
>
> - Revenue was off the chart. (este elemento tiene un - en el comenzo)
> - Profits were higher than ever. (este elemento tiene un - en el comenzo)
>
>  *Everything* is going according to **plan**.

**Ordered Lists**

To create an ordered list, add line items with numbers followed by periods. <br> The numbers don’t have to be in numerical order, but the list should start with the number one.

1. First item
2. Second item
3. Third item
    1. Indented item
    2. Indented item
4. Fourth item

**Unordered Lists**

To create an unordered list, add dashes (-), asterisks (*)*, or plus signs (+) in front of line items. Indent one or more items to create a nested list.

**Code Blocks**

Code blocks are normally indented four spaces or one tab. When they’re in a list, indent them eight spaces or two tabs.

1.  Open the file.
2.  Find the following code block on line 21:

        <html>
          <head>
            <title>Test de HTML en markdown</title>
          </head>

Images

1.  Open the file containing the Linux mascot.
2.  Marvel at its beauty.

    ![Imagen que está en el computador](C:\Users\BlueShift\Downloads\Varios\1069246_10151790091542640_1805570192_n.jpg)

3.  Close the file.

**Links**
To create a link, enclose the link text in brackets (e.g.,"[  ]" [Google]) and then follow it immediately with the URL in parentheses <br> (e.g., (https://google.com)).

**URLs and Email Addresses**

To quickly turn a URL or email address into a link, enclose it in angle brackets.

<https://www.flavianmcdonald.wordpress.com>
<fake@example.com>

**Images**

To add an image, add an exclamation mark (!), followed by alt text in brackets, and the path or URL to the image asset in parentheses. You can optionally add a title after the URL in the parentheses.

![Foto que está en la computadora. This place was so cool!](C:\Users\BlueShift\Downloads\Varios\1069246_10151790091542640_1805570192_n.jpg "Foto que esttá en la pc")

**Linking Images**
<br>
To add a link to an image, enclose the Markdown for the image in brackets, and then add the link in parentheses.

[![Salto Ángel][("Salto Ángel - venezuela")](https://trilhandomontanhas.com/arquivos/2018-10/salto-angel-venezuela-media.jpg) 

[![Salto Ángel]("" "Salto Ángel")](https://trilhandomontanhas.com/arquivos/2018-10/salto-angel-venezuela-media.jpg)
