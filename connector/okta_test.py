import okta

link = okta.Okta.parse_pagination_header('<https://dev-119799.okta.com/api/v1/users?limit=2>; rel="self", <https://dev-119799.okta.com/api/v1/users?after=000ulkru6kNZbmHKZl356&limit=2>; rel="next"')
assert link == "https://dev-119799.okta.com/api/v1/users?after=000ulkru6kNZbmHKZl356&limit=2"
