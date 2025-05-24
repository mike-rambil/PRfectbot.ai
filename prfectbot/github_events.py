def parse_pr_comment_event(payload):
    return {
        'pr_number': payload['issue']['number'],
        'repo_owner': payload['repository']['owner']['login'],
        'repo_name': payload['repository']['name'],
        'comment_body': payload['comment']['body'],
    }


def is_fix_requested(comment_body):
    body = comment_body.lower()
    return "@prfectbot" in body and "fix" in body 