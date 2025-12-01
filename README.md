# Markdown to LaTeX Converter

A lightweight, dependency-free Markdown → LaTeX converter written in Python.  
Designed to be clean, modular, and easily extensible.  
Suitable for academic documents, technical reports, and custom LaTeX workflows.


## ✨ Features

The converter currently supports:

### **Headings**
- `#` → `\chapter{}`
- `##` → `\section{}`
- `###` → `\subsection{}`
- `####` → `\subsubsection{}`

### **Inline Formatting**
- Bold: `**text**` → `\textbf{text}`
- Italics: `*text*` → `\textit{text}`
- Inline code: `` `code` `` → `\texttt{code}`
- Hyperlinks: `[label](http://...)` → `\href{url}{label}`

### **Code Blocks**
Markdown:
````

```python
print("Hello")
```

````

LaTeX:
````
```latex
\begin{lstlisting}[language=python]
print("Hello")
\end{lstlisting}
```
````

### **Lists**
- Unordered lists: `-`, `*`, `+` → `itemize`
- Ordered lists: `1.`, `2.` → `enumerate`
- Automatic list detection and closing

### **Blockquotes**
- `> text` → LaTeX `quote` environment

### **Math Inline**
- `$ math_expr $` preserved with no unwanted escaping

### **Customizable Template**
The generated LaTeX file is embedded into a user-editable template.

## 🚀 Installation

`md-latexier` can be installed globally using **uv**.

First, clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/md-latexier.git
cd md-latexier
```

Then install it as a terminal tool:

```bash
uv tool install .
```

You can verify the installation with:

```bash
md-latexier --help
```

## 🧭 Usage

Convert any Markdown file into a LaTeX `.tex` document:

```bash
md-latexier input.md
```

This will generate `input.tex` in the same directory.

You can also specify a relative or absolute path:

```bash
md-latexier docs/chapter1.md
md-latexier /home/user/notes/report.md
```

The generated LaTeX uses the default template, support for custom templates is comming soon.

## 🏗️ Cooming soon...

- Image support (`\includegraphics`)
- Math display blocks (`$$ ... $$`)
- Table support (`tabularx`)
- Nested list indentation
- Support for custom templates


## 🤝 If you liked the project...

Pull requests and suggestions are welcome!  
Open an issue if you want a new Markdown feature supported. If you like this project please give the repository a **star** ⭐ it would be much appreciated.

