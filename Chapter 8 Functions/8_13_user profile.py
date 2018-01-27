"""
8-13 User Profile: Start with a copy of user_profile.py from before. Build
a profile of yourself by calling build_profile(), using your first and last
namesand three other key-value pairs that describe you.
"""

def build_profile(first_name, last_name, **user_info):
	profile = {}
	profile['first_name'] = first_name
	profile['last_name'] = last_name
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile("marc", "monforte", age = 26,
								ethnicity = "filipino",
								company = "rubicon project")
print user_profile