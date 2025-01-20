def groups_per_user(group_dictionary):
    user_groups = {}
    # Iterate through group_dictionary
    for group, users in group_dictionary.items():
        # Iterate through each user in the group
        for user in users:
            # Add group to the user's group list, creating entry if necessary
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)
    return user_groups


# Example usage
print(groups_per_user({
    "local": ["admin", "userA"],
    "public": ["admin", "userB"],
    "administrator": ["admin"]
}))
