<!-- Claudio Perez -->

# SimCenter Documentation Style Reference

This reference is based on [Purdue Owl](https://owl.purdue.edu/owl/purdue_owl.html), the [Google developer documentation style guide](https://developers.google.com/style?hl=es-419) and the [Python documentation style guide](https://docs.python.org/3.1/documenting/style.html). Some deviations and additions are indicated with footnotes.

>This document is intended to provide a convenient reference, not a comprehensive guide. Pending the development of more extensive SimCenter guidelines, the resources mentioned above are recommended for guidance beyond what is provided here.

## Text Formatting

<details>

<summary><b>Bold face</b> </summary>

Use bold formatting (**), for UI elements and at the beginning of notices. This includes names for buttons, menus, dialogs, windows, list items, or any other feature in the page or console that has a visible name. Don't use code font for UI elements, unless it's an element that meets the requirements for code font. In that case, use both code font and bold.
</details>

<details>
<summary><i>Italics</i></summary>

Proper uses of italics:

- Drawing attention to a specific word or phrase, such as when [defining terms](https://developers.google.com/style/key-terms) or [using words as words](https://developers.google.com/style/formatting-words-as-words).
- Referring to titles of books, movies, web series, and other full-length works, unless they are part of a link.
- Referring to parameter names. For example, when you refer to the parameters of a method like `doSomething(Uri data, int count)`, italicize *data* and *count*.
- Using mathematical variables.

Some improper uses of italics:

- Names of mathematical functions, operators, or units; use the Latex commands `\mathrm` or `\operatorname` appropriately to avoid improper italics when writing mathematical expressions.

</details>

<details>
<summary> <u>Underlining</u> (Don't underline) </summary>

Don't underline.
</details>

<details>
<summary> <code>Code font</code> </summary>

Surround text in double backticks (\`\`) to apply a monospace font to [code in text](https://developers.google.com/style/code-in-text), inline code, and user input. Use code blocks (`.. :code-block::`) for code samples or other blocks of code. Do not override or modify font styles inline. Use code font to mark up code, such as class names, method names, HTTP status codes, console output, and placeholder variables.

Some proper uses:

- Referring to file names.
</details>

<details>
<summary>Capitalization</summary>

Use American English style for [general capitalization](https://developers.google.com/style/capitalization). When possible, use sentence case in low-level headings, titles, and navigation.
</details>

<details>
<summary>Quotation marks</summary>

In general, use American English style when [punctuating quotations](https://developers.google.com/style/quotation-marks). For titles of shorter works-such as articles or episodes in a web series-put titles in quotation marks, unless they are part of a link.
</details>

<details>
<summary>Numbers</summary>

In general, spell out the following:

- Numbers from zero through nine, except as noted below in Numbers as numerals.

- A number that starts a sentence.

    >**Exception:** It's okay, but non-optimal, to begin a sentence with a four-digit year.

- A number that is followed by a numeral (e.g. "This procedure creates fifteen 100,000-byte files.").

- Indefinite and casual numbers (e.g. "The API might return a list of a million songs").

In general, use numerals for the following:

- Numbers 10 and greater.

    **Exceptions:** Always use numerals for the following items, even if they are less than 10:
        Version numbers.
        Technical quantities, such as amounts of memory, amounts of disk space, numbers of queries, or usage limits.
        Page numbers.
        Chapter numbers, sections, pages, and so on.
        Prices.
        Numbers without units, such as numbers used in mathematical expressions.

- Numbers less than 10 when they appear in the same sentence with numbers greater than 9. For example, "The menu contains 15 options but 6 of them are disabled".
- Negative numbers.
- Most fractions.
- Percentages.
- Dimensions.
- Decimals.
- Measurements.
- Numbers in a range.

Fractions

- Express fractions as decimal numbers, when possible.
- When expressing fractions as words, connect the numerator and denominator with a hyphen unless one of them is already hyphenated.

</details>

## Punctuation

- Don't use ampersands (&) as conjunctions or shorthand for *and*. Use *and* instead. That includes headings and navigation. 
  >**Exception:** It's okay to use & in cases where you need to refer to a UI element or the name of a menu that uses &.
- Put quotation marks and end punctuation [outside of link text](https://developers.google.com/style/link-text#punctuation-with-links).

