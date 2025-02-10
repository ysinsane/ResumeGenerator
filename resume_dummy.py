def extract_job_description(url: str) -> str:
    return "This is a dummy JD"

def generate_resume(full_resume: str, job_description: str) -> str:
    return r"""
\documentclass[10pt,a4paper]{article}
\usepackage[margin=1in]{geometry}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{titlesec}

% Formatting commands
\renewcommand{\baselinestretch}{1.2}
\setlength{\parskip}{0.5em}
\setlist[itemize]{noitemsep, topsep=0pt}
\titleformat{\section}{\large\bfseries}{}{0em}{}[\titlerule]

\begin{document}

% Header
\centerline{\textbf{\Huge Nadia Delgado}}
\centerline{\textit{Java Developer}}
\vspace{0.5em}
\centerline{\href{mailto:n.delgado@email.com}{n.delgado@email.com} \textbar\ (123) 456-7890 \textbar\ Detroit, MI}

% Work Experience
\section*{Work Experience}

\textbf{University of Michigan} \hfill \textit{Ann Arbor, MI} \\
\textit{Teaching Assistant, CS110: Introduction to Computer Science} \hfill September 2021 -- Present
\begin{itemize}
    \item Assisted in teaching introductory computer science concepts, including algorithms, data structures, and basic programming.
    \item Conducted weekly office hours, providing one-on-one support for students struggling with course material.
    \item Graded assignments and exams, ensuring timely and constructive feedback to help students improve.
    \item Assisted the professor in developing and refining course content, including lecture slides and programming assignments.
\end{itemize}


\textbf{Deloitte} \hfill \textit{Lansing, MI} \\
\textit{Java Developer} \hfill May 2018 -- 2021
\begin{itemize}
    \item Designed software solutions by analyzing system performance standards, increasing performance efficiency by 27%.
    \item Planned, tracked, and managed 100+ deliverables on short-term sprints and long-term software deployments.
    \item Developed and executed 300+ test procedures for software components.
\end{itemize}

\textbf{Perficient} \hfill \textit{Ann Arbor, MI} \\
\textit{Junior Java Developer} \hfill January 2016 -- April 2018
\begin{itemize}
    \item Designed and coded 60+ unit/integration tests using Perficient methodology.
    \item Utilized strong configuration management and version control to ensure peak system performance throughout 20+ changes.
    \item Created 70+ detailed design documents, unit test plans, and well-documented code used by a 12-week summer intern program.
\end{itemize}

\textbf{Arup} \hfill \textit{Ann Arbor, MI} \\
\textit{Software Developer Intern} \hfill June 2015 -- January 2016
\begin{itemize}
    \item Collaborated with 15+ experts across a range of domains to identify and study datasets to produce visuals and other tools.
    \item Worked with the R\&D team to identify critical, emerging technologies, and performed strategic research.
\end{itemize}

\textbf{Verizon} \hfill \textit{Remote} \\
\textit{Senior Java Developer} \hfill March 2010 -- 2012
\begin{itemize}
    \item Ensured that the workflow engine continued to scale and perform despite load on the platform.
    \item Wrote automated scripts to identify bad workflows, identifying 40+ bad workflows.
    \item Transformed flows with low performance, optimizing workflows by 29%.
    \item Utilized DevOps, agile principles, and Jenkins to enable CI/CD, decreasing production time by 40%.
    \item Handled 20+ critical operation tasks and on-demand support requests from tenant applications.
    \item Ensured that mission-critical applications did not result in an outage situation due to the workflow engine.
\end{itemize}

\textbf{Crum \& Forster Holdings Corp.} \hfill \textit{Trenton, NJ} \\
\textit{Java Developer} \hfill June 2012 -- March 2015
\begin{itemize}
    \item Analyzed 300+ requirements from existing documentation and collaborated with BAs and QAs.
    \item Worked with 6 architects to design and implement 20+ appropriate technical solutions.
    \item Learned and worked with 5 other platforms and technologies, including API Management platform, ESB, and AWS tools.
    \item Estimated work necessary to realize 80+ story/requirement through the delivery lifecycle.
    \item Coded 50+ solutions and unit tests to deliver requirements/stories per defined acceptance criteria and compliance requirements.
    \item Communicated within a multi-disciplined team, across 20 locations and 5 time zones.
\end{itemize}

% Projects
\section*{Projects}

\noindent
\textbf{Inventory Management System} \hfill \textit{Self-Designed}
\vspace{0.5em}  % Add space between title and bullet points
\begin{itemize}
    \item Developed a full-stack inventory management system using Node.js for the backend and React for the frontend.
    \item Designed and implemented the entire system architecture, including database schema and API endpoints.
    \item Created an intuitive user interface with React, ensuring a seamless user experience for managing inventory data.
\end{itemize}

\noindent
\textbf{Data Pipeline Automation System} \hfill \textit{Team Collaboration}
\vspace{0.5em}  % Add space between title and bullet points
\begin{itemize}
    \item Developed an automated data pipeline to process, analyze, and visualize large datasets for performance insights.
    \item Utilized Java for backend processing and Python for data cleaning and analysis.
    \item Designed and implemented an ETL workflow that handled terabytes of data efficiently, reducing processing time by 35%.
    \item Integrated AWS services, including S3 for data storage and Lambda for serverless computing.
    \item Built interactive dashboards with React.js to visualize real-time analytics and performance metrics.
    \item Collaborated with DevOps teams to implement CI/CD pipelines using Jenkins, enabling faster deployment cycles.
\end{itemize}


% Education
\section*{Education}

\textbf{University of Michigan} \hfill \textit{Ann Arbor, MI} \\
\textit{B.S., Computer Science} \hfill September 2011 -- June 2015

% Skills
\section*{Skills}

Java; JavaScript; AngularJS; HTML; CSS; UNIX; SQL; Eclipse; Oracle; React.js; Node.js; Jenkins; AWS; Jira; (REST) APIs

\end{document}

"""