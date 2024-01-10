# Find Closely Matched Words In Python
This repository contains template code to find closely matched words from a list of words

# Introduction
Often we face cases where we have different words to process and consider similar words as the same. An example situation can be a comparison of the data obtained from two different websites where the data can slightly vary from one another. This template should help to get an idea of how to handle those cases using <i>fuzzywuzzy</i> library and <i>Levenshtein distance algorithm</i>. 

# Example
Let's assume that we have two lists of words<be>
<pre>[
    "mercedez",
    "toyota supra",
    "bmw"
]</pre>
and
<pre>[
    "Mercedez benz",
    "supra",
    "bmw"
]</pre>

Here, you can see that the words <code>mercedez</code> and <code>Mercedez benz</code> are both similar to one another. And they're the same company. To compare and consider them as the same data, this template approach will be useful. If you have two words already known instead of a list, you may simply do this:
<pre>from fuzzywuzzy import fuzz
accuracy_ratio = 80
word1 = "mercedez"
word2 = "Mercedez benz"
if fuzz.partial_ratio(word1, word2) > accuracy_ratio:
    print("Matched")
else:
    print("Not matched)</pre>
And that will do the trick.

# Command
<code>pip install fuzzywuzzy python-Levenshtein</code>

# Need a software developer to automate your tasks?
<a href="https://www.fiverr.com/thechoyon">Contact Me on Fiverr</a> | <a href="https://www.linkedin.com/in/tufayel-ahmed-cse/">Contact Me on LinkedIn</a> | <a href="https://www.facebook.com/cse.tufayel/">Contact Me on Facebook</a>
