
def researcher_agent(task):
    print("\n[RESEARCHER] Working on the task...")

    findings = [
        "Artificial intelligence can automate repetitive tasks.",
        "Multi-agent systems allow specialised agents to collaborate.",
        "Python is commonly used to build AI applications."
    ]

    return findings


def analyst_agent(findings):
    print("\n[ANALYST] Analysing the findings...")

    analysis = "The findings show that Python can support specialised AI agents working together."

    return analysis


def reviewer_agent(analysis):
    print("\n[REVIEWER] Checking the analysis...")

    if len(analysis) > 20:
        return "APPROVED: The analysis is sufficiently detailed."

    return "NEEDS IMPROVEMENT: The analysis is too short."


def orchestrator(task):
    print("\n[ORCHESTRATOR] Starting the team...")

    findings = researcher_agent(task)
    analysis = analyst_agent(findings)
    review = reviewer_agent(analysis)

    print("\n[ORCHESTRATOR] All agents have finished.")

    return {
        "findings": findings,
        "analysis": analysis,
        "review": review
    }
team_results = orchestrator("Research multi-agent AI systems")

print("\nFINAL TEAM REPORT:")
print(team_results)