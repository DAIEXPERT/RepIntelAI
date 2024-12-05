from enum import Enum


class ReportType(Enum):
    ReputationOverview = "reputation_report"
    InDepthBrandSentimentAnalysis = "detailed_analysis"
    IndustryTrendReport = "trend_report"
    ResearchReport = "research_report"
    ResourceReport = "resource_report"
    OutlineReport = "outline_report"
    CustomReport = "custom_report"
    DetailedReport = "detailed_report"
    SubtopicReport = "subtopic_report"


class ReportSource(Enum):
    Web = "web"
    Local = "local"
    LangChainDocuments = "langchain_documents"
    LangChainVectorStore = "langchain_vectorstore"
    Static = "static"
    Hybrid = "hybrid"


class Tone(Enum):
    Objective = "Objective (impartial and unbiased presentation of facts and findings)"
    Analytical = "Analytical (detailed sentiment insights)"
    Informative = "Informative (providing essential reputation metrics)"
    Comparative = "Comparative (see how you stack up against competitors)"
    Optimistic = "Optimistic (highlighting positive findings and potential benefits)"
    Formal = "Formal (adheres to academic standards with sophisticated language and structure)"
    Explanatory = "Explanatory (clarifying complex concepts and processes)"
    Descriptive = "Descriptive (detailed depiction of phenomena, experiments, or case studies)"
    Critical = "Critical (judging the validity and relevance of the research and its conclusions)"
    Speculative = "Speculative (exploring hypotheses and potential implications or future research directions)"
    Reflective = "Reflective (considering the research process and personal insights or experiences)"
    Narrative = "Narrative (telling a story to illustrate research findings or methodologies)"
    Humorous = "Humorous (light-hearted and engaging, usually to make the content more relatable)"
    Pessimistic = "Pessimistic (focusing on limitations, challenges, or negative outcomes)"

