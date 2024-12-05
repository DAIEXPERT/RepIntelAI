from multi_agents.agents import ChiefEditorAgent

chief_editor = ChiefEditorAgent({
  "query": "Does Tesla has a good reputation ?",
  "max_sections": 3,
  "follow_guidelines": False,
  "model": "gpt-4o",
  "guidelines": [
    "The report MUST follow the format and structure appropriate for business intelligence and reputation analysis.",
    "Each sub-section MUST include supporting data and references to credible sources. If no sources are available, the sub-section should be omitted or integrated into the previous section.",
    "The report MUST be written in English and focus on delivering actionable insights related to reputation management, sentiment analysis, and brand intelligence."
  ],
  "verbose": False
}, websocket=None, stream_output=None)
graph = chief_editor.init_research_team()
graph = graph.compile()