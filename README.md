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


## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/markdown-to-latex.git
cd markdown-to-latex
```

Ensure you have **Python 3.8+** installed.

No external libraries are required.

## 🏗️ Cooming soon...

- Image support (`\includegraphics`)
- Math display blocks (`$$ ... $$`)
- Table support (`tabularx`)
- Nested list indentation


## 🤝 If you liked the project...

Pull requests and suggestions are welcome!  
Open an issue if you want a new Markdown feature supported. If you like this project please give the repository a **star** ⭐ it would be much appreciated.

