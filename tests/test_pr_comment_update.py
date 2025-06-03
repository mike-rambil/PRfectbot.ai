from unittest.mock import patch
from prfectbot.github_api import post_pr_comment


def test_post_pr_comment_success():
    with patch("prfectbot.github_api.post_comment") as mock_post:
        mock_post.return_value = True
        assert post_pr_comment("octocat", "Hello-World", 42, "Done!") is True
        mock_post.assert_called_once_with("octocat", "Hello-World", 42, "Done!")


def test_post_pr_comment_error():
    with patch(
        "prfectbot.github_api.post_comment", side_effect=Exception("fail")
    ) as mock_post:
        assert post_pr_comment("octocat", "Hello-World", 42, "Done!") is False
        mock_post.assert_called_once()
