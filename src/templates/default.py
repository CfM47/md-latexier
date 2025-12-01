LATEX_TEMPLATE = r"""
\documentclass{scrreprt}
\usepackage{listings}
\usepackage{underscore}
\usepackage{graphicx}
\usepackage[bookmarks=true]{hyperref}
\usepackage[utf8]{inputenc}
\usepackage[english]{babel}
\usepackage{tabularx}
\usepackage{ltablex} 
\keepXColumns

\def\myversion{1.0 }
\date{}
\usepackage{hyperref}

\begin{document}

\begin{flushright}
    \rule{16cm}{5pt}\vskip1cm
    \begin{bfseries}
        \Huge{TITLE_PLACEHOLDER}\\
        \vspace{1.5cm}
        \LARGE{Version \myversion}\\
        \vspace{1.5cm}
    \end{bfseries}
\end{flushright}

% ======= DOCUMENT CONTENT BELOW =======
CONTENT_PLACEHOLDER
% ======================================

\end{document}
"""