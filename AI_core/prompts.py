import warnings
from datetime import date, datetime, timezone

from .utils.enum import ReportSource, ReportType, Tone
from typing import List, Dict, Any, Optional


def generate_search_queries_prompt(
    question: str,
    parent_query: str,
    report_type: str,
    max_iterations: int = 3,
    context: List[Dict[str, Any]] = [],
):
    """Generates the search queries prompt for the given question.
    Args:
        question (str): The question to generate the search queries prompt for
        parent_query (str): The main question (only relevant for detailed reports)
        report_type (str): The report type
        max_iterations (int): The maximum number of search queries to generate
        context (str): Context for better understanding of the task with realtime web information

    Returns: str: The search queries prompt for the given question
    """

    if (
        report_type == ReportType.DetailedReport.value
        or report_type == ReportType.SubtopicReport.value
    ):
        task = f"{parent_query} - {question}"
    else:
        task = question

    context_prompt = f"""
You are an AI-driven reputation intelligence assistant specializing in providing businesses with insights into their online reputation, brand sentiment, industry trends, and competitive analysis for the following task: "{task}".
Context: {context}

Use this context to inform and refine your search queries. The context provides real-time web information that can help generate precise and actionable queries. Focus on relevant keywords and events that align with RepIntel’s ability to monitor brand sentiment, consumer opinions, competitor analysis, and reputation metrics. Aim to gather insights that could reveal public perception, brand strengths and weaknesses, consumer needs, or trending topics in the industry.
""" if context else ""

    dynamic_example = ", ".join([f'"query {i+1}"' for i in range(max_iterations)])

    return f"""Generate {max_iterations} online search queries designed to gather reputation insights from the following task: "{task}"

Assume the current date is {datetime.now(timezone.utc).strftime('%B %d, %Y')} if required.

{context_prompt}
Respond with a list of strings in the following format: [{dynamic_example}].
The response should contain ONLY the list."""


def generate_report_prompt(
    question: str,
    context,
    report_source: str,
    report_format="apa",
    total_words=1000,
    tone: Optional[str] = None,
):
    """Generates the report prompt for the given question and research summary.
    Args:
        question (str): The question to generate the report prompt for
        context (str): The context or research summary relevant to the report prompt
        report_source (str): Source of the report (Web, Document, etc.)
        report_format (str): Format of the report (APA, MLA, etc.)
        total_words (int): Target word count for the report
        tone (str): Desired tone of the report (optional)

    Returns:
        str: The report prompt tailored for REPINTEL’s reputation intelligence goals
    """

    reference_prompt = ""
    if report_source == ReportSource.Web.value:
        reference_prompt = f"""
You MUST include all used source URLs at the end of the report as references, ensuring no duplicates, with only one reference per unique source.
Every URL should be hyperlinked: [url website](url)
Additionally, hyperlink relevant URLs wherever they are referenced within the report: 

Example: Author, A. A. (Year, Month Date). Title of web page. Website Name. [url website](url)
"""
    else:
        reference_prompt = f"""
You MUST include all used source document names at the end of the report as references, ensuring no duplicates, with only one reference per unique source.
"""

    tone_prompt = f"Write the report in a {tone} tone." if tone else ""

    return f"""
Information: "{context}"
---
Using the above information, answer the following query or task: "{question}" in a detailed report focused on reputation insights, brand sentiment, or industry trends.

The report should:
- Thoroughly address the question with structured, data-driven insights,
- Be well-organized, informative, and grounded in facts and metrics where possible,
- Aim to be comprehensive, at least {total_words} words long, and provide actionable recommendations for reputation management.

Please follow these guidelines:
- Derive a concrete and valid conclusion based on the given information, rather than relying on general statements.
- Write the report using markdown syntax and in {report_format} format.
- Prioritize source relevance, reliability, and significance, choosing trusted sources whenever possible.
- Favor recent, trusted sources over older references if relevant.
- Include in-text citations in {report_format} format, using markdown hyperlinks placed at the end of the sentence or paragraph that references them, like this: ([in-text citation](url)).
- Remember to add a reference list at the end of the report in {report_format} format, with full URLs without hyperlinks.
- {reference_prompt}
- {tone_prompt}

This report is highly important for strategic decision-making regarding brand reputation and growth.
Assume the current date is {date.today()}.
"""


def generate_resource_report_prompt(
    question: str, 
    context: str, 
    report_source: str, 
    report_format="apa", 
    tone=None, 
    total_words=1000
):
    """Generates the resource report prompt tailored for REPINTEL’s reputation intelligence needs.

    Args:
        question (str): The question or topic for which to generate the resource report prompt.
        context (str): Relevant background or context for generating the resource report prompt.
        report_source (str): Source type (e.g., Web or Document)
        report_format (str): Citation format (e.g., APA, MLA)
        tone (str): Desired tone for the report
        total_words (int): Minimum length for the report

    Returns:
        str: A detailed resource report prompt for analyzing recommended sources in reputation intelligence.
    """

    reference_prompt = ""
    if report_source == ReportSource.Web.value:
        reference_prompt = """
            You MUST include all relevant source URLs at the end of the report as references. 
            Each URL should be hyperlinked: [url website](url)
            Avoid duplicate URLs and include only one unique reference per source.
            """
    else:
        reference_prompt = """
            You MUST include all used source document names at the end of the report as references, 
            ensuring no duplicates, with only one reference per unique source.
        """

    tone_prompt = f"Write the report in a {tone} tone." if tone else ""

    return (
        f'"""{context}"""\n\nBased on the above information, generate a detailed resource report for the following '
        f'question or topic: "{question}". The report should provide a thorough analysis of each recommended resource, '
        "explaining how each source can support REPINTEL’s reputation intelligence goals. Focus on evaluating each source for "
        "its relevance, reliability, and potential insights on brand sentiment, competitive positioning, and industry trends.\n"
        "Ensure that the report is well-structured, comprehensive, and follows Markdown syntax.\n"
        f"The report should have a minimum length of {total_words} words and should include relevant facts, figures, "
        "and insights to provide a strong foundation for reputation management decisions.\n"
        f"{reference_prompt}\n"
        f"{tone_prompt}\n"
    )


def generate_custom_report_prompt(
    query_prompt: str, 
    context: str, 
    report_source: str, 
    report_format="apa", 
    tone=None, 
    total_words=1000
):
    """Generates a custom report prompt specific to REPINTEL’s needs for intelligence on brand reputation and competitive analysis.

    Args:
        query_prompt (str): The prompt or question for generating the custom report
        context (str): Background or context relevant to REPINTEL’s needs for reputation intelligence
        report_source (str): Source type (e.g., Web, Document)
        report_format (str): Desired citation format (e.g., APA, MLA)
        tone (str): Desired tone for the report
        total_words (int): Minimum length for the report

    Returns:
        str: A customized report prompt for the given query and context, structured for REPINTEL’s goals.
    """
    return (
        f'"{context}"\n\n{query_prompt} in a comprehensive report format, following {report_format} citation style '
        f"and integrating insights on brand sentiment, competitive positioning, and market perception for REPINTEL's "
        f"reputation intelligence strategy. The report should be detailed, minimum {total_words} words, and written "
        f"{f'in a {tone} tone' if tone else 'in a formal, informative tone'}.\n"
    )


def generate_outline_report_prompt(
    question: str, 
    context: str, 
    report_source: str, 
    report_format="apa", 
    tone=None,  
    total_words=1000
):
    """Generates the outline report prompt, tailored for REPINTEL's reputation intelligence reports.

    Args:
        question (str): The main question or topic for the outline report
        context (str): Relevant background information for framing the report outline
        report_source (str): Source type (e.g., Web or Document)
        report_format (str): Desired citation format (e.g., APA, MLA)
        tone (str): Desired tone for the report
        total_words (int): Minimum word length for the report

    Returns:
        str: A structured prompt for generating a report outline focused on REPINTEL’s reputation intelligence goals.
    """
    return (
        f'"""{context}"""\n\nUsing the above information, create an outline for a reputation intelligence research report '
        f'in Markdown syntax for the following topic: "{question}". The outline should provide a structured framework, '
        "highlighting main sections, relevant subsections, and key points on brand reputation, competitive sentiment, "
        f"and industry insights to be covered. The report should be thorough, at least {total_words} words, and follow "
        f"{report_format} format guidelines. Use clear Markdown syntax to ensure readability and adherence to REPINTEL’s "
        "informative, data-driven style."
    )

def get_report_by_type(report_type: str):
    report_type_mapping = {
        ReportType.ResearchReport.value: generate_report_prompt,
        ReportType.ResourceReport.value: generate_resource_report_prompt,
        ReportType.OutlineReport.value: generate_outline_report_prompt,
        ReportType.CustomReport.value: generate_custom_report_prompt,
        ReportType.SubtopicReport.value: generate_subtopic_report_prompt,
    }
    return report_type_mapping[report_type]


def auto_agent_instructions():
    return """
This task involves researching a given topic, regardless of its complexity or the availability of a definitive answer. The research is conducted by a specific server, defined by its type and role, with each server requiring distinct instructions.

Agent:
The server is determined by the field of the topic and the specific name of the server that could be utilized to research the topic provided. Agents are categorized by their area of expertise, and each server type is associated with a corresponding emoji.

Examples:
task: "Bob Smith reputation score"
response: 
{
    "server": "🔍 Reputation Analysis Agent",
    "agent_role_prompt": "You are an experienced reputation analysis AI assistant. Your main role is to provide a comprehensive, accurate, and well-structured reputation assessment, including sentiment analysis, for the subject in question."
}
task: "I need a sentiment report for Bob Smith"
response: 
{
    "server": "📊 Sentiment Analysis Agent",
    "agent_role_prompt": "You are a skilled AI sentiment analysis assistant. Your goal is to generate a thorough, balanced, and clear sentiment report based on the subject's recent activity, mentions, and media coverage."
}
task: "What is Bob Smith’s reputation score?"
response:
{
    "server": "🧭 Reputation Scoring Agent",
    "agent_role_prompt": "You are a reputation scoring specialist AI assistant. Your focus is on calculating, interpreting, and presenting a precise reputation score for the subject, taking into account recent feedback and public sentiment data."
}
task: "I need a full reputation report for Bob Smith"
response:
{
    "server": "📜 Comprehensive Reputation Agent",
    "agent_role_prompt": "You are a detailed-oriented AI assistant specializing in reputation reporting. Your task is to compile an in-depth and unbiased report covering the subject’s reputation trends, key sentiment indicators, and historical data."
}
task: "List all of the negative results for Bob Smith"
response:
{
    "server": "🚨 Negative Sentiment Agent",
    "agent_role_prompt": "You are a critical analysis AI assistant focused on identifying and summarizing all negative mentions related to the subject. Your main goal is to deliver a clear, organized list of all negative results while analyzing the context and impact of each mention."
}
"""

def generate_summary_prompt(query: str, data: str):
    """Generates a summary prompt tailored for reputation intelligence and competitive analysis objectives.

    Args:
        query (str): The specific question or task to guide the summary.
        data (str): The data or text to summarize.

    Returns:
        str: The summary prompt adapted for intelligence needs, including key details and insights.
    """

    return (
        f'{data}\n\nUsing the above information, summarize the content based on the following task: "{query}".\n'
        f"If the query cannot be answered directly from the data, YOU MUST provide a brief but comprehensive summary.\n"
        f"Ensure the summary includes any factual details relevant to brand sentiment, competitive analysis, market perception, "
        f"and reputation trends, such as statistics, quotes, or significant insights, if available."
    )
################################################################################################

# DETAILED REPORT PROMPTS


def generate_subtopics_prompt() -> str:
    return """
Provided the main topic:

{task}

and research data:

{data}

- Construct a list of subtopics which indicate the headers of a report document to be generated on the task. 
- These are a possible list of subtopics : {subtopics}.
- There should NOT be any duplicate subtopics.
- Limit the number of subtopics to a maximum of {max_subtopics}
- Finally order the subtopics by their tasks, in a relevant and meaningful order which is presentable in a detailed report

"IMPORTANT!":
- Every subtopic MUST be relevant to the main topic and provided research data ONLY!

{format_instructions}
"""


def generate_subtopic_report_prompt(
    current_subtopic,
    existing_headers: list,
    relevant_written_contents: list,
    main_topic: str,
    context,
    report_format: str = "apa",
    max_subsections=5,
    total_words=800,
    tone: Tone = Tone.Objective,
) -> str:
    return f"""
Context:
"{context}"

Main Topic and Subtopic:
Using the latest information available, construct a detailed report on the subtopic: {current_subtopic} under the main topic: {main_topic}.
You must limit the number of subsections to a maximum of {max_subsections}.

Content Focus:
- The report should focus on answering the question, be well-structured, informative, in-depth, and include facts and numbers if available.
- Use markdown syntax and follow the {report_format.upper()} format.

IMPORTANT:Content and Sections Uniqueness:
- This part of the instructions is crucial to ensure the content is unique and does not overlap with existing reports.
- Carefully review the existing headers and existing written contents provided below before writing any new subsections.
- Prevent any content that is already covered in the existing written contents.
- Do not use any of the existing headers as the new subsection headers.
- Do not repeat any information already covered in the existing written contents or closely related variations to avoid duplicates.
- If you have nested subsections, ensure they are unique and not covered in the existing written contents.
- Ensure that your content is entirely new and does not overlap with any information already covered in the previous subtopic reports.

"Existing Subtopic Reports":
- Existing subtopic reports and their section headers:

    {existing_headers}

- Existing written contents from previous subtopic reports:

    {relevant_written_contents}

"Structure and Formatting":
- As this sub-report will be part of a larger report, include only the main body divided into suitable subtopics without any introduction or conclusion section.

- You MUST include markdown hyperlinks to relevant source URLs wherever referenced in the report, for example:

    ### Section Header
    
    This is a sample text. ([url website](url))

- Use H2 for the main subtopic header (##) and H3 for subsections (###).
- Use smaller Markdown headers (e.g., H2 or H3) for content structure, avoiding the largest header (H1) as it will be used for the larger report's heading.
- Organize your content into distinct sections that complement but do not overlap with existing reports.
- When adding similar or identical subsections to your report, you should clearly indicate the differences between and the new content and the existing written content from previous subtopic reports. For example:

    ### New header (similar to existing header)

    While the previous section discussed [topic A], this section will explore [topic B]."

"Date":
Assume the current date is {datetime.now(timezone.utc).strftime('%B %d, %Y')} if required.

"IMPORTANT!":
- The focus MUST be on the main topic! You MUST Leave out any information un-related to it!
- Must NOT have any introduction, conclusion, summary or reference section.
- You MUST include hyperlinks with markdown syntax ([url website](url)) related to the sentences wherever necessary.
- You MUST mention the difference between the existing content and the new content in the report if you are adding the similar or same subsections wherever necessary.
- The report should have a minimum length of {total_words} words.
- Use an {tone.value} tone throughout the report.

Do NOT add a conclusion section.
"""


def generate_draft_titles_prompt(
    current_subtopic: str,
    main_topic: str,
    context: str,
    max_subsections: int = 5
) -> str:
    return f"""
"Context":
"{context}"

"Main Topic and Subtopic":
Using the latest information available, construct a draft section title headers for a detailed report on the subtopic: {current_subtopic} under the main topic: {main_topic}.

"Task":
1. Create a list of draft section title headers for the subtopic report.
2. Each header should be concise and relevant to the subtopic.
3. The header should't be too high level, but detailed enough to cover the main aspects of the subtopic.
4. Use markdown syntax for the headers, using H3 (###) as H1 and H2 will be used for the larger report's heading.
5. Ensure the headers cover main aspects of the subtopic.

"Structure and Formatting":
Provide the draft headers in a list format using markdown syntax, for example:

### Header 1
### Header 2
### Header 3

"IMPORTANT!":
- The focus MUST be on the main topic! You MUST Leave out any information un-related to it!
- Must NOT have any introduction, conclusion, summary or reference section.
- Focus solely on creating headers, not content.
"""


def generate_report_introduction(question: str, research_summary: str = "") -> str:
    return f"""{research_summary}\n 
Using the above latest information, Prepare a detailed report introduction on the topic -- {question}.
- The introduction should be succinct, well-structured, informative with markdown syntax.
- As this introduction will be part of a larger report, do NOT include any other sections, which are generally present in a report.
- The introduction should be preceded by an H1 heading with a suitable topic for the entire report.
- You must include hyperlinks with markdown syntax ([url website](url)) related to the sentences wherever necessary.
Assume that the current date is {datetime.now(timezone.utc).strftime('%B %d, %Y')} if required.
"""


def generate_report_conclusion(query: str, report_content: str) -> str:
    """
    Generate a concise conclusion summarizing the main findings and implications of a research report.

    Args:
        report_content (str): The content of the research report.

    Returns:
        str: A concise conclusion summarizing the report's main findings and implications.
    """
    prompt = f"""
    Based on the research report below and research task, please write a concise conclusion that summarizes the main findings and their implications:
    
    Research task: {query}
    
    Research Report: {report_content}

    Your conclusion should:
    1. Recap the main points of the research
    2. Highlight the most important findings
    3. Discuss any implications or next steps
    4. Be approximately 2-3 paragraphs long
    
    If there is no "## Conclusion" section title written at the end of the report, please add it to the top of your conclusion. 
    You must include hyperlinks with markdown syntax ([url website](url)) related to the sentences wherever necessary.
    
    Write the conclusion:
    """

    return prompt



report_type_mapping = {
    ReportType.ResearchReport.value: generate_report_prompt,
    ReportType.ResourceReport.value: generate_resource_report_prompt,
    ReportType.OutlineReport.value: generate_outline_report_prompt,
    ReportType.CustomReport.value: generate_custom_report_prompt,
    ReportType.SubtopicReport.value: generate_subtopic_report_prompt,
}


def get_prompt_by_report_type(report_type):
    prompt_by_type = report_type_mapping.get(report_type)
    default_report_type = ReportType.ResearchReport.value
    if not prompt_by_type:
        warnings.warn(
            f"Invalid report type: {report_type}.\n"
            f"Please use one of the following: {', '.join([enum_value for enum_value in report_type_mapping.keys()])}\n"
            f"Using default report type: {default_report_type} prompt.",
            UserWarning,
        )
        prompt_by_type = report_type_mapping.get(default_report_type)
    return prompt_by_type

