%%% ====================================================================
%%%  @LaTeX-class-file{
%%%     filename        = "simcenterdocumentation.cls",
%%%     version         = "1.0",
%%%     date            = "26 February 2019",
%%%     license         = "LPPL",
%%%     codetable       = "ISO/ASCII",
%%%     keywords        = "LaTeX, simcenterdocumentation",
%%%     docstring       = "This file is the main file for the simcenterdocumentation
%%%                        class, which is intended to be used for documenting
%%%                        SimCenter software packages. The class builds on top
%%%                        of the memoir class and is based on the ucbthesis class.
%%%  }
%%% ====================================================================

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{simcenterdocumentation}[2019/02/26 v1.0 NHERI SimCenter Software Documentation Class]

%    ****************************************
%    *               OPTIONS                *
%    ****************************************
%
% Option values are now declared first thing.  Defaults are set to
% 12 point, onesided, codedoc, final (i.e., not draft) mode
% Currently, there aren't different options available, but this class
% could be extended later on for different SimCenter document types

\newcommand\@codedoc{}
\DeclareOption{documentation}{\renewcommand\@codedoc{0}}
%% \DeclareOption{amazingnewtype}{\renewcommand\@codedoc{1}}
\ExecuteOptions{documentation}

%  The following code relies on the memoir class for oneside/twoside formatting,
%  but changes the default to oneside.
%  Ideas for this code were adapted from an answer on stackexchange,
%    http://tex.stackexchange.com/questions/12933/new-options-and-loaded-class-options-bug
%  (accessed on 12 September 2011).

\newcommand\thes@sidedness{-1}
\DeclareOption{oneside}
  {\renewcommand\thes@sidedness{1}\PassOptionsToClass{\CurrentOption}{memoir}}
\DeclareOption{twoside}
  {\renewcommand\thes@sidedness{2}\PassOptionsToClass{\CurrentOption}{memoir}}

%  Changing the default point size from 10pt to 12pt uses a similar procedure,
%  but it's messier.

\newcommand\thes@ptsize{0}
\DeclareOption{9pt}
  {\renewcommand\thes@ptsize{9}\PassOptionsToClass{\CurrentOption}{memoir}}
\DeclareOption{10pt}
  {\renewcommand\thes@ptsize{10}\PassOptionsToClass{\CurrentOption}{memoir}}
\DeclareOption{11pt}
  {\renewcommand\thes@ptsize{11}\PassOptionsToClass{\CurrentOption}{memoir}}
\DeclareOption{12pt}
  {\renewcommand\thes@ptsize{12}\PassOptionsToClass{\CurrentOption}{memoir}}
\DeclareOption{14pt}
  {\renewcommand\thes@ptsize{14}\PassOptionsToClass{\CurrentOption}{memoir}}
\DeclareOption{17pt}
  {\renewcommand\thes@ptsize{17}\PassOptionsToClass{\CurrentOption}{memoir}}
\DeclareOption{20pt}
  {\renewcommand\thes@ptsize{20}\PassOptionsToClass{\CurrentOption}{memoir}}
\DeclareOption{25pt}
  {\renewcommand\thes@ptsize{25}\PassOptionsToClass{\CurrentOption}{memoir}}
\DeclareOption{30pt}
  {\renewcommand\thes@ptsize{30}\PassOptionsToClass{\CurrentOption}{memoir}}
\DeclareOption{36pt}
  {\renewcommand\thes@ptsize{36}\PassOptionsToClass{\CurrentOption}{memoir}}
\DeclareOption{48pt}
  {\renewcommand\thes@ptsize{48}\PassOptionsToClass{\CurrentOption}{memoir}}
\DeclareOption{60pt}
  {\renewcommand\thes@ptsize{60}\PassOptionsToClass{\CurrentOption}{memoir}}
\DeclareOption{*pt}
  {\renewcommand\thes@ptsize{99}\PassOptionsToClass{\CurrentOption}{memoir}}

% Other options are passed on to the memoir class.

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{memoir}}

% The \ProcessOptions command causes the execution of every option command
% FOO which is declared and for which the user typed the FOO option in their
% \documentclass.  For every undeclared option BAR there will be a warning
% message. (BBF 10/31/94)

\ProcessOptions\relax

% Take care of changed defaults

\ifnum\thes@sidedness<0
  \PassOptionsToClass{oneside}{memoir}
  \renewcommand\thes@sidedness{1}
\fi

\ifnum\thes@ptsize=0
  \PassOptionsToClass{12pt}{memoir}
  \renewcommand\thes@ptsize{12}
\fi

% Now load the memoir class, and configure it appropriately.
\LoadClass{memoir}
\RequirePackage{graphicx}
\RequirePackage{titlesec}
\RequirePackage{hyperref}
\RequirePackage{xcolor}
\RequirePackage{listings}

%\chapterstyle{article}
%\chapterstyle{southall}
%\chapterstyle{verville}
%\chapterstyle{wilsondob}
\chapterstyle{tandh}

% Set section numbering depth. Depth of 3 sets numbering to go up to and including subsubsection
\setcounter{secnumdepth}{3}

\setlrmarginsandblock{1in}{*}{*}
  \@tempdima=1in  \advance\@tempdima 25pt \advance\@tempdima\normalbaselineskip
  \@tempdimb=.75in  \advance\@tempdimb 30pt
\setulmarginsandblock{\@tempdima}{\@tempdimb}{*}

\AtBeginDocument{\checkandfixthelayout}

% Ensure placement of page numbers is consistent throughout

\makepagestyle{somewhatsimple} 
\makeevenhead{somewhatsimple}{\includegraphics[width=0.25\textwidth]{simcenterfooter}}{}{\itshape\leftmark \vspace{-8pt}} 
\makeoddhead{somewhatsimple}{\itshape\leftmark}{}{\includegraphics[width=0.25\textwidth]{simcenterfooter} \vspace{-8pt}} 
\makeevenfoot{somewhatsimple}{}{\thepage}{} 
\makeoddfoot{somewhatsimple}{}{\thepage}{} 
\makeatletter
\makepsmarks{somewhatsimple}{%
  \createmark{chapter}{left}{shownumber}{\@chapapp\ }{.\ }}

\makepagestyle{simple}
\makeevenhead{simple}{\includegraphics[width=0.25\textwidth]{simcenterfooter} \vspace{-8pt}}{}{} 
\makeoddhead{simple}{}{}{\includegraphics[width=0.25\textwidth]{simcenterfooter} \vspace{-8pt}} 
\makeevenfoot{simple}{}{\thepage}{}
\makeoddfoot{simple}{}{\thepage}{}

\makepagestyle{plain}
\makeevenhead{plain}{}{}{} 
\makeoddhead{plain}{}{}{} 
\makeevenfoot{plain}{}{\thepage}{}
\makeoddfoot{plain}{}{\thepage}{}

\pagestyle{simple}
\aliaspagestyle{book}{simple}
\aliaspagestyle{part}{simple}
\aliaspagestyle{chapter}{simple}
\aliaspagestyle{title}{simple}

% Issue warnings if the settings are not appropriate for a final copy

\ifnum\thes@sidedness=2\relax
  \ifdraftdoc\else
  \ClassWarningNoLine{simcenterdocumentation}{^^J\@spaces
 ****** Note: The document has been set to two-sided format. Make sure this is what you want!. \@spaces\@spaces ******}
\fi\fi

\ifnum\thes@ptsize<12\relax
  \ifdraftdoc\else
  \ClassWarningNoLine{simcenterdocumentation}{^^J\@spaces
 ****** Use the \thes@ptsize pt option only for drafts. \@spaces\@spaces
 ******^^J\@spaces
 ****** Use 12-point type ******^^J\@spaces
 ****** or larger for the final drafts.\space\@spaces\@spaces\@spaces
 ******}
\fi\fi

% For some environments we switch back to single-spacing, also
% provides \dsp in case you need double-spacing where single-spacing
% is otherwise used.

\newcommand\ssp{\SingleSpacing}
\newcommand\dsp{\setSpacing{1.37}}

% Table of contents, lists of figures, and lists of tables should always
% be single-spaced.  If one wants them to be double-spaced instead (in a
% double-spaced document), the original macros are available as
% \memoirtableofcontents, \memoirlistoffigures, and \memoirlistoftables.

\let\memoirtableofcontents=\tableofcontents
\renewcommand\tableofcontents{\begin{SingleSpace}\memoirtableofcontents
  \end{SingleSpace}}

\let\memoirlistoffigures=\listoffigures
\renewcommand\listoffigures{\begin{SingleSpace}\memoirlistoffigures
  \end{SingleSpace}}

\let\memoirlistoftables=\listoftables
\renewcommand\listoftables{\begin{SingleSpace}\memoirlistoftables
\end{SingleSpace}}

%%% THIS SECTION DECLARES ENVIRONMENTS FOR CODE SNIPPETS AND ALLOWS FOR SYNTAX HIGHLIGHTING %%%%%%%%%%%%%%%%%%%%
% Set link colors 
\hypersetup{
    colorlinks,
    citecolor=black,
    filecolor=black,
    linkcolor=black,
    urlcolor=blue
}

% Default fixed font does not support bold face
\DeclareFixedFont{\ttb}{T1}{txtt}{bx}{n}{12} % for bold
\DeclareFixedFont{\ttm}{T1}{txtt}{m}{n}{12}  % for normal

% Custom colors for code snippets
\definecolor{deepblue}{rgb}{0,0,0.5}
\definecolor{deepred}{rgb}{0.6,0,0}
\definecolor{deepgreen}{rgb}{0,0.5,0}

% Python style for highlighting
\newcommand\pythonstyle{\lstset{
language=Python,
basicstyle=\ttm,
otherkeywords={self},             % Add keywords here
keywordstyle=\ttb\color{deepblue},
emph={MyClass,__init__},          % Custom highlighting
emphstyle=\ttb\color{deepred},    % Custom highlighting style
stringstyle=\color{deepgreen},
frame=tb,                         % Any extra options here
showstringspaces=false,            %
breaklines=true
}}

% Python environment
\lstnewenvironment{python}[1][]
{
\pythonstyle
\lstset{#1}
}
{}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%  draft option (this is where the draft option is actually implemented)
%
\ifdraftdoc
    \dsp				% Set to double spacing
\fi

%    ****************************************
%    *             FRONT MATTER             *
%    ****************************************
%

% DECLARATIONS
%
% These macros are used to declare arguments needed for the
% construction of the front matter.

% The software name
\def\softwarename#1{\gdef\@softwarename{#1}}
\def\getsoftwarename{\@softwarename}
\def\softwareSwitch#1#2#3{%
   \ifthenelse{\equal{\@softwarename}{#1}}
    {#2}
    {#3}%
}

% Software webpage
\def\softwarepage#1{\gdef\@softwarepage{#1}}
\def\getsoftwarepage#1{\href{\@softwarepage}{\color{blue}{#1}}}

% The software version
\def\softwareversion#1{\gdef\@softwareversion{#1}}
\def\getsoftwareversion{\@softwareversion}

% Institutions
\def\institutions#1{\gdef\@institutions{#1}}

% Function for getting link to feedback survey
\def\insertsurveylink#1{\href{https://docs.google.com/forms/d/e/1FAIpQLSfh20kBxDmvmHgz9uFwhkospGLCeazZzL770A2GuYZ2KgBZBA/viewform?usp=sf_link}{\color{blue}{#1}}}

% The alwayssingle environment ensures that front matter is always
% single column even in a double-column document.

\newenvironment{alwayssingle}
  {\if@twocolumn\@restonecoltrue\onecolumn \else \@restonecolfalse\newpage \fi}
  {\if@restonecol \twocolumn \else \newpage \fi}

% \maketitle outputs the complete titlepage.  It requires all the
% above macros. 

% Set the font that will be used in the front matter headings
\def\fmfont{\fontsize\@xiipt{14.5}\selectfont}
\def\fmsmallfont{\fontsize\@xiipt{14pt}\selectfont}

\def\maketitle{
{\ssp
  \makeatletter
    \setlength{\@tempdima}{28pt}\advance\@tempdima-\baselineskip
    \parskip=\@tempdima minus 4pt
  \makeatother
\begin{alwayssingle}
  \hrule height 0pt
  % Fix things so that they're vertically centered
  % \@tempdima = 2 * ((\stockheight-\textheight) / 2 - \uppermargin) - \topskip
    \@tempdima=\stockheight
    \advance\@tempdima-\textheight
    \advance\@tempdima-2\uppermargin
    \advance\@tempdima-\topskip
    \vspace{\@tempdima}
  \vfill
  \let\footnotesize\small
  \let\footnoterule\relax
  \thispagestyle{empty}
  \setcounter{page}{1}

  \begin{center}
    \includegraphics[width=0.7\textwidth]{simcenterlogo} \\
    \vspace{50pt minus 8pt}    
    \fmfont
    \huge \textbf{\@title}\par
    \vspace{14pt minus 4pt}
    \Large
        {\@author}\par
        \large
        \textit{{\@institutions}}\par
    \vspace{200pt minus 8pt}
    Version \@softwareversion \\
    \vspace{14pt minus 4pt}    
    \@date
    \vspace{14pt minus 4pt}
  \end{center}
  \vfill
  \hrule height 0pt
\end{alwayssingle}

\setcounter{footnote}{0}
}}

% COPYRIGHTPAGE
%
% While it's technically optional, you probably want a copyright page.
% This is a macro, not an environment, because it can be generated
% with the \title, \author, and \year macros.

\def\copyrightpage{
\begin{alwayssingle}
\pagestyle{empty}
{\fmfont
  \begin{center}
           {\Large \textbf{Licenses and Copyright Notices}}\par
  \end{center}
\setcounter{page}{1}
\vspace{0.25in}
\sloppy
\begingroup
\fontsize{12pt}{12pt}\selectfont
The source code of {\@softwarename} is licensed under a BSD 2-Clause License:
"Copyright (c) 2017-{\@\the\year}, The Regents of the University of California
(Regents)." All rights reserved.Redistribution and use in source and binary forms, with or without modification, are permitted provided that
the following conditions are met:
\begin{enumerate}
  \item Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer
  \item Redistributions in binary form must reproduce the above
    copyright notice, this list of conditions and the following
    disclaimer in the documentation and/or other materials provided
    with the distribution
\end{enumerate}
\vspace{ 3pt}

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
“AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
\vspace{ 6pt}

The views and conclusions contained in the software and documentation
are those of the authors and should not be interpreted as representing
official policies, either expressed or implied, of the FreeBSD
Project. Authors take no responsibility, whatsoever, on accuracy of
{\@softwarename}. REGENTS SPECIFICALLY DISCLAIMS ANY WARRANTIES,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE SOFTWARE AND
ACCOMPANYING DOCUMENTATION, IF ANY, PROVIDED HERE UNDER IS PROVIDED
“AS IS”. THE REGENTS HAVE NO OBLIGATION TO PROVIDE MAINTENANCE,
SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.
\vspace{ 6pt}

The compiled binary form of this application is licensed under a GPL
Version 3 license. The licenses are as published by the Free Software
Foundation and appearing in the LICENSE file included in the packaging
of this application.
\vspace{ 6pt}

This software makes use of the QT packages (unmodified): core, gui,
widgets and network. QT is copyright “The Qt Company Ltd” and licensed
under the GNU Lesser General Public License (version 3) which
references the GNU General Public License (version 3).
\vspace{ 6pt}

The licenses are as published by the Free Software Foundation and
appearing in the LICENSE file included in the packaging of this
application.
\endgroup
}
\end{alwayssingle}}

% ACKNOWLEDGMENTS

\def\acknowledgments{
\begin{alwayssingle}
      \pagestyle{empty}
                {\fmfont      
                  \begin{center}
                    {\large \bfseries Acknowledgments}
                  \end{center}
                  \setcounter{page}{1}                  
                  \vspace{0.25in}
                  \sloppy  
                  This material is based upon work supported by the National Science
                  Foundation under Grant No. 1612843. Any opinions, findings, and
                  conclusions or recommendations expressed in this material are those of
                  the author(s) and do not necessarily reflect the views of the National
                  Science Foundation.}
  \end{alwayssingle}}
  
% FRONTMATTER environment
%
% The FRONTMATTER environment makes sure that page numbering is set
% correctly (roman, lower-case, starting at 3) for the front matter
% that follows the abstract.  It also resets page-numbering for
% the remainder of the document (arabic, starting at 1).

\renewenvironment{frontmatter}
  {\setcounter{page}{1}\renewcommand{\thepage}{\roman{page}}}
  {\newpage\renewcommand{\thepage}{\arabic{page}}\setcounter{page}{1}}
  
  
% Rename environments to allow them to switch back to double spacing

% These were taken from memoir.cls 2010/09/19
\newenvironment{memoirquotation}%
             {\list{}{\listparindent 1.5em%
                      \itemindent    \listparindent
                      \rightmargin   \leftmargin
                      \parsep        \z@ \@plus\p@}%
              \item[]}%
             {\endlist}

\newenvironment{memoirquote}%
             {\list{}{\rightmargin\leftmargin}%
              \item[]}%
             {\endlist}

\newenvironment{memoirverse}[1][\linewidth]{%
  \refstepcounter{verse}%
  \setcounter{poemline}{0}\refstepcounter{poemline}%
  \setcounter{vslineno}{1}%
  \let\\=\@vscentercr
  \list{}{\itemsep     \z@
        \itemindent  -\vindent
        \listparindent\itemindent
        \leftmargin   \vleftmargin
        \parsep       \stanzaskip
        \ifdim #1<\linewidth%   %% short line
          \rightmargin        \z@
          \leftmargin         \linewidth
          \advance\leftmargin -#1\relax
          \advance\leftmargin -0.5\leftmargin
          \advance\leftmargin \vindent
        \else
          \ifdim #1>\linewidth%  %% long line
            \rightmargin \z@
            \leftmargin  \vindent
          \else%                   %% default
            \rightmargin \leftmargin
            \advance\leftmargin \vindent
          \fi
        \fi}
  \item[]}{\endlist}

\ifdraftdoc\else

  \renewenvironment{quotation}%
             {\list{}{\listparindent 1.5em%
                      \itemindent    \listparindent
                      \rightmargin   \leftmargin
                      \parsep        \z@ \@plus\p@}%
              \SingleSpacing\item[]}%
             {\endlist}

  \renewenvironment{quote}%
             {\list{}{\rightmargin\leftmargin}%
              \SingleSpacing\item[]}%
             {\endlist}

  \renewenvironment{verse}[1][\linewidth]{%
    \refstepcounter{verse}%
    \setcounter{poemline}{0}\refstepcounter{poemline}%
    \setcounter{vslineno}{1}%
    \let\\=\@vscentercr
    \list{}{\itemsep     \z@
        \itemindent  -\vindent
        \listparindent\itemindent
        \leftmargin   \vleftmargin
        \parsep       \stanzaskip
        \ifdim #1<\linewidth%   %% short line
          \rightmargin        \z@
          \leftmargin         \linewidth
          \advance\leftmargin -#1\relax
          \advance\leftmargin -0.5\leftmargin
          \advance\leftmargin \vindent
        \else
          \ifdim #1>\linewidth%  %% long line
            \rightmargin \z@
            \leftmargin  \vindent
          \else%                   %% default
            \rightmargin \leftmargin
            \advance\leftmargin \vindent
          \fi
        \fi}
  \SingleSpacing\item[]}{\endlist}

\fi

\endinput
