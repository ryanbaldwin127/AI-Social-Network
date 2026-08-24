"""
Utilities for passing original issue data through to aggregator output.
"""

INCLUDED_FIELDS = {"agent", "merged_at", "state", "html_url"}


def pass_input_data_to_per_issue(metrics: dict, issue_data: dict) -> dict:
    """
    Copy each issue's source data into its corresponding per_issue entry.

    Args:
        metrics (dict): output dict containing a "per_issue" section,
            keyed by issue number, to pass data into in place.
        issue_data (dict): input dict of issue records, keyed the same
            way as "per_issue".

    Returns:
        dict: the same metrics dict, mutated in place.
    """
    for issue_num, issue_metrics in metrics["per_issue"].items():
        source_issue = issue_data.get(issue_num)

        if source_issue is None:
            continue

        for field in INCLUDED_FIELDS:
            if field in source_issue:
                issue_metrics.setdefault(field, source_issue[field])

    return metrics
